""" 时间复杂度O(n1.3)
不稳定 """

# 主要思想：根据一定的增量（分组的跨度）分割序列，各子序列使用插入排序，再逐渐减小增量

def shell_sort(arr):
	grap=len(arr)//2
	while grap>0:
	#相当于跨度为grap的插入排序
		for i in range(grap,len(arr)):
			current=arr[i]
			pre_index=i-grap
			#两两比较，大的后移，找到插入点，插入当前元素
			while pre_index>=0 and arr[pre_index]>current:
				arr[pre_index+grap]=arr[pre_index]
				pre_index-=grap
			arr[pre_index+grap]=current
		#逐渐减小跨度（跨度为1时为插入排序）
		grap//=2
	return arr
