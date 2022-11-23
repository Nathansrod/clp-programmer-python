class Transition:
    char = ''
    read = ''               #from stack
    push = ''               #into stack
    targetState = -1

    def __init__(self, char, read, push, targetState):
        self.char = char
        self.read = read
        self.push = push
        self.targetState = targetState

    def __str__(self):
        return f"\n\t\tTransition: [char:{self.char}, read:{self.read}, push:{self.push}, targetState:{self.targetState}]"


class State:
    transitions = []
    isFinal = False

    def __init__(self, transitions, isFinal):
        self.transitions = transitions
        self.isFinal = isFinal
    
    def __str__(self):
        retString = "State:[transitions:["
        for transition in self.transitions:
            retString = f"{retString} ({transition})"
        retString = f"{retString}],\n\tisFinal:{self.isFinal}]"
        return retString

class Automaton:
    states = []
    stack = []

    def __init__(self) -> None:
        #State 0
        self.states.append(State(
            [Transition('?', '?', '$', 1)],
            False
        ))
        #State 1
        self.states.append(State(
            [Transition('o','?','?',2),
             Transition('b','?','?',2)],
            False
        ))
        #State 2
        self.states.append(State(
            [Transition('=','?','?',3)],
            False
        ))
        #State 3
        self.states.append(State(
            [Transition('!','?','?',5),
             Transition('(','?','X',8),
             Transition('i','?','?',4),
             Transition('o','?','?',4),
             Transition('b','?','?',4)],
            False
        ))
        #State 4
        self.states.append(State(
            [Transition(')','X','?',4),
             Transition('?','$','?',10),
             Transition('|','?','?',6),
             Transition('^','?','?',6)],
            False
        ))
        #State 5
        self.states.append(State(
            [Transition('(','?','X',8),
             Transition('i','?','?',7),
             Transition('o','?','?',7),
             Transition('b','?','?',7)],
            False
        ))
        #State 6
        self.states.append(State(
            [Transition('(','?','X',8),
             Transition('i','?','?',9),
             Transition('o','?','?',9),
             Transition('b','?','?',9),
             Transition('!','?','?',5)],
            False
        ))
        #State 7
        self.states.append(State(
            [Transition('^','?','?',6),
             Transition('|','?','?',6),
             Transition('?','$','?',10),
             Transition(')','X','?',4)],
            False
        ))
        #State 8
        self.states.append(State(
            [Transition('(','?','X',8),
             Transition('i','?','?',11),
             Transition('o','?','?',11),
             Transition('b','?','?',11),
             Transition('!','?','?',5)],
            False
        ))
        #State 9
        self.states.append(State(
            [Transition(')','X','?',4),
             Transition('?','$','?',10)],
            False
        ))
        #State 10
        self.states.append(State(
            [],
            True
        ))
        #State 11
        self.states.append(State(
            [Transition('^','?','?',12),
             Transition('|','?','?',12),
             Transition(')','X','?',4)],
            False
        ))
        #State 12
        self.states.append(State(
            [Transition('i','?','?',13),
             Transition('o','?','?',13),
             Transition('b','?','?',13),
             Transition('(','?','X',8)],
            False
        ))
        #State 13
        self.states.append(State(
            [Transition(')','X','?',4)],
            False
        ))

    def __str__(self):
        retString = "Automaton:[states:["
        i = 0
        for state in self.states:
            retString = f"{retString}\n\t{i}:[{state}]"
            i += 1
        retString = retString + "]"
        return retString

    #Prints the stack
    def showStack(self):
        print(f"Automaton Stack: {self.stack}")

    #Pushes a value into the stack
    def pushToStack(self, char):
        self.stack.append(char)
        print(f"Added {char} into the stack {self.stack}")

    #Reads the lastVale in the stack. if it's equal to the
    #returns true if lastValue == char, returns false otherwise
    def readFromStack(self, char):
        lastIndex = len(self.stack) - 1
        lastValue = self.stack[lastIndex]
        if(lastValue == char):
            self.stack.pop()
            print(f"Read {char} from stack {self.stack}")
            return True
        else:
            return False