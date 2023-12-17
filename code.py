from pywebio.input import *
from pywebio.output import *
from pymongo import MongoClient


client = MongoClient('localhost',port=27017)
db = client.voterlist

coll = db.voterlist

def front():
    put_text('                        Welcome to Online Voting System                    ')
    img1 = open('C:/Users/Navansh/Downloads/login1.vote.jpg', 'rb').read()
    put_image(img1, width='50%', height='30%')

def voting():
    sel = radio('Choose what to do?',['LOGIN','REGISTER'])
    if sel == 'LOGIN':
        data = input_group("LOGIN",
            [input('USERNAME', name='Name', type=TEXT, required=True,
                   help_text='Please enter your userid'),
             input('VOTER ID', name='Id', type=PASSWORD ,required=True),
            input('PASSWORD', name='PASS', type=PASSWORD, required=True,
                    help_text='Please enter your password')])

        sel1 = radio('Would you like to go to Voting page',['Yes','No'])
        if sel1 == 'Yes':
            selection = radio("Select your Candidate",
                              ['CANDIDATE A', 'CANDIDATE B', 'CANDIDATE C', 'CANDIDATE D', 'CANDIDATE E'])
            users = {
                'Name': data['Name'],
                'Voter Id': data['Id'],
                'vote_for': selection
            }
            coll.insert_one(users)
            put_text('Your response has been recorded')

            keep_voting = radio('Keep Voting', ['Yes', 'No'])

            if keep_voting == 'Yes':
                voting()
            else:
                return put_text('Voting has been done,Result will be announce soon')
        else:
            voting()

    else:
            data = input_group("REGISTRATION",
                               [input('Enter your name', name='Name', type=TEXT,),
                                input('Enter your Age', name='Age', type=NUMBER),
                                input('Enter your Voter ID', name='Id', type=NUMBER, required=True),
                                input('Enter your Password', name='Pass', type=PASSWORD, required=True)])

            if data['Age'] >= 18:
                put_text('Check your Detail')
                put_table([['NAME', put_text(data['Name'])],
                          ['AGE', put_text(data['Age'])],
                          ['ID', put_text(data['Id'])],
                          ['PASSWORD', put_text(data['Pass'])]])

                check = checkbox(options=['All details are Correct'])
                if check:
                    put_text('You are successfully Registered')
                    sel2= radio('Would you like to go to Voting Page',['Yes','No'])
                    if sel2 == 'Yes':
                        selection = radio("Select your Candidate",
                                          ['CANDIDATE A', 'CANDIDATE B', 'CANDIDATE C', 'CANDIDATE D', 'CANDIDATE E'])
                        users = {
                            'Name': data['Name'],
                            'Voter Id': data['Id'],
                            'vote_for': selection
                            }
                        coll.insert_one(users)
                        put_text('Your response has been recorded')
                    else:
                        voting()

                keep_voting = radio('Keep Voting', ['Yes', 'No'])

                if keep_voting == 'Yes':
                    voting()
                else:
                    return put_text('Voting has been done,Result will be announce soon')
            else:
                put_text('You are not eligible for voting')

if __name__ == '__main__':
    front()
    voting()

