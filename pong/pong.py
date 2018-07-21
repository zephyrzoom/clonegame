import pyglet
from pyglet.window import key
from pyglet.window import mouse

class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.title = pyglet.text.Label('Pong',
                            font_name='Times New Roman',
                            font_size=28,
                            x=self.width//2, y=self.height-20,
                            anchor_x='center', anchor_y='center')
        
        pyglet.resource.path = ['assets']
        pyglet.resource.reindex()
        self.image = pyglet.resource.image('ball.png')
        self.center_image(self.image)
        self.music = pyglet.resource.media('rebound.ogg')
        self.music.play()
        self.ball = pyglet.sprite.Sprite(img=self.image, x=500, y=400)
        self.ball.scale = 0.2
        self.ball.dx = 10.0
        self.racket_image = pyglet.resource.image('racket.png')
        self.racket_left = pyglet.sprite.Sprite(img=self.racket_image, x=50, y=50)
        self.racket_left.scale = 0.5
        self.racket_right = pyglet.sprite.Sprite(img=self.racket_image, x=self.width-50, y=50)
        self.racket_right.scale = 0.5
        self.fps_display = pyglet.clock.ClockDisplay()
        pyglet.clock.schedule_interval(self.update, 1/60.0)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            pyglet.clock.schedule_interval(self.move, 5, self.racket_left)
        elif symbol == key.S:
            self.move(-10, self.racket_left)
        elif symbol == key.UP:
            self.move(10, self.racket_right)
        elif symbol == key.DOWN:
            self.move(-10, self.racket_right)


    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print('The left mouse button was pressed.')


    def on_draw(self):
        self.clear()
        self.title.draw()
        self.ball.draw()
        self.racket_left.draw()
        self.racket_right.draw()
        self.fps_display.draw()

    def center_image(self, image):
        """Sets an image's anchor point to its center"""
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

    def update(self, dt):
        self.ball.x += self.ball.dx * dt

    def move(self, dt, sprite):
        sprite.y += dt

if __name__ == '__main__':
    window = Window()
    pyglet.app.run()