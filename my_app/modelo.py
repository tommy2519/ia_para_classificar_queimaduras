from PIL import Image
import numpy as np
import tensorflow as tf
from keras.preprocessing import image

classificacao = {}

def modelo_ia(file_path):

    global classificacao

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

    # Atribui o resultado dos retornos a classificação
    if predicted_class == 0:

        # Dicionário com as informações da classificação de 1° grau
        classificacao[0] = '\u2022 A lesão por queimadura apresentada é de 1° (Primeiro) Grau.'
        classificacao[1] = '\u2022 Pele de aspecto seco. \n\u2022 Hiperemiado e doloroso. \n\u2022 Sem formação de bolhas. \n\u2022 Costuma descamar em poucos dias. \n\u2022 Regride sem cicatrizes. \n\u2022 Pouca ou nenhuma repercussão sistêmica. \n\u2022 É desconsiderada na avaliação da área atingida. \n'
        classificacao[2] = '\u2022 Agentes térmicos (como calor intenso).\n\u2022 Agentes químicos (substâncias corrosivas).\n\u2022 Agentes radioativos (exposição a radiações).\n\u2022 Agentes elétricos (correntes elétricas).'
        classificacao[3] = '\u2022 As queimaduras de primeiro grau, ao afetarem exclusivamente a epiderme, são tipicamente \nconsideradas lesões superficiais, o que implica em um tratamento geralmente \nsimplificado. Dessa forma, pode-se recorrer a realização do resfriamento \ninicial da área afetada utilizando água fria corrente e a subsequente higienização \ndelicada com água morna e sabão, seguida de secagem cuidadosa da pele.'
        classificacao[4] = 'Apenas a epiderme é atingida'

        print(classificacao[0],"teste--------------teste----------dentro do modelo")

    elif predicted_class == 1:

        # Dicionário com as informações da classificação de 2° grau
        classificacao[0] = '\u2022 A lesão por queimadura apresentada é de 2° (Segundo) Grau.'
        classificacao[1] = '\u2022 Pele de aspecto bolhoso hiperemiado.\n\u2022 Edemaciado.\n\u2022 Doloroso, com erosão ou ulceração.\n\u2022 Ocorre regeneração espontânea.\n\u2022 Há repetelização a partir dos anexos cutâneos.\n\u2022 Cicatrização demorada (2 a 4 semanas).\n\u2022 Pode deixar sequelas superficiais, como discromia, e profundas, como cicatriz.'
        classificacao[2] = '\u2022 Agentes térmicos (como calor intenso).\n\u2022 Agentes químicos (substâncias corrosivas).\n\u2022 Agentes radioativos (exposição a radiações).\n\u2022 Agentes elétricos (correntes elétricas).'
        classificacao[3] = '\u2022 É importante tomar cuidados imediatos após uma queimadura de segundo grau para evitar \ncomplicações, como por exemplo infecções e promover a cicatrização adequada. Nos \ncuidados iniciais se a queimadura for por calor, resfriar a área afetada com água \ncorrente, com o intuito de diminuir a temperatura da pele na região afetada e \nreduzir inflamações, se houver bolhas na área queimada, não deve ser obstruída, \npois pode aumentar o riscos de infecções(elas funcionam como barreira contra os germes). \nCobrir a queimadura com um pano limpo e não aderente para evitar contaminação.'
        classificacao[4] = 'Atinge totalmente a epiderme e a derme de maneira variável.'

    elif predicted_class == 2:
        print("Terceiro Grau")

        # Dicionário com as informações da classificação de 2° grau
        classificacao[0] = '\u2022 A lesão por queimadura apresentada é de 3° (Terceiro) Grau.'
        classificacao[1] = '\u2022 Pele de aspecto variável, principalmente em sua coloração (pálida a preta), Inelástica\n\u2022 Ressecada e endurecida ao toque.\n\u2022 Indolor.\n\u2022 Necessidade de enxerto para que ocorra regeneração.\n\u2022 Sua cicatriz pode ocorrer, mas com retração das bordas.'
        classificacao[2] = '\u2022 Agentes térmicos (como calor intenso).\n\u2022 Agentes químicos (substâncias corrosivas).\n\u2022 Agentes radioativos (exposição a radiações).\n\u2022 Agentes elétricos (correntes elétricas).'
        classificacao[3] = '\u2022 Se tratando dos cuidados iniciais, é pragmático evitar o contato direto ou aplicar \nqualquer substância na lesão, além de cobrir com um pano limpo e anti aderente, \npara evitar infecção. Havendo bolhas, assim como a queimadura de segundo grau não \ndeve-se obstruir.'
        classificacao[4] = 'Todas as camadas da pele são atingidas, podendo alcançar o tecido subcutâneo, tendões, ligamentos, músculos e até ossos'
    # Liberar recursos do modelo (opcional caso haja complicações, remover!)
    tf.keras.backend.clear_session()

    #return f"A queimadura é classificada como: {class_labels[predicted_class]}"
    return classificacao
