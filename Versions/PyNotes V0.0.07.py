#Author: Max Ferney
#Date Created: 8.12.2015
#Date Modified: 8.31.2015
#Version: 0.0.07
#Description: Organize and take notes with PyNotes!


#imports
import os
import sys
import time


#globals
files = []
CPaths = []
#cwd = os.getcwd()
#DoNotChange
ORIGINAL_CWD = os.getcwd()


#classes
class Data():
    FileName=None
    MainCwd = None
    cwd = None
    path = None
    cpaths = []
    cfiles = []
    
    text = ""

    def __init__(self):
        self.MainCwd = os.getcwd()
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)

        self.UPL()

    def InitSettings(self):
        self.FileName=None
        self.cpaths = []
        self.cfiles = []
        self.text = ""

    def UPL(self):
        self.cpaths = list()
        self.cfiles = list()
        cwd = self.cwd
        path = self.path
##        print("##########---FOLDERS---##########")
        for c in os.walk(path).__next__()[1]:
##            print(c)
            self.cpaths.append(c)
##        print("##########----FILES----##########")
        for c in os.walk(path).__next__()[2]:
##            print(c)
            self.cfiles.append(c)

    def readF(self):
        text = self.text
        
        if self.FileName == None:
            print("[ERROR: NO FILE SELECTED]")
            print("Use SelectFile() to select a file.")
            
        else:
            FileName = self.FileName
            with open(FileName, 'r') as f:
                text = f.read()
                self.text = text
            f.close()

        print(self.text)

    def SelectFile(self, file):
        self.UPL()
        self.FileName = file
        self.readF()
        

    def ChangeDir(self, newpath=""):
        if len(str(newpath))==0:
            newpath = self.MainCwd
        elif str(newpath)[-1] == '/':
            newpath = str(newpath)[:-1]
        os.chdir(newpath)
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)
        self.InitSettings()

    def NewFile(self, name, Type='txt'):
        file = name + "." + Type
        with open(file, 'w') as f:
            f.write('[FILE: ' + file + ']' + '\n')
        f.close()

    def EditFile(self, system=False, message=""):
        print("to stop typing, press ENTER, then press CONTROL + C")
        self.readF()
        if self.FileName == None:
            print("[ERROR: NO FILE SELECTED]")
            print("Use SelectFile() to select a file.")
            return None
        text = self.text
        file = self.FileName

        with open(file) as f:
            t = f.read()
        f.close()
        if not system:
            while 1:
                print('-', end='')
                try:
                    line = sys.stdin.readline()

                except KeyboardInterrupt:
                    break

                if not line:
                    break

##                i=0
##                totalstr = len(str(line))
##                
##                if totalstr>60:
##                    while i < totalstr:
##                        lnbrk = line.rfind(' ', i+0, i+60)
##                        templine = line[i:lnbrk]
##                        nextline = '\n' + line[lnbrk:lnbrk+60]
##                        if i!=0:
##                            line += nextline
##                        else:
##                            line = templine + nextline
##                        i+=lnbrk#less than 2 lines now

                t += ("-"+line)
        else:
            t += 'SYSTEM\t'+message+'\n'

        with open(file, 'w') as f:
            f.write(t)
        f.close()

        with open(file) as f:
            text = f.read()
            self.text = text
        f.close()

        

    
    def LP(self):
        self.UPL()
        print("##########---FOLDERS---##########")
        for c in self.cpaths:
            print(c)
        print("##########----FILES----##########")
        for c in self.cfiles:
            print(c)

    def help(self):
        print('''

        ##########---Help Section---##########

        InitSetting()
        -Sets specific variables to the initial settings

        UPL()
        -Update Path List: Updates the directory

        readF()
        -Reads the current file, and stores it
        in variable: [text].
        
        SelectFile(New File)
        -Selects a file. This file is stored and saved 
        until a new file is selected.

        ChangeDir([file])
        -Changes current directory. If left blank, it will
        return to the original directory.

        NewFile(filename, extension=txt)
        -Creates a new file.
        WARNING: IF THE FILE EXISTS, THEN THE ORIGINAL
        WILL BE DELETED

        EditFile()
        -Edits the current file.
        NOTICE: This only works for txt files.

        LP()
        -Lists all folders and files in the current
        directory.

        ''')

    def __str__(self):
        return 'File Name: ' + str(self.FileName) + '\n' +\
               'Main cwd: ' + str(self.MainCwd) + '\n' +\
               'Current cwd: ' + str(self.cwd) + '\n' +\
               'Current path: ' + str(self.path) + '\n'
               
        

    
        


#functions
def UFL(folder="Files\\"):
    global files
    files = list()
    cwd = os.getcwd()
    path = os.path.join(cwd, folder)
    #print("------------FILES------------")
    for c in os.walk(path).__next__()[2]:
        #print(c)
        files.append(c)

def UPL():
    global CPaths
    CPaths = list()
    cwd = os.getcwd()
    path = os.path.join(cwd)
    print("##########---FOLDERS---##########")
    for c in os.walk(path).__next__()[1]:
        print(c)
        CPaths.append(c)
    print("##########----FILES----##########")
    for c in os.walk(path).__next__()[2]:
        print(c)
        CPaths.append(c)

##def OpenFile(fileName, directoryPath="Files/"):
##    fileName = directoryPath+fileName
##    with open(fileName, 'r') as f:
##        text=f.read()
##    f.close()
##    return text

##def NewFile(fileName, directoryPath="Files/"):
##    dirPath=directoryPath + fileName + ".txt"
##    with open(dirPath, 'w') as f:
##        f.write('[FILE: ' + fileName + ']')
##    f.close()

##def AllFiles():
##    UFL()
##    print("------------FILES------------")
##    for f in files:
##        print(str(f))

##def EditFile(fileName):
##    pass

##def ListDir():
##    UPL()
##
##def MainDir():
##    os.chdir(ORIGINAL_CWD)

def startUp():
    def titleDisplay():
        i = 0
        while i<10:
            print()
            i+=1
        print("""
        --------------------
        Welcome to PyNotes V0.0.07
        
        This program is used to take notes
        and save them to a simple text document
        
        Author: Max Ferney
        if you have any questions or concerns
        about this program, you may email
        me at maxferney@gmail.com please set
        the title of the subject to pygame, so
        I know what it is. Thank you.
        --------------------
        """)
        i = 0
        while i<8:
            print()
            i+=1
    titleDisplay()


startUp()


    
