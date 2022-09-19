

nums=["0","+","2","-","3"]
# nums=["1","+","2"]

i=0
output=0
while i <len(nums)-2:
    operand=int(nums[0]) if i==0 else output
    operator=nums[i+1]
    operand_2=int(nums[i+2])

    if operator=="+":
        output=operand+operand_2
    elif operator=="-":
        output=operand-operand_2

    i+=2

print(output)