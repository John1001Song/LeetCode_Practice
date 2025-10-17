"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        # we go through buf based on n, indicating when to stop
        # already get chars
        total = 0
        buf4 = [' ']*4

        while total < n:
            count = read4(buf4)
            # end of file
            if count == 0:
                break
            cur_take = min(count, n-total)
            # insert into buf
            for i in range(cur_take):
                buf[total] = buf4[i]
                total += 1
            # corner case: buf4 is not full, indicates end of file, stop
            if count < 4:
                break
        
        return total

