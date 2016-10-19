import collections
sentence = raw_input("enter the sentence")
words = sentence.split()
word_counts = collections.Counter(words)
for word, count in sorted(word_counts.items()):
    print('"%s" is repeated %d time%s.' % (word, count, "s" if count > 1 else ""))
