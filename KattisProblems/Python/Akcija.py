class akcija:
    def a():
        n = int(input());
        price = 0;
        prices = [];
        for i in range(n):
            prices.append(int(input()));
        prices.sort(reverse = True);
        for i in range(n):
            price += prices[i];
        x = int(n/3);
        for i in range(1, x+1):
            price -= prices[3*i - 1];
        print(price);

akcija.a();