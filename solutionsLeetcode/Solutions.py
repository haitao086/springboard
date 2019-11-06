from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self):
        pass

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        m = {}
        for i, val in enumerate(nums, start=0):
            if target - val in m.values():
                for k, v in m.items():
                    if v == target - val:
                        ret.append(k)
                        break
                ret.append(i)
                break
            else:
                m[i] = val
        return ret

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1 = []
        arr2 = []
        while l1 != None:
            arr1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            arr2.append(l2.val)
            l2 = l2.next
        len1 = len(arr1)
        len2 = len(arr2)
        if len1 > len2:
            arr3 = self.addTwoNumbersArray(arr1, arr2)
        else:
            arr3 = self.addTwoNumbersArray(arr2, arr1)
        # print(arr3)
        len3 = len(arr3)
        i3 = 1
        l3 = ListNode(arr3[0])
        result = l3
        while i3 < len3:
            l3.next = ListNode(arr3[i3])
            l3 = l3.next
            i3 = i3 + 1
        return result

    def addTwoNumbersArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        len1_3 = len(arr1)
        len2 = len(arr2)
        for i, val1 in enumerate(arr1):
            if i < len2:
                arr3.append(arr1[i] + arr2[i])
            else:
                arr3.append(arr1[i])

        # arrange data in arr3
        big_than10 = False
        j = 0
        while j < len1_3:
            if arr3[j] + (1 if big_than10 else 0) > 9:
                arr3[j] = arr3[j] + (1 if big_than10 else 0) - 10
                big_than10 = True
            else:
                arr3[j] = arr3[j] + (1 if big_than10 else 0)
                big_than10 = False
            j = j + 1
        if big_than10:
            # arr3[len1_3 - 1] = arr3[len1_3 - 1] - 10
            arr3.append(1)

        return arr3

    # def test(self):


#         lists  = [1,3,5,2,6,3]
#         for num, member in enumerate(lists, start=-0):
#             print("list content {} :{}".format(num, member))
#
# s =  Solution()
# s.test()
s = Solution()
# l = [1,2,3,5,7]
# print(s.twoSum(l, 7))

l = [2, 7, 11, 15]
print(s.twoSum(l, 9))
l1 = [2,4,3]
l2 = [5,6,4]
print(s.addTwoNumbersArray(l1, l2))
print("end")
