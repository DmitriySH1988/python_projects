'''Задание 1. Приложение заметки (Python)
Информация о проекте
Необходимо написать проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её, читать список
заметок, редактировать заметку, удалять заметку.
Как сдавать проект
Для сдачи проекта необходимо создать отдельный общедоступный
репозиторий (Github, gitlub, или Bitbucket). Разработку вести в этом
репозитории, использовать пул реквесты на изменения. Программа должна
запускаться и работать, ошибок при выполнении программы быть не должно.
Задание
Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.Например:
python notes.py add --title "новая заметка" –msg "тело новой заметки"
Или так:
python note.py
Введите команду: add
Введите заголовок заметки: новая заметка
Введите тело заметки: тело новой заметки
Заметка успешно сохранена
Введите команду:
При чтении списка заметок реализовать фильтрацию по дате.
Критерии оценки
Приложение должно запускаться без ошибок, должно уметь сохранять данные
в файл, уметь читать данные из файла, делать выборку по дате, выводить на
экран выбранную запись, выводить на экран весь список записок, добавлять
записку, редактировать ее и удалять.'''



'''
В данном примере используется класс `Note` для представления заметки. Функция `save_notes` сохраняет заметки в файл в формате JSON, а функция `load_notes` загружает заметки из файла. Заметки хранятся в списке `notes`.

Программа имеет следующие команды:
- `add` - добавляет новую заметку.
- `list` - выводит список всех заметок.
- `edit` - редактирует существующую заметку по её идентификатору.
- `delete` - удаляет существующую заметку по её идентификатору.
- `filter` - фильтрует заметки по указанной дате.
- `exit` - завершает работу программы.

Приложение сохраняет данные заметок в файл `notes.json` и загружает их при следующем запуске.

Вы можете запустить этот код и внести необходимые изменения в соответствии с вашими предпочтениями и требованиями.
'''

import json
import datetime

# Класс заметки
class Note:
    def __init__(self, note_id, title, body, created):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created = created

# Функция сохранения заметок в файл в формате JSON
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, default=serialize_note)

# Функция чтения заметок из файла
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes_data = json.load(file)
            return [deserialize_note(note_data) for note_data in notes_data]
    except FileNotFoundError:
        return []

# Функция сериализации заметки в JSON
def serialize_note(note):
    return {
        'note_id': note.note_id,
        'title': note.title,
        'body': note.body,
        'created': note.created.isoformat()
    }

# Функция десериализации заметки из JSON
def deserialize_note(note_data):
    return Note(
        note_data['note_id'],
        note_data['title'],
        note_data['body'],
        datetime.datetime.fromisoformat(note_data['created'])
    )

# Функция добавления новой заметки
def add_note():
    note_id = input('Введите идентификатор заметки: ')
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    created = datetime.datetime.now()
    note = Note(note_id, title, body, created)
    notes.append(note)
    save_notes(notes)
    print('Заметка успешно сохранена')

# Функция вывода списка заметок
def list_notes():
    for note in notes:
        print(f'Идентификатор: {note.note_id}')
        print(f'Заголовок: {note.title}')
        print(f'Дата создания: {note.created}')
        print('---')

# Функция редактирования заметки
def edit_note():
    note_id = input('Введите идентификатор заметки для редактирования: ')
    for note in notes:
        if note.note_id == note_id:
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новый текст заметки: ')
            note.title = title
            note.body = body
            note.created = datetime.datetime.now()
            save_notes(notes)
            print('Заметка успешно отредактирована')
            return
    print('Заметка с указанным идентификатором не найдена')

# Функция удаления заметки
def delete_note():
    note_id = input('Введите идентификатор заметки для удаления: ')
    for note in notes:
        if note.note_id == note_id:
            notes.remove(note)
            save_notes(notes)
            print('Заметка успешно удалена')
    return
print('Заметка с указанным идентификатором не найдена')

#Функция фильтрации заметок по дате
def filter_notes_by_date():
    date_str = input('Введите дату в формате ГГГГ-ММ-ДД: ')
    try:
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        filtered_notes = [note for note in notes if note.created.date() == date.date()]
        if filtered_notes:
            for note in filtered_notes:
                print(f'Идентификатор: {note.note_id}')
                print(f'Заголовок: {note.title}')
                print(f'Дата создания: {note.created}')
                print('---')
        else:
            print('Заметки на указанную дату не найдены')
    except ValueError:
        print('Некорректный формат даты')

#Основной цикл программы
notes = load_notes()

while True:
    command = input('Введите команду (add, list, edit, delete, filter, exit): ')
    if command == 'add':
        add_note()
    elif command == 'list':
        list_notes()
    elif command == 'edit':
        edit_note()
    elif command == 'delete':
        delete_note()
    elif command == 'filter':
        filter_notes_by_date()
    elif command == 'exit':
        break
    else:
        print('Некорректная команда')

