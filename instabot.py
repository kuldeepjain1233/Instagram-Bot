from selenium import webdriver
import os
import time

class instagrambot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('./chromedriver.exe')
        
        self.driver.get('https://www.instagram.com/')

if __name__ == '__main__':
    ig_bot = instagrambot('temp_username', 'temp_password')