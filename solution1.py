# To indicate the degree of profanity for each sentence in a file full of Twitter tweets, you can use the following Python program:

import re

def calculate_profanity_degree(tweet, profanity_words):
    tweet = tweet.lower()
    words = re.findall(r'\b\w+\b', tweet)
    total_words = len(words)
    profanity_count = 0

    for word in words:
        if word in profanity_words:
            profanity_count += 1

    return profanity_count / total_words

def main():
    profanity_words = set(["word1", "word2", "word3"])  # Set of racial slurs

    with open("tweets.txt", "r") as file:
        for line in file:
            tweet = line.strip()
            profanity_degree = calculate_profanity_degree(tweet, profanity_words)
            print(f"Tweet: {tweet}")
            print(f"Profanity Degree: {profanity_degree}")
            print()

if __name__ == "__main__":
    main()

# Assumptions:
# The file "tweets.txt" contains one tweet per line.
# The racial slurs are provided as a set of words in the variable profanity_words.
# The program calculates the profanity degree as the ratio of profane words to the total number of words in each tweet. It uses word boundaries to ensure exact word matches.
