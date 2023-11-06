from Controller.Controller import Controller
class Viewer:
 
    def start(self):
        controller = Controller()
        print("Добро пожаловать в заметки!\n")
        
        while(True):
            print("\nВыберите нужное действие с помощью ввода значения от 1 до 4, где:\n 1 - Добавить заметку,\n 2 - Удалить заметку по названию,\n 3 - Вывести все заметки,\n 4 - Закрыть программу\n")
            action = input()
            
            match action:
                case "1":
                    print("Введите название заметки:")
                    title = input()
                    print("Введите текст заметки:")
                    body = input()
                    note = controller.createNewNote(title, body)
                    controller.addNewNoteToDB(note)

                case "2":
                    print("Введите название заметки:")
                    title = input()
                    controller.deleteNote(title)

                case "3":
                    print("\nСписок заметок:\n")
                    controller.printDB()

                case "4":
                    exit()

                case _:
                    print("Введено некорректное значение, попробуйте еще раз!")    