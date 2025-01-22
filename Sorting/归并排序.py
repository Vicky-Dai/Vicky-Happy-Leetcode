# 归并排序 归并排序的时间复杂度是 O(n log n)，其中：

#分割操作的时间复杂度是 O(log n)，因为每次都将数组分成两半。
#合并操作的时间复杂度是 O(n)，因为每次都需要比较并合并两个子数组。
lst = list(map(int, input().split(',')))


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf): #这个 while 循环用于将 lefthalf 和 righthalf 中的元素逐个比较，并将较小的元素放入到 alist[k] 中
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return alist


mergeSort(lst)
