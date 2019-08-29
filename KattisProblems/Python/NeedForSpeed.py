class NeedForSpeed:
    def NFS():
        nt = input();
        nt = nt.split();
        n, t = int(nt[0]), float(nt[1]);
        dis = 0;
        speed = 0;
        for i in range(n):
            ds = input();
            ds = ds.split();
            d, s = float(ds[0]), float(ds[1]);
            dis += d;
            speed += s;
        avg_speed = dis/t;
        speed = speed/float(n);
        print(avg_speed-speed);


NeedForSpeed.NFS();


