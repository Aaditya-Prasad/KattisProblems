class onechickenperperson:
    def ocpp():
        nm = input();
        nm = nm.split();
        n, m = int(nm[0]), int(nm[1]);
        if ((n - m) == 1 or (m - n) == 1):
            r = "piece"
        else:
            r = "pieces"
        if(n > m):

            print(f"Dr. Chaz needs {n - m} more {r} of chicken!");
        elif(n < m):
            print(f"Dr. Chaz will have {m - n} {r} of chicken left over!");


onechickenperperson.ocpp();