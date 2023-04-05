import win32com.client
import os
import pandas as pd

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
root_folder = outlook.Folders["ivan.acosta@corusconsulting.com"]

rej = root_folder.Folders['SINIESTROS']
rech = rej.Folders['RECHAZADOS']
#aprov = root_folder.Folders['SINIESTROS']
aprov = rej.Folders['APROBADOS']

siniestros = root_folder.Folders['SINIESTROS']
messages = siniestros.Items


path = os.path.expanduser("C:/Users/E-IACOSTA/Desktop/hfssystem/mailfiles")
nombrepdf="SINIESTRO.pdf"

#FUNCION RESPONDER 



def createReply(email:object):
        reply = email.Reply()
        newBody = "APROBADO RESPUESTA"
        reply.HTMLBody = newBody + reply.HTMLBody
        reply.Move(aprov)




for message in reversed(messages):
    if 'Validación siniestro fallecimiento'.upper() in message.Subject.upper() or 'Validacion siniestro fallecimiento'.upper() in message.Subject.upper():
        data=message.htmlBody
       # pdfs=message.Attachments.Item(1)
        #pdfs.SaveAsfile(path+str(pdfs))
        print("HASTA AQUI CORRE")
        #tbl=pd.read_html(data)
        #print(tbl[0])
     

                
                
aceptado=1

html_responsea='C:/Users/E-IACOSTA/Desktop/hfssystem/system/respuesta/templates/aprove.html'
with open(html_responsea,'r') as file:
    datahtml= file.read()

html_responsed='C:/Users/E-IACOSTA/Desktop/hfssystem/system/respuesta/templates/aprove.html'
with open(html_responsed,'r') as file:
    datahtml= file.read()
    


if aceptado == 0:
    message.HTMLBody = html_responsea
    message.reply()
    message.move(rech)
            
        
            #message.move(rej)
            #message.unread = False
if aceptado == 1:
    message.Subject = "RECHAZADO"
    message.To="ivan.acosta@corusconsulting.com"
    message.HTMLBody=html_responsed
    message.reply()
    message.move(aprov)
            
if aceptado == 2:
    print("entrar a proceso de lectura de qr y texto del pdf")
        #time.sleep(120)