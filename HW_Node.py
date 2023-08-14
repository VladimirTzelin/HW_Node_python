

def main():
    print('Консольная программа "Заметки"')
    input_from_user = ''
    while input_from_user != '0':
        menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            show('all')
        if input_from_user == '2':
            add()
        if input_from_user == '3':
            show('all')
            id_edit_del_show('del')
        if input_from_user == '4':
            show('all')
            id_edit_del_show('edit')
        if input_from_user == '5':
            show('date')
        if input_from_user == '6':
            show('id')
            id_edit_del_show('show')
        if input_from_user == '0':
            print("До новых встреч!")
            break

def menu():
    print("Меню функций:\n"
          "1 - вывод всех  заметок;\n"
          "2 - добавление заметки;\n" 
          "3 - удаление заметки;\n" 
          "4 - редактирование заметки;\n"  
          "5 - выбор заметок по дате;\n" 
          "6 - выбрать заметку по id;\n" 
          "0 - выход.\n\n" 
          "Введите номер функции: ")

def show(text):
    option = True
    array = read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            option = False
            print(Note().map_note(notes))
        if text == 'id':
            option = False
            print('ID: ' + Note().get_id(notes))
        if text == 'date':
            option = False
            if date in Note().get_date(notes):
                print(Note().map_note(notes))
    if option == True:
        print('Нет ни одной заметки...')

def add():
    number = 6
    note = create_note(number)
    array = read_file()
    for notes in array:
        if Note().get_id(note) == Note().get_id(notes):
            Note().set_id(note)
    array.append(note)
    write_file(array, 'a')
    print('Заметка добавлена...\n')

def id_edit_del_show(text):
    number = 6
    id = input('Введите id необходимой заметки: ')
    array = read_file()
    option = True
    for notes in array:
        if id == Note().get_id(notes):
            option = False
            if text == 'edit':
                note = create_note(number)
                Note().set_title(notes, note.get_title())
                Note().set_body(notes, note.get_body())
                Note().set_date(notes)
                print('Заметка изменена...\n')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...\n')
            if text == 'show':
                print(Note().map_note(notes))
    if option == True:
        print('Такой заметки нет, возможно, вы ввели неверный id\n')
    write_file(array, 'a')


def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note(id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array

def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return Note(title=title, body=body)

def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0) #Указатель чтения/записи в файле
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note().to_string(notes))
        file.write('\n')
    file.close


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text

from datetime import datetime
import uuid


class Note():

    def __init__(self, id = str(uuid.uuid1())[0:3],  title = "текст", body = "текст", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(self, note):
        return note.id

    def get_title(self, note):
        return note.title

    def get_body(self, note):
        return note.body

    def get_date(self, note):
        return note.date

    def set_id(self, note):
        note.id = str(uuid.uuid1())[0:3]

    def set_title(self, note, title):
        note.title = title

    def set_body(self, note, body):
        note.body = body

    def set_date(self, note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(self, note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def map_note(self, note):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.date


if __name__ == "__main__":
    notes_file_path = "./notes.csv"  # путь к файлу хранения заметок
    main()










