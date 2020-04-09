numbers = [2,7,11,15]

target = 18

 
# My first solution: 
# time complexity O(n)

for i in range(len(numbers)):
    if target - numbers[i] in numbers[i+1::]:
        l = list(numbers[i+1::])
        print(i + 1, l.index(target-numbers[i])+i+2)
    

# Second solution: with dic

numbers = [2,7,11,15]
target = 9

def twoSum(numbers, target):
    num_dic={}
    for i, num in enumerate(numbers):
        if (target-num) in num_dic:
            print(num_dic[target-num]+1, i+1)
        num_dic[num]=i
    print(num_dic)
        
        
twoSum(numbers,target)
