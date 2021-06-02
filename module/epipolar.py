import numpy as np
import cv2
import matplotlib.pyplot as plt



class Epipolar:
    def __init__(self, img_path_1: str, img_path_2: str, points_1: np.ndarray, points_2: np.ndarray) -> None:
        self.img_path_1 = img_path_1
        self.img_path_2 = img_path_2
        self.points_1 = points_1
        self.points_2 = points_2

    def draw_epi_line(self, path: str) -> None:
        # calc fundamental matrix
        self.F_mat, _ = cv2.findFundamentalMat(self.points_1, self.points_2, cv2.FM_8POINT)
        # setup base image
        img_1 = cv2.imread(self.img_path_1, 0)
        img_2 = cv2.imread(self.img_path_2, 0)
        # epi line for 1st image
        lines1 = cv2.computeCorrespondEpilines(
            self.points_2, 2, self.F_mat)
        lines1 = lines1.reshape(-1,3)
        img5, _ = self._draw_line(
            img_1, img_2, lines1, self.points_1, self.points_2)
        # epi line for 2nd image
        lines2 = cv2.computeCorrespondEpilines(
            self.points_1, 1, self.F_mat)
        lines2 = lines2.reshape(-1,3)
        img3, _ = self._draw_line(
            img_2, img_1, lines2, self.points_2, self.points_1)

        plt.subplot(121),plt.imshow(img5)
        plt.subplot(122),plt.imshow(img3)
        plt.savefig(path)
        plt.show()
    
    def _draw_line(self, img_1, img_2, lines, points_1, points_2) -> None:
        width = img_1.shape[1]
        img_1 = cv2.cvtColor(img_1, cv2.COLOR_GRAY2BGR)
        img_2 = cv2.cvtColor(img_2, cv2.COLOR_GRAY2BGR)
        for line ,p1,p2 in zip(lines, points_1, points_2):
            color = tuple(np.random.randint(0,255,3).tolist())
            x0,y0 = map(int, [0, -line[2] / line[1] ])
            x1,y1 = map(int, [width, -(line[2] + line[0] * width) / line[1]])
            img_1 = cv2.line(img_1, (x0,y0), (x1,y1), color,1)
            img_1 = cv2.circle(img_1, tuple(p1), 5, color, -1)
            img_2 = cv2.circle(img_2, tuple(p2), 5, color, -1)
        return img_1,img_2

    def show_f_matrix(self) -> None:
        print(self.F_mat)