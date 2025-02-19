from modulos.objetos_del_juego.Personajes import Personaje
from modulos.objetos_del_juego.objeto import Objeto
from modulos.objetos_del_juego.personaje.configuraciones_personajes import reescalar_imagenes, rotar_imagen
from modulos.objetos_del_juego.personaje.heroe import Heroe
import pygame

class Enemigo(Personaje):
    """
    Clase que representa a los enemigos en el juego, heredando de Personaje.
    
    Los enemigos pueden moverse horizontalmente, aplicar gravedad y detectar colisiones con el jugador.
    """
    def __init__(self, x, y, tamaño, animaciones, velocidad, screen_width=800):
        """
        Inicializa un enemigo con movimiento automático.
        
        :param x: Posición inicial en el eje X.
        :param y: Posición inicial en el eje Y.
        :param tamaño: Tamaño del enemigo.
        :param animaciones: Diccionario de animaciones.
        :param velocidad: Velocidad de movimiento.
        :param screen_width: Ancho de la pantalla para definir límites de movimiento.
        """
        super().__init__(x, y, tamaño, animaciones, velocidad)
        self.screen_width = screen_width
        self.moviendo_izquierda = True

    def actualizar(self, pantalla, plataformas, jugador):
        """
        Actualiza la posición, animaciones y estado del enemigo.
        
        :param pantalla: Superficie de Pygame donde se renderiza el enemigo.
        :param plataformas: Lista de plataformas en el juego.
        :param jugador: Instancia del jugador para verificar colisiones.
        """
        self.manejar_movimiento_horizontal()
        self.aplicar_gravedad(plataformas)
        self.chequear_colision_con_bordes()
        self.chequear_colision_con_jugador(jugador)
        self.animar(pantalla)

    def manejar_movimiento_horizontal(self):
        """
        Controla el movimiento del enemigo de izquierda a derecha.
        """
        if self.moviendo_izquierda:
            self.rectangulo_principal.x -= self.velocidad
            self.que_hace = "Izquierda"
            self.animacion_actual = self.animaciones["Izquierda"]
        else:
            self.rectangulo_principal.x += self.velocidad
            self.que_hace = "Derecha"
            self.animacion_actual = self.animaciones["Derecha"]

    def chequear_colision_con_bordes(self):
        """
        Verifica colisiones con los bordes de la pantalla y cambia la dirección del enemigo.
        """
        if self.rectangulo_principal.left <= 0:
            self.moviendo_izquierda = False
        if self.rectangulo_principal.right >= self.screen_width:
            self.moviendo_izquierda = True

    def chequear_colision_con_jugador(self, jugador):
        """
        Verifica si el enemigo colisiona con el centro del jugador, de ser asi el jugador pierde una vida.
        
        :param jugador: Instancia del jugador para verificar colisiones.
        """
        # Crear un rectángulo central más pequeño en el rectángulo principal del jugador
        ancho_central = jugador.rectangulo_principal.width // 3  # Un tercio del ancho total
        alto_central = jugador.rectangulo_principal.height // 3  # Un tercio del alto total
        centro_x = jugador.rectangulo_principal.centerx - (ancho_central // 2)
        centro_y = jugador.rectangulo_principal.centery - (alto_central // 2)
        rectangulo_central = pygame.Rect(centro_x, centro_y, ancho_central, alto_central)

        # Verificar la colisión con el rectángulo central
        if self.rectangulo_principal.colliderect(rectangulo_central):
            jugador.perder_vida()
