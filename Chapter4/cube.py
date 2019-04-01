class Cube:
    def __init__(self):
        self.cube = {}

        bools = {}
        numbers = {}
        words = {}
        sentences = {}

        bools['operator_not'] = 'bool'
        bools['operator_assign'] = 'bool'
        bools['operator_and'] = 'bool'
        bools['operator_or'] = 'bool'

        numbers['operator_assign'] = 'number'
        numbers['operator_add'] = 'number'
        numbers['operator_minus'] = 'number'
        numbers['operator_mult'] = 'number'
        numbers['operator_div'] = 'number'
        numbers['operator_greater'] = 'bool'
        numbers['operator_less'] = 'bool'
        numbers['operator_equal'] = 'bool'
        numbers['operator_notequal'] = 'bool'

        words['operator_assign'] = 'word'
        words['operator_add'] = 'sentence'
        words['operator_equal'] = 'bool'
        words['operator_notequal'] = 'bool'

        sentences['operator_assign'] = 'sentence'
        sentences['operator_equal'] = 'bool'
        sentences['operator_notequal'] = 'bool'

        self.cube['bool'] = bools
        self.cube['number'] = numbers
        self.cube['word'] = words
        self.cube['sentence'] = sentences

    def verification(self, operator, data_type1, data_type2):
        types = ['bool','number','word','sentence']

        if data_type1 in types:
            if data_type1 == data_type2:
                if operator in self.cube[data_type1]:
                    return self.cube[data_type1][operator]
                else:
                    return None
            elif 'operator_not' in self.cube[data_type1]:
                return self.cube[data_type1][operator]
            else:
                return None
        else:
            return None

if __name__ == '__main__':
    semantic = Cube()

    print(semantic.verification('operator_add','word', 'number'))
   
