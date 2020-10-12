# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = {}
    paths = []

    for filepath in files:
        key = filepath.split('/')[-1]
        hash.setdefault(key, []).append(str(filepath))

    for query in queries:
        if query in hash:
            for value in hash[query]:
                paths.append(value)

    return paths


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
