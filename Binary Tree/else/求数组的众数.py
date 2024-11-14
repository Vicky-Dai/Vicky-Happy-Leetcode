def find_mode(arr):
    frequency = {}  # 用来记录每个元素的出现次数
    max_count = 0   # 用来记录最大出现次数
    mode = []       # 用来存储众数

    # 计算每个元素的出现次数
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
        # 更新最大出现次数
        if frequency[num] > max_count:
            max_count = frequency[num]

    # 找到所有出现次数等于最大出现次数的元素
    for num, count in frequency.items():
        if count == max_count:
            mode.append(num)

    return mode

# 示例
arr = [1, 2, 2, 3, 3, 4]
print("众数是：", find_mode(arr))

#在 for num, count in frequency.items(): 中：

#num 会遍历字典的每个键（即数组中的不同元素）。
#count 会遍历字典的每个键所对应的值（即该元素的出现次数）。