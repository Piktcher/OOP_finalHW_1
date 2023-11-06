from Model.NoteDB import NoteDB
from Model.Note import Note
class Controller:

    global database
    database = NoteDB() 

    def createNewNote(self, title, body):
        return Note(title, body)

    def addNewNoteToDB(self, note):
        database.addNote(note)
    
    def deleteNote(self, note):
        if (database.deleteNote(note) == "Error"):
            print("Заметка не найдена, попробуйте еще раз!\n")
        else: 
            database.deleteNote(note)
            print("Запись успешно удалена!")
    
    def printDB(self):
        print(database)