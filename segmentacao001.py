import cv2
import numpy as np
import mahotas

#lendo a imagem original
img = cv2.imread("img/cachorro002.jpg")

#transformando a imagem em tons de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#aplica blur na imagem em tons de cinza
suave = cv2.blur(gray, (7, 7))


#aplica o metodo de otsu
#T = mahotas.thresholding.otsu(suave)

#bin = suave.copy()
#bin[bin > T] = 255
#bin[bin < 255] = 0
#bin = cv2.bitwise_not(bin)

ret, bin_img = cv2.threshold(suave, 130,34, cv2.THRESH_BINARY)

#aplica o metodo de canny para encontrar bordas
bordas = cv2.Canny(bin_img, 70, 150,L2gradient = True)

#encontra as bordas e guarda as coordenadas na variavel objetos
(objetos, lx) = cv2.findContours(bordas.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#copia a imagem original
img_contornos = img.copy()
#aplica os contornos na imagem original utilizando as coordenadas da variavel objetos
cv2.drawContours(img_contornos, objetos, -1, (255, 0, 0), 2)


#define a fonte
fonte = cv2.FONT_HERSHEY_SIMPLEX
#coloca um texto na imagem mostrando o numero de objetos encontrados
cv2.putText(img_contornos, f"{str(len(objetos))} objetos encontrados", (10,20), fonte, 0.5, (255,0,0), 0,cv2.LINE_AA)

#mostra a imagem com os contornos aplicados
cv2.imshow("Imagem",img_contornos)
#espera apertar alguma tecla
cv2.waitKey(0)
