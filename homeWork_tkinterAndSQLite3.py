
import tkinter as tk
import sqlite3

connection = sqlite3.connect("homeWork.db")



window = tk.Tk()


def clickHandler():
  header.configure(text="Данные сохранены!")
  cursor.execute("INSERT INTO homeWork VALUES (?,?,?,?)",(firstName, lastName, age, city))
  connection.commit()


window.title("Test")

header = tk.Label(window, text="Введите данные")
header.grid(column=0, row=0)


firstText = tk.Label(window, text="Фамилия:")
firstText.grid(column=0, row=1)
firstName = tk.Entry(window, width=15)
firstName.grid(column=0, row=2)

lastText = tk.Label(window, text="Имя:")
lastText.grid(column=0, row=3)
lastName = tk.Entry(window, width=10)
lastName.grid(column=0, row=4)

ageText = tk.Label(window, text="Возраст:")
ageText.grid(column=0, row=5)
age = tk.Entry(window, width=4)
age.grid(column=0, row=6)

cityText = tk.Label(window, text="Город:")
cityText.grid(column=0, row=7)
city = tk.Entry(window, width=15)
city.grid(column=0, row=8)

firstButton = tk.Button(window, text="Сохранить данные!", command=clickHandler)
firstButton.grid(column=0, row=9)

print(type(city))

connection = sqlite3.connect("homeWork.db")

cursor = connection.cursor()
try:
    cursor.execute("CREATE TABLE homeWork (first_name TEXT, last_name TEXT, age REAL, city TEXT)")
except sqlite3.OperationalError:
    pass
connection.commit()

# cursor.execute("INSERT INTO homeWork VALUES (?,?,?,?)",(firstName, lastName, age, city))

connection.commit()

window.mainloop()