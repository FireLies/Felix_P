# # arr = ["hello", "hello", "world", "im", "here", "yes", "me", "here"]
# # print(', '.join(arr))

# # var = set()
# # duplicate_Type = [x for x in arr if x in var or (var.add(x)) or False]
# # for i in duplicate_Type:
# #     arr.remove(i)

# # print(', '.join(arr))

# item_list = ['item', 5, 'foo', 3.14, True]
# item_list = [e for e in item_list if e not in ('item', 5)]
# print(*item_list)
import time
from random import randint

from idna import valid_string_length

start = time.time()

randomize = []
for i in range(0, 100000):
    randomize.append(randint(0, 1000))

end = time.time()
print(str(round((end - start) * 1000, 3)), "ms")