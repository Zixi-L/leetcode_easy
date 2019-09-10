import random

games = 10000
max_win = 0
total = 0

while games>0:
    win = 0
    x = random.randrange(1,7)
    while x in range(4,7):
        win += x
        x = random.randrange(1,7)
        
    total += win
    max_win = max(max_win,win)
    games -= 1
    
avg_win = round(total/10000,2)
print('Average Amount won = ', avg_win)
print('Max amount won = ', max_win)
