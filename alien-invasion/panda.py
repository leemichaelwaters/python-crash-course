import pygame

class Panda:
    """A class to manage a panda game character."""

    def __init__(self, ai_game):
        """Initialize the game character and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the game character image and get its rect.
        self.image = pygame.image.load('images/panda.bmp')
        self.rect = self.image.get_rect()

        # Start each new game character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the game character at its current location."""
        self.screen.blit(self.image, self.rect)