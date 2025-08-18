class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        # superstring means this string contains both s1 and s2, meanwhile it is the shortest combination
        
        # corner case: if shorter one is already in longer string, return longer one
        if s1 in s2:
            return s2
        if s2 in s1:
            return s1
        

        res = s1+s2
        # smaller length needs to compare 
        upto = min(len(s1), len(s2))
        for k in range(1, upto+1):
            if s1.endswith(s2[:k]):
                if len(res) > len(s1+s2[k:]):
                    res = s1+s2[k:]

            if s2.endswith(s1[:k]):
                if len(res) > len(s2+s1[k:]):
                    res = s2+s1[k:]
        
        return res

