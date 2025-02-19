import pygame as py

from pygame.locals import *
from assets.imagenes.fondo.fondos_juego import CIELO_2
from modulos.values.configuraciones_juego import Configuraciones

# Asegúrate de tener estas variables definidas
# CORAZON = 'path_to_heart_image.png'
# CIELO_1 = 'path_to_background_image.png'
# PLATAFORMA_0 = 'path_to_platform_image.png'
# Además de las clases Heroe, Enemigo, Plataformas y Configuraciones
def get_path_actual(nombre_archivo: str):
    """encuentra el archivo independientemente de en que path este

    Args:
        nombre_archivo (str): en este parametro se pone el nombre del archivo independientemente
                                de si esta el path o no

    Returns:
        _type_: retorna el nombre del archivo en su path actual 
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def nuevo_puntaje(nombre:str, puntos:int)->dict:
    """
    Crea un diccionario con el nombre del jugador y su puntaje.

    Parámetros:
        nombre (str): El nombre del jugador.
        puntos (int): Los puntos obtenidos por el jugador.

    Retorna:
        dict: Diccionario con los datos del puntaje.
    """
    puntaje = {}
    puntaje["nombre"] = nombre
    puntaje["puntaje"] = puntos
    return puntaje

def convertir_csv_lista_diccionarios(nombre_archivo: str) -> list:
    """
    Convierte un archivo CSV de puntajes a una lista de diccionarios.

    Parámetros:
        nombre_archivo (str): El nombre del archivo CSV.

    Retorna:
        list: Lista de diccionarios con los puntajes.

    Excepciones:
        FileNotFoundError: Si no se encuentra el archivo.
        Exception: Si ocurre un error al leer el archivo.
    """
    try:
        with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
            lista = []
            encabezado = archivo.readline().strip("\n").split(",")
            for linea in archivo.readlines():
                puntuacion = {}
                linea = linea.strip("\n").split(",")
                nombre, puntaje = linea
                lista.append(nuevo_puntaje(nombre, int(puntaje)))
        return lista
    except FileNotFoundError:
        print(f"Archivo {nombre_archivo} no encontrado. Se devolverá una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {e}")
        return []
def guardar_puntajes_json(lista: list, nombre_archivo: str):
    """Guarda los puntajes ordenados en un archivo JSON."""
    import json
    try:
        with open(get_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
            json.dump(lista, archivo, indent=4)
    except Exception as e:
        print(f"Error al guardar los puntajes en JSON: {e}")

def ordenar_lista(lista: list, campo_1: str, descendente=True) -> None:
    """
    Ordena una lista de diccionarios en base a un campo específico.

    Parámetros:
        lista (list): Lista de diccionarios a ordenar.
        campo_1 (str): El campo del diccionario por el cual ordenar.
        descendente (bool): Si es `True`, ordena en orden descendente.
    """
    n = len(lista)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if descendente:
                if lista[i][campo_1] < lista[j][campo_1]:
                    lista[i], lista[j] = lista[j], lista[i]
            else:
                if lista[i][campo_1] > lista[j][campo_1]:
                    lista[i], lista[j] = lista[j], lista[i]

class PantallaInicio:
    """
    Representa la pantalla de inicio del juego con opciones de menú.

    Atributos:
        pantalla (Surface): La pantalla donde se muestra el contenido.
        tamaño (tuple): El tamaño de la pantalla.
        fuente (Font): Fuente para el texto grande.
        fuente_pequeña (Font): Fuente para el texto pequeño de botones.
        color_texto (tuple): Color de texto en formato RGB.
        botones (dict): Diccionario con botones y sus áreas de colisión.
        musica_paused (bool): Estado de la música.
    """
    def __init__(self, pantalla, tamaño):
        """
        Inicializa la pantalla de inicio.

        Parámetros:
            pantalla (Surface): La superficie de la pantalla del juego.
            tamaño (tuple): El tamaño de la pantalla.
        """
        self.pantalla = pantalla
        self.tamaño = tamaño
        self.fuente = py.font.Font(None, 74)
        self.fuente_pequeña = py.font.Font(None, 36)
        self.color_texto = (255, 255, 255)
        self.botones = {
            "Play": py.Rect(tamaño[0]//2 - 100, tamaño[1]//2 - 150, 200, 50),
            "Config": py.Rect(tamaño[0]//2 - 100, tamaño[1]//2 - 50, 200, 50),
            "Ranking": py.Rect(tamaño[0]//2 - 100, tamaño[1]//2 + 50, 200, 50)
        }
        self.musica_paused = False

    def mostrar(self):
        """
        Muestra el contenido de la pantalla de inicio.
        """
        self.pantalla.fill((0, 0, 0))  # Pantalla negra
        titulo = self.fuente.render("MiJuego", True, self.color_texto)
        self.pantalla.blit(titulo, (self.tamaño[0]//2 - titulo.get_width()//2, 100))
        
        for texto, rect in self.botones.items():
            py.draw.rect(self.pantalla, (0, 255, 0), rect)
            texto_render = self.fuente_pequeña.render(texto, True, (0, 0, 0))
            self.pantalla.blit(texto_render, (rect.x + (rect.width - texto_render.get_width()) // 2, rect.y + (rect.height - texto_render.get_height()) // 2))

        py.display.flip()

    def manejar_eventos(self, evento):
        """
        Maneja los eventos de la pantalla de inicio.

        Parámetros:
            evento (Event): El evento que se captura de Pygame.

        Retorna:
            str: El siguiente paso según el evento ("play", "config", "ranking").
        """
        if evento.type == MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos()
            if self.botones["Play"].collidepoint(pos):
                return "play"
            elif self.botones["Config"].collidepoint(pos):
                return "config"
            elif self.botones["Ranking"].collidepoint(pos):
                return "ranking"
        return None

class PantallaConfig:
    """
    Representa la pantalla de configuración del juego.

    Atributos:
        pantalla (Surface): La pantalla donde se muestra el contenido.
        tamaño (tuple): El tamaño de la pantalla.
        fuente_pequeña (Font): Fuente para los textos pequeños.
        color_texto (tuple): Color de texto en formato RGB.
        boton_mute (Rect): El área de la opción de mute.
        musica_paused (bool): Estado de la música (pausada o no).
    """
    
    def __init__(self, pantalla, tamaño):
        """
        Inicializa la pantalla de configuración.

        Parámetros:
            pantalla (Surface): La superficie de la pantalla del juego.
            tamaño (tuple): El tamaño de la pantalla.
        """
        self.pantalla = pantalla
        self.tamaño = tamaño
        self.fuente_pequeña = py.font.Font(None, 36)
        self.color_texto = (255, 255, 255)
        self.boton_mute = py.Rect(tamaño[0]//2 - 100, tamaño[1]//2 - 50, 200, 50)
        self.musica_paused = False

    def mostrar(self):
        """
        Muestra el contenido de la pantalla de configuración.
        """
        self.pantalla.fill((0, 0, 0))  # Pantalla negra
        py.draw.rect(self.pantalla, (0, 255, 0), self.boton_mute)
        texto_render = self.fuente_pequeña.render("Mute", True, (0, 0, 0))
        self.pantalla.blit(texto_render, (self.boton_mute.x + (self.boton_mute.width - texto_render.get_width()) // 2, self.boton_mute.y + (self.boton_mute.height - texto_render.get_height()) // 2))
        py.display.flip()

    def manejar_eventos(self, evento):
        """
        Maneja los eventos de la pantalla de configuración.

        Parámetros:
            evento (Event): El evento que se captura de Pygame.

        Retorna:
            str: El siguiente paso según el evento ("inicio").
        """
        if evento.type == MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos()
            if self.boton_mute.collidepoint(pos):
                self.musica_paused = not self.musica_paused
                print(f"Estado de la música pausada: {self.musica_paused}")  # Debug
                
                if self.musica_paused:
                    py.mixer.pause()
                    print("Música pausada")
                else:
                    py.mixer.unpause()
                    print("Música reanudada")
            


                # if self.musica_paused:
                #     py.mixer.music.stop()
                # else:
                #     py.mixer.music.play(-1)  # Reproduce en bucle


        elif evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                return "inicio"
        return None
    # def manejar_eventos(self, evento):
        
    #     if evento.type == MOUSEBUTTONDOWN:
    #         pos = py.mouse.get_pos()
    #         if self.boton_mute.collidepoint(pos):
    #             self.musica_paused = not self.musica_paused
    #             if self.musica_paused:
    #                 py.mixer.music.pause()
    #             else:
    #                 py.mixer.music.unpause()
    #     elif evento.type == KEYDOWN:
    #         if evento.key == K_ESCAPE:
    #             return "inicio"
    #     return None

class PantallaRanking:
    """
    Muestra la pantalla de ranking con los puntajes más altos.

    Atributos:
        pantalla (Surface): La pantalla donde se muestra el contenido.
        tamaño (tuple): El tamaño de la pantalla.
        fuente_pequeña (Font): Fuente para los textos pequeños.
        color_texto (tuple): Color de texto en formato RGB.
        puntajes (list): Lista de los puntajes leídos y ordenados.
    """
    def __init__(self, pantalla, tamaño):
        """
        Inicializa la pantalla de ranking.

        Parámetros:
            pantalla (Surface): La superficie de la pantalla del juego.
            tamaño (tuple): El tamaño de la pantalla.
        """
        self.pantalla = pantalla
        self.tamaño = tamaño
        self.fuente_pequeña = py.font.Font(None, 36)
        self.color_texto = (255, 255, 255)
        self.puntajes = self.leer_puntajes()

    def leer_puntajes(self):
        """
        Lee los puntajes desde el archivo CSV y ordena los 5 mejores.

        Retorna:
            list: Lista con los 5 mejores puntajes.
        """
        try:
            puntajes = convertir_csv_lista_diccionarios('puntuaciones.csv')
            ordenar_lista(puntajes, "puntaje", descendente=True)
            guardar_puntajes_json(puntajes, "puntuaciones_ordenadas.json")
            return puntajes[:5]  # Solo los 5 mejores puntajes
        except Exception as e:
            print(f"Error al leer los puntajes: {e}")
            return []

    def mostrar(self):
        """
        Muestra los puntajes en la pantalla.
        """
        
        self.pantalla.fill((0, 0, 0))  # Pantalla negra
        y_offset = 100
        for puntuacion in self.puntajes:
            texto_render = self.fuente_pequeña.render(f"{puntuacion['nombre']}: {puntuacion['puntaje']}", True, self.color_texto)
            self.pantalla.blit(texto_render, (self.tamaño[0]//2 - texto_render.get_width()//2, y_offset))
            y_offset += 50
        py.display.flip()

    def manejar_eventos(self, evento):
        """
        Maneja los eventos de la pantalla de ranking.

        Parámetros:
            evento (Event): El evento que se captura de Pygame.

        Retorna:
            str: El siguiente paso según el evento ("inicio").
        """
        if evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                return "inicio"
        return None