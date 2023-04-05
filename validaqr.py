
from PIL import Image
import os 
import cv2

    
def recorteQR():
    image = Image.open('C:/Users/E-IACOSTA/Desktop/hfssystem/system/image0.png')
    left = 100
    right = 1300
    top = 4200
    bottom = 5200
    box = (left, top, right, bottom)
    img2 = image.crop(box)
    img2.save('C:/Users/E-IACOSTA/Desktop/hfssystem/system/recortes/imagen_recortada_.png')
    

def  leerQR():
    img = cv2.imread('C:/Users/E-IACOSTA/Desktop/hfssystem/system/recortes/imagen_recortada_.png')
    det = cv2.QRCodeDetector()
    info, box_coordinates, _ = det.detectAndDecode(img)
    extractoqr=info
    data = extractoqr
    datos=data[:100]
    datosclean=datos.replace("[","").replace("]","").replace("'","").replace(".","").replace("|","").split('\n')   
    
    if box_coordinates is None:
        print("No se pudo extraer texto, o QR es invalido")
    else:
        
        print(datosclean)
     
           
def extraerQR():
    if os.path.isdir('C:/Users/E-IACOSTA/Desktop/hfssystem/system/recortes/'):
        recorteQR()
        leerQR()     
    else:
        os.mkdir("C:/Users/E-IACOSTA/Desktop/hfssystem/system/recortes")
        recorteQR()
        leerQR()


    



extraerQR()