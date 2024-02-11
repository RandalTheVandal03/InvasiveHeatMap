import pyglet
from screeninfo import get_monitors
from pyglet.gl import *
from pyglet.window import mouse
from stateButton import *

def mapSpawn():

    #Formats items to fit monitor aspect ratio
    monitor = get_monitors()
    mWidth = monitor[0].width
    mHeight = monitor[0].height
    uWidth = 1000
    uHeight = 626
    widthRatio = mWidth/uWidth
    heightRatio = mHeight/uHeight

    #Initializes the window we will be using
    window = pyglet.window.Window(int(monitor[0].width), int(monitor[0].height))

    #Import image files from "Images" folder, All 50 States meant to be used later on for more efficiency
    #Creates library with all state image files
    SS = {}

    SS['BG'] = pyglet.resource.image('Images/Cool_Blue_BG.png')
    SS['AL'] = pyglet.resource.image('Images/Alabama.png')
    SS['AK'] = pyglet.resource.image('Images/Alaska.png')
    SS['AZ'] = pyglet.resource.image('Images/Arizona.png')
    SS['AR'] = pyglet.resource.image('Images/Arkansas.png')
    SS['CA'] = pyglet.resource.image('Images/California.png')
    SS['CO'] = pyglet.resource.image('Images/Colorado.png')
    SS['CT'] = pyglet.resource.image('Images/Connecticut.png')
    SS['DE'] = pyglet.resource.image('Images/Delaware.png')
    SS['FL'] = pyglet.resource.image('Images/Florida.png')
    SS['GA'] = pyglet.resource.image('Images/Georgia.png')
    SS['HI'] = pyglet.resource.image('Images/Hawaii.png')
    SS['ID'] = pyglet.resource.image('Images/Idaho.png')
    SS['IL'] = pyglet.resource.image('Images/Illinois.png')
    SS['IN'] = pyglet.resource.image('Images/Indiana.png')
    SS['IA'] = pyglet.resource.image('Images/Iowa.png')
    SS['KS'] = pyglet.resource.image('Images/Kansas.png')
    SS['KY'] = pyglet.resource.image('Images/Kentucky.png')
    SS['LA'] = pyglet.resource.image('Images/Louisiana.png')
    SS['ME'] = pyglet.resource.image('Images/Maine.png')
    SS['MD'] = pyglet.resource.image('Images/Maryland.png')
    SS['MA'] = pyglet.resource.image('Images/Massachusetts.png')
    SS['MI'] = pyglet.resource.image('Images/Michigan.png')
    SS['MN'] = pyglet.resource.image('Images/Minnesota.png')
    SS['MS'] = pyglet.resource.image('Images/Mississippi.png')
    SS['MO'] = pyglet.resource.image('Images/Missouri.png')
    SS['MT'] = pyglet.resource.image('Images/Montana.png')
    SS['NE'] = pyglet.resource.image('Images/Nebraska.png')
    SS['NV'] = pyglet.resource.image('Images/Nevada.png')
    SS['NH'] = pyglet.resource.image('Images/New_Hampshire.png')
    SS['NJ'] = pyglet.resource.image('Images/New_Jersey.png')
    SS['NM'] = pyglet.resource.image('Images/New_Mexico.png')
    SS['NY'] = pyglet.resource.image('Images/New_York.png')
    SS['NC'] = pyglet.resource.image('Images/North_Carolina.png')
    SS['ND'] = pyglet.resource.image('Images/North_Dakota.png')
    SS['OH'] = pyglet.resource.image('Images/Ohio.png')
    SS['OK'] = pyglet.resource.image('Images/Oklahoma.png')
    SS['OR'] = pyglet.resource.image('Images/Oregon.png')
    SS['PA'] = pyglet.resource.image('Images/Pennsylvania.png')
    SS['RI'] = pyglet.resource.image('Images/Rhode_Island.png')
    SS['SC'] = pyglet.resource.image('Images/South_Carolina.png')
    SS['SD'] = pyglet.resource.image('Images/South_Dakota.png')
    SS['TN'] = pyglet.resource.image('Images/Tennessee.png')
    SS['TX'] = pyglet.resource.image('Images/Texas.png')
    SS['UT'] = pyglet.resource.image('Images/Utah.png')
    SS['VT'] = pyglet.resource.image('Images/Vermont.png')
    SS['VA'] = pyglet.resource.image('Images/Virginia.png')
    SS['WA'] = pyglet.resource.image('Images/Washington.png')
    SS['WV'] = pyglet.resource.image('Images/West_Virginia.png')
    SS['WI'] = pyglet.resource.image('Images/Wisconsin.png')
    SS['WY'] = pyglet.resource.image('Images/Wyoming.png')

    #Calls dict holding state button hit boxes
    stateList = stateInstantiation()

    #Draws the window
    @window.event
    def on_draw():
        window.clear()
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            
        #Iterates throught the States Dict to display images on window
        for key in SS:
            SS[key].blit(0, 0)
            SS[key].width = uWidth * widthRatio
            SS[key].height = uHeight * heightRatio

            
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button and mouse.LEFT:
            
            xVal = int(x/widthRatio)
            yVal = int(y/heightRatio)

            for x in stateList:
                x.isClicked(xVal, yVal)        

    pyglet.app.run()

#mapSpawn()