import sys
from utils.MCFunctions import MCGate, MCpi


def callMCOption(MCname, sampleSize, gateName, numOfInputs):
    op = {"MCpi"    : "Pi",
          "MCGate"   : f"{gateName}{numOfInputs} Switching activity"}
    result = 0
    if MCname == "MCpi":
        result = MCpi(1, sampleSize)
    elif MCname == "MCGate":
        result = MCGate(gateName, numOfInputs, sampleSize)
    print(f" {MCname}: N = {sampleSize}, {op[MCname]} = {result: .5f}")
    print(" ---------------------------------------------------------------")  


def callMC(MCname = "MCGate", inputSampleSize = 0, gateName="AND", numOfInputs=2):
    inputs = [10, 100, 1000, 10000, 100000, 1000000]
    if inputSampleSize == 0:
        for n in inputs:
            callMCOption(MCname, n, gateName, numOfInputs)
    else:   callMCOption(MCname, inputSampleSize, gateName, numOfInputs)


def executeWhenIllegalArgument(MCname = "MCGate", msg=""):
    print(f"\n Note: Default values used. {msg}\n")  
    callMC(MCname)
     

def handleMenuOption(option):

    def handleMCGateInputs():
        gateNames = ["AND","NAND","OR","NOR","XOR","XNOR","NOT"]
        print(" Enter Gate name:", end=" ")
        gateName = input().strip().upper()
        if gateName not in gateNames: 
            executeWhenIllegalArgument("MCGate", f"The name of the gate must be one of the following: {gateNames}") 
            return 
        if gateName == "NOT":
            handleSampleSizeInput("MCGate", gateName, 1)
            return
        print(f" Enter the number of inputs for gate {gateName}:", end=" ")
        numOfInputs = input()
        if numOfInputs.isnumeric():
            numOfInputs = int(numOfInputs)
            if   numOfInputs <= 0:                      executeWhenIllegalArgument("MCGate", f"The number of inputs has to be a positive integer") 
            elif gateName != "NOT" and numOfInputs < 2: executeWhenIllegalArgument("MCGate", f"Gate {gateName} must have at least 2 inputs") 
            else:                                       handleSampleSizeInput("MCGate", gateName, numOfInputs)
        else:                                           executeWhenIllegalArgument("MCGate", f"The number of inputs has to be a positive integer") 

    def handleSampleSizeInput(MCname, gateName="", numOfInputs=0):
        print(" Enter sample size:", end=" ")
        sampleSize = input()
        if sampleSize.isnumeric() and sampleSize != "0":
            callMC(MCname, int(sampleSize), gateName, numOfInputs)
        else:
           executeWhenIllegalArgument(MCname, "Only one postive integer allowed as an argument for the sample size.") 
    
    if   option == 1:   callMC("MCpi")
    elif option == 2:   handleSampleSizeInput("MCpi")
    elif option == 3:   callMC()
    elif option == 4:   handleMCGateInputs()


def promtInput():
    print("\n Choose an option:", end=" ")
    option = input()
    while option not in ["1", "2", "3", "4", "5"]:
        print(" Please choose an option between 1 and 5:", end=" ")
        option = input()
    return int(option)


def displayMenu():
    print("\n-------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\tMonte Carlo Simulations")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("| (1) Monte Carlo Pi estimation                                    -> sample sizes = [10, 100, 1000, 10000, 100000, 1000000]  |")
    print("| (2) Monte Carlo Pi estimation                                    -> Enter a sample size                                     |")
    print("| (3) Monte Carlo 2 input AND Gate switching activity estimation   -> sample sizes = [10, 100, 1000, 10000, 100000, 1000000]  |")
    print("| (4) Monte Carlo X input Logic Gate switching activity estimation -> Enter a sample size                                     |")
    print("| (5) Exit                                                                                                                    |")
    print("-------------------------------------------------------------------------------------------------------------------------------")


def main(argv):
    if len(argv) == 1:
        displayMenu()
        option = promtInput()
        while option != 5:
            handleMenuOption(option)
            displayMenu()
            option = promtInput()
    else:
        print("No arguments allowed.")

if __name__ == "__main__":
    main(sys.argv)