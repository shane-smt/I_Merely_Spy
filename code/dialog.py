import pygame


def end_dialog(dialog) -> None:
    del dialog
    return None


class Dialog:
    def __init__(self, dialog_text, sprite_image, dialog_box_image, font, font_size, font_color, dialog_box_position,
                 sprite_position):
        # Initialize the dialog text and sprite image
        self.dialog_text = dialog_text
        self.sprite_image = sprite_image
        self.dialog_box_image = dialog_box_image
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.dialog_box_position = dialog_box_position
        self.sprite_position = sprite_position

        # Initialize the current line of dialog and the index of the current character
        self.current_line = 0
        self.current_char = 0

        # Split the dialog text into a list of lines
        self.lines = self.dialog_text.split("\n")

        # Create a font object for rendering the dialog text
        self.font_object = pygame.font.Font(self.font, self.font_size)

    def update(self):
        # Update the current line and character based on player input
        # You can use Pygame's key.get_pressed() function to check for specific keys being pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.current_char += 1
        if self.current_char >= len(self.lines[self.current_line]):
            self.current_char = 0
            self.current_line += 1
        if self.current_line >= len(self.lines):
            # End the dialog when all lines have been displayed
            end_dialog(self)

    def draw(self, surface):
        # Render the dialog box and sprite image
        surface.blit(self.dialog_box_image, self.dialog_box_position)
        surface.blit(self.sprite_image, self.sprite_position)

        # Render the current line of dialog text
        text = self.font_object.render(self.lines[self.current_line][:self.current_char], True, self.font_color)
        text_rect = text.get_rect()
        text_rect.center = (self.dialog_box_position[0] + self.dialog_box_position[2] // 2,
                            self.dialog_box_position[1] + self.dialog_box_position[3] // 2)
        surface.blit(text, text_rect)
