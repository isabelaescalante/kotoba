import YaccKotoba
import virtualMachine

def parseCode(data) :
    YaccKotoba.parse(data)
    virtualMachine.execute_program()


if __name__ == '__main__':
    data = '''kotoba program1;
        declare word w[4.0], number n, sentence s, number arr[5.0], number len;

        begin
        {
            set s = "The dog is running.";
            set arr = {2.0, 34.5, 67.56, 4.1, 0.12};

            set w = call s.tokenize();

            set n = 0.0;

            set len = call w.size();

            while(n < len) {
                kprint(w[n]);
                set n = n + 1.0;
            }

            set s = w[0.0] + w[1.0];

            kprint(s);

            set n = 0.0;
        }
        end
    '''
    parseCode(data)