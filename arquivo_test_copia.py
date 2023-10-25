import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image


# Carregar o modelo treinado------------> ponha a versão do modelo trainado aqui
model = tf.keras.models.load_model('modelo_v3.h5')

# Caminho para a imagem a ser testadab #########################################
test_image_path = 'queimadura_segundo_grau5566644.jpeg'

# Carregar e pré-processar a imagem
img = image.load_img(test_image_path, target_size=(256, 256))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0  # Normalizar a imagem

# Fazer a previsão
prediction = model.predict(img_array)

# Mapear os índices das classes para os graus de queimadura
class_labels = {0: 'Primeiro Grau', 1: 'Segundo Grau', 2: 'Terceiro Grau'}
predicted_class = np.argmax(prediction)

# Exibir o resultado
print(f"A queimadura é classificada como: {class_labels[predicted_class]}")
