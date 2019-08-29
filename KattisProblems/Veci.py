import math


class Veci:
    def V():
        inp = input();
        num = [];
        sum = 0;
        x = len(inp);
        skip, solved = False, False;
        for i in range(x):
            num.append(int(inp[i]));
        i = 1;
        while not solved:
            for r in range(1, x - 1):
                if (num[-i] > num[-i - r]):
                    num[-i], num[-i - r] = num[-i - r], num[-i];
                    solved = True;
                    break;
            i += 1;
            if i >= x:
                solved = True;
                skip = True;
        if not skip:
            for i in range(x):
                sum += num[i] * 10 ** (x-i-1)
        print(sum)


Veci.V();
