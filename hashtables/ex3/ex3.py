def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    intersects = []

    hash = {}
    for list in arrays:
        for key in list:
            if key in hash:
                hash[key] += 1
            else:
                hash[key] = 1

            if hash[key] == len(arrays):
                intersects.append(key)

    return intersects


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
