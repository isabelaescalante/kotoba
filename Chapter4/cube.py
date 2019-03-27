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
        numbers['operator_greater'] = 'number'
        numbers['operator_less'] = 'number'
        numbers['operator_equal'] = 'number'
        numbers['operator_notequal'] = 'number'

        words['operator_assign'] = 'word'
        words['operator_add'] = 'sentence'

        sentences['operator_assign'] = 'sentence'

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
   
