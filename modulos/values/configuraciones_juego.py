import pygame as py
from assets.imagenes.fondo.fondos_juego import CIELO_1
FPS = 60
score = 0
vidas = 3

class Configuraciones:

    def __init__(self, tamaño, FPS, caption="Title", icon=""):
        
        py.mixer.init()
        
            
        
        self.tamaño = tamaño

        self.pantalla = py.display.set_mode(self.tamaño)

        self.bandera_inicio = True
        # self.py = py
        self.FPS = FPS
        
        self.clock = py.time.Clock()

        self.set_caption(caption)

    def set_caption(self, caption):
        py.display.set_caption(caption)

    def set_icon(self, icon):
        pass

    def set_fps(self, FPS):
        self.FPS = FPS

    def set_music(self, musica):
        self.music = py.mixer.Sound(musica)
        
        
        
    def set_volume(self):
        self.music.set_volume(0.1)

    def play_music(self):
        self.music.play(-1)
        
    def stop_music(self):
        self.music.mixer.paused()

    def set_background_image(self, fondo, tamaño):
        self.fondo = fondo
        self.fondo = py.image.load(fondo)
        self.fondo = py.transform.scale(self.fondo, tamaño)

    def set_fuente(self):
        pass

    def fill_screen(self, color=None):
        if color != None:
            self.pantalla.fill(color)
        else:
            self.pantalla.blit(self.fondo, (0, 0))
            