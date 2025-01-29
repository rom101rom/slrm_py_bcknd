from random import sample


insert_rows = []

for i in range(0, 10):
    insert_rows.append(tuple(sample(range(0, 99999), 5)))
    print(insert_rows)

print(str(insert_rows)[1:-1])