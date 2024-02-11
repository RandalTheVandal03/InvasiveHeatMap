# Dean and Sag
import pyglet
from pyglet.window import  mouse
from screeninfo import get_monitors

i = 0
def info(stateList, stateName):
    monitor = get_monitors()
    mWidth = int(monitor[0].width/3)
    mHeight = int(monitor[0].height*2/3)

    listy = stateList

    numofanimals = len(listy)

    numofpages = (numofanimals//15) + 1

    output = ""
    global i

    if numofanimals >= 15:
        for i in range (0, 15):
            output += listy[i][5] + "      " + listy[i][1] + "    " + listy[i][0] + "\n"
    elif numofanimals < 15:
        for i in range (0, numofanimals):
            output += listy[i][5] + "      " + listy[i][1] + "    " + listy[i][0] + "\n"

    output = f"Classification:    Common Name:    Scientific Name:\n" + output
    print(output)



    

    window = pyglet.window.Window(mWidth, mHeight)
    window.set_caption("State Screen")

    image = pyglet.resource.image('Images/state_background.png')
    image.width = mWidth
    image.height = mHeight
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

    state_name = pyglet.text.Label(str(stateName).upper(),
                            font_name= "Arial",
                            font_size=24,
                            bold = True,
                            color = (0, 166, 210, 255),
                            x=mWidth//4, y=mHeight*7/8,
                            anchor_x='center', anchor_y='center')

    organism_text = f"{numofanimals} Organisms"
    organism_count = pyglet.text.Label(organism_text,
                            font_name= "Arial",
                            font_size=16,
                            bold = True,
                            color = (0, 166, 210, 255),
                            x=mWidth//2, y=mHeight*0.84,
                            anchor_x='center', anchor_y='center')

    word = ''
    for x in range(16):
        if x != 0:
            for y in listy[x]:
                word = word + y + " "
            word = word + '\n'
    details = pyglet.text.Label(word,
                            font_name= "Arial",
                            font_size=12,         #15 lines per window
                            bold = True,
                            color = (0, 166, 210, 255),
                            multiline=True,
                            width = 500,
                            x=55, y=150,
                            anchor_x= 'left' , anchor_y='bottom')

    pages_text = f"{numofpages} Pages"
    details1 = pyglet.text.Label(pages_text,
                            font_name= "Arial",
                            font_size=14,         
                            bold = True,
                            color = (0, 166, 210, 255),
                            multiline=True,
                            width = 500,
                            x=mWidth//2, y=mHeight*1/8,
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
            if next_sprite.x <= x <= next_sprite.x + next_sprite.width:
                if next_sprite.y <= y <= next_sprite.y + next_sprite.height:
                    global i
                    if (numofanimals - i > 0):
                        if(numofanimals - i >= 15):
                            output = ""
                            for i in range(i, i + 15):
                                output += listy[i][5] + "      " + listy[i][1] + "    " + listy[i][0] + "\n"
                                output = f"Classification:    Common Name:    Scientific Name:\n" + output
                                i += 15
                        else:
                            for i in range(i, numofanimals - i):
                                output += listy[i][5] + "      " + listy[i][1] + "    " + listy[i][0] + "\n"
                                output = f"Classification:    Common Name:    Scientific Name:\n" + output
                                i += 15
                                


    pyglet.app.run()
