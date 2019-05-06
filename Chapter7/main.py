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
declare number x;
begin
{
    set x = 4.0/2.0;
    kprint(x);
}
end
  '''
    
    parseCode(data)
    print(getFinalVariables())
    print("")
    print(getOutput())
