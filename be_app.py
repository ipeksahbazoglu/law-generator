import streamlit as st
import random

def load_words(file_path="words.txt"):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [w.strip() for w in f if w.lower().startswith("be")]

def get_random_word(words, sub_prefix=None):
    if sub_prefix:
        filtered = [w for w in words if w.lower().startswith("be" + sub_prefix.lower())]
        if not filtered:
            return f"No words found starting with 'be{sub_prefix}'"
        return random.choice(filtered)
    return random.choice(words)

# Streamlit app
st.title("📚 'be-' Word Generator")
st.write("Be-cause why not?")

# Load words
be_words = load_words("words.txt")

col1, col2 = st.columns(2)

with col1:
    if st.button("bequeath a word"):
        word = get_random_word(be_words)
        st.success(word)

