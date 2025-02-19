import pygame

def reescalar_imagenes(diccionario_animaciones, tamaño):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(img, tamaño)

def rotar_imagen(imagenes):
    lista_imagenes = []
    for img in imagenes:
        imagen_rotada = pygame.transform.flip(img, True, False)
        lista_imagenes.append(imagen_rotada)
    return lista_imagenes

personaje_quieto = [pygame.image.load("assets/imagenes/personaje_principal/InuYasha_quieto.png")]

personaje_camina_derecha = [
    pygame.image.load("assets/imagenes/personaje_principal/InuYasha_caminando_derecha_1.png"),
    pygame.image.load("assets/imagenes/personaje_principal/InuYasha_caminando_derecha_2.png")
]

personaje_camina_izquierda = rotar_imagen(personaje_camina_derecha)
personaje_salta_derecha = [pygame.image.load("./assets/imagenes/personaje_principal/InuYasha_saltando-1.png (1).png")]
personaje_salta_izquierda = rotar_imagen(personaje_salta_derecha)
personaje_ataca_derecha = [pygame.image.load("./assets/imagenes/personaje_principal/InuYasha_ataque_derecha.png")]
personaje_ataca_izquierda = rotar_imagen(personaje_ataca_derecha)

animaciones = {
    "Quieto": personaje_quieto,
    "Derecha": personaje_camina_derecha,
    "Izquierda": personaje_camina_izquierda,
    "Salta": personaje_salta_derecha,
    "Ataca_derecha": personaje_ataca_derecha,
    "Ataca_izquierda": personaje_ataca_izquierda
}
enemigo_camina_derecha = [
    pygame.image.load(r"assets\imagenes\enemigos\Male_Deadite_Trailer_Park-removebg-preview.png"),
    pygame.image.load(r"assets\imagenes\enemigos\Male_Deadite_Trailer_Park2-removebg-preview.png")
]
enemigo_camina_izquierda = rotar_imagen(enemigo_camina_derecha)

animaciones_enemigo = {
    "Quieto": personaje_quieto,
    "Derecha": enemigo_camina_derecha,
    "Izquierda": enemigo_camina_izquierda
}

reescalar_imagenes(animaciones, (50, 50))  # Adjust the size as needed
reescalar_imagenes(animaciones_enemigo, (50,50))

velocidad = 5


