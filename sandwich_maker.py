import pyinputplus as pyip, sys, copy

BREAD = {'wheat': 1, 'white': 1.5, 'sourdough': 2}
PROTEIN = {'chicken': 2, 'turkey': 3, 'ham': 2.5, 'tofu': 3}
CHEESE = {'cheddar': 2, 'swiss': 2, 'mozarella': 1.5}
MISC = {'mayo': 0.5, 'mustard': 0.5, 'lettuce': 1, 'tomato': 1}

def single_selector(tastyDict, sandwichList, sandwichNo):
    response = pyip.inputChoice(choices=list(tastyDict.keys()))
    sandwichList[1][sandwichNo].append(response)
    sandwichList[2][sandwichNo] += tastyDict[response]
    return None

def multiple_selector(tastyDict, sandwichList, sandwichNo):
    tempDict = copy.deepcopy(tastyDict)
    counter = 0
    while True:
        if len(tempDict) == 0:
            print("No more to add from this group, exiting")
            break
        else:
            if counter == 0:
                response = pyip.inputChoice(choices=list(tempDict.keys()))
                sandwichList[1][sandwichNo].append(response)
                sandwichList[2][sandwichNo] += tempDict[response]
                tempDict.pop(response)
                counter += 1
            else:
                if pyip.inputYesNo(prompt="Do you want to add more options?\n") in ("yes", "y"):
                    response = pyip.inputChoice(choices=list(tempDict.keys()))
                    sandwichList[1][sandwichNo].append(response)
                    sandwichList[2][sandwichNo] += tempDict[response]
                    tempDict.pop(response)
                    counter += 1
                else:
                    break
    return None


if __name__=='__main__':    
    print("Please point the number of sandwiches: ")
    sandwichNumber = pyip.inputNum(min=1)
    sandwichList = [list(range(sandwichNumber)), [[] for i in range(sandwichNumber)], [0]*sandwichNumber]   # [0] -> list of sandwich no, [1] -> list of lists of sandwich content, [2] -> list of sandwich price
    print("\n")
    for i in range(sandwichNumber):
        print(f"Please select options for sandwich number {i+1}" + "\n" + "-" * 50)
        print("Please select bread type.")
        single_selector(BREAD, sandwichList, i)
        print("Please select protein type.")
        single_selector(PROTEIN, sandwichList, i)  
        if pyip.inputYesNo(prompt="Do you want cheese?\n") in ("yes", "y"):
            print("Please select cheese type.")
            single_selector(CHEESE, sandwichList, i)
        if pyip.inputYesNo(prompt="Do you want mayo, mustard, lettuce or tomato?\n") in ("yes", "y"):
            multiple_selector(MISC, sandwichList, i) 
    print("Your ordered sandwiches are: ")
    for i in range(sandwichNumber):
        print(f"{i+1} sandwich is: ")
        print(sandwichList[1][i])
        print(f"It costs {sandwichList[2][i]} dollars")