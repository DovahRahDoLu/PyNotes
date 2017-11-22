#Author: Max Ferney
#Date Created: 8.12.2015
#Date Modified: 2.1.2016
#Version: 0.3.01
#Description: Organize and take notes with PyNotes!


#imports
import os
import sys
import time
import textwrap


#globals
files = []
CPaths = []
#DoNotChange
ORIGINAL_CWD = os.getcwd()


#classes
class PyNotes:
    FileName=None
    MainCwd = 'C:\\Users\\lisaf_000\\Desktop\\Python\\PyNotes'
    cwd = None
    path = None
    cpaths = []
    cfiles = []
    InitializeTimeStamp = None
    version = '0.3.01'
    lastIndex = 0
    
    text = ""

    def __init__(self):
        #self.MainCwd = os.getcwd()
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)

        self.InitializeTimeStamp = str(time.asctime())

        self.UPL()

    def InitSettings(self):
        self.FileName=None
        self.cpaths = []
        self.cfiles = []
        self.text = ""
        self.cwd = self.MainCwd
        self.path = os.path.join(self.cwd)

    def UPL(self):
        self.cpaths = list()
        self.cfiles = list()
        cwd = self.cwd
        path = self.path
        for c in os.walk(path).__next__()[1]:
            self.cpaths.append(c)
        for c in os.walk(path).__next__()[2]:
            self.cfiles.append(c)

    def readF(self, sts=False, Display=True):
        #sts = Since Time Stamp
        text = self.text

        AllLines=True
        lines=200
        
        if self.FileName == None:
            print("[ERROR: NO FILE SELECTED]")
            print("Use SelectFile() to select a file.")
            
        else:
            FileName = self.FileName
            with open(FileName, 'r') as f:
                text = f.read()
                self.text = text
            f.close()

        DisplayText = ""
        counted_lines = 0
        lastIndex = 0
        if sts or not AllLines:
            if not sts:
                for n in text:
                    if counted_lines >= lines:
                        lastIndex = text.index(n)
                        break
                    elif n == '\n':
                        counted_lines+=1
                    
            else:
                lastIndex = text.rfind('TIMESTAMPSTR')
                
            DisplayText = text[lastIndex:]
            
            if Display:
                # \t is for tab before timest
                print('\t', end='')
            
        else:
            DisplayText = self.text

        self.text = DisplayText
        if Display:
            print(DisplayText)

    def sf(self, file, show_text=True):
        self.UPL()
        self.FileName = file
        if not show_text:
            self.readF(sts=True, Display=False)
        else:
            self.readF(sts=True, Display=True)
        

    def cd(self, newpath=''):
        if len(str(newpath))==0 or str(newpath)=="" or str(newpath)=='sysmain':
            newpath = self.MainCwd
        elif str(newpath)[-1] == '/':
            newpath = str(newpath)[:-1]
        os.chdir(newpath)
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)
        #self.InitSettings()

    def search(self):
##        keywords = []
##        print('Input Keywords. type \'done\' when you are finished')
##        ask = ''
##        while ask != 'done':
##            ask = input()
        string_type = input('keyword type (title, subtitle, WIP(time)): ')
        keyword = input('Keyword: ')
        max_chr = int(input('max characters: '))
        self.readF(Display=False)
