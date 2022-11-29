import resolve_notation as rn

class LogicalStructure:
    polishNotations = []
    inputs = [0,0,0,0,0,0,0,0]
    outputs = [0,0,0,0,0,0,0,0]
    booleans = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def __init__(self, inputs, outputs, polishNotations):
        self.inputs = inputs
        self.outputs = outputs
        self.polishNotations = polishNotations

    def __str__(self):
        return f'LogicalStructure: [inputs: {self.inputs}, outputs: {self.outputs}, polishNotations: {self.polishNotations}'
    
    def updateOutputs(self):
        for polish in self.polisNotations:
            resolvedValue = rn.resolve(polish, self.inputs, self.outputs, self.booleans)
            
