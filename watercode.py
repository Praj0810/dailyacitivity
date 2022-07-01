def waterArea(height):
    lside, rside = 0 , len(height)-1
    maxres = 0
    while lside < rside: 
        lhgt = height[lside]
        rhgt = height[rside]
        waterarea = min(lhgt, rhgt)*(rside-lside)
        maxres = max(maxres, waterarea)
        if rhgt > lhgt:
            lside += 1
        else:
            rside -= 1
    
    return maxres

#height = [1,1]

#height = [1,8,6,2,5,4,8,3,7]

height = [1, 5, 4, 3]

#height = [3, 1, 2, 4, 5]

print(waterArea(height))
