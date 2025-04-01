# 归并排序 归并排序的时间复杂度是 O(n log n)，其中：

#分割操作的时间复杂度是 O(log n)，因为每次都将数组分成两半。
#合并操作的时间复杂度是 O(n)，因为每次都需要比较并合并两个子数组。

# 主要思想：每轮都对相邻的子序列进行两两归并
# 归并的含义：将两个有序的子序列合并成一个有序的序列，两个数组依次比较，较小的数放入新数组中，如果一个数组都放完了，剩下的数组直接全都放到新数组中就可以。ps：归并对两个数组的长度没有要求


# 递归方法：将大问题逐步分解成一个个小问题，先解决小问题（调用本身函数）,再解决大问题
def recursion_merge_sort(arr):
    #分割成不同子序列，各子序列分别再分割
    mid=len(arr)//2
    arr1=arr[:mid]
    arr2=arr[mid:]
    if len(arr1)>1:
        arr1=recursion_merge_sort(arr1)
    if len(arr2)>1:
        arr2=recursion_merge_sort(arr2)
    result=[]
    #合并两个已经排好顺序的子序列
    while arr1 and arr2:
        if arr1[0]<arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
            
    if arr1:
        result=result+arr1
    if arr2:
        result=result+arr2
    return result

# 非递归方法：先解决小问题，将得到的结果替换自己本身的值（迭代），将小问题一步步合并
def non_recursion_merge_sort(arr):
    # 分割未排序序列,步长 i，逐渐增大步长
    i = 1
    while i < len(arr):
        low = 0
        while low < len(arr):
            mid = low + i
            high = min(mid + i, len(arr))
            if mid < high:  
                left, right = arr[low:mid], arr[mid:high]
                # 将每个子序列进行两两比较,合并成一个有序序列
                result = []
                while left and right:
                    if left[0] < right[0]:
                        result.append(left.pop(0))
                    else:
                        result.append(right.pop(0))
                # 处理剩余部分
                result += left or right # 是 Python 短路逻辑（short-circuit logic）的一种简写方式 
                # 用新得到的结果替换原数组的值
                arr[low:high] = result
            low += 2 * i
        i *= 2
    return arr
