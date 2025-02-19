import pygame as py
from modulos.values.juego import Objeto_Juego

py.init()  # Inicializa todos los módulos de Pygame

game = Objeto_Juego((1350, 680), 30, "Inuyasha random")
game.init()