import pygame
import pytmx
from pytmx import load_pygame
import os

from utilities.game.tile import Tile
from utilities.game.tileset import TileSet
from utilities.game.tilemap import TileMap
from utilities.game.player import Player

from utilities.game.projectile import Projectile

PATH = ""


class Game:
    def __init__(self, config_file, project_path):
        global PATH
        pygame.init()
        PATH = project_path
        self.screen = pygame.display.set_mode((config_file['Width'], config_file['Height']))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(os.path.join(PATH, project_path + "/assets/Individual Tiles/Tile7.png"))
        self.rect = self.background.get_rect()

    def run(self):
        pytmx_map = load_pygame(PATH + "/assets/levels/test_level.tmx")
        # tile_set = TileSet(PATH + "/assets/Tileset.png")
        # tile_map = TileMap(pytmx_map)

        # tile_map.read_csv(PATH + "/assets/levels/test_level.csv")
        player = Player(100, 100, PATH + "/assets/SpritesheetGuns.png", PATH + "/assets/IconsAndParticles.png", "steve")

        walls = pygame.sprite.Group(self.get_tiles(pytmx_map))
        players = pygame.sprite.Group(player)
        projectiles = pygame.sprite.Group()

        while True:
            self.clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit(0)

            # get input
            projectile = player.do_action(events)
            if projectile is not None:
                projectiles.add(projectile)

            # Check if player collides with wall
            player_collision = pygame.sprite.groupcollide(players, walls, False, False, pygame.sprite.collide_mask)
            self.wall_player_handler(player_collision)
            # Check if bullet collides with wall
            pygame.sprite.groupcollide(walls, projectiles, False, True, pygame.sprite.collide_mask)
            # Check if bullet collides with player
            projectile_collision = pygame.sprite.groupcollide(projectiles, players, True, False, pygame.sprite.collide_mask)

            # handle player collision

            # handle player hit

            # for sprite in sprites:
            #
            #     if not pygame.display.get_surface().get_rect().contains(self.rect):
            #         sprite.kill()
            #     elif sprite.__class__ == Projectile:
            #         sprite.move()
            # LOAD Background
            # tile_map.render() # draw

            # LOAD Player
            self.screen.fill(color="0x807071")  # draw background
            walls.draw(self.screen)
            players.draw(self.screen)
            projectiles.draw(self.screen)
            pygame.display.update()

    @staticmethod
    def wall_player_handler(collisions, previous):
        for key, values in collisions.items():
            print(f"Player: {key.rect.x}, {key.rect.y}")
            if isinstance(values, list):
                for value in values:
                    print(f"Collision: {value.rect.x}, {value.rect.y}")
            else:
                print(f"Collision: {values.rect.x}, {values.rect.yw}")

    @staticmethod
    def get_tiles(pytmx_map):
        tiles = pygame.sprite.Group()
        for layer in pytmx_map.visible_layers:
            print(*layer, sep="\n")
            for x, y, gid in layer:
                if gid == 0:
                    pass
                else:
                    tile = pytmx_map.get_tile_image_by_gid(gid)
                    tile_sprite = Tile(x * 32, y * 32, tile)
                    tiles.add(tile_sprite)
        return tiles

    def load_image(self, file):
        file = file
        image = pygame.image.load(file)
        self.rect = image.get_rect()

        self.screen.blit(image, self.rect)
        pygame.display.update()
