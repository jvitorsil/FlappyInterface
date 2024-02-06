import pyxel

pyxel.init(200, 150)

# Céu: pinta a tela de azul
# cls(cor)
pyxel.cls(12)

# Sol: desenha um círculo de raio 15px em (50px, 25px)
# circ(x, y, raio, cor)
pyxel.circ(50, 25, 15, 10)

# Chão: retângulo na parte de baixo do sistema de coordenadas
# rect(x, y, largura, altura, cor)
pyxel.rect(0, 120, 200, 30, 3)

# Casa
pyxel.rect(90, 90, 70, 35, 15)

# Porta
pyxel.rect(97, 100, 15, 25, 2)
pyxel.circ(99, 112, 1, 1)

# Janelas
pyxel.rect(117, 100, 15, 15, 2)
pyxel.rect(119, 102, 11, 11, 5)

pyxel.rect(137, 100, 15, 15, 2)
pyxel.rect(139, 102, 11, 11, 5)

# Telhado
pyxel.rect(95, 70, 60, 21, 4)
pyxel.tri(85, 90, 95, 90, 95, 70, 4)
pyxel.tri(155, 90, 165, 90, 155, 70, 4)

# Mostra a cena
pyxel.show()