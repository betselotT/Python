class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = []
        for i in range(len(nums1)):
            temp.append(nums1[i])
        nums1.clear()
        for i in range(m):
            nums1.append(temp[i])
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()
        print(nums1)
