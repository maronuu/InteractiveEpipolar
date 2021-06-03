from typing import Tuple

import numpy as np
import cv2



class Display:
    """Display class for UI
    """
    def __init__(self, n_points: int, img_path_1: str, img_path_2: str) -> None:
        self.n_points = n_points
        # store input points here
        self.points_1 = np.zeros((self.n_points, 2), dtype=int)
        self.points_2 = np.zeros((self.n_points, 2), dtype=int)
        # point counter of each image
        self._ref_cnt_img_1 = 0
        self._ref_cnt_img_2 = 0
        # dot color for each image
        self.dot_color_1 = (255, 0, 0)
        self.dot_color_2 = (0, 255, 0)
        # setup 2 views
        self.img_path_1 = img_path_1
        self.img_path_2 = img_path_2
        self.window_1 = None
        self.window_2 = None
        self._setup_display()

    def get_from_mouse_click(self) -> Tuple[np.ndarray]:
        while 1:
            cv2.imshow("view_1", self.window_1)
            cv2.imshow("view_2", self.window_2)
            # check if to quit
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            elif self._ref_cnt_img_1 > self.n_points or self._ref_cnt_img_2 > self.n_points:
                raise IndexError("number of input points is greater than the given limit")
            elif self._ref_cnt_img_1 == self._ref_cnt_img_2 == self.n_points:
                break
        # finalize input
        cv2.destroyAllWindows()
        return self.points_1, self.points_2

    def _setup_display(self, is_event=True) -> None:
        self.window_1 = cv2.imread(self.img_path_1)
        self.window_2 = cv2.imread(self.img_path_2)
        if is_event:
            cv2.namedWindow("view_1", cv2.WINDOW_KEEPRATIO)
            cv2.namedWindow("view_2", cv2.WINDOW_KEEPRATIO)
            cv2.setMouseCallback("view_1", self._draw_dot_1)
            cv2.setMouseCallback("view_2", self._draw_dot_2)

    def _draw_dot_1(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            self.points_1[self._ref_cnt_img_1][0] = x
            self.points_1[self._ref_cnt_img_1][1] = y
            cv2.circle(
                img=self.window_1,
                center=(x, y),
                color=self.dot_color_1,
                radius=3,
                thickness=-1,
            )
            self._ref_cnt_img_1 += 1

    def _draw_dot_2(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            self.points_2[self._ref_cnt_img_2][0] = x
            self.points_2[self._ref_cnt_img_2][1] = y
            cv2.circle(
                img=self.window_2,
                center=(x, y),
                color=self.dot_color_2,
                radius=3,
                thickness=-1,
            )
            self._ref_cnt_img_2 += 1