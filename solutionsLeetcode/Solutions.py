from typing import List


class Solution:

    def __init__(self):
        pass

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        m = {}
        for i, val in  enumerate(nums,start=0) :
            if target - val in m.values() :
                for k , v in m.items() :
                    if v == target - val  :
                        ret.append(k)
                        break
                ret.append(i)
                break
            else :
                m[i] = val
        return ret

#     def test(self):
#         lists  = [1,3,5,2,6,3]
#         for num, member in enumerate(lists, start=-0):
#             print("list content {} :{}".format(num, member))
#
# s =  Solution()
# s.test()
s = Solution()
# l = [1,2,3,5,7]
# print(s.twoSum(l, 7))

l = [2,7,11,15]
print(s.twoSum(l, 9))