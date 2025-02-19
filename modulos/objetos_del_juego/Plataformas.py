import pygame
from modulos.objetos_del_juego.objeto import*
from assets.imagenes.plataformas.plataformas_paths import PLATAFORMA_0

class Plataformas(Objeto):
    """
    Clase que representa una plataforma en el juego.

    Atributos:
        superficie (Surface): Imagen de la plataforma.
        rectangulo (Rect): Rectángulo que define la posición y colisión de la plataforma.
    """
    def __init__(self, x, y, tamaño, imagen):
        """
        Inicializa una nueva plataforma.

        Parámetros:
            x (int): Coordenada X de la posición inicial de la plataforma.
            y (int): Coordenada Y de la posición inicial de la plataforma.
            tamaño (tuple): Tamaño de la plataforma (ancho, alto).
            imagen (str): Ruta del archivo de imagen para la plataforma.
        """
        super().__init__(x, y, tamaño, imagen)
        self.superficie = pygame.image.load(imagen)
        self.superficie = pygame.transform.scale(self.superficie, tamaño)
        self.rectangulo = self.superficie.get_rect(topleft=(x, y))
        
    def definir_plataformas(self):
        """
        Define y devuelve una lista con las plataformas del juego. Actualmente, solo incluye el piso.

        Retorna:
            list: Una lista de objetos de tipo Plataformas.
        """
        plataformas = []
        piso = Plataformas(0, 630, (1350, 20), PLATAFORMA_0)
        plataformas.append(piso)
        return plataformas

        
        
        
    