from simple_factory import Operator

class Calculator:
    def __init__(self):
        self.operator = Operator

    def getResult(self, firstNumber: object, secondNumber: object, operatorSample: object) -> object:
        self.operator = Operator
        return self.operator.getResult(firstNumber, secondNumber, operatorSample)

