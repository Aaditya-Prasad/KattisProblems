
class Job_Expenses:
    def JE():
        f = int(input());
        d = input();
        bank = 0;
        debt = 0;
        r = d.split();
        for i in range(f):
            s = int(r[i]);
            if s > 0:
                bank += s;
            else:
                debt -= s;
        if (bank >= debt):
            print(debt);
        else:
            print(debt);


Job_Expenses.JE();