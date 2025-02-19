import pygame

class Objeto:
    def __init__(self, x, y, tamaño, imagen=""):
        """
        Inicializa un objeto con una superficie y un rectángulo.
        
        :param x: Posición inicial en el eje X.
        :param y: Posición inicial en el eje Y.
        :param tamaño: Tamaño del objeto (ancho, alto).
        :param imagen: Ruta de la imagen a cargar (opcional).
        """
        
        self.objeto = {}
        if imagen != "":
            self.objeto["superficie"] = pygame.image.load(imagen)
            self.objeto["superficie"] = pygame.transform.scale(self.objeto["superficie"], tamaño)
        else:
            self.objeto["superficie"] = pygame.Surface(tamaño)

        self.objeto["rectangulo"] = self.objeto["superficie"].get_rect()
        self.objeto["rectangulo"].x = x
        self.objeto["rectangulo"].y = y
    
    def get_rectangles(self,main:pygame.Rect):
        """
        Genera un diccionario con subdivisiones del rectángulo principal.
        
        :param main: Un rectángulo de Pygame que representa el área principal del objeto.
        """
        self.dictionary = {}
        if len(main) > 0 and isinstance(main, pygame.Rect):
            self.dictionary["main"] = main
            self.dictionary["bottom"] = pygame.Rect(main.left, main.bottom - 12, main.width, 12)
            self.dictionary["right"] = pygame.Rect(main.right - 10, main.top, 10, main.height)
            self.dictionary["left"] = pygame.Rect(main.left, main.top, 10, main.height)
            self.dictionary["top"] = pygame.Rect(main.left, main.top , main.width, 12)
    
    def crear_rectangulo(self,pantalla):
        """
        Dibuja el objeto en la pantalla en la posición especificada.
        
        :param pantalla: Superficie de Pygame donde se renderizará el objeto.
        """
        pantalla.blit(self.objeto["superficie"],self.objeto["rectangulo"])
    
    
