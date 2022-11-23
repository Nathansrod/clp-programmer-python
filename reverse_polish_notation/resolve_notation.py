import constants

def resolve(notation, inputs, outputs, booleans):
  in_out = []
  
  index = 0

  while(index < len(notation)):
    if notation[index] not in constants.OPERATORS:
      address = int(notation[index][1])
      if notation[index][0] == 'i':
        notation[index] = inputs[address - 1]
      elif notation[index][0] == 'o':
        notation[index] = outputs[address - 1]
      elif notation[index][0] == 'b':
        notation[index] = booleans[address - 1]
    index += 1

  for item in notation:
    if item not in constants.OPERATORS:
      in_out.append(item)
    else:
      if item == constants.OPERATORS[2]:
        operand = in_out.pop()
        operation = not operand
        in_out.append(operation)
      else:
        frist_op = in_out.pop()
        second_op = in_out.pop()
        if item == constants.OPERATORS[0]:
          operation = frist_op and second_op
          in_out.append(operation)
        elif item == constants.OPERATORS[1]:
          operation = frist_op or second_op
          in_out.append(operation)

  return in_out
