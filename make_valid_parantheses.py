

input_= "lee(t(c)o)de)"

class Solution:
    def minRemoveToMakeValid(self, input_) :
       
        input_list=[a for a in input_]
        stack_=[]
        for i in range(len(input_list)):
            if input_list[i]=="(":
                stack_.append(i)

            if input_list[i]==")":
                if len(stack_)==0:
                    input_list[i]=""
                else:
                    stack_.pop()
            

        for index in stack_:
            input_list[index]=""

        output="".join([a for a in input_list])
        return output



s=Solution()
print(s.minRemoveToMakeValid(input_))


