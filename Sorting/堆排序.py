""" 时间复杂度O(nlogn)
不稳定 """
# 主要思想：若升序排列，根据大顶堆（根节点值大于等于所有左右子树的值的完全二叉树），每次排序将堆顶元素与最后一个值交换，调整大顶堆，交换…

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
