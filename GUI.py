import InstaBot
import time
from tkinter import *

user_insta = InstaBot.Instabot('', '')

screen = Tk()
screen.geometry("200x200")

def login():
    start = time.time()

    userN = username.get()
    passW = password.get()

    user_insta = InstaBot.Instabot(userN, passW)
    user_insta.login()
    print('Login in {:.2f} sec'.format(time.time() - start))


def search_tag():
    start = time.time()

    tagS = tag.get()

    user_insta.open_tag(tagS)
    user_insta.open_first_post()
    print('First post found in {:.2f} sec'.format(time.time() - start))


def run_likes(number):
    print(number)


#input username

username = Entry(screen, width=10)
username.pack()
password = Entry(screen, width=10)
password.pack()
login_btn = Button(screen, text="Login", command=login).pack()


#input password (hide password)
#login button

#tag
#how many likes/how long
#sart/stop button

tag = Entry(screen, width=10)
tag.pack()
search_btn = Button(screen, text="Search", command=search_tag).pack()

number_of_likes = Entry(screen, width=10)
number_of_likes.pack()
likes_btn = Button(screen, text="Run", command=run_likes).pack()

screen.mainloop()