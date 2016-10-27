from simple_factory import Operator

class Calcultor:
    def __init__(self):
        self.operator = Operator

    def getResult(self, firstNumber, secondNumber, operatorSimble):
        return self.operator.getResult(self, firstNumber, secondNumber, operatorSimble)
