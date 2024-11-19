'''You are pick a number between 0 and 100.
Program has 8 attempts.
You print "-", "+" or "=" for every attempt'''
low = 0
high = 100
for i in range(1, 9):
    def mid_num(higher_num:int, lower_num:int):
        mid = int((higher_num - lower_num) / 2) + lower_num
        return mid

    
    print(f'Attempt #{i}, is it {mid_num(high, low)}?')
    
    a = str(input())
    if a == '=':
        print('You`r win!')
        break
    elif a == '-':
        high = mid_num(high, low)
        mid_num(high, low)
    elif a == "+":
        low = mid_num(high, low)
        mid_num(high, low)

