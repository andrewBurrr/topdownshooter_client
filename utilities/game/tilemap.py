# import numpy as np
import pygame
import os
from utilities.game.tile import Tile
#
#
# class TileMap:
#     def __init__(self, tile_set, screen, size=(20, 20), rect=None):
#         self.size = size
#         self.tile_set = tile_set
#         self.tile_map = np.zeros(size, dtype=int)
#
#         # h, w = self.size
#         self.screen = screen
#         if rect:
#             self.rect = pygame.Rect(rect)
#         else:
#             self.rect = self.screen.get_rect()
#
#     def render(self):
#         m, n = self.tile_map.shape
#         for i in range(m):
#             for j in range(n):
#                 if self.tile_map[i, j] != 9:
#                     tile = self.tile_set.tiles[self.tile_map[i, j]]
#                     self.screen.blit(tile, (j * 32, i * 32))
#
#     def read_csv(self, filename):
#         self.tile_map = np.genfromtxt(os.path.join(filename), delimiter=',', dtype=int)
#         self.render()
#
#     def get_walls(self):
#         m, n = self.tile_map.shape
#         return [self.tile_set.tiles[self.tile_map[i, j]] for i in range(m) for j in range(n) if self.tile_map[i, j] != 9]
#
#     def __str__(self):
#         return f"{self.__class__.__name__} {self.size}"

class TileMap:
    def __init__(self, pytmx_map):
        fin
        for y in range(20):
            for x in range(20):
                # tile = pytmx_map.get_tile_image(x, y, 0)
                # tile_sprite = Tile(x * 32, y * 32, tile)
                # initial_tiles.add(tile_sprite)
                #
                gid = pytmx_map.get_tile_gid(x, y, 1)
                if gid == 0 or gid == 15:
                    pass
                else:
                    tile = pytmx_map.get_tile_image(x, y, 1)
                    tile_sprite = Tile(x * 32, y * 32, tile)
                    tile.set_colorkey(0)
                    final_tiles.add(tile_sprite)