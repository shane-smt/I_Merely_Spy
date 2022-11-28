import pygame
from settings import TILESIZE, TEST_MAP
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        # This is to prevent the need to pass the surface object to the level class init
        self.display_surface = pygame.display.get_surface()
        # Sprite Groups Setup
        self.visible_sprites = YSortCamGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.build_map()

    def build_map(self):

        for row_index, row in enumerate(TEST_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == "-":
                    Tile((x, y), (self.visible_sprites, self.obstacles_sprites))
                if col == "p":
                    self.player = Player((x, y), (self.visible_sprites), self.obstacles_sprites)  # noqa

    def run(self):
        # Update and Draw all Level Elements
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCamGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.cam_offset = pygame.math.Vector2()

    def custom_draw(self, player):
        """Custom draw replaces the inbuilt draw method from the sprite.sprite.Group class. The changes allow for
        perspective changes such as being behind or in front of objects. This also implements a camera to the class
        allowing the player to always be centered as they move about the level """
        self.cam_offset.x = player.rect.centerx - self.half_width
        self.cam_offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.cam_offset
            self.display_surface.blit(sprite.image, offset_position)
