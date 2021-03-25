import cv2
import numpy as np
import skvideo.io

from ocvart.utils import cprint, get_shortest_side
from ocvart.shapes import CircleGrid


if __name__ == '__main__':
    frame = np.ones((3000, 3000, 3), dtype=np.uint8) * 255
    cg = CircleGrid(center=(2000, 1500), n_circles=80, n_lines=100)
    frame = cg.draw(frame)
    cv2.imwrite("out.png", frame)
    