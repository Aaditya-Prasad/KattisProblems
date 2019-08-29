class Janitor_Troubles:
    def JT():
        import math;

        # max area = sqrt((s-a)(s-b)(s-d)(s-c))

        sides = input();
        sidess = sides.split(' ');
        a, b, c, d = float(sidess[0]), float(sidess[1]), float(sidess[2]), float(sidess [3]);
        s = a + b + c + d;
        s = s/2;
        inside = (s-a)*(s-b)*(s-c)*(s-d);
        insides = float(inside);

        result = math.sqrt(insides);

        print(result);


Janitor_Troubles.JT();

