movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]

#1
def mo(dict):
    if dict["imdb"] > 5.5:
        print(True)
    else:
        print(False)


mo(movies[0])


#2
def mo1(l):
    l1=[]
    for i in range(len(l)):
        if l[i]['imdb'] > 5.5:
            l1.append(l[i]['name'])
    return l1
movies_with_high_5 = mo1(movies)
print(movies_with_high_5)


#3
def mo2(s):
    for i in range (len(movies)):
        if movies[i]['category'] == s:
            print(movies[i]['name'])
mo2(input())


#4
def average(movies):
    avg = 0
    total = len(movies)
    for i in movies:
        avg = avg + i['imdb']
    print(avg/total)


average(movies)

#5
def categor(movies, nm):
    l5 = []
    avg2 = 0
    for i in movies:
        current = i['category']
        if current == nm:
            l5.append(i)

    total2 = len(l5)
    for i in l5:
        avg2 = avg2 + i['imdb']
    return avg2/total2


n = categor(movies, 'Thriller')
print(n)