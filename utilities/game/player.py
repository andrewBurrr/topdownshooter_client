import pygame
from utilities.game.spritesheet import SpriteSheet
from utilities.game.projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, player_sprite, projectile_sprite, name):
        pygame.sprite.Sprite.__init__(self)
        player_ss = SpriteSheet(player_sprite)
        self.player_images = player_ss.load_grid_images(2, 2, rot=90)
        self.image = self.player_images[2]
        self.mask = pygame.mask.from_surface(self.image)
        self.project_sprite = projectile_sprite
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = None
        self.name = name
        self.speed = 3
        self.health = 100
        self.shot_delay = 150
        self.last_shot = pygame.time.get_ticks()

    def point_at(self, mouse_x, mouse_y):
        self.direction = pygame.math.Vector2(mouse_x, mouse_y) - self.rect.center
        angle = self.direction.angle_to(pygame.math.Vector2(0, -1))
        self.image = pygame.transform.rotate(self.player_images[2], angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, x, y):
        self.rect.move_ip(x * self.speed, y * self.speed)

    def do_action(self, events):
        self.point_at(*pygame.mouse.get_pos())
        keys = pygame.key.get_pressed()
        self.move(keys[pygame.K_d] - keys[pygame.K_a], keys[pygame.K_s] - keys[pygame.K_w])
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return Projectile(self.rect.centerx, self.rect.centery, self.direction, self.project_sprite, 16)
        return None
