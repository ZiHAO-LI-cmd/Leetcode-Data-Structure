class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = []
        p1 = 0
        p2 = 0
        while p1 < m or p2 < n:
            if p1 == m:
                tmp.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                tmp.append(nums1[p1])
                p1 += 1
            elif nums1[p1] <= nums2[p2]:
                tmp.append(nums1[p1])
                p1 += 1
            else:
                tmp.append(nums2[p2])
                p2 += 1
        nums1[:] = tmp
        # nums1 = tmp