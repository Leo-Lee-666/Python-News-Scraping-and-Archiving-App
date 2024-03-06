#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10661531
#    Student name: Hyeonwoo Lee(Leo)
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/). [1PT0202]
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# A module with useful functions on pathnames including:
# normpath: function for 'normalising' a  path to a file to the path-naming
# conventions used on this computer.  Apply this function to the full name
# of your HTML document so that your program will work on any operating system.
# exists: returns True if the supplied path refers to an existing path
from os.path import *

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd
 
# Import the standard Tkinter GUI functions.
from tkinter import *


# Import the date and time function.
# This module *may* be useful, depending on the websites you choose.
# Eg convert from a timestamp to a human-readable date:
# >>> datetime.fromtimestamp(1586999803) # number of seconds since 1970
# datetime.datetime(2020, 4, 16, 11, 16, 43)
from datetime import datetime

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
internet_archive = 'InternetArchive'


################ PUT YOUR SOLUTION HERE #################

#defintion to get order of date's title. numbers will be put in later by code
dates_order = [] 

#function definition which do extract from archived html file
def extract_and_creat_html(): 

    #List of archived html file titles. listed up, to pull off later
    datelists = ['Sat_16_May_2020.html', 'Sun_17_May_2020.html',
             'Mon_18_May_2020.html', 'Tue_19_May_2020.html',
             'Wed_20_May_2020.html', 'Thu_21_May_2020.html',
             'Fri_22_May_2020.html', 'latest.html']

    #open archived html file
    #News file open function according to requirements of code.
    #Reference and application from 'news_archivist.py ' program
    #In datelists[dates_order[len(dates_order)-1]], it helps to open html file
    #in number of different cases.(one of the strong and creativity part of
    #this coding)
    news = open("Internet_Archive/" + datelists[dates_order[len(dates_order)-1]],
                'r', encoding = "UTF-8")
    web_page= news.read()

    #open new html file to write in.
    news_file = open('UPI_news_file.html', 'w')

    #write codings in html file(UPI_news_file)'. These are important to show up
    #tidy page.
    #make a title of page and style of texts and contents
    #refernced from 'Take Home Task 2 (THT2) - Instructions(THT2-NewsArchivist.
    #pdf)' and Leo's practical question '1-TreasureIsland.py'
    news_file.write('''<!DOCTYPE html>
    <html>
      <head>
          <title>News UPI</title>
          <style>
          body  {background-color: skyblue}
          p     {width: 70% margin-left: auto; margin-right: auto; text-align: left}
          h1	{width: 70% margin-left: auto; margin-right: auto; text-align: center}
          h2	{width: 70% margin-left: auto; margin-right: auto; text-align: center}
          hr	{border-style: solid; margin-top; margin-bottom: lem}

          img {
              width: 50%;
          }
          </style>
      </head>
      <body>
         <h1> News Archive UPI</h1>
    ''')
    
    news_file.write('      <ul>\n') 

    #find(extract) content and write down in 'UPI_news_file.html'
    #reference from week 8 practical solution 'movie_title_scraper_V2.py'
    #find titles of each articles
    titles = findall('<item>\s+<title>(.*?)</title>', web_page)
    #find each article's news descriptions. Used view page source (Ctrl + U)
    #button in the page to find range. it was not comes out from just rss 
    abstract = findall('.jpg&quot;&gt;(.*?)</description>', web_page) 
    #find full story
    full_story = findall('</title>\s+<link>(.*?)</link>\s+<guid isPermaLink="false">'
                         , web_page)
    #find each news article's date
    dateline = findall('<pubDate>(.*?)-0400', web_page)
    #find image link of each articles. Used view page source (Ctrl + U) button
    #in the page to find range. it was not comes out from just rss
    news_image = findall('<media:description>&lt;img src=&quot;(.*?)&quot;&gt;',
                         web_page)

    news_date = findall('<pubDate>(.*?)2020', web_page)#find news date
    #write down news date in 'UPI_news_file.html'
    news_file.write('       <h2> ' + news_date[0] + ' 2020</h2>\n')

    #find link of news logo
    news_logo = findall('<url>(.*?)</url>\s+</image>', web_page)
    #write down logo image link and image style in 'UPI_news_file.html'.
    #Refrence from 'Take Home Task 2 (THT2) - Instructions(THT2-
    #NewsArchivist.pdf
    news_file.write('        <p style = "text-align:center"><img src="'
                    + news_logo[0] + '"></p>\n')

    # there was no direct link to website in the source, so just put it myself.
    #referenced from ITD104-Lecture07-Demos '01f-aircraft-hyperlinks.html'
    news_file.write('        <p><strong>News source :</strong><a href ="https://www.upi.com/Top_News/?nav=tn">https://www.upi.com/Top_News/?nav=tn</a></p>\n')
    #write down archivist name in 'UPI_news_file.html'
    news_file.write('        <p><strong>Archivist: </strong>Hyeonwoo Lee (Leo) </p>\n')
    #Used to divide columns, referenced from 'Take Home Task 2 (THT2) -
    #Instructions(THT2-NewsArchivist.pdf)'
    news_file.write('        <hr width = "80%" size = 5px>\n')
    
    #definition of numbers to put content in separately.
    news_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #definition to show up news order
    news_order = ['1. ', '2. ', '3. ', '4. ', '5. ',
                  '6. ', '7. ', '8. ', '9. ', '10. ']

    #the loop code to allocate each article's information 
    for repetition in range(len(news_numbers)):
        #write down titles orderly
        news_file.write('       <h2>' + news_order[repetition]
                        + titles[repetition] + '</h2>\n') 
        #write down article's image urls orderly
        news_file.write('       <p style = "text-align:center"><img src="'
                        + news_image[repetition] + '"></p>\n')
        #write down descriptions orderly
        news_file.write('       <p>' + abstract[repetition] + '</p>\n')
        #write down full story urls orderly. referenced from ITD104-Lecture07
        #-Demos '01f-aircraft-hyperlinks.html'
        news_file.write('       <p><strong>Full story: </strong><a href ="'
                        + full_story[repetition] + '">'
                        + full_story[repetition] +'</a></p>\n')
        #write down article's datelines orderly
        news_file.write('       <p><strong>Dateline: </strong>'
                        + dateline[repetition] + '</p>\n')
        #Used to divide columns, referenced from 'Take Home Task 2 (THT2)
        #- Instructions(THT2-NewsArchivist.pdf)'
        news_file.write('       <hr width = "80%" size = 5px>\n')

    #to end html structure, write important things
    news_file.write('  </ul>\n')
    news_file.write('</body>\n')
    news_file.write('</html>')

    news_file.close()
