def run():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    bag_size = 50
    n = len(values)

    result = bag(bag_size, weights, values, n)
    print(result)


def bag(bag_size, weights, values, n):
    if n == 0 or bag_size == 0:
        return 0

    if weights[n - 1] > bag_size:
        return bag(bag_size, weights, values, n - 1)

    return max(values[n - 1] + bag(bag_size - weights[n - 1], weights, values, n - 1),
            bag(bag_size, weights, values, n - 1))


if __name__ == '__main__':
    run()
