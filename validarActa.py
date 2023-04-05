
import time
from PIL import Image
import pytesseract


def leerimagen():

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    imagen = Image.open('C:/Users/E-IACOSTA/Desktop/hfssystem/system/image0.png')
    ocr_result = pytesseract.image_to_string(imagen, lang='eng')
    text_file=open("extract.txt","w")
    text_file.write(ocr_result)
         
def validaActa():
    f= open('extract.txt')
    mensaje = f.read()
    datos=mensaje[:900]
        #se quitan signos y caracteres de la cadena 
    datos=datos.replace("[","").replace("]","").replace("'","").replace(".","").replace(" ","")
        #ID ELECTRONICO
    findie=int(datos.find("IdentificadorElectronico"))
    sliceie=findie+24
    ieposition=sliceie+18
    ieclean=datos[sliceie:ieposition:1]
    
    findcurp=int(datos.find("Poblacion"))
    slicecurp=findcurp+9
    curpposition=slicecurp+18
    curpclean=datos[slicecurp:curpposition:1]
    #CLEAN DATOS
    ielectronico=ieclean.replace("\n","").replace(" ","")
    curp=curpclean.replace("\n","").replace(" ","")
    #return ielectronico, curp
    print(ielectronico)
    print(curp)
     
leerimagen()      
validaActa()  