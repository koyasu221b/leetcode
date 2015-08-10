class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        map = {}
        for index, num in enumerate(nums):
            actual_index = index + 1
            if num not in map:
                map[num]= [actual_index]
            else:
                map[num].append(actual_index)

        for num, index_array in map.iteritems():
            searched = target - num
            if searched in map:
                index1 = index_array[0]
                if len(map[searched]) == 1:
                    index2 = map[searched][0]
                else:
                    index2 = map[searched][1]

                return [index1, index2] if index1 < index2 else [index2, index1]

        return []
