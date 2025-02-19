import pygame as py
from modulos.objetos_del_juego.Personajes import Personaje
from modulos.objetos_del_juego.personaje.configuraciones_personajes import reescalar_imagenes



class ObjetoEspecial:
    """
    Clase que representa un objeto especial en el juego que puede tener efectos sobre el personaje.

    Atributos:
        superficie (Surface): Imagen del objeto especial.
        rectangulo (Rect): Rectángulo para manejar la posición y colisión del objeto.
        efecto (str): El efecto que aplica el objeto ("vida" o "habilitar_proyectiles").
        activo (bool): Indica si el objeto está activo o ya fue recogido.
    """
    def __init__(self, x, y, tamaño, imagen_path, efecto):
        """
        Inicializa un nuevo objeto especial.

        Parámetros:
            x (int): Coordenada X de la posición del objeto en pantalla.
            y (int): Coordenada Y de la posición del objeto en pantalla.
            tamaño (tuple): Tamaño del objeto (ancho, alto).
            imagen_path (str): Ruta del archivo de imagen del objeto.
            efecto (str): Tipo de efecto que aplica el objeto ("vida" o "habilitar_proyectiles").
        """
        self.superficie = py.image.load(imagen_path)
        self.superficie = py.transform.scale(self.superficie, tamaño)
        self.rectangulo = self.superficie.get_rect(center=(x, y))  # Cargar la imagen correctamente
        self.efecto = efecto  # "vida" o "habilitar_proyectiles"
        self.activo = True

    def dibujar(self, pantalla):
            """
            Dibuja el objeto especial en la pantalla.

            Parámetros:
                pantalla (Surface): La superficie de la pantalla donde se dibujará el objeto.
            """
            
            pantalla.blit(self.superficie, self.rectangulo)
            
            
    def aplicar_efecto(self, heroe):
        """
        Aplica el efecto correspondiente al personaje.

        Parámetros:
            heroe (Personaje): El objeto de la clase Personaje que recibirá el efecto.
        """
        if self.efecto == "vida":
            heroe.vidas += 1
        elif self.efecto == "habilitar_proyectiles":
            heroe.proyectiles_habilitados = True
        self.activo = False  # El objeto ya fue recogido
