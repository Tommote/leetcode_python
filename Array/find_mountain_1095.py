# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:

    def __init__(self, arr) -> None:
        
        self.arr = arr 

    def get(self, index: int) -> int:
        return self.arr[index] 
    def length(self) -> int:
        return len(self.arr)



class Solution:

    def search_binary_find_max(self, target: int, mountain_arr: 'MountainArray') ->int:

        l_p, r_p = 0, mountain_arr.length()-1
        while l_p<=r_p:
            mid_p = (l_p+r_p)//2 
            if mountain_arr.get(mid_p) > mountain_arr.get(mid_p+1):
                r_p = mid_p-1
            else:
                l_p = mid_p+1
        return l_p
    def search_binary_find_target(self, target: int, mountain_arr: 'MountainArray', reverse=True, left_p=0, right_p =0) ->int:

        l_p, r_p = left_p, right_p
        while l_p<=r_p:
            mid_p = (l_p+r_p)//2 
            temp = mountain_arr.get(mid_p)
            if temp==target:
                return mid_p
            elif reverse :
                if temp > target:
                    r_p = mid_p-1
                else:
                    l_p = mid_p+1
            else:
                if temp < target:
                    r_p = mid_p-1
                else:
                    l_p = mid_p+1
        return l_p
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()
        mount_top = self.search_binary_find_max(target, mountain_arr)  
        x1 = self.search_binary_find_target(target, mountain_arr, True, 0, mount_top-1)
        x2 = self.search_binary_find_target(target, mountain_arr, False, mount_top, mountain_arr.length()-1)
        
        if x1>=0 and x1<N and mountain_arr.get(x1)==target :
            return x1 
        elif x2>=0 and x2<N and mountain_arr.get(x2)==target:
            return x2 
        else:
            return -1


m = MountainArray([1,5,2])

s = Solution()
print(s.findInMountainArray(0, m))