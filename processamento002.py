import numpy as np
import cv2 as cv

#cria uma imagem totalmente preta
image = np.zeros((512,512,3), np.uint8)

#desenha uma linha:
#	o primeiro parametro e a imagem que quer desenhar
#	o segundo parametro marca onde começara o triangulo (x,y)
#	o terceiro parametro marca onde finalizara o triangulo (x,y)
#	o quarto parametro define a cor da linha (Blue, Green, Red)
#	o quinto parametro define a espessura da linha
image = cv.line(image,(0,0),(511,511),(255,0,0),5)

#desenha um retangulo:
#	o primeiro parametro e a imagem que quer desenhar
#	o segundo parametro marca onde começara o triangulo (x,y)
#	o terceiro parametro marca onde finalizara o triangulo (x,y)
#	o quarto parametro define a cor da linha (Blue, Green, Red)
#	o quinto parametro define a espessura da linha
image = cv.rectangle(image,(384,0),(510,128),(0,255,0),3)

image = cv.rectangle(image,(0,0),(200,200),(0,0,255),3)


#desenha um circulo:
#	o primeiro parametro e a imagem que quer desenhar
#	o segundo parametro marca o centro do circulo
#	o terceiro parametro marca o raio do circulo
#	o quarto parametro define a cor da linha (Blue, Green, Red)
#	o quinto parametro define a espessura da linha ( se for negativo o circulo fica preenchido)
image = cv.circle(image,(447,63), 63, (0,0,255), -1)


#desenha um elipse
#	o primeiro parametro é a imagem que quer desenhar
#	o segundo parametro marca o centro da elipse
#	O terceiro parametro marca o comprimentos dos eixos(x,y)
#		(comprimento do eixo principal, comprimento do eixo secundário)
#	o quarto argumento é o angulo da elipse anti horario
#	o quinto argumento define a curvatura da linha que ficara invisivel
#	o sexto argumento define a curvatura da linha que ficara a mostra
#	o setimo define a cor da linha
#	o oitavo argumento define a espessura da linha
image = cv.ellipse(image,(256,256),(150,50),0,90,380,(0,255,255),-1)

#define uma matriz cujas coordenadas são os vertices (x,y)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))

#desenha as linhas interligadas
#	primeiro argumento é a imagem no qual vai ser desenhado
#	segundo argumento são os pontos (definidos anteriormente)
#	terceiro define se o ultimo e primeiro ponto vão se ligar
#	quarto argumento define a cor
image = cv.polylines(image,[pts],True,(0,255,255))


#define a fonte e guarda na variavel
font = cv.FONT_HERSHEY_SIMPLEX

#coloca um texto na imagem
#	a imagem que vai ser colocada o texto
#	
cv.putText(image,'Fidel',(45,500), font, 6,(255,255,255),3,cv.LINE_AA)


cv.imshow('TesTe',image)
cv.waitKey(0)
cv.destroyAllWindows()