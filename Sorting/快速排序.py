""" 时间复杂度O(nlogn)
不稳定"""
#快排确定顺序主要是先确定一个点，然后再确定其他点（这个过程递归）怎么做呢？
#找一个初始基准（可以任意，这里选的是数组最后一个）然后把数组分成两部分，左边的比基准小，右边的比基准大
#这里i控制的是左边数组的最后一个，j控制的是整个数组的遍历
#最后把初始基准放到i+1的位置（这样左边的都比基准小，右边的都比基准大），就得到了一个确定好的点，然后再分别对左右两部分进行递归，找到确定的点
def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)
 
def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i+1] # 交换基准值和i+1的位置
    return i + 1

quick_sort(array, 0, len(array) - 1)

# 另一种实现
def quick_sort(arr):
#递归实现，先找到终止条件
	if len(arr)<2:
		return arr
	#选择arr[0]为基准元素,将arr[1:]与其进行比较
	left, right=[],[]
	for i in range(1,len(arr)):
		if arr[i] <=arr[0]:
			left.append(arr[i])
		else:
			right.append(arr[i])
	#每进行一次排序，基准元素的位置已经确定，分别将小于和大于基准元素的子序列进行快排
	return quick_sort(left)+[arr[0]]+quick_sort(right)



""" 假设我们有数组 array = [1, 10, 7, 8, 9, 5]，基准值 x = 5。

初始化：

i = -1，x = 5，数组是 [1, 10, 7, 8, 9, 5]。
开始遍历：

j = 0，array[j] = 1，满足条件 1 <= 5，i += 1，i = 0。交换 array[0] 和 array[0]，数组没有变化 [1, 10, 7, 8, 9, 5]。

j = 1，array[j] = 10，10 > 5，不满足条件，跳过。

j = 2，array[j] = 7，7 > 5，不满足条件，跳过。

j = 3，array[j] = 8，8 > 5，不满足条件，跳过。

j = 4，array[j] = 9，9 > 5，不满足条件，跳过。

j = 5，array[j] = 5，满足条件 5 <= 5，i += 1，i = 1。交换 array[1] 和 array[5]，数组变为 [1, 5, 7, 8, 9, 10]。

结束遍历：

最终，我们交换基准值 x = 5 和 array[i + 1] = array[2]，得到数组 [1, 5, 7, 8, 9, 10]，基准值 5 已经放到了正确的位置。
 """