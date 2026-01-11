# Simple Spam Detection Probability

# Training data (fake example)
spam_words = ["win", "free", "prize"]
total_emails = 100
spam_emails = 20

def probability_word_in_spam(word):
    return 0.9 if word in spam_words else 0.1

def probability_spam_given_word(word):
    p_spam = spam_emails / total_emails
    p_word_given_spam = probability_word_in_spam(word)
    p_word = (p_word_given_spam * p_spam) + (0.1 * (1 - p_spam))
    return (p_word_given_spam * p_spam) / p_word

word = "free"
print(f"Probability email is spam given word '{word}': {round(probability_spam_given_word(word), 2)}")
