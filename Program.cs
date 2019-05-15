using System;
using System.Collections;


namespace KattisProblems
{
    class Program
    {
        static void Main(string[] args)
        {
            Qbf.Run();
            //thiswaspushed
            //thiswasalsopushed
        }
    }
    class Qbf
    {
        public static void Run()
        {
            string x = Console.ReadLine();
            int num = Int32.Parse(x);
            int i, id;
            string[] r = new string[num];
            ArrayList al = new ArrayList(26);

            al.Add('a');
            al.Add('b');
            al.Add('c');
            al.Add('d');
            al.Add('e');
            al.Add('f');
            al.Add('g');
            al.Add('h');
            al.Add('i');
            al.Add('j');
            al.Add('k');
            al.Add('l');
            al.Add('m');
            al.Add('n');
            al.Add('o');
            al.Add('p');
            al.Add('q');
            al.Add('r');
            al.Add('s');
            al.Add('t');
            al.Add('u');
            al.Add('v');
            al.Add('w');
            al.Add('x');
            al.Add('y');
            al.Add('z');
            for (i = 0; i < num; i++)
            {
                r[i] = Console.ReadLine();
            }
            for (i = 0; i < num; i++)
            {

                ArrayList ml = new ArrayList(26);
                ml = (ArrayList)al.Clone();
                char[] s = r[i].ToCharArray();

                //int[] ide = new int[26];
                int l = s.Length;
                // string l1 = l.ToString();
                for (id = 0; id < l; id++)
                {
                    int ind = ml.IndexOf(char.ToLower(s[id]));
                    if (ind > -1)
                    {
                        ml.RemoveAt(ind);
                    }
                    // char re = Convert.ToChar(al[id]);
                    // if(s[id] == re){
                    //   al.RemoveAt(id);
                    //   Console.WriteLine(s[id]);
                    // Console.WriteLine(id.ToString());
                    // }
                }

                if (ml.Count == 0)
                {
                    Console.Write("pangram");
                }
                else
                {
                    Console.Write("missing ");
                    foreach (char c in ml)
                    {
                        Console.Write(c);
                    }
                }
                Console.WriteLine();
                ml.Clear();
            }


        }
    }
}


