import pygame
from utilities.game.spritesheet import SpriteSheet


class AbstractPlayer(pygame.sprite.Sprite):
    def __init__(self, player_sprite, start_position, velocity):
        pygame.sprite.Sprite.__init__(self)
        player_ss = SpriteSheet(player_sprite)
        self.player_images = player_ss.load_grid_images(2, 2, rot=90)
        self.image = self.player_images[2]
        self.rect = self.image.get_rect(center=start_position)
        self.mask = pygame.mask.from_surface(self.image)
        self.previous_direction = (0, 0)
        self.velocity = velocity
        self.direction = None

    def rotate_transform(self, angle):
        self.image = pygame.transform.rotate(self.player_images[2], angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, x, y):
        self.previous_direction = (x, y)
        self.rect.move_ip(x * self.velocity, y * self.velocity)

    def shoot(self):
        # return list of attributes needed to spawn bullet
        pass

    def collide(self, mask, x=0, y=0):
        player_mask = pygame.mask.from_surface(self.image)
        offset = (int(self.rect.x - x), int(self.rect.y - y))
        return mask.overlap(player_mask, offset)

    def collide_fix(self):
        # determine x and y with proper signs to reveres previous move
        self.rect.move_ip(-self.previous_direction[0] * self.velocity, -self.previous_direction[1] * self.velocity)


class Player(AbstractPlayer):
    def __init__(self, x, y, player_sprite):
        AbstractPlayer.__init__(self, player_sprite, (x, y), 3)
        self.rect = self.image.get_rect(center=(x, y))
        self.health = 100
        self.shot_delay = 150
        self.last_shot = pygame.time.get_ticks()

    def rotate(self, x, y):
        self.direction = pygame.math.Vector2(x, y) - self.rect.center
        angle = self.direction.angle_to(pygame.math.Vector2(0, -1))
        self.rotate_transform(angle)
