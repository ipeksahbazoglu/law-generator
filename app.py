import streamlit as st
import random
import re

def load_laws(file_path="cleaned_laws.txt"):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip().rstrip("\\") for line in f if line.strip()]

def parse_law(law):
    """Split into name and content if possible"""
    match = re.match(r"^(.*?):\s*(.*)", law)
    if match:
        return match.group(1), match.group(2)
    else:
        return "Law", law

def get_random_law(laws, initial=None):
    if initial:
        filtered = [law for law in laws if law[0].lower() == initial.lower()]
        if not filtered:
            return "No matching law", f"No laws found starting with '{initial}'"
        law = random.choice(filtered)
    else:
        law = random.choice(laws)
    return parse_law(law)

# Streamlit App
st.title("⚖️ Ivan Fesenko's Laws")
st.write("Pick a random law from the infamous collection.")

# Load laws from file
laws = load_laws("cleaned_laws.txt")

col1, col2 = st.columns(2)

with col1:
    if st.button("I'm Feeling Lucky!"):
        title, content = get_random_law(laws)
        st.subheader(title)
        st.write(content)

