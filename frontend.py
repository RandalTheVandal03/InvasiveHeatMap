# Dean and Sag
import pyglet

window = pyglet.window.Window(1280, 720)
window.set_caption("Welcome Screen")

image = pyglet.resource.image('animalpics.jpg')

label = pyglet.text.Label('Endangered Map',
                          font_name='Arial',
                          font_size=36,
                          x=window.width//2, y=window.height//1.5,
                          anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    label.draw()

music = pyglet.resource.media('Music/National_Anthem.mp3')
music.play()

pyglet.app.run()

