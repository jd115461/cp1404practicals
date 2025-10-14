"""
Word Occurrences
Estimate: 17 minutes 51 seconds 810 millisecond
Actual: 9 minutes 38 seconds 680 millisecond
"""

words_to_count = {}

text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()

for word in words:
    try:
        words_to_count[word] += 1
    except KeyError:
        words_to_count[word] = 1

max_length = max((len(word) for word in words))

for word in sorted(words_to_count):
    print(f"{word:{max_length}} : {words_to_count[word]}")
