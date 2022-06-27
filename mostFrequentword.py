l1 = ['Facebook', 'Google', 'Google']
l2 = ['Facebook', 'Facebook', 'Google', 'Google']
l3 = ['Google', 'Facebook', 'Facebook', 'Google']

sl2 = sorted(l2)
sl3 = sorted(l3)


#method one:
res = max(set(sl3), key = sl3.count)
print(res)

#method two:
def mostfreq(sl2):
    count = 0
    num = sl2[0]

    for word in sl2:
        temp = sl2.count(word)
        if (temp > count):
            count = temp
            num = word

    return num

print(mostfreq(sl2))
