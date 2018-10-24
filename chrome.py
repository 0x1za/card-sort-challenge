x = [1, 2, 3, 4]



def reverse(x):
    length = len(x) - 1

    y = length / 2

    i = 0
    while i <= y:
        new = x[length - i]
        old = x[i]
        x[i], x[length - i] = new, old

        i += 1

    return x

print (reverse(x))
