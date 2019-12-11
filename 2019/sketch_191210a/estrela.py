22# -*- coding: utf-8 -*-
from cores import *

class Estrela():

    """ Classe Estrela, cor sorteada, tamanho sorteado por default """
    full_screen = False
    ins_override = -1

    def __init__(self, x, y, tam=100):
        self.x, self.y = x, y
        self.tamanho = tam
        self.vy = -0.5

    def desenha(self, ins, cor, amp):
        """ Desenha polígono em torno das coordenadas do objeto """
        raio1, raio2 = amp, amp / 4
        self.tamanho = amp
        colorMode(RGB)
        cor_final = paleta(ins, cor)
        stroke(cor_final)
        strokeJoin(ROUND)
        if Estrela.full_screen:
            translate(width / 2, height / 2)
            rotate(HALF_PI)
            translate(-width / 2, -height / 2)
        if ins in (0, 1):
            fill(0, 10) # preto bem fraquinho
            apply_override()
            estrela(self.x, self.y, 7, raio1 * .6, raio2 * .6)
        if ins in (2, 3):
            pushMatrix()
            translate(self.x, self.y)
            apply_override()
            estrela(0, 0, 4, raio1, raio2)
            rotate(QUARTER_PI)
            s = 4 if ins == 5 else 5
            cor2 = paleta(s, cor)
            stroke(cor2, min(255, amp))
            apply_override()
            estrela(0, 0, 4, raio1 * .8, raio2 * .8)
            popMatrix()
        if ins in (4, 5):
            pushMatrix()
            translate(self.x, self.y)
            rotate(radians(frameCount))
            apply_override()
            if amp > 10:
                estrela(0, 0, 10, raio1, 50)
            else:
                estrela(0, 0, 10, raio1, 5)
            popMatrix()
        if Estrela.full_screen:
            translate(width / 2, height / 2)
            rotate(-HALF_PI)
            translate(-width / 2, -height / 2)


    def anda(self, tom=None):
        """ atualiza a posição do objeto e devolve do lado oposto se sair """
        # if Estrela.full_screen:
        #     w, h = height, width
        # else:
        w, h = width, height
        if tom is not None:
            self.x = map(tom, -24, 24, self.tamanho * 2, w - self.tamanho * 2)
        # self.x += self.vx
        self.vy = -.35 * 40 / (tom + 40)
        self.y += self.vy
        tam = self.tamanho
        if self.x > w + tam:
            self.x = -tam
        if self.y > h + tam:
            self.y = -tam
        if self.x < -tam:
            self.x = w + tam
        if self.y < -tam:
            self.y = h + tam

def apply_override():
    if Estrela.ins_override == 6:
        stroke(255)
        noFill()
        strokeWeight(1)

def estrela(cx, cy, pontas, raio1, raio2):
    pontos = pontas * 2
    parte = 360. / pontos
    beginShape()  # comece a forma!
    for p in range(pontos):  # para cada p
        angulo = radians(p * parte)  # calcula angulo
        if p % 2 == 0:  # se for par
            raio = raio1
        else:  # senão, se for impar
            raio = raio2
        x = cx + raio * sin(angulo)
        y = cy + raio * cos(angulo)
        vertex(x, y)  # vertex é um ponto
    endShape(CLOSE)  # termina forma
