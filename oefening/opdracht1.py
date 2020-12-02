import time, os

class timeRunning():

    def __init__(self, timeS):
        timeSecond = timeS
        print("Je programma gaat nu ", timeS, "seconden aan blijven")
        time.sleep(1)
        os.system("cls")
    
    def timeRun(self):
        timee = 0


        while timee < int(timeS):
            timee = timee + 1
            print(timee)
            time.sleep(1)
            os.system("cls")


        if timee == timeSecond:
            gameIsRunning = False
        

        

gameIsRunning = True

while gameIsRunning:

    print("Hoelang moet dit programma runnen?")
    timeS = input()

    os.system("cls")
    tijd = timeRunning(timeS)
    time.sleep(1)

    tijd.timeRun()