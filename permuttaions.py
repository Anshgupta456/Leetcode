class Solution:
    def permute(self, num):
        if len(num)==0:
            return []

        result=[]
        start=[]

        def recursiveperm(list,final,temp):
            length=len(list)

            if length==0:
                final.append(temp)
                return

            for i in range(length):
                nexttemp=temp[:]
                nexttemp.append(list[i])
                templist=list[:]
                templist.pop(i)
                recursiveperm(templist,final,nexttemp)

        recursiveperm(num,result,start)
        return result
