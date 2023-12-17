from pywebio.input import*
from pywebio.output import *

def d2():
    data = input_group("REGISTRATION",
                       [input('Enter your name', name='Name', type=TEXT),
                        input('Enter your Age',name='Age',type=NUMBER),
                        input('Enter your Voter ID',name='Id',type=TEXT),
                        input('Enter your Password', name='Pass', type=PASSWORD)])
    put_button()
    put_text('Check your details')
    put_table(['NAME','AGE','ID','PASSWORD'],
              [data['Name'],data['Age'],data['Id'],data['Pass']])




if __name__ == '__main__':
        d2()