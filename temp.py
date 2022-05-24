set_tuple = {
    (2, 1, 3),
    (3, 2, 1),
    (4, 3, 2),
    (4, 4, 1),
    (2, 5, 1),
    (2, 6, 0),
}


id = 4
for i in set_tuple:
    if i[1] == id:
        set_tuple.remove(i)
        break

print(set_tuple)
