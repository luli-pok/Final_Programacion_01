import pygame
from modulos.objetos_del_juego.objeto import Objeto
from modulos.objetos_del_juego.personaje.heroe import Heroe

class Trampa(Objeto):
    def __init__(self, x, y, tamaño, imagen=""):
        """
        Inicializa una trampa que inflige daño al jugador cuando colisiona con ella.
        
        :param x: Posición X en la pantalla.
        :param y: Posición Y en la pantalla.
        :param tamaño: Tupla con el tamaño de la trampa (ancho, alto).
        :param imagen: Ruta de la imagen de la trampa.
        """
        super().__init__(x, y, tamaño, imagen)
        self.activa = True  # La trampa puede hacer daño mientras esté activa

    def actualizar(self, pantalla, heroe):
        """
        Verifica si la trampa colisiona con el héroe y le resta una vida si es necesario.
        También dibuja la trampa en la pantalla.
        
        :param pantalla: Superficie de Pygame donde se renderizará la trampa.
        :param heroe: Objeto del héroe con un rectángulo de colisión.
        """
        if self.activa and self.objeto["rectangulo"].colliderect(heroe.rectangulo_principal):
            if not heroe.invulnerable:
                heroe.perder_vida()
            self.activa = False  # Se desactiva tras activarse
        
        # Dibuja la trampa en la pantalla
        self.crear_rectangulo(pantalla)
    
