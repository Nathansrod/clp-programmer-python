from .automaton import Automaton
from .constants import *

def simplifySentece(sentence):
    #Removing spaces
    sentence = sentence.replace(' ','') 

    #Sentence to uppercase
    sentence = sentence.upper()

    #Replaces I1, I2, ..., I8 with i:
    i = 0
    while i < len(INPUT_LABELS):
        print(f"SIMP: Replacing {INPUT_LABELS[i]} with i")
        sentence = sentence.replace(INPUT_LABELS[i], 'i')
        i += 1

    #Replaces O1, O2, ..., O8 with o:
    i = 0
    while i < len(OUTPUT_LABELS):
        print(f"SIMP: Replacing {OUTPUT_LABELS[i]} with o")
        sentence = sentence.replace(OUTPUT_LABELS[i], 'o')
        i += 1

    #Replaces B1, B2, ..., B8 with b:
    i = 0
    while i < len(BOOLEAN_LABELS):
        print(f"SIMP: Replacing {BOOLEAN_LABELS[i]} with b")
        sentence = sentence.replace(BOOLEAN_LABELS[i], 'b')
        i += 1

    #Checking if every char in sentence is present in the alphabet
    i = 0
    error = False
    while (i < len(sentence) and error == False):
        if not (sentence[i] in ALPHABET):
            error = True
        i += 1

    return (sentence, error)

        
def interpretSentece(sentence):
    automaton = Automaton()

    charIndex = 0
    stateIndex = 0
    error = False
    accepted = False

    original_sentence = sentence
    (sentence, simplifyError) = simplifySentece(sentence)
    print("SIMPLIFING SENTENCE...")
    print(f"simplified sentence: {sentence} simpError: {simplifyError}")

    if(simplifyError == False):
        while(error == False and accepted == False and charIndex < len(sentence)):

            currentChar = sentence[charIndex]    
            currentState = automaton.states[stateIndex]
            transitionIndex = -1

            i = 0
            
            print("VERYFING SENTENCE...")
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

        print("FINAL STEP...")
        print(f"stopState: {stateIndex}")
        if((stateIndex == 4 or stateIndex == 7 or stateIndex == 9) and not error):
            if(automaton.readFromStack('$')):
                print(f"Sentence: {original_sentence} is accepted")
            else:
                print(f"Sentence: {original_sentence} is rejected")    
        else:
            print(f"Sentence: {original_sentence} is rejected")

        if(error):
            print("Syntax error!")
    else:
        print("Invalid label!")
