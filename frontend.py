# Dean and Sag
import tkinter
import pyglet
from pyglet.window import mouse
import customtkinter
from PIL import Image, ImageTk

window = pyglet.window.Window(1280, 720)
window.set_caption("Welcome Screen")


image = pyglet.resource.image('Images/pbear.jpg')
birds = pyglet.resource.image("Images/brds.png")
pyglet.font.add_file('Images/blow.ttf')
double_bubble = pyglet.font.load("Blow")


label = pyglet.text.Label('Endangered Species Map',
                          font_name= "Blow",
                          font_size=72,
                          bold = True,
                          color = (0, 166, 210, 255),
                          x=window.width//2, y=window.height//2 + 285,
                          anchor_x='center', anchor_y='center')

label_shadow = pyglet.text.Label('Endangered Species Map',
                          font_name= "Blow",
                          font_size=72,
                          bold = True,
                          color = (22, 46, 66, 255),
                          x=window.width//2 - 7.5, y=window.height//2 + 280,
                          anchor_x='center', anchor_y='center')


batch = pyglet.graphics.Batch()

butt_image = pyglet.resource.image('Images/start.png')

sprite = pyglet.sprite.Sprite(butt_image, x= window.width // 2 - 200, y = window.height//2 - 425, batch = batch)
sprite.anchor_x = "center"
sprite.anchor_y = "center"
sprite.scale = .1

sprite1 = pyglet.sprite.Sprite(birds, x= 60, y = 225, batch = batch)
sprite1.anchor_x = "center"
sprite1.anchor_y = "center"
sprite1.scale = .55
sprite1.rotation = -17



@window.event
def on_draw():
    window.clear()
    image.blit(-15, -111)
    batch.draw()
    label_shadow.draw()
    label.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button & mouse.LEFT:
        if 470 <= x <= 805:
            if 65 <= y <= 200:
                window.close()


music = pyglet.resource.media('Music/National_Anthem.mp3')
music.play()

pyglet.app.run()

