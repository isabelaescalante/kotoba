import YaccKotoba
import virtualMachine
import json
import os
import webbrowser

def parseCode(data) :

    YaccKotoba.parse(data)
    virtualMachine.execute_program()

def getFinalVariables() :
    return virtualMachine.finalVariables()

def getOutput() :
    return virtualMachine.printValues

def getInputs() :
    return virtualMachine.inputValues
    


if __name__ == '__main__':
    code = '''kotoba program1;
    
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


    parseCode(code)
    variables = getFinalVariables()
    output = getOutput()
    inputs = getInputs()
    
    data = {
        "code" : code,
        "input" : inputs,
        "variables" : variables,
        "output" : output
    }
    
    with open('result_files/compilationResult.json', 'w') as f:
        json.dump(data, f)


    filename = 'file:///Users/isaescalante96/Desktop/Tec/Octavo%20Semestre/Compiladores/Kotoba/Interface/index.html'

    webbrowser.open_new_tab(filename)