##        if string_type == '':
        keyword_index = self.text.find(keyword, self.lastIndex)
        self.lastIndex = keyword_index
        
        substring = ''
        for c in range(self.lastIndex, self.lastIndex+max_chr):
            substring += self.text[c]

        print(substring)
        self.lastIndex += 1
            
    
    def NewFile(self, name, TITLE=' ', Type='txt'):
        file = name + "." + Type
        dateCreated = time.asctime()
        with open(file, 'w') as f:
            f.write('\t[FILE: ' + file + ']\n')
            f.write('\t[DATE CREATED: ' + str(dateCreated)+\
                    ']\n')
            f.write('\t[Title: ' + TITLE + ']\n')
        f.close()

    def EditFile(self, file='', InLoop=False, system=False, message=""):
        if not InLoop:
        
            #use line numbers in text to go back and edit line
            #will be used with index
            if len(file)>0:
                self.sf(file)
            self.readF(sts=True)
            
            #this reads from last timestamp, not whole text
            if self.FileName == None:
                return None
            file = self.FileName
            text = self.text

            # Initial Variables
            bp = input('input bullet point: ')
            #create predefined variable custom error
            try:
                bp = int(bp)
                bp = chr(bp)
            except ValueError:
                bp = str(bp)

            #text for saving
            SaveText = str(input('type(y/n) for TimeStamp text: ')) #controls if last save text is turned on
            savebool = False
            if SaveText == 'y':
                savebool = True

            width = 55
            lenI = 1

            #text commands
            Coding = False
            
            sidenoted = False
            sidenotePretext = ''

            highlighting = False
            highlightPretext = ''

            delete_last_line = False
            last_string = ''
            
        
        '''
        All indenting and bullet point editing will be
        done and implemented in the GUI version of
        PyNotes, expected to be in version v1.

        since the program uses textwrap, which reads and
        edits the text that was inputed...
        use that ability to do bulletpoints/indentation

        this above statement has been officially completed
        as of version 0.1.08.


        ##replace last index[-1] with [-(len(bp))]

        ##implement code key_command, for code input
            this will have no bullet points
            indents will be either 2 or 4
            textwrap will be turned off

        ##add subtitle key_command

        pySlideShow
            clear screen for each slide
            include margins/borders
            -text version
            -PySlides is pygame version

        ##Shorten the read text
            make it in the  past 50 lines
            or in the past 300 characters
            ##or since the last TIMESTAMPSTR

        ##put the timestampstr at before rest of text

        ##Make a new file for the outline.
            this will use the bp pretty much.
            import the new data class, and
            modify so:
                class outliner(data):
                    def EditFile() #this is only
                                   #thing changed

        ##needs modify previous lines
            erase lines..
            maybe not break on input.........
                This can cause a TON of problems..
                if it is even possible in the first place

        ##Add SideNote Capability
            if there is something not related to the topic

        #<REVISIT> Implement a Highlight Mode(
            It would make the object more noticible
            try to use fonts or abstract characters
            try using Colorama
                (only works in system console)

            Use Error Text Colors, special colors.
                needs to make a custom font for this

            #use <>[]{}()//\\||(make tags)

        AUTOSAVE
            an autosave feature to pretty much run the
            editfile function multiple times.
                editFile(inloop=False):
                    ...
                    editFile(inloop=True)
                    ...

        Implement Search feature
            display all TITLELINEs
            add tags
            allow the user to search for a title/tags
            

        Look into Ipython/jupyter
        
        ###Custom Made Warning    
        import warnings as w
        >>> w.showwarning("message", Warning, "mod", 21)



        Add a spell checker feature
            This will be able to edit everything up to
            the top
            Use a text file for reference, maybe one for
            each topic or study.
                place a text file in the corresponding
                subject

        <<<This should be implemented as soon as possible>>>
        ##Add a command to entirely delete the above line
            make it easy not to mistake it, or call it
            accidentally
        look for a bullet point, so that other lines
        can be deleted


        Create a few custom errors for more specific
            error handling
            predefined variables in function
                bullet point, save


        TextWrap Function
        Hightlight and sidenote are pretty much identical.
            Make it a function, maybe with the textwrap
            function.

        Allow subtitle to be indented

                     
        '''
        
        with open(file) as f:
            t = f.read()
        f.close()
        if not system:
            pretext = bp
            ind_lvl = 0
            key_commands = ['DONE', '-->',
                            '--->', '<---',     #user errors
                            '00>', '<00',       #user errors
                            '==>', '<==',       #user errors
                            '--', '<-', '->',   #user errors
                            ',--', '--.',       #user errors
                            '--',               #user errors
                            '-->>', '<<--',     #user errors
                            '<--', 'CHBP',
                            'TITLELINE', 'SUBTITLE',
                            'CODEMODE', 'CODEEXIT',
                            'BULLETS', 'SIDENOTE',
                            'DELETE_LAST_LINE']

