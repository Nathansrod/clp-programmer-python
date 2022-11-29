import resolve_notation as rn

class LogicalStructure:
    polishNotations = []
    inputs = [False,False,False,False,False,False,False,False]
    outputs = [False,False,False,False,False,False,False,False]
    booleans = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    def __init__(self, polishNotations):
        self.polishNotations = polishNotations

    def __str__(self):
        return f'LogicalStructure: [inputs: {self.inputs}, outputs: {self.outputs}, polishNotations: {self.polishNotations}'
    
    def updateOutputs(self):
        for polishTuple in self.polishNotations:
            identifier = polishTuple[0]
            polish = polishTuple[1]
            resolvedValue = rn.resolve(polish, self.inputs, self.outputs, self.booleans)
            address = int(identifier[1]) - 1
            if(identifier[0] == 'O'):
                self.outputs[address] = resolvedValue
            elif(identifier[0] == 'B'):
                self.booleans[address] = resolvedValue

    def clearPolish(self):
        self.polishNotations.clear()
        print("Polish notations cleared in LogicalStructure")

    def updatePolishNotations(self, polishNotations):
        self.clearPolish()
        self.polishNotations = polishNotations
        print("Polish notations updated in Logical Structure")

    def updateInputs(self, inputs):
        self.inputs = inputs
        print("Inputs updated in LogicalStructure")

    def updateBooleans(self, booleans):
        self.booleans = booleans
        print("Booleans updated in LogicalStructure")