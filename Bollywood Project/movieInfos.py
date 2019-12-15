import csv
import wikipedia
import pandas as pd
import requests
import os
import threading
import string 

counter = 0

def findMovieDetails(tables):
    movie_index = -1
    #find where the movie information is stored at
    for i in range(len(tables)):
        if 'Directed by' in str(tables[i]):
            movie_index = i

    if movie_index != -1:
        movie_name = list(tables[movie_index])[0]
        release_year = 0
        running_time = 0
        for i in range(len(tables[movie_index])):
            if 'Release date' in tables[movie_index]._get_values[i]:
                release_year = tables[movie_index]._get_values[i][1].split('\xa0')
                print(release_year)
                release_year = release_year[len(release_year)-1]
        
        for i in range(len(tables[movie_index])):
            if 'Running time' in tables[movie_index]._get_values[i]:
                running_time = tables[movie_index]._get_values[i][1].split(' ')[0]
        print(movie_name, " ", release_year, " ", running_time)
        return movie_name, release_year, running_time
    print(0, " ", 0, " ", 0)
    return 0, 0, 0

def findSongTime(tables):
    song_minutes = 0.0
    songIndex = -1
    number_songs = 0

    for i in range(len(tables)):
        if 'Singer(s)' in str(tables[i]):
            songIndex = i

    if songIndex == -1:
        return 0, 0

    else:

        print(len(tables[songIndex]._get_values[0]))
        for i in range(len(tables[songIndex]._get_values)):
            times = str(tables[songIndex]._get_values[i][len(tables[songIndex]._get_values[i])-1]).split(':')
            track_time = 0
            if len(times) == 2:
                try:
                    track_time = float(int(times[0]) + int(times[1])/60.0)
                except ValueError:
                    pass

            #will deal with datasets where the total time is already there
            if track_time != 0:
                if round(track_time, 2) != round(song_minutes, 2):
                    number_songs = number_songs + 1
                    song_minutes = song_minutes + track_time

        song_minutes = round(song_minutes, 2)
        return song_minutes, number_songs

def populatemovies1(list_of_movies):
    global counter
    with open('movies1.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Movie Name', 'Release Year', 'Movie Runtime', 'Total Song Length', 'Number of Songs'])

        #write details to the movies.csv file
        for i in range(len(list_of_movies)):
            movie_name = list_of_movies[i].split("\n")[0]
            tables = 0
            try:
                print("Trying (", counter, ") ", movie_name)
                counter += 1
                worked = False
                try:
                    html = wikipedia.page(movie_name).html()
                    worked = True
                except TimeoutError:
                    pass
                except ConnectionError:
                    pass
                if worked:
                    if "</table>" in html:
                        tables = pd.read_html(html)
                        movie_details = findMovieDetails(tables)
                        movie_songs = findSongTime(tables)
                        if movie_songs[1] != 0 and movie_details[1] != 0 and movie_details[2] != 0:
                            employee_writer.writerow([movie_details[0], movie_details[1], movie_details[2], movie_songs[0], movie_songs[1]])
                            print("index: ", i, " ", movie_name, " added to file.")
            except wikipedia.exceptions.PageError:
                print("Page doesn't exist")
            except wikipedia.exceptions.DisambiguationError:
                print("Many results, so ", movie_name, " was not added")

def populatemovies2(list_of_movies):
    global counter
    with open('movies2.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Movie Name', 'Release Year', 'Movie Runtime', 'Total Song Length', 'Number of Songs'])

        #write details to the movies.csv file
        for i in range(len(list_of_movies)):
            movie_name = list_of_movies[i].split("\n")[0]
            tables = 0
            try:
                print("Trying (", counter, ") ", movie_name)
                counter += 1
                try:
                    html = wikipedia.page(movie_name).html()
                    worked = True
                except TimeoutError:
                    pass
                except ConnectionError:
                    pass
                if worked:
                    if "</table>" in html:
                        tables = pd.read_html(html)
                        movie_details = findMovieDetails(tables)
                        movie_songs = findSongTime(tables)
                        if movie_songs[1] != 0 and movie_details[1] != 0 and movie_details[2] != 0:
                            employee_writer.writerow([movie_details[0], movie_details[1], movie_details[2], movie_songs[0], movie_songs[1]])
                            print("index: ", i, " ", movie_name, " added to file.")
            except wikipedia.exceptions.PageError:
                print("Page doesn't exist")
            except wikipedia.exceptions.DisambiguationError:
                print("Many results, so ", movie_name, " was not added")


