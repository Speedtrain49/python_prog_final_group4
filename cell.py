import pygame, sys
class Cell:
    def __init__(self,value,row,col,screen):
        self.set_value = 0
        self.sketchedValue = None
        self.value = value
        self.col = col
        self.row = row
        self.rown = row*55
        self.coln = col*55
        self.screen = screen
        self.static = False
        self.sketeched = False
        self.entered = False

    def set_cell_value(self,value):
        self.set_value = value
        self.sketeched = False
        self.entered = True

    def set_static_cell_value(self,value):
        self.set_value = value
        self.static = True
    def set_sketched_value(self,value):
        self.sketchedValue = value
        self.sketeched = True

    def draw(self, selected):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.coln - 52, self.rown - 52, 50, 50))
        if self.value > 0 and self.sketeched == False:
            font_number = pygame.font.Font(None,35)
            text_font = font_number.render(str(self.set_value), 0, (0,0,0))
            self.screen.blit(text_font, (self.coln - 30, self.rown - 30))
        elif self.sketeched and self.sketchedValue > 0:
            font_number = pygame.font.Font(None, 25)
            text_font = font_number.render(str(self.sketchedValue), 0, "grey")
            self.screen.blit(text_font, (self.coln - 40, self.rown - 40))
        elif self.entered:
            font_number = pygame.font.Font(None,35)
            text_font = font_number.render(str(self.set_value), 0, (0,0,0))
            self.screen.blit(text_font, (self.coln - 30, self.rown - 30))
        if selected == True:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.coln - 52, self.rown - 52, 50, 50), 2)
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), (self.coln - 52, self.rown - 52, 50, 50), 2)
