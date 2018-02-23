def answer(str):
     # your code here
    # Note: * has a highest priority than +
    #       * in the most right has highest priority than the ones in the left
    #       i.e. (2*4*3) = (2*(4*3)) it does not matter from the value pres. though. 
    #   Data structure
    #   list of *, list of +, list of numbers, and the output str.
    #   Algorithm:
    #   1. read char from right
    #   2. Based of its type put it in its list
    #   3. if it is + or EOF, flush number list to output str, then * list.
    #   4. repeat 1-3 till input str is empty
    #   5. flush + list in the output str 
    #initialization
    outStr = ''
    plusList = ''
    multList = ''
    numberList = ''
    for c in str:
        if c == '+':
            #Step #3
            plusList += c  #add + to the list
            #flush numb and mult lists
            outStr += numberList
            numberList = ''
            outStr += multList
            multList = ''
        elif c == '*':
            multList += c
        else:
            numberList += c
    outStr += numberList
    outStr += multList
    outStr += plusList
    return outStr
    
    

f = answer('2+3*2')
f2 = answer('2*4*3+9*3+5')


        