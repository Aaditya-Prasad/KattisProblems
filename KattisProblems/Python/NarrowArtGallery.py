class narrowartgallery:
    def nag():
        while(True):
            inp = input().split();
            inp = map(int, inp);
            if inp[0] == 0 and inp[1] == 0:
                break;
            temp = [];
            for i in range(inp[0]):
                inpp = input().split();
                inpp = map(int, inpp);
                temp[0].append(inpp[0]);
                temp[1].append(inpp[1]);

print("Hello World");
