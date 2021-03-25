"""
Author: Alex Cannan
Date Created: 2021/3/24
Purpose: Home for circle-like shapes to overlay in frame
"""

import cv2
import numpy as np

from ocvart.utils import get_shortest_side

class CircleGrid:
    def __init__(self, center=None, radius=None, n_circles=15, n_lines=29):
        self.center = center
        self.radius = radius
        self.n_circles = n_circles
        self.n_lines = n_lines

    def draw(self, frame):
        """ Creates polar-like grid on frame. """
        inner_backoff = 0.07
        outer_backoff = 0.07
        
        shortest_side = get_shortest_side(frame)
        if self.radius is None:
            self.radius = shortest_side // 2
        if self.center is None:
            self.center = (frame.shape[0] // 2, frame.shape[1] // 2)
        circle_radii = np.linspace(self.radius*inner_backoff,
                                   self.radius*(1-outer_backoff),
                                   self.n_circles, dtype=int)
        for r in circle_radii:
            cv2.circle(frame, self.center, r, [0,0,0], 4)
        line_angles = np.linspace(0, 2*np.pi, self.n_lines, endpoint=False)
        for a in line_angles:
            line_begin = (int(np.cos(a) * self.radius * inner_backoff + self.center[0]),
                        int(np.sin(a) * self.radius * inner_backoff + self.center[1]))
            line_end = (int(np.cos(a) * self.radius * (1-outer_backoff) + self.center[0]),
                        int(np.sin(a) * self.radius * (1-outer_backoff) + self.center[1]))
            cv2.line(frame, line_begin, line_end, [0,0,0], 4)
        return frame