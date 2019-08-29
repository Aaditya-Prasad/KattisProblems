class linethemup:
    def LTU():
        num = int(input());
        names = [];
        for i in range(num):
            name = input();
            names.append(name);
        bames = names[:];
        tames = names[:];
        tames.sort();
        bames.sort(reverse = True);
        if names == tames:
            print("INCREASING");
        elif names == bames:
            print("DECREASING");
        else:
            print("NEITHER");

linethemup.LTU();
