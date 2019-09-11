class sumkindofproblem:
    def skop():
        n = int(input());
        for i in range(n):
            ln = input().split();
            x = int(ln[1]);
            first = x * (x + 1)/2;
            odd = x**2;
            even = x**2 + x;
            print(f"{ln[0]} {int(first)} {odd} {even}");

sumkindofproblem.skop();