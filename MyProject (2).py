from tkinter import *

import mysql.connector as sql
import webbrowser

import random


con = sql.connect(host = "localhost",username = "root",password = "amar2005")
if con.is_connected():
    print("Successfully Connected")
    
cursor = con.cursor()

cursor.execute("create database if not exists movie")
cursor.execute("use movie")
cursor.execute('''CREATE TABLE if not exists moviesdb (
Movie_ID     integer       NOT NULL UNIQUE,
Movie_Name   varchar(1000) NOT NULL,
Year         year          NOT NULL,
Genre        varchar(1000) NOT NULL,
Rating       decimal(5,2)  NOT NULL check (rating <= 10),
Age_Rating   varchar(50)   NOT NULL,
Trailer_Link varchar(1000) NOT NULL, 
Cast         varchar(1000) NOT NULL,
Director     varchar(1000) NOT NULL,
Summary      varchar(1000) NOT NULL)''')

master = Tk()
master.geometry("1000x1000")
master['bg'] = '#000000'   

def addmoviebutton():
    addwindow = Toplevel(master)
    addwindow.title("Add Movies")
    addwindow.geometry("1000x1000")
    addwindow['bg'] = '#000000'
    Label(addwindow,text = "Enter the Movie Details Here: ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=200,y=10)
    
    Label(addwindow,text = "ID: ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=50)
    global addid
    addid = Entry(addwindow,width=50,font = ('Fixedsys',20),bg = '#000000',fg='#38E54D')
    addid.place(x=500,y=50)
    
    Label(addwindow,text = "Name: ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=100)
    global addname
    addname = Entry(addwindow,width=50,font = ('Fixedsys',20),bg = '#000000',fg='#38E54D')
    addname.place(x=500,y=100)
    
    Label(addwindow,text = "Year Of Release: ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=150)
    global addyear
    addyear = Entry(addwindow,width=50,font = ('Fixedsys',20),bg = '#000000',fg='#38E54D')
    addyear.place(x=500,y=150)
    
    Label(addwindow,text = "Genres: ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=200)
    global addgenre
    addgenre = Entry(addwindow,width=50,font = ('Fixedsys',20),bg = '#000000',fg='#38E54D')
    addgenre.place(x=500,y=200)
    
    Label(addwindow,text = "Rating: ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=250)
    global addrating
    addrating = Entry(addwindow,width=50,font = ('Fixedsys',20),bg = '#000000',fg='#38E54D')
    addrating.place(x=500,y=250)
    
    Label(addwindow,text = "Age Rating: ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=300)
    global addagerating
    addagerating = Entry(addwindow,width=50,font = ('Fixedsys',20),bg = '#000000',fg='#38E54D')
    addagerating.place(x=500,y=300)
    
    Label(addwindow,text = "Trailer Link: ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=350)
    global addlink
    addlink = Entry(addwindow,width=50,font = ('Fixedsys',20),bg = '#000000',fg='#38E54D')
    addlink.place(x=500,y=350)
    
    Label(addwindow,text = "Cast: ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=400)
    global addcast
    addcast = Entry(addwindow,width=50,font = ('Fixedsys',20),bg = '#000000',fg='#38E54D')
    addcast.place(x=500,y=400)
    
    Label(addwindow,text = "Director: ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=450)
    global adddirector
    adddirector = Entry(addwindow,width=50,font = ('Fixedsys',20),bg = '#000000',fg='#38E54D')
    adddirector.place(x=500,y=450)
    
    Label(addwindow,text = "Summary: ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=500)
    global addsummary
    addsummary = Entry(addwindow,width=50,font = ('Fixedsys',20),bg = '#000000',fg='#38E54D')
    addsummary.place(x=500,y=500)

    addmoviebutton = Button(addwindow, text = "Add Movie To Database", command = addmovie,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    addmoviebutton.place(x=500,y=550)
    
def addmovie():
    i_d = addid.get()
    name = addname.get()
    year = addyear.get()
    genre = addgenre.get()
    rating = addrating.get()
    age_rating = addagerating.get()
    trailer_link = addlink.get()
    cast = addcast.get()
    director = adddirector.get()
    summary = addsummary.get()
    addquery = '''insert into moviesdb values ({},'{}','{}','{}',{},'{}','{}','{}','{}','{}')'''.format(i_d,name,year,genre,rating,age_rating,trailer_link,cast,director,summary)
    cursor.execute(addquery)
    con.commit()

def open_trailer(url):
   webbrowser.open_new_tab(url)

def display_movie(i):
    displaywindow = Toplevel(master)
    displaywindow.title(str(i))
    displaywindow.geometry("500x500")
    displaywindow['bg'] = '#000000'
    display_query = "select * from moviesdb where movie_name = '{}'".format(str(i))
    cursor.execute(display_query)
    display_list = cursor.fetchall()
    for i in display_list:
        Label(displaywindow,text="ID: "+str(i[0]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=50)
        Label(displaywindow,text="Title: "+str(i[1]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=100)
        Label(displaywindow,text="Year of Release: "+str(i[2]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=150)
        Label(displaywindow,text="Genre: "+str(i[3]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=200)
        Label(displaywindow,text="Rating: "+str(i[4]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=250)
        Label(displaywindow,text="Age Rating: "+str(i[5]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=300)
        link = Label(displaywindow, text="Trailer Link: " + str(i[6]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        link.place(x=100,y=350)
        link.bind("<Button-1>", lambda e: [open_trailer(str(j[6]))])
        Label(displaywindow,text="Cast: "+str(i[7]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),wraplength=1000).place(x=100,y=400)
        Label(displaywindow,text="Director: "+str(i[8]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=500)
        Label(displaywindow,text="Summary: "+str(i[9]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),wraplength=1000).place(x=100,y=550)

    
def search_window():
    searchwindow = Toplevel(master)
    searchwindow.title("Search Options")
    searchwindow.geometry("1000x1000")
    searchwindow['bg'] = '#000000'
    Label(searchwindow,text="How would you like to search",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=0)
    #TITLE
    global titleentry
    titleentry=Entry(searchwindow, width=20 ,text = "Enter the Title",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')  
    titleentry.place(x=500, y=50)
    titlebutton = Button(searchwindow, height = 1, width=20, text = "Search By Title    ", command = title_search,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    titlebutton.place(x=100, y=50)
    #GENRE
    global genreentry
    genreentry=Entry(searchwindow, width=20, text = "Enter the Genre   ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')  
    genreentry.place(x=500, y=100)
    genrebutton = Button(searchwindow, height = 1, width=20, text = "Search By Genre    ", command = genre_search,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    genrebutton.place(x=100, y=100)
    #ACTOR
    global actorentry
    actorentry=Entry(searchwindow, width=20, text = "Enter The Actor   ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')  
    actorentry.place(x=500, y=150)
    actorbutton = Button(searchwindow, height = 1, width=20, text = "Search By Actor    ", command = actor_search,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    actorbutton.place(x=100, y=150)
    #DIRECTOR
    global directorentry
    directorentry=Entry(searchwindow, width=20, text = "Enter The Director",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')  
    directorentry.place(x=500, y=200)
    directorbutton = Button(searchwindow, height = 1, width=20, text = "Search By Director", command = director_search,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    directorbutton.place(x=100, y=200)
    #YEAR
    global yearentry
    yearentry=Entry(searchwindow, width=20, text = "Enter The Year",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')  
    yearentry.place(x=500, y=250)
    yearbutton = Button(searchwindow, height = 1, width=20, text = "Search By Year     ", command = year_search,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    yearbutton.place(x=100, y=250)
    #RATING
    global ratingentry
    ratingentry=Entry(searchwindow, width=20, text = "Enter The Rating  ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')  
    ratingentry.place(x=500, y=300)
    ratingbutton = Button(searchwindow, height = 1, width=20, text = "Search By Rating  ", command = rating_search,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    ratingbutton.place(x=100, y=300)
    #RANDOM
    randombutton = Button(searchwindow, height = 1, width=20, text = "Random Search   ", command = random_search,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    randombutton.place(x=100,y=350)


def title_search():
    title = titleentry.get()
    display_movie(title.title())

def genre_search():
    genre = genreentry.get()
    genre_query = '''select movie_name from moviesdb where genre like "%{}%"'''.format(genre)
    cursor.execute(genre_query)
    genre_list = cursor.fetchall()
    for g in genre_list:
        display_movie(str(g[0]))
    
def actor_search():
    actor = actorentry.get()
    cast_query = "select movie_name from moviesdb where cast like '%{}%'".format(actor)
    cursor.execute(cast_query)
    cast_list = cursor.fetchall()
    for c in cast_list:
        display_movie(str(c[0]))
             
def director_search():
    actor = actorentry.get()
    cursor.execute("select movie_name, director from moviesdb")
    director_list = cursor.fetchall()
    for d in director_list:
        if director.title() in eval(str("("+str(d[1])+",)")):
             display_movie(str(d[0]))


def year_search():
    year = yearentry.get()
    year_query =  "select movie_name, year from moviedb where year = {}".format(str(year))
    cursor.execute(year_query)
    year_list = cursor.fetchall()
    for y in year_list:
        display(str(i[0]))

def rating_search():
    rating = ratingentry.get()
    cursor.execute("select movie_name, rating from moviesdb where rating = {}".format(str(rating)))
    rating_list = cursor.fetchall()
    for r in rating_list:
        display(str(r[0]))
        
def random_search():
    cursor.execute("select count(*) from moviesdb")
    a=cursor.fetchall()
    random_select = random.randint(0,int(a[0][0])-1)
    cursor.execute("select movie_name from moviesdb")
    random_list =  cursor.fetchall()
    b = random_list[random_select][0]
    display_movie(b)

def edit_movie():
    global edit_window
    edit_window = Toplevel(master)
    edit_window.geometry("1000x1000")
    edit_window.title("edit window")
    edit_window['bg']='#000000'
    Label(edit_window,text="what movie would you like to edit",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=300,y=0)
    global edit_entry
    edit_entry = Entry(edit_window, width=20 ,text = "Enter the Movie",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    edit_entry.place(x=300,y=50)
    edit_button = Button(edit_window, height = 1, width=20, text = "Edit Details", command = edit_display,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    edit_button.place(x=300,y=100)
    
def edit_display():
    global edit_mov
    edit_mov = edit_entry.get()
    edit_query = "select * from moviesdb where movie_name = '{}'".format(edit_mov)
    cursor.execute(edit_query)
    edit_list = cursor.fetchall()
    for i in edit_list:
        Label(edit_window,text="ID: "+str(i[0]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=10,y=150)
        
        Label(edit_window,text="Title: "+str(i[1]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=10,y=200)
        global Edit_Title_Entry
        Edit_Title_Entry = Entry(edit_window, width=20, text = "Enter The Title",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Title_Entry.place(x=1300,y=200)
        Edit_Title_Button = Button(edit_window,text="Edit Title?", command = edit_title, bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Title_Button.place(x=1000,y=200)
        
        Label(edit_window,text="Year of Release: "+str(i[2]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=10,y=250)
        global Edit_Year_Entry
        Edit_Year_Entry = Entry(edit_window, width=20, text = "Enter The Year",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Year_Entry.place(x=1300,y=250)
        Edit_Year_Button = Button(edit_window,text="Edit Year?",command = edit_year, bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Year_Button.place(x=1000,y=250)
        
        Label(edit_window,text="Genre: "+str(i[3]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=10,y=300)
        global Edit_Genre_Entry
        Edit_Genre_Entry = Entry(edit_window, width=20, text = "Enter The Genre",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Genre_Entry.place(x=1300,y=300)
        Edit_Genre_Button = Button(edit_window,text="Edit Genre?", command = edit_genre,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Genre_Button.place(x=1000,y=300)

        Label(edit_window,text="Rating: "+str(i[4]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=10,y=350)
        global Edit_Rating_Entry
        Edit_Rating_Entry = Entry(edit_window, width=20, text = "Enter The Rating  ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Rating_Entry.place(x=1300,y=350)
        Edit_Rating_Button = Button(edit_window,text="Edit Rating?", command = edit_rating, bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Rating_Button.place(x=1000,y=350)
        
        Label(edit_window,text="Age Rating: "+str(i[5]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=10,y=400)
        global Edit_Age_Entry
        Edit_Age_Entry = Entry(edit_window, width=20, text = "Enter The Age Rating  ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Age_Entry.place(x=1300,y=400)
        Edit_Age_Button = Button(edit_window,text="Edit Age Rating", command = edit_age_rating, bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Age_Button.place(x=1000,y=400)
        
        link = Label(edit_window, text="Trailer Link: " + str(i[6]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        link.place(x=10,y=450)
        link.bind("<Button-1>", lambda e: [open_trailer(str(j[6]))])
        global Edit_Link_Entry
        Edit_Link_Entry = Entry(edit_window, width=20, text = "Enter The Link ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Link_Entry.place(x=1300,y=450)
        Edit_Link_Button = Button(edit_window,text="Edit Link", command = edit_trailer_link, bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Link_Button.place(x=1000,y=450)
        
        Label(edit_window,text="Cast: "+str(i[7]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center',wraplength=1000).place(x=10,y=500)
        global Edit_Cast_Entry
        Edit_Cast_Entry = Entry(edit_window, width=20, text = "Enter The Cast ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Cast_Entry.place(x=1300,y=500)
        Edit_Cast_Button = Button(edit_window,text="Edit Cast", command = edit_cast, bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Cast_Button.place(x=1000,y=500)
        
        Label(edit_window,text="Director: "+str(i[8]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=10,y=600)
        global Edit_Director_Entry
        Edit_Director_Entry = Entry(edit_window, width=20, text = "Enter The Director ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Director_Entry.place(x=1300,y=600)
        Edit_Director_Button = Button(edit_window,text="Edit Director", command = edit_director, bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Director_Button.place(x=1000,y=600)
        
        Label(edit_window,text="Summary: "+str(i[9]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center',wraplength=1000).place(x=10,y=650)
        global Edit_Summary_Entry
        Edit_Summary_Entry = Entry(edit_window, width=20, text = "Enter the Summary  ",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Summary_Entry.place(x=1300,y=650)
        Edit_Summary_Button = Button(edit_window,text="Edit Summary", command = edit_summary, bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        Edit_Summary_Button.place(x=1000,y=650)

def edit_title():
    Title_Edit = Edit_Title_Entry.get()
    edit_mov = edit_entry.get()
    update_query = "update moviesdb set movie_name = '{}' where movie_name = '{}'".format(Title_Edit,edit_mov)
    cursor.execute(update_query)
    con.commit()
    
def edit_year():
    Year_Edit = Edit_Year_Entry.get()
    edit_mov = edit_entry.get()
    update_query = "update moviesdb set year = '{}' where movie_name = '{}'".format(Year_Edit,edit_mov)
    cursor.execute(update_query)
    con.commit()
    
def edit_genre():
    Genre_Edit = Edit_Genre_Entry.get()
    edit_mov = edit_entry.get()
    update_query = "update moviesdb set genre = '{}' where movie_name = '{}'".format(Genre_Edit,edit_mov)
    cursor.execute(update_query)
    con.commit()
    
def edit_rating():
    Rating_Edit = Edit_Rating_Entry.get()
    edit_mov = edit_entry.get()
    update_query = "update moviesdb set rating = {} where movie_name = '{}'".format(Rating_Edit,edit_mov)
    cursor.execute(update_query)
    con.commit()
    
def edit_age_rating():
    Age_Edit = Edit_Age_Entry.get()
    edit_mov = edit_entry.get()
    update_query = "update moviesdb set age_rating = '{}' where movie_name = '{}'".format(Age_Edit,edit_mov)
    cursor.execute(update_query)
    con.commit()
    
def edit_trailer_link():
    Link_Edit = Edit_Link_Entry.get()
    edit_mov = edit_entry.get()
    update_query = "update moviesdb set trailer_link = '{}' where movie_name = '{}'".format(Link_Edit,edit_mov)
    cursor.execute(update_query)
    con.commit()

def edit_cast():
    Cast_Edit = Edit_Cast_Entry.get()
    edit_mov = edit_entry.get()
    update_query = "update moviesdb set cast = '{}' where movie_name = '{}'".format(Cast_Edit,edit_mov)
    cursor.execute(update_query)
    con.commit()

def edit_director():
    Director_Edit = Edit_Director_Entry.get()
    edit_mov = edit_entry.get()
    update_query = "update moviesdb set director = '{}' where movie_name = '{}'".format(Director_Edit,edit_mov)
    cursor.execute(update_query)
    con.commit()

def edit_summary():
    Summary_Edit = Edit_Summary_Entry.get()
    edit_mov = edit_entry.get()
    update_query = "update moviesdb set summary = '{}' where movie_name = '{}'".format(Summary_Edit,edit_mov)
    cursor.execute(update_query)
    con.commit()
    
def delete_movie():
    global delete_window 
    delete_window = Toplevel(master)
    delete_window.title("Search Options")
    delete_window.geometry("1000x1000")
    delete_window['bg'] = '#000000'
    Label(delete_window,text="What movie would you delete?",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=300,y=0)
    global delete_entry
    delete_entry=Entry(delete_window, width=20 ,text = "Enter the Title",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')  
    delete_entry.place(x=300, y=50)
    delete_button = Button(delete_window, height = 1, width=20, text = "Delete?   ", command = delete_display,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    delete_button.place(x=300, y=100)
    
def delete_display():
    delete_movie_name = delete_entry.get()
    delete_display_query = "select * from moviesdb where movie_name = '{}'".format(delete_movie_name)
    cursor.execute(delete_display_query)
    delete_list = cursor.fetchall()
    for i in delete_list:
        Label(delete_window,text="ID: "+str(i[0]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=150)
        Label(delete_window,text="Title: "+str(i[1]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=200)
        Label(delete_window,text="Year of Release: "+str(i[2]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=250)
        Label(delete_window,text="Genre: "+str(i[3]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=250)
        Label(delete_window,text="Rating: "+str(i[4]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=300)
        Label(delete_window,text="Age Rating: "+str(i[5]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=350)
        link = Label(delete_window, text="Trailer Link: " + str(i[6]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
        link.place(x=100,y=350)
        link.bind("<Button-1>", lambda e: [open_trailer(str(j[6]))])
        Label(delete_window,text="Cast: "+str(i[7]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center',wraplength=1000).place(x=100,y=400)
        Label(delete_window,text="Director: "+str(i[8]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=100,y=500)
        Label(delete_window,text="Summary: "+str(i[9]),bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center',wraplength=1000).place(x=100,y=550)
    delete_command_button = Button(delete_window, height = 1, width=20, text = "Confirm Delete?", command = delete_command,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center')
    delete_command_button.place(x=300, y=700)    
    
def delete_command():
    delete_movie_name = delete_entry.get()
    delete_movie_name = delete_movie_name.title()
    delete_query = "delete from moviesdb where Movie_name = '{}'".format(delete_movie_name)
    cursor.execute(delete_query)
    con.commit()
    
    
    
cursor.execute("select count(*) from moviesdb")
a=cursor.fetchall()
Label(master,text="Welcome to the Database",bg = '#000000',fg='#38E54D',font = ('Fixedsys',40),justify='center' ).place(x=400,y=50)
Label(master,text="Currently serving " + str(a[0][0]) + " Movies",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=400,y=100)
Label(master,text="What would you like to do?",bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=400,y=150)
Button(master,text="Search movies",command=search_window,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=400,y=200)
Button(master,text="Add movies",command=addmoviebutton,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=400,y=250)
Button(master,text="Delete movies",command=delete_movie,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=400,y=300)
Button(master,text="Edit Movies",command=edit_movie,bg = '#000000',fg='#38E54D',font = ('Fixedsys',20),justify='center').place(x=400,y=350)


mainloop()

                   

        

    

    
    

            
    
    
    
