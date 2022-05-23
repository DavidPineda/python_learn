def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"first_name": "David", "last_name": "Pineda"}

    super_list = [
        {"first_name": "David", "last_name": "Pineda"},
        {"first_name": "Claudia", "last_name": "Villamizar"},
        {"first_name": "Maria", "last_name": "Pineda"},
        {"first_name": "Consuelo", "last_name": "Diaz"},
        {"first_name": "Gilberto", "last_name": "Pineda"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    print("")

    for value in super_list:
        print(value)

if __name__ == '__main__':
    run()
