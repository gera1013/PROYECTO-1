from gl import Render, color, linalgNormal
from obj import ObjFile, Texture
from shaders import *

r = Render(1920, 1080)

r.background = Texture('sky.bmp')
r.glClear()

posModel = [0, 0, 0]
r.lookAt(posModel, [0.5, 0, 1])

## MENARA TOWER
print("Menara...")
r.active_shader = phong
r.texture = Texture('menara.bmp')
r.glLoadObj('menara.obj', [-2.9, -4.3, -1], [1/70, 1/70, 1/70], [0, 0, 0])

## KA27 HELICOPTER
print("\nKA27...")
r.light = [-0.7, 0.5, 0]
r.light = linalgNormal(r.light)
r.active_shader = toonShader
r.texture = Texture('ka27.bmp')
r.glLoadObj('ka27.obj', [0.6, -0.3, -0.2], [1/200, 1/200, 1/200], [0, 7, 0])

## AW101 HELICOPTER
print("\nAW101...")
r.light = [0, 1, 0]
r.active_shader = thermalVision
r.texture = Texture('aw101.bmp')
r.glLoadObj('aw101.obj', [0.6, 0.3, -0.2], [1/300, 1/300, 1/300], [0, -8, 0])

## BERIEV AIRPLANE
print("\nBeriev...")
r.active_shader = toonShader
r.texture = Texture('beriev.bmp')
r.glLoadObj('beriev.obj', posModel, [1/100, 1/100, 1/100], [0, 10, 0])

## MISSILE 1
print("\nMissile 1...")
r.active_shader = tvStatic
r.texture = None
r.glLoadObj('missile.obj', [-0.4, -0.45, 0], [1/1200, 1/1500, 1/1200], [8, 0, 0])

## MISSILE 2
print("\nMissile 2...")
r.active_shader = tvStatic
r.texture = None
r.glLoadObj('missile.obj', [0, -0.45, 0], [1/1200, 1/1500, 1/1200], [8, 0, 0])

## Renderizar
r.glFinish('output.bmp')
print("\nDone")
