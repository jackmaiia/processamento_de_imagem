from matplotlib import pyplot as plt
import cv2


img = cv2.imread('img/gato002.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Função calcHist para calcular o hisograma da imagem

h = cv2.calcHist([img], [0], None, [256], [0, 256])
h_eq = cv2.equalizeHist(img)

plt.title("Histograma")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.xlim([0, 256])
plt.plot(h)
plt.show()