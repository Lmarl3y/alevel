students = int(input('Number of students: '))
books = int(input('Number of books: '))

each = books // students
left = books % students

print(f'Number of books each: {each}\nNumber of books remaining: {left}')