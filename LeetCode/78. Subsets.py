class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # prepare a output list 
        # then, iterate these singular elements 
        #     iterate elements in the output list
        #.    add this singular into all elements in the output list 
        #     this process will add the singular element into the output 
        #.    because initial output list has an empty list element 
        # repeat this process 

        # the overall style looks like a Tower of Hanoi
        # for existing elements, duplicate them and add one new element to all existings 
        # then all existing elements size +1 and the tower bottom shape enlarger
        # the new element is the new 1 element on the tower top 

        output = [[]]

        for num in nums:
            new_layer = []
            for existing in output:
                # print('output', output)
                # print('existing', existing)
                # print('num', num)
                new_existing = existing + [num]
                # print('new existing', new_existing)
                new_layer.append(new_existing)
                # print('new layer', new_layer)
                # print()

            output.extend(new_layer)
        return output
        