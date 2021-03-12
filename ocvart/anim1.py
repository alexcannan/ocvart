import cv2
import numpy as np
import skvideo.io

from ocvart.utils.cprint import cprint


def weewoo(n):
    for i in range(n):
        if i % 2 != 0:
            s = "wee"
        else:
            s = "woo"
        cprint(s*i, "RED")


def get_shortest_side(frame):
    return min(frame.shape[:-1])


def circlegrid1(frame, n_circles=15, n_lines=29):
    """ Creates polar-like grid on frame. """
    inner_backoff = 0.07
    outer_backoff = 0.07
    
    shortest_side = get_shortest_side(frame)
    max_radius = shortest_side // 2
    center = (frame.shape[0] // 2, frame.shape[1] // 2)
    circle_radii = np.linspace(max_radius*inner_backoff,
                               max_radius*(1-outer_backoff),
                               n_circles, dtype=int)
    for r in circle_radii:
        cv2.circle(frame, center, r, [0,0,0], 4)
    line_angles = np.linspace(0, 2*np.pi, n_lines, endpoint=False)
    for a in line_angles:
        line_begin = (int(np.cos(a) * max_radius * inner_backoff + center[0]),
                      int(np.sin(a) * max_radius * inner_backoff + center[1]))
        line_end = (int(np.cos(a) * max_radius * (1-outer_backoff) + center[0]),
                    int(np.sin(a) * max_radius * (1-outer_backoff) + center[1]))
        cv2.line(frame, line_begin, line_end, [0,0,0], 4)
    return frame


if __name__ == '__main__':
    frame = np.ones((3000, 3000, 3), dtype=np.uint8) * 255
    frame = circlegrid1(frame)
    cv2.imwrite("out.png", frame)
    