def remove_duplicates(some_list):
    return set(some_list)


def run():
    my_list = [1, 1, 2, 2, 3, 4, 5]
    print(my_list)
    my_list_w_dup = list(remove_duplicates(my_list))
    print(my_list_w_dup)


if __name__ == '__main__':
    run()
