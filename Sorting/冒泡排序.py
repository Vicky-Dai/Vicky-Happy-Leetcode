""" 时间复杂度O(n2) """
# 每次排序时，从头开始两两进行比较，较小的数向前“冒”，较大的数向后“沉”

def bubble_sort(arr):
	for i in range(0,len(arr)):
	#每排序一次，经过两两比较最大值“沉”到最后
		for j in range(1,len(arr)-i):
		#将第一个元素到未排序好的元素进行两两比较，大数靠后
			if arr[j]<arr[j-1]:
				arr[j-1],arr[j]=arr[j],arr[j-1]
	return arr
