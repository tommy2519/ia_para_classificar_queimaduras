from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image


def modelo_ia(file_path):
    # Carregar o modelo treinado
    model = tf.keras.models.load_model('modelos/modelo_v3.h5')

    # Caminho para a imagem a ser testada
    test_image_path = file_path

    # Carregar e pré-processar a imagem
    img = image.load_img(test_image_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Fazer a previsão
    prediction = model.predict(img_array)

    # Mapear os índices das classes para os graus de queimadura
    class_labels = {0: 'Primeiro Grau', 1: 'Segundo Grau', 2: 'Terceiro Grau'}
    predicted_class = np.argmax(prediction)

    # Liberar recursos do modelo (opcional caso haja complicações, remover!)
    tf.keras.backend.clear_session()

    return f"A queimadura é classificada como: {class_labels[predicted_class]}"
