import pyglet
from pyglet.window import key
from pyglet.gl import gl

# colors
on_colour = (0, .5, .8, 1)
off_colour = (0.5,0,0.8,1)

window = pyglet.window.Window(width=300, height=300, caption='Press key/button to start')
window.set_fullscreen(True)

# sets the background color
gl.glClearColor(*off_colour)
window.clear()

boat = pyglet.media.load("audio_tracks\\Boat_Amie.wav", streaming=False)

player = pyglet.media.Player()
player.queue(boat)
player.EOS_LOOP = 'loop' 
firston = False

@window.event
def on_key_press(symbol, modifiers):
    global firston
    if symbol == key.R:
        print('Repeat play')
        boat.play()
    else:
        if not firston:
            firston = True
            player.play()
    if firston:
        print("On colour")
        gl.glClearColor(*on_colour)
        window.clear()

                             
@window.event
def on_key_release(symbol, modifiers):
    global firston
    player.pause()
    firston = False
    if not firston:
        print("Off colour")
        gl.glClearColor(*off_colour)
        window.clear()


pyglet.app.run()
