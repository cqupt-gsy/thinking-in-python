class Operator:
    def getResult(self, firstNumber, secondNumber, operatorSimble):
        operators = {'+': PlusOperator, '-': MinusOperator,
                '*': MultiOperator, '/': DivOperator}
        return operators.get(operatorSimble).getResult(self, firstNumber, secondNumber)

class PlusOperator:
    def getResult(self, firstNumber, secondNumber):
        return firstNumber + secondNumber

class MinusOperator:
    def getResult(self, firstNumber, secondNumber):
        return firstNumber - secondNumber

class MultiOperator:
    def getResult(self, firstNumber, secondNumber):
        return firstNumber * secondNumber

class DivOperator:
    def getResult(self, firstNumber, secondNumber):
        if ( 0 == secondNumber):
            raise ValueError('Second number can not be zero')
        return firstNumber / secondNumber

