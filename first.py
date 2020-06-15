def search_pairs(array, k):
    unic = []
    for i in array:
        for j in array:
            if i + j == k and ([i, j] not in unic and [j, i] not in unic):
                unic += [[i, j]]
    print(unic)


search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5)
