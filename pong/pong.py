import pyglet
from pyglet.window import key
from pyglet.window import mouse


window = pyglet.window.Window()
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')


@window.event
def on_draw():
    window.clear()
    title.draw()
    ball.draw()
    racket_left.draw()
    racket_right.draw()
    fps_display.draw()

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def update(dt, sprite):
    sprite.x += sprite.dx * dt

if __name__ == '__main__':

    title = pyglet.text.Label('Pong',
                          font_name='Times New Roman',
                          font_size=28,
                          x=window.width//2, y=window.height-20,
                          anchor_x='center', anchor_y='center')
    pyglet.resource.path = ['assets']
    pyglet.resource.reindex()
    image = pyglet.resource.image('ball.png')
    center_image(image)
    music = pyglet.resource.media('rebound.ogg')
    music.play()
    ball = pyglet.sprite.Sprite(img=image, x=500, y=400)
    ball.scale = 0.2
    ball.dx = 10.0
    racket_image = pyglet.resource.image('racket.png')
    racket_left = pyglet.sprite.Sprite(img=racket_image, x=50, y=50)
    racket_left.scale = 0.5
    racket_right = pyglet.sprite.Sprite(img=racket_image, x=window.width-50, y=50)
    racket_right.scale = 0.5
    fps_display = pyglet.clock.ClockDisplay()
    pyglet.clock.schedule_interval(update, 1/60.0, sprite=ball)
    pyglet.app.run()