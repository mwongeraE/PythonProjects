def flatten(lists):
    results = []
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            results.append(lists[i][j])
    return results
print flatten(n)
