import argparse
from NLUDefault import NLUDefault
from NLGDefault import NLGDefault
from FSM import FSM

def main():
    parser = argparse.ArgumentParser("Homework 1 dialog manager system")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-s", "--system", choices=["FSM"])
    parser.add_argument("-l", "--NLU", default="Default")
    parser.add_argument("-g", "--NLG", default="Default")
    args = parser.parse_args()
    
    system = args.system
    NLU = args.NLU
    NLG = args.NLG
    
    print("NLU = {}, system = {}, NLG = {}".format(NLU, system, NLG))
   
    NLUModule = None
    DMModule = None
    NLGModule = None

    if NLU == "Default":
        NLUModule = NLUDefault()

    if NLG == "Default":
        NLGModule = NLGDefault()

    if system == "FSM":
        DMModule = FSM(NLUModule, NLGModule)
    else:
        print("{} not implemented".format(system))
        return
 
    print("Welcome to the HW2 Dialog System")
    while True:
        inputStr = input("> ")
        if inputStr == "Quit":
            break

        try:
            outputStr = DMModule.execute(inputStr)
        except Exception as e:
            print(e)
            break

        print(outputStr)
        

if __name__ == "__main__":
    main()
