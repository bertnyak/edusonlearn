def lalala(a , b):
    result = []
    for i in range(a, b):
        if i % 2 == 0:
            result.append(i)
    return result

print(lalala(1,10))