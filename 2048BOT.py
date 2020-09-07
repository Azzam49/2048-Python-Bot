from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


browser = webdriver.Firefox() 
print("Lunching 2048 in the browser...")
browser.get("https://gabrielecirulli.github.io/2048/")
time.sleep(4)

MoveBot = browser.find_element_by_tag_name("html")
GameOver = browser.find_element_by_class_name("retry-button")
Score = browser.find_element_by_class_name("score-container")
HighestScore = browser.find_element_by_class_name("best-container")
Retry = browser.find_element_by_class_name("retry-button")
Cookie = browser.find_element_by_class_name("cookie-notice-dismiss-button")

def RetryGame():
    GameOver = True
    while GameOver:
        re = input("\nType r to restart the game or q for quit!\n: ")
        if re.lower() == "r":
            time.sleep(1)
            Retry.click()
            initBot()
            GameOver = False
        elif re.lower() == "q":
            print("Thanks for watching ! , Closing now ...")
            time.sleep(2)
            browser.quit()
            sys.exit()
        else:
            print("invalid entry! try again..")
            
def initBot():
    time.sleep(1)
    GameOn = True
    print("Game Started !")

    if Cookie.is_displayed() == True:
        Cookie.click()
        
    while GameOn:
        MoveBot.send_keys(Keys.UP)
        time.sleep(1)
        MoveBot.send_keys(Keys.RIGHT)
        time.sleep(1)
        MoveBot.send_keys(Keys.DOWN)
        time.sleep(1)
        MoveBot.send_keys(Keys.LEFT)
        time.sleep(1)

        if Retry.is_displayed() == True:
            GameOn = False
            print("GAME OVER!")
            print(f"Your Score : {Score.text}")
            print(f"Highest Score : {HighestScore.text}")
            RetryGame()
                

                
initBot()







