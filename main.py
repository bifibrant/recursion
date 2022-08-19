import math

MAX_STORE = 12
TAM_VALUES = [[-1 for k in range(MAX_STORE)] for n in range(MAX_STORE)]
T5_VALUES = [[[[[-1 for b in range(MAX_STORE)] for a in range(2)] for l in range(MAX_STORE)] for k in range(MAX_STORE)] for n in range(MAX_STORE)]
S5_VALUES = [[[[[-1 for b in range(MAX_STORE)] for a in range(2)] for l in range(MAX_STORE)] for k in range(MAX_STORE)] for n in range(MAX_STORE)]

def Tam(n, k):
    if k == 0 or k > n + 1:
        return 0

    if TAM_VALUES[n][k] != -1:
        return TAM_VALUES[n][k]

    result = int((2 * math.factorial(2 * k + 1) * math.factorial(4 * n - 2 * k + 3)) / (
            math.factorial(k - 1) * math.factorial(k + 1) * math.factorial(n - k + 1) * math.factorial(
        3 * n - k + 4)))
    TAM_VALUES[n][k] = result
    return result

def T(*args):
    result = 0

    if len(args) == 1:
        n = args[0]

        for k in range(0, n + 2):
            for l in range(0, n + 2):
                for b in range(0, n + 1):
                    result += T(n, k, l, 0, b)
                    result += T(n, k, l, 1, b)
        return result

    elif len(args) == 3:
        n = args[0]
        k = args[1]
        l = args[2]

        if l == 0 or k == 0:
            return 0

        for b in range(0, n + 1):
            result += T(n, k, l, 0, b)
            result += T(n, k, l, 1, b)
        return result

    elif len(args) == 5:
        n = args[0]
        k = args[1]
        l = args[2]
        a = args[3]
        b = args[4]

        if l == 0 or k == 0:
            return 0

        if n == 0:
            if k == 1:
                if l == 1 and (a == 0 or a == 1) and b == 0:
                    return 1
                else:
                    return 0
            else:
                return 0

        if T5_VALUES[n][k][l][a][b] != -1:
            return T5_VALUES[n][k][l][a][b]

        if a == 0 and b == 0:
            result = 0
            for kp in range(k - 1, n + 1):
                result += T(n - 1, kp, l - 1)
            T5_VALUES[n][k][l][a][b] = result
            return result

        if a == 1 and b == n:
            result = 0

            for lp in range(l - 1, n + 1):
                result += T(n - 1, k - 1, lp)
            T5_VALUES[n][k][l][a][b] = result
            return result

        if a == 0 and b > 0:
            result = 0
            for i in range(0, k + 1):
                result += Tam(b - 1, i) * T(n - b, k - i, l, 0, 0)
            T5_VALUES[n][k][l][a][b] = result
            return result

        if a == 1:
            return 0

def S(*args):
    result = 0

    if len(args) == 1:
        n = args[0]

        for k in range(0, n + 2):
            for l in range(0, n + 2):
                for b in range(0, n + 1):
                    result += S(n, k, l, 0, b)
                    result += S(n, k, l, 1, b)
        return result

    elif len(args) == 3:
        n = args[0]
        k = args[1]
        l = args[2]

        if l == 0 or k == 0:
            return 0

        for b in range(0, n + 1):
            result += S(n, k, l, 0, b)
            result += S(n, k, l, 1, b)
        return result

    elif len(args) == 5:
        n = args[0]
        k = args[1]
        l = args[2]
        a = args[3]
        b = args[4]

        if l == 0 or k == 0:
            return 0

        if n == 0:
            if k == 1:
                if l == 1 and (a == 0 or a == 1) and b == 0:
                    return 1
                else:
                    return 0
            else:
                return 0

        if S5_VALUES[n][k][l][a][b] != -1:
            return S5_VALUES[n][k][l][a][b]

        if a == 0 and b == 0:
            result = 0
            for kp in range(k - 1, n + 1):
                result += S(n - 1, kp, l - 1)
            S5_VALUES[n][k][l][a][b] = result
            return result

        if a == 1 and b == n:
            result = 0

            for lp in range(l - 1, n + 1):
                result += S(n - 1, k - 1, lp)
            S5_VALUES[n][k][l][a][b] = result
            return result

        if a == 0 and b > 0:
            result = 0
            for i in range(0, k + 1):
                result += Tam(b - 1, i) * S(n - b, k - i, l, 0, 0)
            S5_VALUES[n][k][l][a][b] = result
            return result

        if a == 1:
            return S(n, l, k, 0, n - b)

if __name__ == '__main__':

    for n in range(0, MAX_STORE-1):
        print("|T("+str(n)+")| = ", T(n))
        print("|S("+str(n)+")| = ", S(n))
        print("")


