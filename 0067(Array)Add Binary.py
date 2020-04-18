a = '111'
b = '11'

# a+b >>> '1010'


# tips:
temp = 3

while temp:
    temp -= 1

print(temp)
# >>> 0 
# means the while loop ends when temp = 0

# ---------------------------------------

reminder = 0
result = ''

a = list(a)
b = list(b)

while a or b or reminder:
    if a :
        reminder += int(a.pop())
    if b :
        reminder += int(b.pop())
        
    result += str(reminder % 2) # add new elements at the end of the string, result[::-1]
    reminder //=2

print(result[::-1])

