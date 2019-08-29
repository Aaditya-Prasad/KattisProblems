class Secure_Doors:
    def SD():
        cases = int(input());
        logger = [];
        for i in range(cases):
            log = input();
            logs = log.split();
            action = logs[0];
            name = logs[1];
            if(action == 'entry'):
                if name in logger:
                    print(f"{name} entered (ANOMALY)");
                else:
                    print(f"{name} entered");
                    logger.append(name);
            else:
                if name in logger:
                    print(f"{name} exited");
                    logger.remove(name);
                else:
                    print(f"{name} exited (ANOMALY)");

        pass;



Secure_Doors.SD();
