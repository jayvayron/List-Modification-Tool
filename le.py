import os
from time import sleep
import sys


def _pre_pre_check():
    print("List Entry Module [Version 0.1]\nNo Copyright (Open Source) 2021 \nAuthor: Jay Vayron. No rights reserved. [LOL]")
    sleep(1)
    print('\n-----------------------------------------------------------------------------------')
    print('--For help, type \'##help\' to get detailed documentation on the various functions.--')
    print('-----------------------------------------------------------------------------------')
    _pre_checkis = _pre_check()

def _pre_check():
    global filepath
    filepath = os.getcwd()+'amongusnames.txt'
    if os.path.exists(filepath) == True:
        print('\n**********  SUCCESS: File is accessible.  **********')
        call1 = _file_content()
    elif os.path.exists(filepath) == False:
        print('**********  ERROR: File not found.  **********')
        query = input('You want the file to be created? [\'Y\'= Yes / \'N\'= No (Program will close.)]: ')
        if query == 'Y' or query == 'y':
                with open(filepath, 'w') as output:
                    output.write('')
                print('File was created in the directory: '+ filepath)
                a = open(filepath, 'r')
                b = a.read()
                global plist
                plist = list(b)
                print("Value alloted to plist in list type.")
                now = _adding_names_pre()
        elif query == 'N' or query == 'n':
            sys.exit()
        elif query not in ['Y','y','N','n']:
            print("**********  ERROR: Invalid INPUT.  **********")
            sys.exit()

def _file_content():
    name = open( filepath, "r")
    b = name.read()
    if b != '':
        print('\nFile contains data (NOT EMPTY).')
        print('The values inside the list are : \n\n'+ b)
        w = b.replace("["," ")
        x = w.replace("]"," ")
        y = x.replace("'","")
        z = y.replace(",","")
        global plist
        prime_str = ''
        plist = []
        for i in range(0,len(z)):
            if z[i] != " ":
                prime_str += z[i]
            if z[i] == " ":
                plist.append(prime_str)
                prime_str = ''  
        plist.pop(0) #popping the first element created by default ('').
        print('\nData stored in variable called plist in the form of list.')
        print("Now you can enter additional names in the list.")
        call2 = _adding_names_pre()
    elif b == '':
        print('File is empty.')
        plist = []
        print("Now you can add names in the list.")
        call2 = _adding_names_pre()

def help_description():
    print('\n')
    print('This section helps to interact with various functions inside this tiny program XD')
    input("Press ENTER to continue...\n")
    print('TIP #1: Every function inside this program can be accessed by typing \'##\' before the function names. ')
    input('Press ENTER to continue...\n')
    print('TIP #2: Type help(function) to get detailed description.')
    input('Press ENTER to continue...\n')
    print("===== Below from here would list all functions in this module. =====")
    input('Press ENTER to continue...\n')
    print("(1) freemode (##freemode)\n(2) blowup (##blowup)\n(3) help (##help)\n(4) ##getlist\n(5) ##cls\n")
    _adding_names_pre()

def help(command):
    if command == '':
        print('========== Now you are in help mode. ==========')
    if command == 'freemode':
        print('This function helps to access all funtions other including \'##help\' and \'break\'.\nYou can use \'##\' before all functions described in list given in \'##help\' function.')
    else:
        print("\nGoing back in list modification mode.")
        _adding_names_pre()
        sleep(1)

def _error_call():
    print('********** ERROR: Not a valid input. **********')
    print('\nReturning to Modification mode...')
    sleep(1.5)
    _adding_names()

def _adding_names_pre():
    print('\n========== Now you are in list modification mode. ==========')
    sleep(1)
    print("\nTo close the program type \'break()\'")
    print("\nTo get a brief desc about commands in list modification mode, type \'#help()\'")
    _adding_names()

def _adding_names():
    validlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.','_']
    m = 0
    n = 0
    global o
    o = 0
    # validlistint = []
    # validlistspecial = []
    global inputvar
    inputvar = input('Enter username : ')
    if inputvar == 'break()':
        sys.exit()
    elif inputvar == 'help()':
        help('')
    elif inputvar == '#help()':
        help_description()
    elif inputvar == '':
        _adding_namesis = _adding_names()
    elif inputvar not in ['break()','help()','#help()c']:
        for i in inputvar:
            if i not in validlist:
                m += 1
        if m != 0:
            _error_call()
        elif m == 0:
            _adding_namesis = _adding_names_2()

def _adding_names_2():
    global o
    if inputvar[0] == '.' or inputvar[-1] == '.':
        o += 1
        _error_call()
    elif o == 0:
        _adding_namesis = _adding_names_3()

def _adding_names_3():
    plist.append(inputvar)
    with open(filepath, 'w') as output:
        output.write(str(plist))
    _adding_names()


_pre_pre_check()