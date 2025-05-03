from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR_ACCOUNT="chefsteps"
USERNAME="fammi_es"
PASSWORD="Tinnachutki"


class InstaFollower:
    def __init__(self):
         chrome_options=webdriver.ChromeOptions()
         chrome_options.add_experimental_option("detach",True)
         self.driver=webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(4.2)

        username=self.driver.find_element(By.NAME,value="username")
        pass_word=self.driver.find_element(By.NAME,value="password")

        username.send_keys(USERNAME)
        time.sleep(2.1)
        pass_word.send_keys(PASSWORD,Keys.ENTER)

        # logIn=self.driver.find_element(By.XPATH,value="//div[contains(text(), 'Log in')]")
        # logIn.click()
        time.sleep(7)
        try:
            save_or_not=self.driver.find_element(By.XPATH,"//button[contains(text(), 'Not now')]")
            save_or_not.click()
            time.sleep(2)
        except:
            print("Nothing appeared")
        
    def find_follower(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(8.2)

        try:
            follower_count=self.driver.find_element(By.XPATH,"//a[contains(@href,'/followers/')]")
            follower_count.click()
            time.sleep(5)
        except:
            print("Followerslink/popup not found")
            return
        
        modal=self.driver.find_element(By.XPATH,"//div[@role='dialog']//div[contains(@style,'overflow')]")
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons=self.driver.find_elements(By.XPATH,"//button[normalize-space()='Follow']")

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                try:
                    cancel_button=self.driver.find_element(By.XPATH,"//button[contains(text(), 'Cancel')]")
                    cancel_button.click()
                    time.sleep(1)
                except:
                    pass



    # html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div

bot=InstaFollower()

bot.login()
bot.find_follower()
bot.follow()
