class TheDragonOfLoowater:
    def TDOL():
        while(True):
            solved = False;
            line = input();
            if line == '0 0':
                break;
            newline = line.split();
            heads = int(newline[0]);
            knights = int(newline[1]);
            headss = [];
            knightss = [];
            for i in range(heads):
                headss.append(int(input()));
            for i in range(knights):
                knightss.append(int(input()));
            headss.sort();
            knightss.sort();
            cost = 0;
            p = 0;
            for i in range(heads):
                while not(solved):
                    h = headss[i];
                    for l in knightss:
                        p += 1;
                        if p == len(knightss):
                            print("Loowater is doomed");
                            break;
                        if l >= h:
                            cost += ld;
                            break;
