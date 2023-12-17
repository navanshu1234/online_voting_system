from pywebio.input import *
from pywebio.output import *
import math, random

def f1():
    put_text('                        Welcome to Online Voting System                    ')
    img1 = open('C:/Users/Navansh/Downloads/login1.vote.jpg', 'rb').read()
    put_image(img1, width='50%', height='50%')
    put_buttons(['LOGIN','REGISTER'], onclick=...)


# function to generate OTP
def generateId():
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    Id = ""

    # length of password can be changed
    # by changing value in range
    for i in range(4):
        Id += digits[math.floor(random.random() * 10)]

    return Id


# Driver code
if __name__ == "__main__":
    put_text("Id of 4 digits:", generateId())