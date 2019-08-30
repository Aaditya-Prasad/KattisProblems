
class platform:
    def __init__(self, y, x1, x2):
        self.y = y;
        self.x1 = x1;
        self.x2 = x2;
        # self.range = [];
        # for i in range(int((x2-x1)/.5)):
        #     self.range.append(x1+.5*i);
        #     pass


class platforme:
    def p():
        total = 0;
        n = int(input());
        platforms = [];
        for i in range(n):
            ln = input().split();
            temp = platform(int(ln[0]), int(ln[1]), int(ln[2]));
            platforms.append(temp);
        temp = platform(0, 0, 10000);
        platforms.append(temp);
        for i in range(len(platforms)-1):
            current1 = 10000;
            current2 = 10000;
            rn = platforms[i];
            plats = platforms[:];
            plats.pop(i);
            for p in plats:
                if p.x1 < rn.x1 + .5 < p.x2:
                    if 0 < rn.y - p.y < current1:
                        current1 = rn.y - p.y;
                if p.x1 < rn.x2 - .5 < p.x2:
                    if 0 < rn.y - p.y < current2:
                        current2 = rn.y - p.y;
            total += current1 + current2;
        print(total);

platforme.p();




