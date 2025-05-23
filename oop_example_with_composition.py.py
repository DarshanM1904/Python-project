class Gun:
    def __init__(self, bullet, macsion):
        self.bullet = bullet
        self.macsion = macsion

    def fire(self):
        print(f'Sniper with macsion: {self.macsion} and bullet: {self.bullet}')

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.gun = Gun(bullet='12', macsion='24M')  # Corrected: use Gun directly

    def task(self):
        print(f'Hi {self.name}, {self.id}')
        self.gun.fire()

# Create object and call task
jb = Person(id='007', name='James Bond')
jb.task()
