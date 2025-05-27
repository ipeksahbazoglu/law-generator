import random

def load_laws(file_path="cleaned_laws.txt"):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def get_random_law(laws, initial=None):
    if initial:
        filtered = [law for law in laws if law[0].lower() == initial.lower()]
        if not filtered:
            return f"No laws found starting with '{initial}'"
        return random.choice(filtered)
    return random.choice(laws)

if __name__ == "__main__":
    laws = load_laws("cleaned_laws.txt")
    print("Example random law:", get_random_law(laws))
    print("Example law starting with 'T':", get_random_law(laws, 'T'))
