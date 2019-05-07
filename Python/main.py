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

           set s=w[0.0]+w[1.0];

           kprint(s);

           set n = 0.0;
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

    
    filename = "file:///Users/isaescalante96/Desktop/Tec/Octavo_Semestre/Compiladores/Kotoba/Interface/index.html"
        
    webbrowser.open_new_tab(filename)

