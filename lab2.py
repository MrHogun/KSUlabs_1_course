def sets():
    """Створення функ-ї що створює, додає/видаляє елементи, робить зріз об'єднання та переріз множин"""

    x = {6, 5, 4, 3, 2, 1}
    y = {9, 8, 7, 6, 5, 4}

    x.add(7)
    print("x:", x)

    y.remove(4)
    print("y:", y)

    slice_x = x.difference(x.difference({2, 3, 4, 5}))
    print("зріз x:", slice_x)

    union_set = x.union(y)
    print("об'єднання x та y:", union_set)

    intersection_xy = x.intersection(y)
    print("переріз x та y:", intersection_xy)

sets()
print()

def dictionaries():
    """Створення функ-ї що створює, додає/видаляє елементи, робить зріз об'єднання переріз та сортування словників"""

    x = {'x1': 1, 'x2': 2, 'xy3': 3}
    y = {'xy3': 3, 'y4': 4, 'y5': 5}

    x['y4'] = 4
    print("x:", x)

    del y['y4']
    print("y:", y)

    slice_x = {k: v for k, v in x.items() if k in ['x1', 'x2']}
    print("зріз x:", slice_x)

    union_xy = {**x, **y}
    print("об'єднання x та y:", union_xy)

    intersection_xy = {k: v for k, v in x.items() if k in y}
    print("переріз x та y:", intersection_xy)

    sorted_x = dict(sorted(x.items()))
    print("сортування x:", sorted_x)

dictionaries()
print()

def lists():
    """Створення функ-ї що створює, додає/видаляє елементи, робить зріз об'єднання переріз та сортування списків"""

    x = [1, 2, 3, 4]
    y = [3, 4, 5, 6]
    print("x:", x)
    print("y:", y)

    x.append(5)
    print("x з доданим елементом:", x)

    y.remove(5)
    print("y з видаленим елементом:", y)

    slice_x = x[1:4]
    print("зріз x:", slice_x)

    union_xy = x + y
    print("об'єднання x та y:", union_xy)

    intersection_xy = list(set(x).intersection(set(y)))
    print("переріз x та y:", intersection_xy)

    sorted_x = sorted(x)
    print("сортування x:", sorted_x)

lists()
print()