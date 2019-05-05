import YaccKotoba
import virtualMachine

if __name__ == '__main__':
    data = '''kotoba program1;
        declare number z;

        function number fib(number n) {
            if(n < 2.0) {
                return n;
            } 

            return ;
        }

        begin
        {
            set z = 5.0;
            call fib(z);
        }
        end
    '''

    YaccKotoba.parse(data)

    virtualMachine.execute_program()
    