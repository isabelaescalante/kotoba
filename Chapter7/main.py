import YaccKotoba
import virtualMachine

def parseCode(data) :

    YaccKotoba.parse(data)
    virtualMachine.execute_program()

def getFinalVariables() :
    return virtualMachine.finalVariables()

def getOutput() :
    return virtualMachine.printValues
    


if __name__ == '__main__':
    data = '''kotoba program1;
    
          declare number x, number f;

          function number fib(number n) {
              declare number a, number aAux, number b, number bAux;
               if(n < 2.0){
                   return n;
               }else{
                   set aAux = n - 1.0;
                   set bAux = n - 2.0;
                   set a = call fib(aAux);
                   set b = call fib(bAux);
                   return (a + b);
               }
           }

          begin
          {
              set x = 7.0;
              set f = call fib(x);
              kprint(f);
          }
          end
  '''

    parseCode(data)
    print(getFinalVariables())
    print("")
    print(getOutput())

