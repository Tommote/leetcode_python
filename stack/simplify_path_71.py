class Solution:
    def simplifyPath(self, path: str) -> str:

        str_list = path.split('/')

        ret_stack = []

        for chs in str_list:

            if chs=='' or chs=='.':
                continue
            elif chs == '..':
                if len(ret_stack) > 0:
                    ret_stack.pop()
            else:
                ret_stack.append(chs)
        

        ret = ''
        for chs in ret_stack:
            ret = ret + '/'
            ret = ret + chs
        
        return ret if ret != '' else '/'

s = Solution()
print( s.simplifyPath('/../') )