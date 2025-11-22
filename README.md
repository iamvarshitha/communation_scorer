AI Communication Scorer

This project implements the AI Communication Scorer case study objective: to build a full-stack tool (UI + Logic) that accepts a user-provided transcript and produces a detailed, rubric-based score (0-100) and criterion-specific feedback.

The solution utilizes **Streamlit** for a simple web-based UI and follows a modular Python architecture to combine rule-based checks with NLP scoring placeholders, adhering strictly to the provided rubric weights.

How to Run Locally

Follow these steps to set up and run the Streamlit application on your local machine.

1. Prerequisites

You must have **Python 3.8+** installed.

2. Setup

Save the following four files into a single directory:
* `requirements.txt`
* `rubric_config.py`
* `scorer_logic.py`
* `streamlit_app.py`

3. Install Dependencies

Open your terminal or command prompt, navigate to the project directory, and install Streamlit:

```bash
# Navigate to your project folder
cd path/to/ai-scorer

streamlit run streamlit_app.py

# Install Streamlit (and any other requirements)
# Note: The provided requirements.txt only contains 'streamlit'
pip install -r requirements.txt

