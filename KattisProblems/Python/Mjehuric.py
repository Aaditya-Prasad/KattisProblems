
class Mjehuric:
    def M():
        nums = input();
        num = nums.split(' ');
        nu = [];
        for i in range(5):
            nu.append(int(num[i]));

        while nu != [1, 2, 3, 4, 5]:
            for i in range(4):

                if nu[i] > nu[i+1]:
                    nu[i], nu[i+1] = nu[i+1], nu[i];
                    print(nu[0], nu[1], nu[2], nu[3], nu[4])


Mjehuric.M();