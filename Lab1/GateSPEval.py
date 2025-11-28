import sys
from utils.spNGate import evaluateSpFunction

def executeDefaultExamples():
    gates = ["AND", "NAND", "OR", "NOR", "XOR", "XNOR"]
    for gateName in gates:
        evaluateSpFunction(gateName, [0.5, 0.5])
        evaluateSpFunction(gateName, [0.5, 0.5, 0.5])
    evaluateSpFunction("NOT", 0.5)

def getInputSPs():
    errorMsg = "\n Error: The signal probabilties of the inputs must have values inside the range [0,1] and they have to be separated by \",\"."
    inputSPsString = input()
    inputSPsList = inputSPsString.split(",")
    inputsSPs = []
    for iSPs in inputSPsList:
        try:
            prob = float(iSPs.strip())
            if prob >= 0.0 and prob <= 1.0:
                prob = round(prob, 5)
                inputsSPs.append(prob)
            else:
                raise Exception(errorMsg)
        except ValueError:
            print(errorMsg)
            return False, None
        except Exception as e:
            print(e)
            return False, None

    return True, inputsSPs

def executeWhenIllegalArgument():
    print("\n ### Executing default examples ###")
    executeDefaultExamples()
    print("\n\n Note: Something went wrong with your input so the default examples were executed instead.\
           \n       Scroll up to see the error message(s).")   


def promtGateNameAndISPsInput():
    print(" Enter gate name:", end=" ")
    gateName = input().strip().upper()

    print(" Enter the signal probabilities of the inputs seperated by \",\":", end=" ")
    inputsSuccess, inputsNsp = getInputSPs()

    if not inputsSuccess  or evaluateSpFunction(gateName, inputsNsp) == -1 :
        executeWhenIllegalArgument() 


def handleMenuOption(option):
    if option == 1:
        executeDefaultExamples()
    elif option == 2:
        promtGateNameAndISPsInput()
    

def promtInput():
    print("\n Choose an option:", end=" ")
    option = input()
    while option not in ["1", "2", "3"]:
        print(" Please choose an option between 1 and 3:", end=" ")
        option = input()
    print()
    return int(option)

def displayMenu():
    print("\n---------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\tSignal Probability evaluation of a Gate")
    print("---------------------------------------------------------------------------------------------------------------------")
    print("| (1) Execute default examples                                                                                      |")
    print("| (2) Enter the gate name and the signal probabilities of the inputs                                                |")
    print("| (3) Exit                                                                                                          |")
    print("---------------------------------------------------------------------------------------------------------------------")


def main(argv):
    if len(argv) == 1:
        displayMenu()
        option = promtInput()
        while option != 3:
            handleMenuOption(option)
            displayMenu()
            option = promtInput()
    else:
        print("No arguments allowed.")


main(sys.argv)
