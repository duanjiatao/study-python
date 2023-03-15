# 循环嵌套

import numpy as np

i = 0
c = 0
while i < 10:
    for j in range(10):
        # print(f"i={i} j={j}")
        c += 1
    i = i + 1
print(c)

for i in range(10):
    if i == 5:
        print(i)
        break
else:
    print("for else执行")

nums = np.random.randint(10, size=10)
print("排序前:", nums)

# BubbleSort
for i in range(len(nums)):
    is_swap = False
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp
            is_swap = True
    if not is_swap:
        break

print("排序后:", nums)
