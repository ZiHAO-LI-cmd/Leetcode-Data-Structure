class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 哈希表
        # hashmap = {}
        # res = []
        # for element in nums1:
        #     if element not in hashmap:
        #         hashmap[element] = 1
        #     else:
        #         hashmap[element] += 1

        # for e in nums2:
        #     if e in hashmap and hashmap[e] != 0:
        #         hashmap[e] -= 1
        #         res.append(e)

        # return res


        # 双指针
        # nums1.sort()
        # nums2.sort()
        # p1 = 0
        # p2 = 0
        # res = []
        # while p1 < len(nums1) and p2 < len(nums2):
        #     if nums1[p1] < nums2[p2]:
        #         p1 += 1
        #     elif nums2[p2] < nums1[p1]:
        #         p2 += 1
        #     else:
        #         res.append(nums1[p1])
        #         p1 += 1
        #         p2 += 1
        # return res

        # Python Counter
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2
        return list(num.elements())