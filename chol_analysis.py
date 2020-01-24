def HDL_analysis(HDL_Level):
    if HDL_Level >= 60:
        return "Normal"
    elif 40 <= HDL_Level < 60:
        return "Borderline low"
    else:
        return "Low"

def cholesterol_analysis():
    print("cholesterol_analysis")
    HDLinput = input("Enter test result: ")
    test_info = HDLinput.split("=")
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("The cholesterol level is {}".format(answer))

def interface():
    choice = 0
    while choice != "9":
        print("Cholesterol Calculator")
        print("Options: ")
        print(" 1 - Cholesterol Analysis")
        print(" 9 - Quit")
        choice = input("Enter your option: ")
        if choice == '9':
            return
        elif choice == "1":
            cholesterol_analysis()
    

if __name__ == "__main__":
    interface()
