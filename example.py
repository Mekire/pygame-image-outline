"""
Example usage of the get_outline function.
"""

import os
import sys
import pygame as pg
from outline import get_outline


CAPTION = "Outline with Rotation"


class Control(object):
    def __init__(self,image):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.angle = 0.0
        self.rotation_speed = 1
        self.original_image = image
        self.make_images(self.original_image)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def make_images(self,image):
        self.angle = (self.angle-self.rotation_speed)%360
        self.image = pg.transform.rotozoom(image,self.angle,1)
        self.rect = self.image.get_rect(center=(50,50))
        raw = pg.transform.smoothscale(image,(300,300))
        raw = pg.transform.rotozoom(raw,self.angle,1)
        self.out = get_outline(raw,color=(255,0,0),threshold=100)
        self.out_rect = self.out.get_rect(center=self.screen_rect.center)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.make_images(self.original_image)
            self.screen.fill((255,255,255))
            self.screen.blit(self.image,self.rect)
            self.screen.blit(self.out,self.out_rect)
            pg.display.update()
            self.clock.tick(self.fps)
            caption = "{} - FPS: {:.2f}".format(CAPTION,self.clock.get_fps())
            pg.display.set_caption(caption)


if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"] = '1'
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode((500,500))
    SHIP = pg.image.load("ship_up.png").convert_alpha()
    run_it = Control(SHIP)
    run_it.main_loop()
    pg.quit()
    sys.exit()
