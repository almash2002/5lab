'''Тізім қайтаратын функция жазып шығу. Алдын ала
студенттердің пәндері және бағалары бар тізім құрастыр.
 Және сол тізім бойынша студенттің атын еңгізген кезде,
 сол студенттің бағаларын шығарып бертін болсын.'''

Students = [
    {
        "name": "Almash",
        "subject": "Functional-Programming",
        "rating": [4, 3, 5, 5, 4]
    },
    {
        "name": "Aruzhan",
        "subject": "Functional-Programming",
        "rating": [3, 2, 3, 4, 3]
    },
    {
        "name": "Aliya",
        "subject": "Functional-Programming",
        "rating": [3, 5, 4, 3, 5]
    }
]


def print_students(students):
    string = str(input())
    for student in students:
        if student["name"] == string:
            print(student["rating"])


print_students(Students)
