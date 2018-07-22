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
        self.music = pyglet.resource.media('rebound.ogg', streaming=False)

        self.ball = pyglet.sprite.Sprite(img=self.image, x=0, y=0)
        self.ball.scale = 0.3
        self.ball.dx = 150.0
        self.ball.dy = 150.0

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

    def update(self, dt):
        self.ball.x += self.ball.dx * dt
        self.ball.y += self.ball.dy * dt
        
        self.move(self.racket_left_move, self.racket_left)
        self.move(self.racket_right_move, self.racket_right)

        self.collise()
    
    def collise(self):
        if self.ball.y > self.height - self.ball.height:
            self.ball.y = self.height - self.ball.height
            self.ball.dy = -self.ball.dy
        if self.ball.y < 0:
            self.ball.y = 0
            self.ball.dy = -self.ball.dy
        if self.ball.x < 0:
            self.ball.x = 0
            self.ball.x = 0
            self.ball.dy = 0
        if self.ball.x > self.width - self.ball.width:
            self.ball.x = self.width - self.ball.width
            self.ball.dy = 0
        
        if self.ball.x <= self.racket_left.x + self.racket_left.width and   \
                self.ball.y + self.ball.height / 2 <= self.racket_left.y + self.racket_left.height and  \
                self.ball.y + self.ball.height / 2 >= self.racket_left.y and \
                self.ball.x > self.racket_left.x + self.racket_left.width + self.ball.dx / 60 * 2:

            self.music.play()
            self.ball.x = self.racket_left.x + self.racket_left.width
            self.ball.dx = -self.ball.dx
        
        if self.ball.x + self.ball.width >= self.racket_right.x and   \
                self.ball.y + self.ball.height / 2 <= self.racket_right.y + self.racket_right.height and  \
                self.ball.y + self.ball.height / 2 >= self.racket_right.y and \
                self.ball.x + self.ball.width < self.racket_right.x + self.ball.dx / 60 * 2:
            self.music.play()
            self.ball.x = self.racket_right.x - self.ball.width
            self.ball.dx = -self.ball.dx

    def move(self, dt, sprite):
        sprite.y += dt
        if sprite.y > self.height - sprite.height:
            sprite.y = self.height - sprite.height
        if sprite.y < 0:
            sprite.y = 0

if __name__ == '__main__':
    window = Window()
    pyglet.app.run()