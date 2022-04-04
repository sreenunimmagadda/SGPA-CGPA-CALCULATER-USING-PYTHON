import manage

def calc(res):
    if res == "O" or res == "o" or res == "S" or res == "s" or res == "A" or res == "a" or res == "B" or res == "b" or res == "C" or res == "c" or res == "D" or res == "d" or res == "F" or res == "f":
        if res == "O" or  res == "o":
            return 10
        elif res == "S" or res == "s":
            return 9
        elif res == "A" or res == "a":
             return 8
        elif res == "B" or res == "b":
             return 7
        elif res == "C" or res == "c":
             return 6
        elif res == "D" or res == "d":
             return 5
        elif res == "F" or res == "f":
             return 0
    elif res != "O" or res != "o" or res != "S" or res != "s" or res != "A" or res != "a" or res != "B" or res != "b" or res != "C" or res != "c" or res != "D" or res != "d" or res != "F" or res != "f":
        print("Please check your values....")
        manage.main()
    
#calc("a")
