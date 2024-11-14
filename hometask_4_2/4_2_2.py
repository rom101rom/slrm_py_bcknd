def matrice_print(side_len: int):
    for i in range(1, (side_len ** 2) + 1):
        if i % 5 == 0:
            print(i, end='\n')
        else: 
            print(i, end=' ')

matrice_print(5)