# rubric_config.py
# The central source of truth for all scoring weights, keywords, and thresholds.

# --- 🎯 Overall Weights (Must sum to 100) ---
TOTAL_WEIGHT = 100
WEIGHTS = {
    "Salutation Level": 5,
    "Key word Presence": 30,
    "Flow": 5,
    "Speech Rate": 10,
    "Grammar Errors": 10,
    "Vocabulary Richness": 10,
    "Filler Word Rate": 15,
    "Sentiment/Positivity": 15, # Placeholder for NLP-based score
}

# --- 💬 Content & Structure Rules ---

# Salutation Level (Max Score: 5)
SALUTATION_RUBRIC = {
    "No Salutation": 0,
    "Normal": 2, # e.g., "Hi", "Hello"
    "Good": 4, # e.g., "Good Morning", "Hello everyone"
    "Excellent": 5, # e.g., "I am excited to introduce..."
}
SALUTATION_KEYWORDS = {
    "Normal": ["hi", "hello"],
    "Good": ["good morning", "good afternoon", "good evening", "good day", "hello everyone"],
    "Excellent": ["excited to introduce", "feeling great"],
}

# Key Word Presence (Max Score: 30, 5 points per item)
# These keywords must be detectably present in the transcript.
KEYWORD_LIST = [
    "name",
    "age",
    "school/class",
    "family",
    "hobbies/interest",
    "unique point/fun fact"
]
KEYWORD_SCORE_PER_ITEM = 5

# Flow (Max Score: 5) - Simple checks for proper start and end markers.
FLOW_KEYWORDS = {
    "START": ["hello", "hi", "good morning", "good afternoon", "greetings"],
    "END": ["thank you for listening", "thank you", "that's all", "bye", "in conclusion"]
}

# --- 🗣️ Speech Metrics Rules ---

# Speech Rate (Words Per Minute, Max Score: 10)
SPEECH_RATE_RUBRIC = {
    "Ideal": {"range": (111, 140), "score": 10},
    "Fast": {"range": (140, float('inf')), "score": 6}, # > 140 WPM
    "Slow": {"range": (81, 110), "score": 6},
    "Too slow": {"range": (0, 80), "score": 2}, # <= 80 WPM
}

# **CRITICAL FIX:** Standard rate used to estimate duration if the user enters 0.
STANDARD_SPEAKING_RATE_WPM = 150.0 

# Grammar Errors (Max Score: 10)
# Score = 1 - min(errors_per_100_words / 10, 1) * 10
GRAMMAR_SCORE_FORMULA = lambda errors_per_100_words: (1 - min(errors_per_100_words / 10, 1)) * 10

# Vocabulary Richness (Type-Token Ratio - TTR, Max Score: 10)
TTR_RUBRIC = {
    (0.9, 1.0): 10,
    (0.7, 0.89): 8,
    (0.5, 0.69): 6,
    (0.3, 0.49): 4,
    (0.0, 0.29): 2,
}

# Filler Word Rate (Max Score: 15)
FILLER_WORDS = [
    "um", "uh", "like", "you know", "so", "actually", "basically", "right",
    "i mean", "well", "kinda", "sort of", "okay", "hmm", "ah", "i guess"
]
FILLER_RATE_MAX_PENALTY = 10 # 10% filler word rate results in a 0 score.
FILLER_SCORE_FORMULA = lambda filler_rate: max(0, 15 - (filler_rate / FILLER_RATE_MAX_PENALTY) * 15)


# --- 🧪 Sample Data for Testing ---
SAMPLE_TRANSCRIPT = (
    "Hello everyone, myself Muskan, studying in class 8th B section from Christ Public School. "
    "I am 13 years old. I live with my family. There are 3 people in my family, me, my mother and my father. "
    "One special thing about my family is that they are very kind hearted to everyone and soft spoken. "
    "One thing I really enjoy is play, playing cricket and taking wickets. "
    "A fun fact about me is that I see in mirror and talk by myself. One thing people don't know about me is that "
    "I once stole a toy from one of my cousin. My favorite subject is science because it is very interesting. "
    "Through science I can explore the whole world and make the discoveries and improve the lives of others. "
    "Thank you for listening."
)
SAMPLE_DURATION_SECONDS = 52.0 # Defined as float to prevent Streamlit errors