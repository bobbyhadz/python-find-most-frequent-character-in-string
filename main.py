# Find the most frequent character in a String in Python

from collections import Counter

string = 'aaabbc'


counter = Counter(string)

# ✅ Find most frequent character in string
most_frequent = counter.most_common(1)[0]
print(most_frequent)  # 👉️ ('a', 3)

print(most_frequent[0])  # 👉️ 'a'

# ✅ Find N most frequent characters in string

most_frequent_2 = counter.most_common(2)
print(most_frequent_2)  # 👉️ [('a', 3), ('b', 2)]
