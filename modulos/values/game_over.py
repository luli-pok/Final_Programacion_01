import pygame as py


class GameOver:
    def __init__(self, pantalla, puntuacion):
        self.pantalla = pantalla
        self.puntuacion = puntuacion
        # self.ir_a_inicio_callback = ir_a_inicio_callback
        self.fuente = py.font.Font(None, 74)
        self.fuente_pequeña = py.font.Font(None, 36)
        self.color_texto = (255, 255, 255)
        self.input_active = True
        self.nombre_jugador = ""

    def mostrar_pantalla_game_over(self):
        self.pantalla.fill((0, 0, 0))  # Pantalla negra
        texto_game_over = self.fuente.render("Game Over", True, self.color_texto)
        texto_puntuacion = self.fuente.render(f"Puntuación: {self.puntuacion}", True, self.color_texto)
        texto_ingrese_nombre = self.fuente_pequeña.render("Ingrese su nombre:", True, self.color_texto)
        self.pantalla.blit(texto_game_over, (self.pantalla.get_width() // 2 - texto_game_over.get_width() // 2, 100))
        self.pantalla.blit(texto_puntuacion, (self.pantalla.get_width() // 2 - texto_puntuacion.get_width() // 2, 200))
        self.pantalla.blit(texto_ingrese_nombre, (self.pantalla.get_width() // 2 - texto_ingrese_nombre.get_width() // 2, 300))
        
        # Mostrar el nombre del jugador
        nombre_jugador_surface = self.fuente_pequeña.render(self.nombre_jugador, True, self.color_texto)
        self.pantalla.blit(nombre_jugador_surface, (self.pantalla.get_width() // 2 - nombre_jugador_surface.get_width() // 2, 350))

        py.display.flip()

    def manejar_eventos(self, evento):
        if evento.type == py.KEYDOWN:
            if evento.key == py.K_RETURN:
                self.guardar_puntuacion()
                self.input_active = False             
                py.quit()
                exit()
                # self.ir_a_inicio_callback()  # Llama a la función para ir a la pantalla de inicio
            elif evento.key == py.K_BACKSPACE:
                self.nombre_jugador = self.nombre_jugador[:-1]
            else:
                self.nombre_jugador += evento.unicode

    def guardar_puntuacion(self):
        try:
            nombre_archivo = './modulos/values/puntuaciones.csv'
            with open(nombre_archivo, "a", encoding="utf-8") as archivo:
                archivo.write(f"{self.nombre_jugador},{self.puntuacion}\n")
            print("Puntuación guardada en el archivo CSV.")
        except Exception as e:
            print(f"Error al guardar la puntuación: {e}")

    def ejecutar(self):
        while self.input_active:
            for evento in py.event.get():
                if evento.type == py.QUIT:
                    self.input_active = False
                    py.quit()
                    exit()
                self.manejar_eventos(evento)

            self.mostrar_pantalla_game_over()
            py.time.delay(100)
