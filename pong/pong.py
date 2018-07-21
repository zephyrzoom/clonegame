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
        self.racket_left = pyglet.sprite.Sprite(img=self.racket_image, x=20, y=50)
        self.racket_left.scale = 0.5

        self.racket_right = pyglet.sprite.Sprite(img=self.racket_image, x=self.width-20-self.racket_left.width, y=50)
        self.racket_right.scale = 0.5

        self.fps_display = pyglet.clock.ClockDisplay()
        self.racket_left_move = 0
        self.racket_right_move = 0
        pyglet.clock.schedule_interval(self.update, 1/60.0)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            self.racket_left_move = 4
        elif symbol == key.S:
            self.racket_left_move = -4
        elif symbol == key.UP:
            self.racket_right_move = 4
        elif symbol == key.DOWN:
            self.racket_right_move = -4

    def on_key_release(self, symbol, modifiers):
        if symbol == key.W or symbol == key.S:
            self.racket_left_move = 0
        if symbol == key.UP or symbol == key.DOWN:
            self.racket_right_move = 0


    def on_draw(self):
        self.clear()
        self.title.draw()
        self.ball.draw()
        self.racket_left.draw()
        self.racket_right.draw()
        self.fps_display.draw()

    def center_image(self, image):
        """
        Sets an image's anchor point to its center
        """
        image.anchor_x = image.width / 2
        image.anchor_y = image.height / 2

    def update(self, dt):
        self.ball.x += self.ball.dx * dt

        self.move(self.racket_left_move, self.racket_left)
        self.move(self.racket_right_move, self.racket_right)

    def move(self, dt, sprite):
        sprite.y += dt
        if sprite.y > self.height - sprite.height:
            sprite.y = self.height - sprite.height
        if sprite.y < 0:
            sprite.y = 0

if __name__ == '__main__':
    window = Window()
    pyglet.app.run()