def populatemovies3(list_of_movies):
    global counter
    with open('movies3.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Movie Name', 'Release Year', 'Movie Runtime', 'Total Song Length', 'Number of Songs'])

        #write details to the movies.csv file
        for i in range(len(list_of_movies)):
            movie_name = list_of_movies[i].split("\n")[0]
            tables = 0
            try:
                print("Trying (", counter, ") ", movie_name)
                counter += 1
                try:
                    html = wikipedia.page(movie_name).html()
                    worked = True
                except TimeoutError:
                    pass
                except ConnectionError:
                    pass
                if worked:
                    if "</table>" in html:
                        tables = pd.read_html(html)
                        movie_details = findMovieDetails(tables)
                        movie_songs = findSongTime(tables)
                        if movie_songs[1] != 0 and movie_details[1] != 0 and movie_details[2] != 0:
                            employee_writer.writerow([movie_details[0], movie_details[1], movie_details[2], movie_songs[0], movie_songs[1]])
                            print("index: ", i, " ", movie_name, " added to file.")
            except wikipedia.exceptions.PageError:
                print("Page doesn't exist")
            except wikipedia.exceptions.DisambiguationError:
                print("Many results, so ", movie_name, " was not added")


def populatemovies4(list_of_movies):
    global counter
    with open('movies4.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Movie Name', 'Release Year', 'Movie Runtime', 'Total Song Length', 'Number of Songs'])

        #write details to the movies.csv file
        for i in range(len(list_of_movies)):
            movie_name = list_of_movies[i].split("\n")[0]
            tables = 0
            try:
                print("Trying (", counter, ") ", movie_name)
                counter += 1
                try:
                    html = wikipedia.page(movie_name).html()
                    worked = True
                except TimeoutError:
                    pass
                except ConnectionError:
                    pass
                if worked:
                    if "</table>" in html:
                        tables = pd.read_html(html)
                        movie_details = findMovieDetails(tables)
                        movie_songs = findSongTime(tables)
                        if movie_songs[1] != 0 and movie_details[1] != 0 and movie_details[2] != 0:
                            employee_writer.writerow([movie_details[0], movie_details[1], movie_details[2], movie_songs[0], movie_songs[1]])
                            print("index: ", i, " ", movie_name, " added to file.")
            except wikipedia.exceptions.PageError:
                print("Page doesn't exist")
            except wikipedia.exceptions.DisambiguationError:
                print("Many results, so ", movie_name, " was not added")

def findMovies():
    all_movies = []
    for w in range(1960, 2019):
        if w != 1992 and w!= 1995: #1992 is incorrectly formatted so we'll skip over it
            movie_webpage = pd.read_html(wikipedia.page("List of Bollywood films of "+str(w)).html())
            movie_table_indecies = []
            movie_name_index = -1
            for i in range(len(movie_webpage)):
                if "Director" in movie_webpage[i]:
                    movie_table_indecies.append(i)
                    if movie_name_index == -1:
                        for j in range(len(list(movie_webpage[i]))):
                            if "Title" == list(movie_webpage[i])[j]:
                                movie_name_index = j


            #adds things to the all_movies array
            for i in range(len(movie_table_indecies)):
                for j in range(len(movie_webpage[movie_table_indecies[i]])):
                    print(movie_webpage[movie_table_indecies[i]]._get_values[j][movie_name_index])
                    all_movies.append(movie_webpage[movie_table_indecies[i]]._get_values[j][movie_name_index])
            
            print("done with \"List of Bollywood films of "+str(w)+"\"")
            print(len(all_movies))
        
    return all_movies

if __name__ == '__main__':
    list_of_movies = []
    if os.path.getsize("zebFile.txt"):
        f = open("zebFile.txt", "r")

        for line in f:
            list_of_movies.append(line)

        f.close()
            
    else:
        list_of_movies = findMovies()
        f = open("zebFile.txt", "w")

        for movie in list_of_movies:
            f.write(str(movie)+"\n")
        
        f.close()

    if pd.read_csv('movies.csv').empty:
        print("file is emtpy")
        #populatemovies(list_of_movies)

        t1 = threading.Thread(target=populatemovies1, args=(list_of_movies[0:int(len(list_of_movies)/4)], ))
        t2 = threading.Thread(target=populatemovies2, args=(list_of_movies[int(len(list_of_movies)/4):int(len(list_of_movies)/2)], ))
        t3 = threading.Thread(target=populatemovies3, args=(list_of_movies[int(len(list_of_movies)/2):int(3*len(list_of_movies)/4)], ))
        t4 = threading.Thread(target=populatemovies4, args=(list_of_movies[int(3*len(list_of_movies)/4):], ))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()

        #populatemovies(list_of_movies)
    else:
        print("The file isn't empty")