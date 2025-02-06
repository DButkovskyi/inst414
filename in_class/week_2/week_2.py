from nltk.tokenize import TweetTokenizer 
from collections import Counter

def print_top_words(file, top_n=10):
    tk = TweetTokenizer()
    with open(file, 'r') as file:
        text = file.read()
    text = text.lower()
    tokens = tk.tokenize(text)
    word_freq = Counter([word for word in tokens if word.isalnum()])
    print(f"Top {top_n} words in {file.name}:")
    for word, freq in word_freq.most_common(top_n):
        print(f"{word}    {freq}")
    print("\n")

file_path_1 = 'in_class/week_2/test01_cc_sharealike.txt'
file_path_2 = 'in_class/week_2/test02_the_last_question.txt'

# print_top_words(file_path_1)
# print_top_words(file_path_2)

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    print_top_words(file_path)