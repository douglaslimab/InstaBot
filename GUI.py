import InstaBot
import time
from tkinter import *

screen = Tk()
screen.title = "InstaBot"
screen.geometry("200x200")

waiting_time = 30

def login():
    start = time.time()

    userN = username.get()
    passW = password.get()

    global user_insta
    user_insta = InstaBot.Instabot(userN, passW)
    user_insta.login()
    print('Login in {:.2f} sec'.format(time.time() - start))


def search_tag():
    start = time.time()

    tagS = tag.get()

    user_insta.open_tag(tagS)
    user_insta.open_first_post()
    print('First post found in {:.2f} sec'.format(time.time() - start))


def run_likes():

    nol = number_of_likes.get()
    print(int(nol))
    for i in range(int(nol)):
        start = time.time()

        # analise and like
        user_insta.like_post()

        user_insta.next_post()
        time.sleep(waiting_time - (time.time() - start))

        # analise and follow
        # douglas_insta.follow()

        print('{:04d} | {:.2f} sec'.format(i, time.time() - start))


username = Entry(screen, width=20)
username.pack()
password = Entry(screen, width=20)
password.pack()
login_btn = Button(screen, width=20, text="Login", command=login).pack()

tag = Entry(screen, width=20)
tag.pack()
search_btn = Button(screen, text="Search", command=search_tag).pack()

number_of_likes = IntVar()
number_of_likes = Entry(screen, width=20)
number_of_likes.pack()
likes_btn = Button(screen, text="Run", command=run_likes).pack()

#input password (hide password)

#how many likes/how long
#sart/stop button



screen.mainloop()