import csv
file = "filmsDZ17.csv"

with open(file, newline='') as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
    print(reader[0])
    print(reader[-1])

title_info = []
year_info = []


def func_title_rating():
    for film in reader:
        if film['rating'] > '9':
            print(film["title"])


def func_title_film(film_yes):
    for film in reader:
        if film["title"].startswith(film_yes):
            title_info.append(film["title"])


def func_title_sort(film_yes):
    for i, film in enumerate(reader):
        if film["title"].startswith(film_yes):
            print(f'Назва фільму: ({film["title"]})\tв базі є такий фільм під номером:-({i + 1})')


def func_title_num(num):
    for i, film in enumerate(reader):
        if num == i+1:
            print('назва фільму: ', film['title'], ', рік: ', film['year'], ', опис: ', film['description'])


def func_genre_title():
    genres = []
    for i in reader:
        i['gen'] = eval(i['gen'])
        for j in i['gen']:
            genres.append(j['genre'])
    genres = set(genres)
    for gen in genres:
        print(gen)
    return True


def func_genre_title_films(genre_yes):
    for d in reader:
        for j in d['gen']:
            if j['genre'] == genre_yes:
                print(d['title'])


def func_year_yes(num_year):
    for year in reader:
        if year['year'] == num_year:
            year_info.append(year['year'])


def func_num_year(num_year):
    for i, year in enumerate(reader):
        if year['year'] == num_year:
            print(f'Назва фільму: ({year["title"]})\tв базі є такий фільм під номером:-({i + 1})')


def add_film():
    add_title = input('Введіть назву фільму: ').capitalize()
    add_year = input("Введіть дату випуску фільму у прокат: ")
    add_rating = input('Введіть рейтінг фільму: ')
    name_title = [[None, f'{add_title}', f'{add_year}', None, None, None, None, f'{add_rating}', None, None, None, None, None, None, None, None, None, None]]
    with open('filmsDZ17.csv', 'a') as myFile:
        writer = csv.writer(myFile)
        writer.writerows(name_title)
    with open('filmsDZ17.csv', newline='') as csvfile:
        reader_new = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
        for i, film in enumerate(reader_new):
            if film['title'] == add_title:
                print(f'Назва фільму: ({film["title"]})\tв базі є такий фільм під номером:-({i + 1})')


