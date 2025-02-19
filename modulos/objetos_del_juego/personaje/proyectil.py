import pygame as py
from pygame.math import Vector2
class Proyectil:
    """
    Clase que representa un proyectil en el juego, que se mueve en una dirección y puede ser disparado por el personaje.

    Atributos:
        superficie (Surface): Imagen del proyectil.
        rectangulo (Rect): Rectángulo que define la posición y colisión del proyectil.
        velocidad (int): Velocidad con la que el proyectil se mueve.
        direccion (str): Dirección en la que se mueve el proyectil ("Derecha" o "Izquierda").
    """
    def __init__(self, x, y, tamaño, velocidad, direccion, imagen):
        """
        Inicializa un nuevo proyectil.

        Parámetros:
            x (int): Coordenada X de la posición inicial del proyectil.
            y (int): Coordenada Y de la posición inicial del proyectil.
            tamaño (tuple): Tamaño del proyectil (ancho, alto).
            velocidad (int): Velocidad de movimiento del proyectil.
            direccion (str): Dirección del proyectil ("Derecha" o "Izquierda").
            imagen (str): Ruta del archivo de imagen para el proyectil.
        """
        self.superficie = py.image.load(imagen)
        self.superficie = py.transform.scale(self.superficie, tamaño)
        self.rectangulo = self.superficie.get_rect(center=(x, y))
        self.velocidad = velocidad
        self.direccion = direccion  # "Derecha" o "Izquierda"

    def actualizar(self):
        """
        Actualiza la posición del proyectil en función de su dirección y velocidad.
        El proyectil se moverá hacia la derecha o izquierda dependiendo de la dirección asignada.
        """
        if self.direccion == "Derecha":
            self.rectangulo.x += self.velocidad
        elif self.direccion == "Izquierda":
            self.rectangulo.x -= self.velocidad

    def dibujar(self, pantalla):
        """
        Dibuja el proyectil en la pantalla.

        Parámetros:
            pantalla (Surface): La superficie de la pantalla donde se dibujará el proyectil.
        """
        pantalla.blit(self.superficie, self.rectangulo)