##            user_errors = ['--.', '-..'
##                           ',__', '__.']
##            for u in user_errors:
##                key_commands.append(u)
            
            print("""
            to end input: type 'DONE' or press Ctrl+c
            to indent: type '-->'
            to unindent: type '<--'
            to make title line: type 'TITLELINE'
            to make subtitle line: type 'SUBTITLE'
            to make a sidenote: type 'SIDENOTE'
            to change the bullet point: type 'CHBP'
            to enter Code Input: type 'CODEMODE'
            to exit Code Input: type 'CODEEXIT'
            to see bullet points: type 'BULLETS'
            to erase last line: type 'DELETE_LAST_LINE'
                
            """)
            def specialPoints():
                for i in range(1, 9):
                    print(str(i) + ' = ' + chr(i))
                for i in range(11, 32):
                    print(str(i) + ' = ' + chr(i))


            def tag_string(tag, string):
                note = input('NOTE: ')
                highlightPretext = pretext
                pretext = pretext[:-lenI]
                string = tag + tag + \
                         ' ' + note + ' ' + \
                         tag + tag
                highlighting = True
                if len(pretext) + len(string) >= 55:
                    print(pretext + string + '\n')
                else:
                    print(pretext + string)
    
                            
            #This checks if the last time modified was on
            #the same date as the current date..
            #This is to separate your notes by day.
            #It returns true if last modified date is
            #current date.
            def lastDateMatches(string):
                strStart=t.rfind(string)
                date = t[(strStart+20):(strStart+26)]
                initDate = str(self.InitializeTimeStamp)[4:10]

                if date == initDate:
                    return True
                else:
                    return False
                    

            timestampstring = "TIMESTAMPSTR:  "+\
                              '['+\
                              str(self.InitializeTimeStamp)+\
                              ']'
            
            if not lastDateMatches('TIMESTAMPSTR'):
                long_line = ''
                for s in range(54):
                    long_line += '+'
                t += '\n' + long_line
                t += '\n' + \
                     '\t' + timestampstring + \
                     '\n' + \
                     '\t#####Last Save: [' + \
                     time.asctime() + \
                     ']#####\n'
                t += long_line + '\n\n\n'
                

                #20-26

                 
            while 1:
                try:
                    if pretext == '' :
                        pretext = bp
                        width = 55
                        
                    elif sidenoted:
                        sidenoted = False
                        pretext = sidenotePretext
                    elif highlighting:
                        highlighting = False
                        pretext = highlightPretext
                        
                    string = input(str(pretext))
                    lenI = len(bp)
                    

                    
                    #key_commands
                    if string.lower() == 'done':
                        break
                        
                    elif string == '-->' or \
                         string == '--->' or \
                         string == '->':
                        spaces = '  '
                        for i in range(lenI):
                            spaces += ' '
                        pretext = spaces + pretext
                        ind_lvl += 1
                        width -= len(spaces) #2

                    elif string == '<--' or \
                         string == '<---' or \
                         string == '<-':
                        if ind_lvl > 0:
                            pretext = pretext[lenI+2:]
                            ind_lvl -= 1
                            width += len(spaces) #2

                    elif string == 'CHBP':
                        char = input('input bullet point: ')
                        try:
                            char = int(char)
                            newbp = chr(char)
                        except ValueError:
                            char = str(char)
                            newbp = str(char)
                        pretext = pretext[:-lenI] + newbp
                        bp = newbp
                            
                    elif string == 'TITLELINE':
                        ind_lvl = 0
                        pretext = ''
                        string2 = input('input title: ')
                        string = "--[" + string2 + "]--"
                        print(string)
                    elif string == 'SUBTITLE':
                        ind_lvl = 0
                        pretext = ''
                        string2 = input('input subtitle: ')
                        string = "[" + string2 + "]"
                        print(string)

                    elif string == 'CODEMODE':
                        ind_lvl = 0
                        pretext = '  '
                        Coding = True
                        savedBp = bp
                        bp = '  '
                    elif string == 'CODEEXIT':
                        Coding = False
                        pretext = ''
                        bp = savedBp
                        
                    elif string == 'BULLETS':
                        specialPoints()
                        
                    elif string == 'SIDENOTE':
                        note = input('NOTE: ')
                        sidenotePretext = pretext
                        pretext = pretext[:-lenI]
                        string = "<>" + note + "<>"
                        sidenoted = True
                        if len(pretext) + len(string) >= 55:
                            print(pretext + string + '\n')
                        else:
                            print(pretext + string)
                    elif string == 'HIGHLIGHT':
                        note = input('NOTE: ')
                        highlightPretext = pretext
                        pretext = pretext[:-lenI]
                        string = chr(4) + chr(4) + \
                                 ' ' + note + ' ' + \
                                 chr(4) + chr(4)
                        highlighting = True
                        if len(pretext) + len(string) >= 55:
                            print(pretext + string + '\n')
                        else:
                            print(pretext + string)

                    elif string == 'DELETE_LAST_LINE':
                        t = t[0:-len(last_string)]
                        print(pretext[:lenI] +\
                              'deleted string: [' +\
                              last_string + ']')

                    #Make this conditional a function    
                    elif len(string) > width:
                        lines = textwrap.wrap(string, width)
                        new_string = ''
                        for l in lines:
                        
                            index = lines.index(l)
                            if index == len(lines)-1:
                                new_string += l + \
                                              '\n'
                            else:
                                new_string += l + \
                                              '\n' + \
                                              pretext[:-lenI] + \
                                              '  '

                        string = new_string
                            
                    
                    #does not write key commands
                    key_match = 3
                    for k in key_commands:
                        if string == k:
                            key_match -= 1
                            
                    if key_match < 3:
                        t += ''

                    #finalizes text variable "t"

                    else:
                        if string == '':
                            t += '\n'   #blank lines will be blank, not bullets
                            last_string = '\n'
                        elif len(string) > width:
                            t += pretext + string
                            last_string = pretext + string
                        else:
                            t += pretext + string + '\n'
                            last_string = pretext + string + '\n'

                    
                except KeyboardInterrupt:
                    break
                    
            else:
                t += 'SYSTEM\t'+message+'\n'



        #This shows the time of the last save,
        #if savebool is true.

        if savebool:
            t += '\n\tLast Save: [' + \
                 time.asctime() + \
                 ']\n\n'
            

        #Ask to backup file
        backupText = str(input('BackUp File?(y/n)'))
        backup = False
        if backupText.lower() == 'y' or backupText.lower() == 'yes':
            backup = True
            
        #Save File
        with open(file, 'w') as f:
            f.write(t)
        f.close()

        #Write to file backup location too, if backup=True
        if backup:
            currentCwd = self.cwd
            os.chdir(self.MainCwd)
            with open('Backup/'+file, 'w') as f:
                f.write(t)
            f.close()
            os.chdir(currentCwd)
            print("Backup Successful!")

        #Set current text to text in the file
        with open(file) as f:
            text = f.read()
            self.text = text
        f.close()

        

    
    def lp(self):
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
        
        sf(New File)
        -Selects a file. This file is stored and saved 
        until a new file is selected.

        cd([file])
        -Changes current directory. If left blank, it will
        return to the original directory. Type '..' to
        move up one level in the directory.

        NewFile(filename, extension=txt)
        -Creates a new file.
        WARNING: IF THE FILE EXISTS, THEN THE ORIGINAL
        WILL BE DELETED

        EditFile()
        -Edits the current file.
        NOTICE: This only works for txt files.

        lp()
        -Lists all folders and files in the current
        directory.

        search()
        -Searches through a file for keywords, and
        displays results. The user may display the
        line of the text file. This works for date
        and title lines, as in the range of the text.
        WIP-- It will include only the text with a
        higher indent level under the selected line.

        help()
        -Displays this text...

        ''')

    def __str__(self):
        return 'File Name: ' + str(self.FileName) + '\n' +\
               'Main cwd: ' + str(self.MainCwd) + '\n' +\
               'Current cwd: ' + str(self.cwd) + '\n' +\
               'Current path: ' + str(self.path) + '\n' +\
               'Time Stamp: ' +\
               str(self.InitializeTimeStamp) + '\n' +\
               'Version: v' + str(self.version) + '\n' +\
               'Version Log: ' + '\n'
               
        

    
        


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


def startUp():
    def titleDisplay():
        for i in range(8):
            print()
        print("""
        --------------------
        Welcome to PyNotes V0.3.01
        
        This program is used to take notes
        and save them to a simple text document
        
        Author: Max Ferney
        if you have any questions or concerns
        about this program, you may email
        me at maxferney@gmail.com please set
        the title of the subject to PyNotes, so
        I know what it is. Thank you.

        This is now on Github!!!
        so everything above is done through github..
        or something like that, you can email me
        if you would like to though still.
        (Use FileManager to start)
        --------------------
        """)
        for i in range(4):
            print()
    titleDisplay()


startUp()
FileManager = PyNotes()
#(You can rename filemanager to a shorter variable,
# I use the variable 'a')


#This is only if you have subdirectories in your files
#folder

def quickstart(path, system=False, file=None):
    global a
    
    a = PyNotes()
    a.cd()
    a.cd('Files')
    a.cd(path)
    if not system:
        pass
    if system:
        #this is reading it twice
        a.sf(file, show_text=False) #this fixes it
        a.EditFile() 
    

def notes():
    
    
    #Wed Oct 28 08:34:13 2015
    day = time.asctime()[:3]
    hour = time.asctime()[11:13]
    minute = time.asctime()[14:16]
    str_time = time.asctime()[11:16]
    
    day = day.lower()
    hour = int(hour)
    minute = int(minute)


    def convert_time(time='08:00'):
        time_hour = int(time[0:2])
        time_min = int(time[3:])

        minutes = 0
        minutes += (time_hour * 60) + time_min

        return minutes
        

    def is_in_time(days=['mon', 'wed', 'fri'],
                   starttime='08:00',
                   endtime='08:50',
                   minutes_before_start=30):
        
        start_minutes = convert_time(starttime)
        current_minutes = convert_time(str_time)
        end_minutes = convert_time(endtime)
        
        for d in days:
            if day == d:
                if current_minutes >= (start_minutes - minutes_before_start) and \
                   current_minutes <= end_minutes:
                    return True
                else:
                    return False

    #classes
    SOCL = False
    CSCI = False
    WRIT = False
    MCOM = False

    #Sociology
    if is_in_time(['mon', 'wed', 'fri'],'10:00','10:50',30):
        SOCL = True
    #Computer Science Excel
    elif is_in_time(['mon', 'wed'],'17:00','18:15',30):
        CSCI = True
    #Writing
    elif is_in_time(['mon', 'wed'],'18:30','19:45',10):
        WRIT = True
    #MCOM
    elif is_in_time(['tue', 'thu'],'15:30','16:45',30):
        MCOM = True

    #Start Notes
    if SOCL:
        quickstart('SOCL', True, 'SociologyNotes.txt')
    elif CSCI:
        quickstart('CSCI', True, 'excel.txt')
    elif WRIT:
        quickstart('WRIT', True, 'SpringSemesterNotes.txt')
    elif MCOM:
        quickstart('MCOM', True, 'MCOM_notes 01.txt')
    else:
        print("you are not in class right now.")
        print("use: quickstart(path) to see notes.")
        #turn this into a raise error, possibly
        


    
    
    

