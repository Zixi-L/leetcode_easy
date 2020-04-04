def reverse(x):
    reverse_x = 0
    abs_x = abs(x)
    while abs_x!= 0:
        temp = abs_x%10
        reverse_x = reverse_x*10 + temp
        abs_x = abs_x//10
        
    #Since reverse_x can not exceed [-2**31,2**31-1]. So if condition has to be placed after while loop
    if reverse_x < 2147483647:
        if x > 0:
            return reverse_x
        else:
            return -reverse_x
    else:
        return 0

    
   
