import pygame
from utilities.game.spritesheet import SpriteSheet


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, sprite, speed):
        pygame.sprite.Sprite.__init__(self)
        projectile_ss = SpriteSheet(sprite)
        projectile_images = projectile_ss.load_grid_images(4, 3)
        self.image = projectile_images[9]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(self.pos.x, self.pos.y))
        self.angle = pygame.math.Vector2(direction).normalize()
        self.pos = pygame.math.Vector2(x, y)
        self.speed = 7
        self.offset(speed)

    def offset(self, player_size):
        self.pos = self.angle * player_size
        self.rect.move_ip(self.pos.x, self.pos.y)

    def move(self):
        self.pos = self.angle * self.speed
        self.rect.move_ip(self.pos.x, self.pos.y)
