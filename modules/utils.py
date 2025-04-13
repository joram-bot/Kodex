# utils.py
def filter_content(text):
    banned_words = ["offensive_word1", "offensive_word2"]
    for word in banned_words:
        if word in text:
            return "Sorry, I can't respond to that."
    return text
