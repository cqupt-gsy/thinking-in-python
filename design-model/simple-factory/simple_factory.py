class Operator:
    @staticmethod
    def getResult(firstNumber, secondNumber, operatorSample):
        operators = {'+': PlusOperator, '-': MinusOperator,
                     '*': MultiOperator, '/': DivOperator}
        return operators.get(operatorSample).getResult(firstNumber, secondNumber)


class PlusOperator:
    @staticmethod
    def getResult(firstNumber, secondNumber):
        return firstNumber + secondNumber


class MinusOperator:
    @staticmethod
    def getResult(firstNumber, secondNumber):
        return firstNumber - secondNumber


class MultiOperator:
    @staticmethod
    def getResult(firstNumber, secondNumber):
        return firstNumber * secondNumber


class DivOperator:
    @staticmethod
    def getResult(firstNumber, secondNumber):
        if 0 == secondNumber:
            raise ValueError('Second number can not be zero')
        return firstNumber / secondNumber
