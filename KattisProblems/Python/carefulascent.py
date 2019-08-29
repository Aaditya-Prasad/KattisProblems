class carefulascent:
    def CA():
        fir = input();
        fir = fir.split();
        firx, total_time = float(fir[0]), float(fir[1]);
        vo = firx/total_time;
        num = int(input());
        average_shield = float(0);
        time = total_time;
        for i in range(num):
            info = input();
            infoo = info.split();
            l, u, f = float(infoo[0]), float(infoo[1]), float(infoo[2]);
            ln = u - l;
            lnn = ln/total_time;
            average_shield += lnn * f;
            time -= ln;
        average_shield += time/total_time
        print(vo/average_shield);

carefulascent.CA();