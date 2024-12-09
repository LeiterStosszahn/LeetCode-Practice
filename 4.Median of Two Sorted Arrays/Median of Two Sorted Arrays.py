class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        Lst=nums1+nums2
        Lst.sort()
        lstlen=len(Lst)
        if lstlen%2==0:
            return (Lst[lstlen>>1]+Lst[(lstlen>>1)-1])/2
        else:
            return Lst[(lstlen-1)>>1]