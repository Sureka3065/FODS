from collections import Counter

reviews = [
    "The product is amazing! I love it.",
    "Not satisfied with the quality.",
    "This is the best purchase I've made.",
    "The customer service was terrible.",
    "I would recommend this product to others."
]

all_text = ' '.join(reviews)

words = all_text.lower().split()

word = Counter(words)

print("Word Frequency Distribution:")
for word, frequency in word.items():
    print(f"{word}: {frequency}")
