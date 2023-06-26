def dec2bin(target: int):
    remainder: list[int] = []

    while target != 0:
        remainder.append(target % 2)
        target //= 2

    remainder.reverse()
    return remainder

def dec2bin(target: float):
    i = int(target) # 정수 부분
    f = target - i # 소수 부분

    a = []
    while i != 0:
        a.append(i % 2)
        i //= 2

    a.reverse()

    b = []
    n = 0

    while f != 0:
        temp = f * 2
        b.append(int(temp))
        f = temp - int(temp)
        n += 1
        if n >= 100: break

    return a, b

def dec2hex(target: int):
    remainder: list[int] = []

    while target != 0:
        remainder.append(target % 16)
        target //= 16

        for i in range(len(remainder)):
            match remainder[i]:
                case 10: remainder[i] = 'A'
                case 11: remainder[i] = 'B'
                case 12: remainder[i] = 'C'
                case 13: remainder[i] = 'D'
                case 14: remainder[i] = 'E'
                case 15: remainder[i] = 'F'

    remainder.reverse()
    return remainder

print(dec2bin(26.1242))
print(dec2hex(26))