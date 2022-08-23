from re import X
from tkinter import Y
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df= pd.read_excel('EgyptProPlayersV1.xlsx')

table = pd.pivot_table(df, values=['goals','assist','Total goals & assists'], index="Player Name", aggfunc=np.sum)
accept =['yes','y','ya','yeb','ok']
refuse = ['no','n']
char_kinds=['pie','bar']

print('\t data is cleaned successfully.\n\n')

def userInput():
    user_input = input('Do you want to see some charts? yes or no\n\n ').lower().strip()
    if user_input in accept:
        while True:
            char_kind = input('Do you want pie or bar chart?\n\n').lower().strip()
            if char_kind in char_kinds:
                show(char_kind)
                break
            else:
                print('please enter a valid chart "pie" or "bar"')
    elif user_input in refuse:
        exit()
    else:
        print('\t\t Enter yes or no ')
        userInput()

def show(char_kind):
    table.plot(kind=f'{char_kind}',subplots=True)
    plt.xlabel('Player')
    plt.ylabel('Total goals & assists')
    plt.show()
    userInput()



def exit():
    quit()

userInput()