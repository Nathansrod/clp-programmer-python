from .resolve_notation import resolve

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
            resolvedValue = resolve(polish, self.inputs, self.outputs, self.booleans)
            print(f"\t>RESOLVING: identifier:{identifier} polish:{polish} resolvedValue:{resolvedValue}")
            address = int(identifier[1]) - 1
            if(identifier[0] == 'O'):
                self.outputs[address] = resolvedValue
            elif(identifier[0] == 'B'):
                self.booleans[address] = resolvedValue
        print(f"Outputs updated in LogicalStructure, outputs: {self.outputs}")
        return self.outputs

    def clearPolish(self):
        self.polishNotations.clear()
        print("Polish notations cleared in LogicalStructure")

    def updatePolishNotations(self, polishNotations):
        self.clearPolish()
        self.polishNotations = polishNotations
        print(f"Polish notations updated in LogicalStructure, polishNotations: {self.polishNotations}")

    def updateInputs(self, inputs):
        self.inputs = inputs
        print(f"Inputs updated in LogicalStructure, inputs: {self.inputs}")

    def updateBooleans(self, booleans):
        self.booleans = booleans
        print(f"Booleans updated in LogicalStructure, booleans: {self.booleans}")

    def resetStructure(self):
        self.inputs = [False,False,False,False,False,False,False,False]
        self.outputs = [False,False,False,False,False,False,False,False]
        self.booleans = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]