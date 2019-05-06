import YaccKotoba
import virtualMachine

def parseCode(data) :
    YaccKotoba.parse(data)
    virtualMachine.execute_program()


if __name__ == '__main__':
    data = '''kotoba program1;
        declare word w[4.0], number n, sentence s, number arr[5.0];

        begin
        {
            set s = "The dog is running.";
            set arr = {2.0, 34.5, 67.56, 4.1, 0.12};

            set w = call s.tokenize();

            set n = 0.0;

            set s = w[n] + w[1.0];

            kprint(w[n]);
            kprint(arr[3.0]);
            kprint(s);
        }
        end
    '''
    parseCode(data)