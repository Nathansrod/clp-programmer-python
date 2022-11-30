from .constants import OPERATORS

def resolve(notation, inputs, outputs, booleans):
    in_out = []
    
    index = 0
    notation_resolve = []

    for index in range(0, len(notation)):
        if notation[index] not in OPERATORS:
            address = int(notation[index][1])
            if notation[index][0] == 'I':
                notation_resolve.insert(index, inputs[address - 1])
            elif notation[index][0] == 'O':
                notation_resolve.insert(index, outputs[address - 1])
            elif notation[index][0] == 'B':
                if len(notation[index]) == 3:
                    address = int(notation[index][1::])
                notation_resolve.insert(index, booleans[address - 1])
        else:
            notation_resolve.insert(index, notation[index])
        index += 1

    for item in notation_resolve:
        if item not in OPERATORS:
            in_out.append(item)
        else:
            if item == OPERATORS[2]:
                operand = in_out.pop()
                operation = not operand
                in_out.append(operation)
            else:
                frist_op = in_out.pop()
                second_op = in_out.pop()
                if item == OPERATORS[0]:
                    operation = frist_op and second_op
                    in_out.append(operation)
                elif item == OPERATORS[1]:
                    operation = frist_op or second_op
                    in_out.append(operation)

    return in_out[0]
