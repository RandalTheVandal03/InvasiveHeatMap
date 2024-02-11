# Dean and Sag
import tkinter
import pyglet
from pyglet.window import  mouse
import customtkinter
from PIL import Image, ImageTk



listy = [['sexy fox', 'Short-tailed albatross', 'Wherever fiund', '7', 'Endangered', 'Birds'],['Phoebastria (=Diomedea) albatrus', 'long-tailed', 'Wherever fiund', '7', 'Endangered', 'Birds']]

numofanimals = len(listy)

numofpages = (numofanimals//15) + 1

output = ""
i = 0

if numofanimals >= 15:
    for i in range (0, 15):
        output += listy[i][5] + "      " + listy[i][1] + "    " + listy[i][0] + "\n"
elif numofanimals < 15:
    for i in range (0, numofanimals):
        output += listy[i][5] + "      " + listy[i][1] + "    " + listy[i][0] + "\n"

output = f"Classification:    Common Name:    Scientific Name:\n" + output
print(output)





window = pyglet.window.Window(600, 600)
window.set_caption("State Screen")

image = pyglet.resource.image('Images/state_background.png')
back_button = pyglet.resource.image('Images/prev.png')
next_button = pyglet.resource.image("Images/next.png")

batch = pyglet.graphics.Batch()

'''
back_sprite = pyglet.sprite.Sprite(back_button, x= window.width // 2 - 250, y = window.height//2 - 275, batch = batch)
back_sprite.anchor_x = "center"
back_sprite.anchor_y = "center"
back_sprite.scale = 0.5
'''

next_sprite = pyglet.sprite.Sprite(next_button, x= window.width // 2 + 150, y = window.height//2 - 275, batch = batch)
next_sprite.anchor_x = "center"
next_sprite.anchor_y = "center"
next_sprite.scale = 0.5

#statename = state + " Name"
state_name = pyglet.text.Label('State Name',
                          font_name= "Arial",
                          font_size=24,
                          bold = True,
                          color = (0, 166, 210, 255),
                          x=window.width//2 - 200, y=window.height//2 + 270,
                          anchor_x='center', anchor_y='center')

organism_count = pyglet.text.Label('test organism count',
                          font_name= "Arial",
                          font_size=16,
                          bold = True,
                          color = (0, 166, 210, 255),
                          x=window.width//2, y=window.height//2 + 230,
                          anchor_x='center', anchor_y='center')

details = pyglet.text.Label("Ferns and allies, endangered, artusian sheild fern, phobestria, \nFerns and allies, endangered, artusian sheild fern, phobestria, albatross (= Diometra)\nFerns and allies, endangered, artusian sheild fern, phobestria, albatross (= Diometra)\nFerns and allies, endangered, artusian sheild fern, phobestria, albatross (= Diometra)\nFerns and allies, endangered, artusian sheild fern, phobestria, albatross (= Diometra)Ferns and allies, endangered, artusian sheild fern, phobestria, \nFerns and allies, endangered, artusian sheild ferFerns and allies, endangered, artusian sheild fern, phobestria, \nFerns and allies, endangered, artusian sheild ferFerns and allies, endangered, artusian sheild fern, phobestria, \nFerns and allies, endangered, artusian sheild ferFerns and allies, endangered, artusian sheild fern, phobestria, \nFerns and allies, endangered, artusian sheild ferFerns and allies, endangered, artusian sheild fern, phobestria, \nFerns and allies, endangered, artu",
                          font_name= "Arial",
                          font_size=12,         #15 lines per window
                          bold = True,
                          color = (0, 166, 210, 255),
                          multiline=True,
                          width = 500,
                          x=55, y=150,
                          anchor_x= 'left' , anchor_y='bottom')

pages_text = f"{numofpages} Pages"
details1 = pyglet.text.Label( pages_text,
                          font_name= "Arial",
                          font_size=14,         
                          bold = True,
                          color = (0, 166, 210, 255),
                          multiline=True,
                          width = 500,
                          x=window.width//2 +150, y=window.height//2 - 225,
                          anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    image.blit(0,0)
    state_name.draw()
    details.draw()
    details1.draw()
    organism_count.draw()
    #back_sprite.draw()
    next_sprite.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button & mouse.LEFT:
        print(x,y)
        if 470 <= x <= 805:
            if 65 <= y <= 200:
                window.close()

pyglet.app.run();
