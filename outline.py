"""
Function for finding the outline of a simple image.  The image must be
connected. Interior concavities will not be outlined; if this functionality
is needed, it is easily accomplished using PIL.
"""

import pygame as pg


def get_outline(image, color=(0,0,0), threshold=127):
    """Returns an outlined image of the same size.  The image argument must
    either be a convert surface with a set colorkey, or a convert_alpha
    surface. The color argument is the color which the outline will be drawn.
    In surfaces with alpha, only pixels with an alpha higher than threshold will
    be drawn.  Colorkeyed surfaces will ignore threshold."""
    mask = pg.mask.from_surface(image,threshold)
    outline_image = pg.Surface(image.get_size()).convert_alpha()
    outline_image.fill((0,0,0,0))
    for point in mask.outline():
        outline_image.set_at(point,color)
    return outline_image
