def minDistance(word1, word2):
    distance = [[i] for i in range(len(word1) + 1)]
    distance[0] = [i for i in range(len(word2) + 1)]
    for i in range(1 , len(word1)+1):
        for j in range(1 , len(word2) +1):
            delete = distance[i-1][j] + 1
            insert = distance[i][j-1] + 1
            replace = distance[i-1][j-1]
            if word1[i-1] != word2[j-1]:
                replace += 1
            distance[i].append(min(delete, insert, replace))
    return distance[-1][-1]

word1 = input("Enter word1: ")
word2 = input("Enter word2: ")
print(minDistance(word1 ,word2))