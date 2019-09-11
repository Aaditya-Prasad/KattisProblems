class narrowartgallery:

    @staticmethod
    def nextto(a, b, c):
        x, y = c.index(a), c.index(b) #finding the rooms
        
    @staticmethod
    def nag():
        while(True):
            inp = input().split();
            inp = list(map(int, inp));
            if inp[0] == 0 and inp[1] == 0:
                break;
            rooms = [[], []]; #left is 0, right is 1
            blocked = [];
            for i in range(inp[0]):
                inpp = input().split();
                inpp = list(map(int, inpp));
                rooms[0].append(inpp[0]);
                rooms[1].append(inpp[1]);
            val = sum(map(sum, rooms));

            for i in range(inp[1]):
                minn = min([min(r) for r in rooms]);
                for b in blocked:
                    if b



narrowartgallery.nag();