from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time
import InstaBot

waiting_time = 30

userN = input('Enter Username: ')
passW = input('Enter Password: ')
start = time.time()

douglas_insta = InstaBot.Instabot(userN, passW)
douglas_insta.login()
print('Login in {:.2f} sec'.format(time.time() - start))

#douglas_insta.open_explore()
tag = input('Enter tag: ')
start = time.time()

douglas_insta.open_tag(tag)
douglas_insta.open_first_post()
print('First post found in {:.2f} sec'.format(time.time() - start))

for i in range(1200):
    start = time.time()

    # analise and like
    douglas_insta.like_post()

    douglas_insta.next_post()
    time.sleep(waiting_time - (time.time() - start))

    # analise and follow
#    douglas_insta.follow()

    print('{:04d} | {:.2f} sec'.format(i, time.time() - start))