import pilas
from pilas.actores import Actor
#Clase LADRILLO
class Ladrillo(Actor):
        def __init__(self, x=0,y=240):
            import random
            xLa=[300,250,200,0,-200,-250,-300]
            imagen = pilas.imagenes.cargar('Personajes/ladri.png')
            random.shuffle(xLa)
            Actor.__init__(self, imagen)
            self.rotacion = 0
            self.x = xLa
            self.y = y
            self.radio_de_colision = 30
            self.escala=0.1

        def actualizar(self):
            self.y=self.y-2
            if self.y == -210:
                self.y=240
