import sgp3_1 as t1
import sys,time

def main():
    while True:
        print("1. First year - First sem(1-1)")
        print("2. First year - Second sem(1-2)")
        print("3. Second year - First sem(2-1)")
        print("4. Second year - Second sem(2-2)")
        print("5. Third year - First sem(3-1)")
        print("6. Third year - Second sem(3-2)")
        print("7. Fourth year - First sem(4-1)")
        print("8. Fourth year - Second sem(4-2)")
        print("press q to quit program")
        
        i = input("Enter your semiser: ")
        try:
            j = int(i)
            if i != j:
                if j == 1:
                    print(" ")
                    print(t1.sem1_1())
                    print(" ")
                    time.sleep(1)
                elif j == 2:
                    print(" ")
                    print(t1.sem1_2())
                    print(" ")
                    time.sleep(1)
                elif j == 3:
                   print(" ")
                   print(t1.sem2_1())
                   print(" ")
                   time.sleep(1)
                elif j == 4:
                    print(" ")
                    print(t1.sem2_2())
                    print(" ")
                    time.sleep(1)
                elif j == 5:
                    print(" ")
                    print(t1.sem3_1())
                    print(" ")
                    time.sleep(1)
                elif j == 6:
                    print(" ")
                    print(t1.sem3_2())
                    print(" ")
                    time.sleep(1)
                elif j == 7:
                    print(" ")
                    print(t1.sem4_1())
                    print(" ")
                    time.sleep(1)
                elif j == 8:
                    print(" ")
                    print("empty")
                    print(" ")
                    time.sleep(1)
                else:
                    print(" ")
                    print("Error...")
                    print(" ")
        except:        
            temp = str(i)
            if temp == "q" or temp == "Q":
                print(" ")
                print("quit")
                time.sleep(2)
                sys.exit()
            else:
                print(" ")
                print("Error...")
                print(" ")
            
main()
