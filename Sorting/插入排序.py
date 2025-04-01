""" 时间复杂度O(n2)
稳定 """
# 主要思想：就是整理牌，一张一张摸的时候！依次将元素插入到排好序序列的合适的位置（在排好序的序列中从后向前依次两两比较）

def insert_sort(arr):
	for i in range(1,len(arr)):
	#i为当前要插入元素下标，与已经排好序的arr[:i]从后向前依次两两比较
		pre_index=i-1
		current=arr[i]
		#如果待插入的值小，则比他大的值后移，直到找到插入点
		while pre_index>=0 and arr[pre_index]>current:
			arr[pre_index+1]=arr[pre_index]
			pre_index-=1
		arr[pre_index+1]=current
	return arr
