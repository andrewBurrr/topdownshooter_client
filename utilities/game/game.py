import pygame
from pytmx import load_pygame
import os

from utilities.game.tile import Tile
from utilities.game.player import Player

from utilities.game.projectile import Projectile

PATH = ""


class Game:
    FPS = 60

    def __init__(self, config_file, project_path):
        global PATH
        pygame.init()
        PATH = project_path
        self.screen = pygame.display.set_mode((config_file['Width'], config_file['Height']))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(os.path.join(PATH, project_path + "/assets/Individual Tiles/Tile7.png"))
        self.rect = self.background.get_rect()

    def draw(self, walls, players, projectiles):
        self.screen.fill(color="0x807071")
        walls.draw(self.screen)
        players.draw(self.screen)
        projectiles.draw(self.screen)
        pygame.display.update()

    def handle_collision(self, walls, players, projectiles):
        # player collides with wall
        player_collisions = pygame.sprite.groupcollide(players, walls, False, False, self.collide_check)
        if len(player_collisions) != 0:
            for player in players:
                print("fixing")
                player.collide_fix()

        # bullet collides with wall
        projectile_collisions = pygame.sprite.groupcollide(projectiles, walls, True, False, self.collide_check)
        if projectile_collisions is not None:
            # TODO projectile hit animation
            pass

        # bullet collides with player
        projectile_collisions = pygame.sprite.groupcollide(projectiles, players, True, False, self.collide_check)
        if projectile_collisions is not None:
            # TODO projectile hit animation
            # TODO player damage
            pass

    def run(self):
        pytmx_map = load_pygame(PATH + "/assets/levels/test_level.tmx")
        player = Player(100, 100, PATH + "/assets/SpritesheetGuns.png")

        walls = pygame.sprite.Group(self.get_tiles(pytmx_map))
        players = pygame.sprite.Group(player)
        projectiles = pygame.sprite.Group()

        while True:
            self.clock.tick(self.FPS)

            # TODO draw menu

            self.draw(walls, players, projectiles)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit(0)

            # TODO get actions
            # get keys pressed
            keys = pygame.key.get_pressed()
            # move player according to keys
            player.move(keys[pygame.K_d] - keys[pygame.K_a], keys[pygame.K_s] - keys[pygame.K_w])
            # rotate player
            mouse_x, mouse_y = pygame.mouse.get_pos()
            player.rotate(mouse_x, mouse_y)
            # shoot projectile
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    projectiles.add(Projectile(player.rect.centerx, player.rect.centery, player.angle, PATH + "/assets/IconsAndParticles.png", 16))
            # move projectiles
            for projectile in projectiles:
                projectile.remove()
            self.handle_collision(walls, players, projectiles)

            # TODO if game over

    @staticmethod
    def collide_check(sprite1, sprite2):
        return pygame.sprite.collide_mask(sprite1, sprite2)

    @staticmethod
    def get_tiles(pytmx_map):
        tiles = []
        for layer in pytmx_map.visible_layers:
            for x, y, gid in layer:
                if gid == 0:
                    pass
                else:
                    tile = pytmx_map.get_tile_image_by_gid(gid)
                    tile_sprite = Tile(x * 32, y * 32, tile)
                    tiles.append(tile_sprite)
        return tiles

    def load_image(self, file):
        file = file
        image = pygame.image.load(file)
        self.rect = image.get_rect()

        self.screen.blit(image, self.rect)
        pygame.display.update()
