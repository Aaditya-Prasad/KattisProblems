class Trick:
    def T():
        moves = input();
        l = len(moves);
        current = [1, 0, 0];

        for i in range(l):
            if moves[i] == 'A':
                current[0], current[1] = current[1], current[0];
            elif moves[i] == 'B':
                current[1], current[2] = current[2], current[1];
            else:
                current[0], current[2] = current[2], current[0];
        print(current.index(1) + 1);


Trick.T();
