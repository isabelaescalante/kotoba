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
    code = ''

    fileCode = open("code.txt","r")

    if fileCode.mode == 'r':
        code = fileCode.read()

    fileCode.close()

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
