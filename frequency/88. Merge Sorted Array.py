class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m-1, n-1, len(nums1)-1
        while p1>=0 and p2>=0: #!!!这里不能写while p1 and p2 因为这样==0的情况就会被跳过
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1

        if p2>=0:
            nums1[:p2+1] = nums2[:p2+1]
        
