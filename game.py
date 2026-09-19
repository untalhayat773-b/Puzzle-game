import random
import streamlit as st

# Page Config
st.set_page_config(
    page_title="Brain Twist - Puzzle Game", page_icon="🧩", layout="centered"
)

# Custom Styling
st.markdown(
    """
    <style>
    .main {background-color: #f5f7fa;}
    .stButton>button {width: 100%; background-color: #4CAF50; color: white; font-weight: bold; border-radius: 8px; padding: 10px;}
    </style>
""",
    unsafe_allow_html=True,
)

st.title("🧩 Brain Twist: Ultimate Puzzle Challenge")
st.write(
    "Solve the puzzles correctly to level up and test your IQ! No API keys"
    " required—pure logic gameplay."
)

# Initialize Session State for Game Progress
if "score" not in st.session_state:
  st.session_state.score = 0
if "level" not in st.session_state:
  st.session_state.level = 1

# Sample Puzzle Database (Math & Word Puzzles)
puzzles = [
    {
        "question": (
            "I have keys but no locks. I have space but no room. You can"
            " enter, but can't go outside. What am I?"
        ),
        "options": ["A Computer Keyboard", "A House", "A Car", "A Book"],
        "answer": "A Computer Keyboard",
    },
    {
        "question": "What is 7 + 7 ÷ 7 + 7 × 7 - 7?",
        "options": ["50", "56", "48", "14"],
        "answer": "50",
    },
    {
        "question": (
            "Rearrange the letters to form a fruit: 'P P A L E'"
        ),  # APPLE
        "options": ["APPLE", "PINE", "PEACH", "PLUM"],
        "answer": "APPLE",
    },
    {
        "question": (
            "If 3 cats can catch 3 mice in 3 minutes, how long will it take 100"
            " cats to catch 100 mice?"
        ),
        "options": ["100 minutes", "3 minutes", "300 minutes", "1 minute"],
        "answer": "3 minutes",
    },
]

# Select current puzzle based on level
current_puzzle_idx = (st.session_state.level - 1) % len(puzzles)
active_puzzle = puzzles[current_puzzle_idx]

st.markdown(f"### 🏆 Score: {st.session_state.score} | Level: {st.session_state.level}")
st.markdown("---")

# Display Puzzle
st.subheader(f"Level {st.session_state.level Puzzle}")
st.write(active_puzzle["question"])

# User Choice
user_choice = st.radio("Choose your answer:", active_puzzle["options"])

if st.button("Submit Answer 🎯"):
  if user_choice == active_puzzle["answer"]:
    st.success("🎉 Correct Answer! Well done.")
    st.session_state.score += 10
    st.session_state.level += 1
    st.rerun()
  else:
    st.error("❌ Incorrect! Try again or reset your game.")

if st.button("🔄 Reset Game"):
  st.session_state.score = 0
  st.session_state.level = 1
  st.rerun()
  
