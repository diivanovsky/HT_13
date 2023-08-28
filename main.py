import os


# 1 Task

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


try:
    limit = int(input("How many numbers? "))
    if limit <= 0:
        raise ValueError("It must be positive")

    sequence = fib(limit)
    for number in sequence:
        print(number)

except ValueError as ve:
    print("Error:", ve, "Enter only numbers")


# Task 2

def numbers():
    seq = [1, 2, 3]
    index = 0
    while True:
        yield seq[index]
        index = (index + 1) % len(seq)


try:
    count = int(input("How many numbers do you want to see? "))
    output = numbers()

    result = "-".join(str(next(output)) for x in range(count))
    print(result)

except ValueError:
    print("Enter only numbers")


# Task 3


os_name = os.name
print("Имя вашей ОС:", os_name)
c_path = os.getcwd()
print("Путь до текущей папки:", c_path)

# Sort by type
ext = ['.txt', '.jpg', '.png', '.doc']
dir = {}

for ext in ext:
    dir_name = ext[1:].upper() + "_files"
    dir_path = os.path.join(c_path, dir_name)
    os.makedirs(dir_path, exist_ok=True)
    dir[ext] = dir_path

for filename in os.listdir(c_path):
    if os.path.isfile(os.path.join(c_path, filename)):
        file_extension = os.path.splitext(filename)[1]
        if file_extension in dir:
            source_path = os.path.join(c_path, filename)
            dest_path = os.path.join(dir[file_extension], filename)
            os.rename(source_path, dest_path)

# Information about sort
for ext, dir_path in dir.items():
    file_count = len([fname for fname in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, fname))])
    tot_s = sum(os.path.getsize(os.path.join(dir_path, f)) for f in os.listdir(dir_path)) / 1024 / 1024 / 1024
    print(f"In folder {ext[1:]} replaced {file_count} files, their size - {round(tot_s, 2)} Gb")

# Rename
dir_path = dir['.txt']
files = [fname for fname in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, fname))]
if len(files) > 0:
    file_to_rename = files[0]
    new_file_name = "some_" + file_to_rename
    source_path = os.path.join(dir_path, file_to_rename)
    dest_path = os.path.join(dir_path, new_file_name)
    os.rename(source_path, dest_path)
    print(f"File {file_to_rename} was renamed as {new_file_name}")

# Task 4
import re

text = '''Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном заседании вину инкриминируемого 
правонарушения признала в полном объёме и суду показала, что 14 сентября 1876 года, будучи в состоянии алкогольного 
опьянения от безысходности, в связи с состоянием здоровья позвонила со своего стационарного телефона в полицию, сообщив 
о том, что у неё в квартире якобы заложена бомба. После чего приехали сотрудники полиции, скорая и пожарные, которым 
она сообщила, что бомба — это она.'''

# Заменяем ФИО подсудимого на 'N'
pattern = r'Эверт\-Колокольцева Елизавета Александровна'
replacement = input("Че вместо будет? ")

new_text = re.sub(pattern, replacement, text)

print(new_text)
