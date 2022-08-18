class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n==0 :
            return 1

        if n==1 :
            return x 

        if n%2==0 :

            temp = self.myPow(x, n//2) 
            return temp*temp 

        else:
            temp = self.myPow(x, (n-1)//2)
            return temp*temp*x 
    
