class Solution:
    def checkValidString(self, s: str) -> bool:
        # if len(s)<=1 or all(i=='(' for i in s) or all(i==')' for i in s):return False
        # elif "(" in s and ")" or '*' in s:
        #     return True
        # return False

       
                
        # open=s.count('(')
        # close=s.count(')')
        # em=s.count('*')

        # r=(open)-close
        # f=(abs(r)-em)
        # if not r:
        #     return True
        # elif not f:
        #     return True
        # else :
        #     return False

        l=0
        r=0
        for i in s:
            if i=='(':
                r+=1
                l+=1
            elif i==')':
                l-=1
                r-=1
            else:
                l-=1
                r+=1
            if r<0:
                return False
            l=max(l,0)
        return l==0
