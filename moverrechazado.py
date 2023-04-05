import win32com.client

def moverrechazado():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    root_folder = outlook.Folders.Item(1)

    inbox = outlook.GetDefaultFolder(6)
    Actas = root_folder.Folders['RECHAZADO']
    messages = inbox.Items

    for message in messages:
        if 'Rechazado' in message.Subject:
            message.Move(Actas)