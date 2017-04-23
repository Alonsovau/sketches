# 找出序列中出现最多的元素
words = [
    'a', 'b', 'my', 'iu', 'zx', 'l', 'o', 'v', 'e', 'iu', 'zx',
    'zx', 'iu', 'iu1', 'iu'
]
from collections import Counter
word_counter = Counter(words)
top_three = word_counter.most_common(3)
print(top_three)
print(word_counter)
print(word_counter['my'])

# 继续计数
next_words = ['zx', 'iu']
for word in next_words:
    word_counter[word] += 1
print(word_counter['iu'])
# 或者用update
next_words2 = ['iu']
word_counter.update(next_words2)
print(word_counter['iu'])

# 加减
testword1 = ['zx', 'iu', 'zx', 'zx']
testword2 = ['iu', 'zx', 'iu', 'iu']
counter1 = Counter(testword1)
counter2 = Counter(testword2)
print(counter1 - counter2)
print(counter1 + counter2)