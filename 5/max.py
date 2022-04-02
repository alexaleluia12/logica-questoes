
def max_inner(a, b):
    if a > b:
        return a
    else:
        return b

def max_(a, b, c):
    return max_inner(max_inner(a, b), max_inner(b, c))


if __name__ == '__main__':
    print(max_(45, 9, 3))
    print(max_(3, 9, 45))
    print(max_(9, 45, 3))
