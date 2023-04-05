import cv2

def  leerQR():
    img = cv2.imread('C:/Users/E-IACOSTA/Desktop/hfssystem/system/recortes/imagen_recortada_.png')
    det = cv2.QRCodeDetector()
    info, box_coordinates, _ = det.detectAndDecode(img)
    extractoqr=info

    if box_coordinates is None:
        print("No se pudo extraer texto, o QR es invalido")
    else:
        return extractoqr
    

#cv2.waitKey(0)
#cv2.destroyAllWindows()