def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weights_hash = {}
    for i in range(length):
        second = limit - weights[i]
        if second in weights_hash:
            return i, weights_hash[second]

        weights_hash[weights[i]] = i
    return None
