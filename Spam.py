import pyautogui
import keyboard
import time

spam_text = input("Enter the text you want to spam: ")
repeat_count = int(input("Enter the number of times to spam: "))
arithmetic=input("Do want to add an arithmetic increase in numerical str attached with the spam word (ex: spammer1, spammer2,....spammerN)(Y/N): ")
Interv=float(input("what should be the time interval between the words while typing(recommended: 0.03): "))
# Wait for n seconds to switch to the target application
print("You have 10 seconds to click on the target application where the text should be spammed.")
time.sleep(10)


# Move to a specific location and click
#pyautogui.moveTo(200, 200, duration=1)
#pyautogui.click()
a = 0
for i in range(repeat_count):
    if arithmetic=='y':
        a+=1
        pyautogui.write(str(spam_text)+str(a), interval=Interv)
        pyautogui.press('enter')
    else:
        pyautogui.write(str(spam_text), interval=Interv)
        pyautogui.press('enter')
    #You can replace the "I'm spammer lol" with any text message that you want to spam.
    #You can also remove the str(a) If u don't want any arithmetic increase in numerical to your spam like (spammer1, spammer2, spammer3, spammer4....spammerN)

# keyboard.hotkey('ctrl', 's')  # For example, to save a document
#Code edited by Ridhan, YAY!

