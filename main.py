import func as t1

print('Вас вiтає бiблiотека фiльмiв')
print('''Якщо ви бажаєте шукати фiльм по назвi, то введiть - (title)
Якщо ви бажаєте шукати фiльм по жанру, то введiть - (genre)
Якщо ви бажаєте шукати фiльм по даті випуску фільму у прокат, то введiть - (year)
Якщо не знайдете фільм, то ви можете самостійно його добавити''')
zirka = "*" * 100 + "\n"
print(f'{zirka}')

fraza = True
while fraza:
    greetings = input('Введіть (title), (genre) чи (year): ').lower()
    print(f'{zirka}')
    if greetings == "title" or greetings == "genre" or greetings == "year":
        fraza = False
        if greetings == "title":
            print('Можливо вас зацікавить список фільмів з рейтингом > 9: ')
            t1.func_title_rating()
            print(f'{zirka}')
            film_yes = input("Введіть назву фильму: ").title()
            t1.func_title_film(film_yes)
            if len(t1.title_info) != 0:
                t1.func_title_sort(film_yes)
                print(f'{zirka}')
                num = input('Введіть номер фільму: ')
                print(f'{zirka}')
                t1.func_title_num(int(num))
                break
            else:
                print('Нажаль немає такого фільму')
                print(f'{zirka}')
                print('''Ви бажаєте самостійно його добавити?
                Якщо так, то введіть - (Y)
                Якщо ні, то введіть - (N)''')
                print(f'{zirka}')
                yes_no = input('Введіть (Y) чи (N): ').capitalize()
                print(f'{zirka}')
                if yes_no == 'Y':
                    t1.add_film()
                    print(f'{zirka}')
                    print('Ваш фільм додан до списку')
                    break
                else:
                    print('Шкода що вам не допомогли')
                    break
        if greetings == "genre":
            print('Жанри: ')
            t1.func_genre_title()
            print(f'{zirka}')
            genre_yes = input("Введіть назву жанру: ").capitalize()
            print(f'{zirka}')
            print('Список фільмів з цим жанром: ')
            t1.func_genre_title_films(genre_yes)
            print(f'{zirka}')
            film_yes = input("Введіть назву фильму з цього жанру: ").title()
            t1.func_title_film(film_yes)
            if len(t1.title_info) != 0:
                t1.func_title_sort(film_yes)
                print(f'{zirka}')
                num = input('Введіть номер фільму: ')
                print(f'{zirka}')
                t1.func_title_num(int(num))
                break
            else:
                print('немає такого фільму')
        if greetings == "year":
            num_year = input("Введіть дату випуску фільму у прокат: ")
            print(f'{zirka}')
            t1.func_year_yes(num_year)
            if len(t1.year_info) != 0:
                print(f'у {num_year} році були зняті такі фільми: ')
                t1.func_num_year(num_year)
                print(f'{zirka}')
                num = input('Введіть номер фільму: ')
                print(f'{zirka}')
                t1.func_title_num(int(num))
                break
            else:
                print('таких фільмів немає')






