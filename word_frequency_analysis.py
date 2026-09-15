from collections import Counter
import string


def load_text(filename):
    """Read text from a file."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def preprocess_text(text):
    """Convert text to lowercase and remove punctuation."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()


def remove_stopwords(words):
    """Remove a small set of common English words."""
    stopwords = {
        "i", "a", "the", "and", "to", "of", "in",
        "is", "it", "when", "with", "but", "can",
        "them", "that", "are", "as", "from", "what"
    }
    return [word for word in words if word not in stopwords]


def get_word_frequencies(words):
    """Count how frequently each word occurs."""
    return Counter(words)


def display_top_words(frequencies, number=10):
    """Display the most frequent words."""
    print(f"Top {number} words:")
    print("-" * 25)

    for word, count in frequencies.most_common(number):
        print(f"{word}: {count}")


def main():
    text = load_text("sample_text.txt")
    words = preprocess_text(text)
    filtered_words = remove_stopwords(words)
    frequencies = get_word_frequencies(filtered_words)

    print(f"Total words after filtering: {len(filtered_words)}")
    print(f"Unique words after filtering: {len(frequencies)}")
    print()

    display_top_words(frequencies)


if __name__ == "__main__":
    main()
