import pygame as py
from modulos.objetos_del_juego.personaje.configuraciones_personajes import *
from modulos.objetos_del_juego.Personajes import Personaje
from modulos.objetos_del_juego.personaje.proyectil import Proyectil

class Heroe(Personaje):
    """
    Clase que representa al héroe del juego, heredando de Personaje.
    
    Incluye mecánicas de movimiento, salto, ataque, disparo de proyectiles e invulnerabilidad temporal.
    """
    def __init__(self, x, y, tamaño, animaciones, velocidad):
        """
        Inicializa un héroe con habilidades adicionales.
        
        :param x: Posición inicial en el eje X.
        :param y: Posición inicial en el eje Y.
        :param tamaño: Tamaño del héroe (ancho, alto).
        :param animaciones: Diccionario con animaciones del héroe.
        :param velocidad: Velocidad de desplazamiento horizontal.
        """
        super().__init__(x, y, tamaño, animaciones, velocidad)
        self.vidas = 3
        self.saltando = False
        self.velocidad_y = 0  # Inicializar la velocidad vertical
        self.atacando = False
        self.direccion_ataque = ""
        self.invulnerable = False
        self.tiempo_invulnerabilidad = 2000  # 2 segundos de invulnerabilidad
        self.ultimo_daño = 0
        self.tiempo_ataque = 500  # Duración del ataque en milisegundos
        self.ultimo_ataque = 0  # Tiempo del último ataque
        self.proyectiles_habilitados = False 
        self.proyectiles = []

    def actualizar(self, pantalla, plataformas, enemigos):
        """
        Actualiza la posición, animaciones y estado del héroe.
        
        :param pantalla: Superficie de Pygame donde se renderiza el héroe.
        :param plataformas: Lista de plataformas con las que interactúa.
        :param enemigos: Lista de enemigos en el juego.
        """
        self.mover()
        self.aplicar_gravedad(plataformas)
        # self.chequear_colision_con_enemigos(enemigos)
        self.animar(pantalla)
        self.gestionar_invulnerabilidad()
        self.gestionar_ataque()  # Gestión del estado de ataque

    def mover(self):
        """
        Controla el movimiento horizontal y el salto del héroe.
        """
        keys = py.key.get_pressed()
        if not self.atacando:  # Permitir movimiento solo si no está atacando
            if keys[py.K_RIGHT]:
                self.rectangulo_principal.x += self.velocidad
                self.que_hace = "Derecha"
                self.animacion_actual = self.animaciones["Derecha"]
            if keys[py.K_LEFT]:
                self.rectangulo_principal.x -= self.velocidad
                self.que_hace = "Izquierda"
                self.animacion_actual = self.animaciones["Izquierda"]
            if keys[py.K_UP] and not self.saltando:
                self.saltando = True
                self.velocidad_y = -15
                self.que_hace = "Salta"
                self.animacion_actual = self.animaciones["Salta"]
            if not self.saltando and self.que_hace != "Izquierda" and self.que_hace != "Derecha":
                self.que_hace = "Quieto"
                self.animacion_actual = self.animaciones["Quieto"]

    def aplicar_gravedad(self, plataformas):
        """
        Aplica gravedad al héroe y gestiona colisiones con plataformas.
        """
        self.velocidad_y += 1  # Acelerar la caída
        self.rectangulo_principal.y += self.velocidad_y

        # Verificar colisión con las plataformas
        for plataforma in plataformas:
            if self.rectangulo_principal.colliderect(plataforma.rectangulo):
                if self.velocidad_y > 0:  # Solo ajustar si el héroe está cayendo
                    self.rectangulo_principal.bottom = plataforma.rectangulo.top
                    self.saltando = False
                    self.velocidad_y = 0

        # Asegurarse de que el héroe no caiga fuera de la pantalla
        if self.rectangulo_principal.bottom >= 680:
            self.rectangulo_principal.bottom = 680
            self.saltando = False
            self.velocidad_y = 0

    # def chequear_colision_con_enemigos(self, enemigos):
    #     if not self.invulnerable:
    #         for enemigo in enemigos:
    #             if self.rectangulo_principal.colliderect(enemigo.rectangulo_principal):
    #                 print("Colisión detectada con enemigo.")  # Mensaje de depuración
    #                 self.perder_vida()
    #                 break  # Solo perder una vida por colisión

    def atacar(self, direccion):
        """
        Activa el estado de ataque del héroe en la dirección indicada.
        
        :param direccion: Dirección del ataque ("Derecha" o "Izquierda").
        """
        self.atacando = True
        self.direccion_ataque = direccion
        self.ultimo_ataque = py.time.get_ticks()  # Tiempo del último ataque
        if direccion == "Derecha":
            self.que_hace = "Ataca_derecha"
            self.animacion_actual = self.animaciones["Ataca_derecha"]
        elif direccion == "Izquierda":
            self.que_hace = "Ataca_izquierda"
            self.animacion_actual = self.animaciones["Ataca_izquierda"]

    def gestionar_ataque(self):
        """
        Controla la duración del ataque del héroe.
        """
        if self.atacando:
            ahora = py.time.get_ticks()
            if ahora - self.ultimo_ataque > self.tiempo_ataque:
                self.atacando = False  # Terminar el ataque después del tiempo especificado

    def perder_vida(self):
        """
        Reduce la cantidad de vidas y activa la invulnerabilidad temporal.
        """
        if not self.invulnerable:  # Verificar si no es invulnerable antes de perder vida
            self.vidas -= 1
            self.invulnerable = True
            self.ultimo_daño = py.time.get_ticks()  # Guardar el tiempo del daño recibido
            print(f"Vida perdida. Vidas restantes: {self.vidas}")  # Mensaje de depuración
            print("Invulnerabilidad activada.")  # Mensaje de depuración

    def gestionar_invulnerabilidad(self):
        """
        Controla el tiempo de invulnerabilidad después de recibir daño.
        """
        if self.invulnerable:
            ahora = py.time.get_ticks()
            if ahora - self.ultimo_daño > self.tiempo_invulnerabilidad:
                self.invulnerable = False
                print("Invulnerabilidad desactivada.")  # Mensaje de depuración

 
    def disparar(self, imagen_proyectil, direccion):
        """
        Crea y dispara un proyectil en la dirección especificada.
        
        :param imagen_proyectil: Ruta de la imagen del proyectil.
        :param direccion: Dirección del disparo ("Derecha" o "Izquierda").
        """
        if self.proyectiles_habilitados:
            velocidad_proyectil = 10
            tamaño_proyectil = (45, 45)  # Tamaño del proyectil
            x = self.rectangulo_principal.centerx
            y = self.rectangulo_principal.centery
            proyectil = Proyectil(x, y, tamaño_proyectil, velocidad_proyectil, direccion, imagen_proyectil)
            self.proyectiles.append(proyectil)

 