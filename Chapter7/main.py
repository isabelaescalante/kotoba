import YaccKotoba
import virtualMachine

if __name__ == '__main__':
    data = '''kotoba program1;
      
           declare number x;

           function void fib(number n) {
                declare number a, number b, number aux, number i;

                set a = 0.0;
                set b = 1.0;
                set i = 2.0;
                kprint(a);
                kprint(b);

                while(i < (n + 1.0)) {
                    set aux = a + b;
                    set a = b;
                    set b = aux;
                    set i = i + 1.0;
                    kprint(aux);
                }
                
               
                return "void";
       }


           begin
           {
               set x = 7.0;
               call fib(x);
           }
           end
   '''



    YaccKotoba.parse(data)

    virtualMachine.execute_program()
    