import YaccKotoba
import virtualMachine

def parseCode(data) :
    YaccKotoba.parse(data)
    virtualMachine.execute_program()


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