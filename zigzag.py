class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        l = len(s)


        arr=["" for x in range(l)]
        row = 0
        
        for i in range(l):

            arr[row] += s[i]

            if row == numRows - 1:
                down = False

            elif row == 0:
                down = True

            if down:
                row += 1
            else:
                row -= 1

    
        final = ""
        for i in range(l):
            final += arr[i]
        return final
        