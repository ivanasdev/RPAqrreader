import argparse
import cv2

parser=argparse.ArgumentParser()

#Se obtieneel fichero donde esta el codigo QR
#parser.add_argument("-f", "NombreYRutadelfichero", type=str, help="Ruta y nombre del fichero de imagen QR a leer")
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fichero", type=str, 
    help="Ruta y nombre del fichero de imagen QR a leer")
parser.add_argument("-s", "--Solo_Valor", type=str, 
    help="Mostrar sólo el valor leído (sí/no)")
args = parser.parse_args()
 


FileQR = input("Introduzca el fichero QR a leer: ")


#LEER EL QR
img = cv2.imread(FileQR)
det = cv2.QRCodeDetector()

valorQRLeido, pts, st_code = det.detectAndDecode(img)

print(valorQRLeido)