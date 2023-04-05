import win32com.client
import os 
#import registro_civil as rc
import pandas as pd

import time

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
root_folder = outlook.Folders["ivan.acosta@corusconsulting.com"]

rej = root_folder.Folders['SINIESTROS']
rechazados = rej.Folders['RECHAZADOS']
#aprov = root_folder.Folders['SINIESTROS']
aprov = rej.Folders['APROBADOS']

siniestros = root_folder.Folders['SINIESTROS']
messages = siniestros.Items

path = os.path.expanduser("C:/Users/E-IACOSTA/Desktop/hfssystem/mailfiles")
nombrepdf="SINIESTRO.pdf"

html_response='C:/Users/E-IACOSTA/Desktop/hfssystem/system/respuesta/templates/aprove.html'
with open(html_response,'r') as file:
    datahtml= file.read()
    

for message in reversed(messages):
    if 'Validación siniestro fallecimiento'.upper() in message.Subject.upper() or 'Validacion siniestro fallecimiento'.upper() in message.Subject.upper():

        data=message.htmlBody
        pdfs=message.Attachments.Item(1)
        pdfs.SaveAsfile(path+str(pdfs))

        table = pd.read_html(data)

        print(table[0])
       
        nombrecliente = ""
        apellidopaterno = ""
        apelllidomaterno = ""
        ielectronico = ""
        bpagente = ""
        numerocredito = ""
        sucursalcredito = ""
        curpofical = ""


        for i in range(len(table[0][0])-1):
            if "NOMBRE" in table[0][0][i].upper():
                nombrecliente = table[0][1][i].replace(" ","").replace(".","")
            if "APELLIDO PATERNO" in table[0][0][i].upper():
                apellidopaterno = table[0][1][i].replace(" ","").replace(".","")
            if "APELLIDO MATERNO" in table[0][0][i].upper():
                apelllidomaterno = table[0][1][i].replace(" ","").replace(".","")
            if "IDENTIFICADOR" in table[0][0][i].upper():
                ielectronico = table[0][1][i].replace(" ","").replace(".","")
            if "BP" in table[0][0][i].upper():
                bpagente = table[0][1][i].replace(" ","").replace(".","")
            if "NÚMERO DE CRÉDITO" in table[0][0][i].upper():
                numerocredito = table[0][1][i].replace(" ","").replace(".","")
            if "SUCURSAL" in table[0][0][i].upper():
                sucursalcredito = table[0][1][i].replace(" ","").replace(".","")
            if "CURP" in table[0][0][i].upper():
                curpofical = table[0][1][i].replace(" ","").replace(".","")
        dataRc = {"nombreclean":nombrecliente,"apellidopaterno":apellidopaterno,"amdef":apelllidomaterno,"iedef":ielectronico,"bpdef":bpagente,"creditodef":numerocredito,"sucursaldef":sucursalcredito,"curpdef":curpofical}
        
        if len(dataRc["curpdef"]) != 18:
            curp_inv = True

        print(dataRc)
        

        print("----"*10)
        print("----"*10)
        print("----"*10)
        print("LAS VARIABLES DEL PRIMER CORREO SON: ")

               

        #aceptado = rc.registro(dataRc)
        aceptado=0
        print("terminamos validación de gabriel")
        print("aceptado",aceptado)
        print("----"*10)
"""
        if aceptado == 0:
          
          
            message.HTMLBody = 
        
            message.reply()
        
            #message.move(rej)
            #message.unread = False
        if aceptado == 1:
            message.Subject = "RECHAZADO"
            message.To="ivan.acosta@corusconsulting.com"
            message.HTMLBody =
            message.reply()
            message.move(aprov)
            
        if aceptado == 2:
            print("entrar a proceso de lectura de qr y texto del pdf")
        #time.sleep(120)


"""