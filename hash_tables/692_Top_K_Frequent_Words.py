# python 692_Top_K_Frequent_Words.py
# words = ["i", "love", "leetcode", "i", "love", "coding"]
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

count = {}

buckets = [[] for _ in range(len(words))]

for word in words:
    count[word] = count.get(word, 0) + 1

for word, frqe in count.items():
    buckets[frqe].append(word)


# print(sorted(count))

new_arr = sorted(sorted(count), key=count.get, reverse=True)


print(new_arr[:k])

# for work in range(len(buckets)-1, 0, -1):
# for num, freq in count.items():
#     print(num, freq)

# print(count, buckets)
# print(buckets)
