from pywebio.input import *
from pywebio.output import *
from pymongo import MongoClient

client = MongoClient('localhost',port=27017)
db = client.voterlist

coll = db.voterlist


def voting():
    name = input("Enter your name",type=TEXT)
    age = int(input("enter your age",type=NUMBER))

    if age>=18:
        put_text('Check your Detail')

        put_table([['Name','Age'],[name,age]])

        check = checkbox(options =['All details are Correct'])
        if check:
            selection = radio("Select your Candidate",['CANDIDATE A','CANDIDATE B','CANDIDATE C','CANDIDATE D','CANDIDATE E'])

            users = {
                'name':name,
                'age':age,
                'vote_for': selection
            }
            coll.insert_one(users)
            put_text('Your response has been recorded')

            keep_voting = radio('Keep Voting',['Yes','No'])

            if keep_voting == 'Yes':
                    voting()
            else:
                return put_text('Voting has been done,Result will be announce soon')
    else:
         put_text('You are not eligible for voting')



if __name__ == '__main__':
    voting()

