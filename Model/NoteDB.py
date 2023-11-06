from Model.Note import Note
class NoteDB:

    def __init__(self):
        self.database = list()

    def addNote(self, note):
        self.database.append(note)

    def printDB(self):
        print(self.database)

    def deleteNote(self, title):
        finder = False
        for i in range(len(self.database)):
            if (title in str(self.database[i])):
                finder = True
                self.database.pop(i)
                break
        if (finder == False):
            return "Error"
        else: return "Success"

    def __str__(self):
        for i in range(len(self.database)):
            self.database[i] = str(self.database[i]) + "\n"
        return ''.join(self.database)