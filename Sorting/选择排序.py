""" 时间复杂度O(n2)
不稳定 """
# 主要思想：从未排好序的选择最小的元素放在最前面（交换），相当于拿到一叠牌，每次把后面最小的牌放到最前面
def select_sort(arr):
	for i in range(0,len(arr)):
	#每一次排序后将最小的值放到最前面:从后面未排序的序列中找到最小值的索引，与当前arr[i]交换
		min_index=i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[min_index]:
				min_index=j
		if min_index!=i:
			arr[i],arr[min_index]=arr[min_index],arr[i]
	return arr
			
