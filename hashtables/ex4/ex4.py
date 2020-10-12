def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    hash = {}
    for key in a:
        if abs(key) in hash:
            result.append(abs(key))
        else:
            hash[abs(key)] = 0
    print(result)
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
