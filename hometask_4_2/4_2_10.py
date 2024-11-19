'''You are pick a number between 0 and 100.
Program has 8 attempts.
You print "-", "+" or "=" for every attempt'''
low = 0
high = 100
for i in range(1, 9):
    mid = int((high - low) / 2) + low
    print(f'Attempt #{i}, is it {mid}?')
    a = str(input())
    if a == '=':
        print('You`r win!')
        break
    elif a == '-':
        high = mid
        mid = int((high - low) / 2) + low
        print("low", low, "high", high, "mid", mid)
    elif a == "+":
        low = mid
        mid = int((high - low) / 2) + low
        print("low", low, "high", high, "mid", mid)

