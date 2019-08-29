class Aaah:
    def count(inp):
        counte = 0;
        for c in inp:
            if c == 'a':
                counte += 1;
        return counte;

    def A():
        first = input();
        second = input();
        if (Aaah.count(second) <= Aaah.count(first)):
            print('go');
        else:
            print('no');

Aaah.A();
