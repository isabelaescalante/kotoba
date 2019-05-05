import YaccKotoba
import virtualMachine

if __name__ == '__main__':
    data = '''kotoba program1;
        declare number x, number f;
        
        function number fib(number n) {
            declare number a, number aAux, number b, number bAux;
            kprint("n = ");
            kprint(n);

           if(n < 2.0){
               kprint("N is < 2");
              return n;
           }else{
               kprint("N is NOT < 2");
               set aAux = n - 1.0;
               set bAux = n - 2.0;
               set a = call fib(aAux);
               set b = call fib(bAux);
               kprint("a = ");
               kprint(a);
               kprint("b = ");
               kprint(b);
               return (a + b);
          }
      }


        begin
        {
           set x = 3.0;
           set f = call fib(x);
           kprint(f);
        }
        end
    '''

    YaccKotoba.parse(data)

    virtualMachine.execute_program()
    