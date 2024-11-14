def triangle_table(n: int):
    count = 0
    for i in range(n):
        for b in range(i + 1):
            count += 1
            print (count, end=' ')
        print() # while string become too wide - line breaks
triangle_table(int(input()))