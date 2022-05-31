import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(tile_sprite, (32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

    def __str__(self):
        return f"Tile: X:{self.rect.x}, Y:{self.rect.y}"
