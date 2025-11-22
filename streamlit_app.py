# streamlit_app.py

import streamlit as st
import json
from rubric_config import SAMPLE_TRANSCRIPT, SAMPLE_DURATION_SECONDS
from scorer_logic import calculate_final_score

# --- UI Setup and Configuration ---

st.set_page_config(
    page_title="AI Communication Scorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🗣️ Nirmaan AI Communication Scorer")
st.markdown("---")

# --- Initialize Session State ---
# Sets up default values for input fields on first run
if 'transcript' not in st.session_state:
    st.session_state.transcript = ""
if 'duration' not in st.session_state:
    st.session_state.duration = 0.0 
    
# Instructions Sidebar
with st.sidebar:
    st.header("Instructions")
    st.info("1. Paste the full transcript text.\n2. **Duration is optional.** If left as 0, the Speech Rate will be ESTIMATED based on a standard WPM.\n3. Click 'Calculate Score'.")
    
    # Optional button to load the sample data, for immediate testing
    if st.button("Load Sample Data (for testing)"):
        st.session_state.transcript = SAMPLE_TRANSCRIPT
        st.session_state.duration = float(SAMPLE_DURATION_SECONDS)
        st.rerun() # Force a rerun to populate the input fields

# --- Input Section ---
col1, col2 = st.columns([3, 1])

with col1:
    # Text area for the main input transcript
    transcript = st.text_area(
        "1. Paste Transcript Text Here:",
        key="transcript_input",
        value=st.session_state.transcript,
        height=300,
        placeholder="e.g., Hello everyone, my name is Alex..."
    )

with col2:
    # Number input for duration, allowing 0 for estimation fallback
    duration = st.number_input(
        "2. Audio Duration (Seconds, Optional - Enter 0 for Estimation):",
        key="duration_input",
        value=float(st.session_state.duration),
        min_value=0.0, 
        step=1.0
    )

# Button to trigger the scoring logic
score_button = st.button("3. Calculate Score", type="primary")

st.markdown("---")

# --- Output Section (Triggered by Button Click) ---

if score_button:
    
    # Input validation: only need to check for transcript text
    if not transcript:
        st.error("🚨 **Error:** Please enter a transcript before calculating the score.")
    else:
        # 1. Run the scoring logic
        with st.spinner('Analyzing transcript and calculating scores...'):
            results = calculate_final_score(transcript, float(duration))

        overall_score = results["overall_score"]
        max_score = results["max_overall_score"]
        per_criterion_scores = results["per_criterion_scores"]

        # 2. Display Overall Score
        st.header("Results Overview")
        score_col, feedback_col = st.columns([1, 2])

        with score_col:
            st.metric(
                label="Overall Communication Score", 
                value=f"{overall_score}/{max_score}",
                delta=f"Achieved {overall_score}% of the total weight"
            )
            st.warning("⚠️ **NOTE:** 'Grammar Errors' and 'Sentiment/Positivity' are scored using placeholders. For real scores, external NLP libraries are required.")

        with feedback_col:
            st.subheader("General Feedback")
            if overall_score >= 80:
                st.success("Excellent submission! The structure and content are well-covered, with only minor areas for improvement.")
            elif overall_score >= 60:
                st.info("Good effort. Focus on improving specific areas like flow and vocabulary richness.")
            else:
                st.error("The submission requires substantial improvement. Review the detailed feedback below to target key missing components.")

        st.markdown("---")
        
        # 3. Display Detailed Breakdown
        st.header("Detailed Criterion Breakdown")
        
        for item in per_criterion_scores:
            criterion = item["criterion"]
            score = item["score"]
            max_c_score = item["max_score"]
            feedback = item["feedback"]
            
            # Use an expander to keep the UI clean
            with st.expander(f"**{criterion}** - Score: {score}/{max_c_score}", expanded=False):
                st.markdown(f"**Feedback:** {feedback}")
                st.code(json.dumps(item["details"], indent=4), language="json")
                if "NOTE" in item:
                     st.caption(f"**Note:** {item['NOTE']}")