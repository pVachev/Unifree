notebook = []

def printNotebook():
    for note in notebook:
        print('%d. %s' %(notebook.index(note) + 1, note))

while True:
    codeOperation = int(input("Please enter code operation: (1. Add 2. Delete. 3.Update 4.Exit): "))

    if codeOperation == 1:
        newNote = input("Enter the new note: ")
        notebook.append(newNote)
        printNotebook()
    if codeOperation == 2:
        noteIndex = int(input("Please enter the number of the note you wish to delete: "))
        notebook.pop(noteIndex - 1)
        printNotebook()
    if codeOperation == 3:
        updatedNoteIndex = int(input("Please enter the number of the note you wish to update: "))
        newText = input("Please enter the new text: ")
        notebook[updatedNoteIndex - 1] = newText
        printNotebook()
    if codeOperation == 4:
        break