#archive latest news html from web page
#refernced from 'news_archivist.py'
def extract_latest_html():
    web_page = urlopen('https://rss.upi.com/news/top_news.rss')#open url
    web_page_contents = web_page.read().decode('UTF-8')#do read and decode
    #make a latest archive html file in located folder
    text_file = open('Internet_Archive/latest.html', 'w', encoding = 'UTF-8')
    text_file.write(web_page_contents)#write down contents
    text_file.close()


window = Tk()
window.title('UPI News Archive')#make a title of program
window.geometry('950x350')#define the size of gui
window.configure(bg='skyblue')#decide background color

#load image file. Refernced from ITD104-Lecture06-Demos '14-used_cars.py'
img = PhotoImage(file= 'UPI5.png')
#make a label to show up image. Refernced from ITD104-Lecture06-Demos
#'14-used_cars.py'
img_lbl = Label(window, image = img)
ex_lbl = Label(window, text = " UPI News Archive",
               font = ('Arial', 15))#add text
lbl = Label(window, text = " Choose which day's news to extract ..",
            font = ('Arial', 15))#add text

#lists of dates to put in to list box
dates = ['Sat, 16 May 2020','Sun, 17 May 2020','Mon, 18 May 2020',
         'Tue, 19 May 2020','Wed, 20 May 2020','Thu, 21 May 2020',
         'Fri, 22 May 2020','latest']

# definition of button function to extract from archive htmls
def extract_html():
    #if somthing selected from list box... Refernced from Practical06-Solution
    #'shopping_list_Listbox.py'
    if choices.curselection() != ():        
        
        #Function to prevent overlapping codes
        for choice_loop in range(8):
            #if chosen date is same as dates[choice_loop]...
            #Refernced from Practical06-Solutions 'shopping_list_Listbox.py'
            if choices.get(choices.curselection()) == dates[choice_loop]:
                #put int into dates_order list..Refernced from
                #Practical06-Solutions 'shopping_list_saveable.py'
                dates_order.append(int(choice_loop))
                extract_and_creat_html()# do extract from selected file
                #change comment
                lbl['text'] = " __News extracted from archive ..! __  " 
                         
#function of open html file
def display_html():
    #if somthing selected from list box... Refernced from Practical06-Solutions
    #'shopping_list_Listbox.py'
    if choices.curselection() != ():
        # open html file which is already extracted
        webopen('UPI_news_file.html', 'r')
        lbl['text'] = " Choose which day's news to extract .. " #change comment

#button function, archive latest  file
def archive_news():
    extract_latest_html()#extract Latest news file and archive
    lbl['text'] = " __Latest news archived succesfully__ " #change comment

#make a listbox which shows up dates. Refernced from Practical06-Solutions
#'shopping_list_Listbox.py'
choices = Listbox(window, font = ('Arial', 20), height = len(dates))
for item in (dates):#put dates into list
    choices.insert(END, item)#put dates into listbox from lists

#make a buttons and lik to functions
extract_html = Button(window, text = ' Extract from archive \n to HTML news file ',
                     font = ('Arial', 15), command = extract_html)

display_html = Button(window, text = ' Display HTML \n news file ',
                     font = ('Arial', 15), command = display_html)

archive_news = Button(window, text = ' Archive latest \n news from the web ',
                     font = ('Arial', 15), command = archive_news)
#Arrange the buttons
img_lbl. grid(row = 2)
lbl .grid(row = 3, column = 1)
ex_lbl.grid(row = 1, column = 1)
choices.grid(row = 2, column = 1)
extract_html.grid(row = 2, column = 2)
archive_news.grid(row = 3, column = 0)
display_html.grid(row = 3, column = 2)
window.mainloop()
