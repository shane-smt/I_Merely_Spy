import pygame
from settings import TILESIZE
from tile import Tile
from player import Player
from utilities import import_csv_layout


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
        layout = {"boundry": import_csv_layout("../map/Boundry.csv"),
                  "walls": import_csv_layout("../map/Walls.csv"),
                  "wallover": import_csv_layout("../map/Wallover.csv"),
                  "entities": import_csv_layout("../map/Entities.csv"),
                  "surfaces": import_csv_layout("../map/Surfaces.csv"),
                  "objects": import_csv_layout("../map/Objects.csv")}

        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == "boundry":
                            Tile((x, y), [self.obstacles_sprites], "invisible")  # noqa
        self.player = Player((x-100, y-100), (self.visible_sprites), self.obstacles_sprites)  # noqa

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

        self.floor_surf = pygame.image.load('../graphics/tilemap/floor.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        """Custom draw replaces the inbuilt draw method from the sprite.sprite.Group class. The changes allow for
        perspective changes such as being behind or in front of objects. This also implements a camera to the class
        allowing the player to always be centered as they move about the level """
        self.cam_offset.x = player.rect.centerx - self.half_width
        self.cam_offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.cam_offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.cam_offset
            self.display_surface.blit(sprite.image, offset_position)
