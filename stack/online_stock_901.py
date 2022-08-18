class StockSpanner:

    def __init__(self):

        self.m_stack = [] 
        self.curr_num = 0

    def next(self, price: int) -> int:

        if len(self.m_stack)==0 :
            self.m_stack.append((price,0))
            self.curr_num += 1
            return 1        
        
        while len(self.m_stack)>0 and self.m_stack[-1][0]<price:
            self.m_stack.pop()

        if len(self.m_stack)==0:
            return self.curr_num+1
        ret =  self.curr_num - self.m_stack[-1][1] + 1
        self.m_stack.append((price,self.curr_num)  )
        self.curr_num += 1

        return ret 
