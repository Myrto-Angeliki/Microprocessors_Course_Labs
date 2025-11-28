def displayGateSp(gateName, inputsNsp, ans):
    opt = "probabilities" if gateName != "NOT" else "probability"
    if not (type(ans) is list):
        print(f"\n {gateName} Gate signal probability output for input {opt} {inputsNsp}: {ans: .5f}")
    else:
        for inSp, outSp in zip(inputsNsp, ans):
           print(f"\n {gateName} Gate signal probability output for input {opt} {inSp}: {outSp: .5f}") 
    print("--------------------------------------------------------------------------------------------")


def displayStart(endString = ""):
    print("\n--------------------------------------------------------------------------------------------")
    print(f" ### Executing signal probability evaluation of {endString} gate ###")


def getFinalSp(gateName, s):
    gates = ["XNOR", "OR", "NAND"]
    if gateName in gates:
        return (1.0-s)
    else:
        return s


def getPartialSpOfGate(gateName, s, inputSp):
    if gateName == "AND" or gateName == "NAND":
        return s*inputSp
    elif gateName == "OR" or gateName == "NOR":
        return s*(1.0-inputSp)
    elif gateName == "XOR" or gateName == "XNOR":
        return (s*(1.0-inputSp) + (1.0-s)*inputSp)
    else:
        return s

def initializeS(gateName, fisrtSp):
    if gateName == "OR" or gateName == "NOR":
        return (1.0 - fisrtSp)
    else:
        return fisrtSp
    

def getSpOfNGate(inputsNsp, gateName, displayMode=1):
    if displayMode==1: displayStart(f"a {len(inputsNsp)}-input {gateName}")
    s = initializeS(gateName, inputsNsp[0])
    for inputSp in inputsNsp[1:]:
        s = getPartialSpOfGate(gateName, s, inputSp)
    s = getFinalSp(gateName, s)
    if displayMode==1: displayGateSp(gateName, inputsNsp, s)
    return s


def handleNotGate(inputsNsp, displayMode=1):
    if displayMode==1: displayStart("a NOT")
    if not (type(inputsNsp) is list):
        sp = (1.0 - inputsNsp)
    elif len(inputsNsp) == 1:
        sp = (1.0 - inputsNsp[0])
        inputsNsp = inputsNsp[0]
    else:
        if displayMode==1: print(f"\n Warning: a NOT gate has only one input. {len(inputsNsp)} NOT gates will be created for each input.")
        sp = [(1.0 - sp) for sp in inputsNsp]
    if displayMode==1: displayGateSp("NOT", inputsNsp, sp)
    return sp


def checkForNotGate(gateName):
    if gateName != "NOT":   return False
    else:                   return True
    

def checkForNumOFInputs(gateName, inputsNsp):
    if len(inputsNsp) > 1:
        return True
    else:
        print(f"\n Error: {gateName} must have at least two inputs.")
        return False


def checkGateName(gateName):
    validGateNames = ["AND", "NAND", "OR", "NOR", "XOR", "XNOR", "NOT"]
    if gateName in validGateNames:
        return True
    else:
        print(f"\n Error: The name of the gate must be one of the following: {validGateNames}.")
        return False
    
def evaluateSpFunction(gateName, inputsNsp, displayMode=1):
    if checkGateName(gateName): 
        if not checkForNotGate(gateName):
            if checkForNumOFInputs(gateName, inputsNsp):
                return getSpOfNGate(inputsNsp, gateName, displayMode)
            else:
                return -1
        else:
            return handleNotGate(inputsNsp, displayMode)
    else:
        return -1
