from selenium import webdriver
import os
import time
import pyautogui

class instagrambot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'

        self.driver = webdriver.Chrome('chromedriver')
        self.login()
        
    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(1)
        
        self.driver.find_element_by_name('username').send_keys(self.username)

        self.driver.find_element_by_name('password').send_keys(self.password)

        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(3)
        pyautogui.click(509, 691)
        time.sleep(3)
        pyautogui.click(537, 748)

    def nav_user(self,user):
        self.driver.get('{}/{}/'.format(self.base_url,user))
    
    def follow_user(self, user):
        time.sleep(2)
        self.nav_user(user)
        time.sleep(6)

        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        
        follow_button.click()

    def unfollow_user(self, user):
        time.sleep(2)
        self.nav_user(user)
        time.sleep(6)
        pyautogui.click(665,264)
        time.sleep(2)
        pyautogui.click(530,688)
        

if __name__ == '__main__':
    ig_bot = instagrambot('tech_insights', 'thepasscode1233')
    
    ig_bot.nav_user('therock')
    ig_bot.follow_user('therock')
