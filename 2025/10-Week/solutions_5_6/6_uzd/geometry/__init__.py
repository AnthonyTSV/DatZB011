# geometry/__init__.py
from .circle import area as circle_area, perimeter as circle_perimeter
from .rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from .triangle import area as triangle_area, perimeter as triangle_perimeter
from .square import area as square_area, perimeter as square_perimeter

__all__ = [
    'circle_area',
    'circle_perimeter',
    'rectangle_area',
    'rectangle_perimeter',
    'triangle_area',
    'triangle_perimeter',
    'square_area',
    'square_perimeter'
]
