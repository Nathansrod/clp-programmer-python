from automaton import *

automaton = Automaton()

print("Type the sentence: ")
sentence = input()

charIndex = 0
stateIndex = 0
error = False
accepted = False

while(error == False and accepted == False and charIndex < len(sentence)):

    currentChar = sentence[charIndex]    
    currentState = automaton.states[stateIndex]
    transitionIndex = -1

    i = 0

    print(f"currentChar: {currentChar}")
    print(f"currentState: {stateIndex}")

    #Search for a transition that reads the currentChar
    while(i < len(currentState.transitions)):
        if(currentState.transitions[i].char == currentChar):
            transitionIndex = i
        i += 1

    #Found a transition - THIS TRANSITION IS NOT AN EMPTY TRANSITION
    if(transitionIndex != -1):
        transition = currentState.transitions[transitionIndex]
        print(f"Found normal transition: {transition}")

        #This transition reads from the stack
        if(transition.read != '?'):
            if(automaton.readFromStack(transition.read)):
                stateIndex = transition.targetState
                charIndex += 1
            else:
                error = True #Error, as the automaton couldn't read the char in the stack
        elif(transition.push != '?'): #This transition pushes into the stack
            automaton.pushToStack(transition.push)
            stateIndex = transition.targetState
            charIndex += 1
        else: #This transition does nothing to the stack
            stateIndex = transition.targetState
            charIndex += 1
    else: #Didn't find a normal transition, so let's search for an empty transition
        i = 0
        while(i < len(currentState.transitions)):
            if(currentState.transitions[i].char == '?'):
                transitionIndex = i
            i += 1

        #Found an empty transition - THIS TRANSITION DOESN'T INCREMENT charIndex
        if(transitionIndex != -1):
            transition = currentState.transitions[transitionIndex]
            print(f"Found empty transition: {transition}")

            #This transition reads from the stack
            if(transition.read != '?'):
                if(automaton.readFromStack(transition.read)):
                    stateIndex = transition.targetState
                else:
                    error = True #Error, as the automaton couldn't read the char in the stack
            elif(transition.push != '?'): #This transition pushes into the stack
                automaton.pushToStack(transition.push)
                stateIndex = transition.targetState
            else: #This transition does nothing to the stack
                stateIndex = transition.targetState
        else: #Couldn't find an empty transition. This is an error
                error = True


print(f"stopState: {stateIndex}")
if(stateIndex == 4 or stateIndex == 7 or stateIndex == 9):
    if(automaton.readFromStack('$')):
        print(f"Sentence: {sentence} is accepted")
    else:
        print(f"Sentence: {sentence} is rejected")    
else:
    print(f"Sentence: {sentence} is rejected")

if(error):
    print(f"Error!")
