import argparse

import numpy as np

from module.display import Display
from module.epipolar import Epipolar



def main():
    display = Display(
        n_points=8, img_path_1=args.img1, img_path_2=args.img2)
    points_1, points_2 = display.get_from_mouse_click()
    
    epipolar = Epipolar(
        img_path_1=args.img1, img_path_2=args.img2, 
        points_1=points_1, points_2=points_2)
    epipolar.draw_epi_line(args.output)

    if args.detail:
        epipolar.show_f_matrix()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--img1', type=str, default='./data/left.jpg', 
        help='path to 1st image')
    parser.add_argument(
        '--img2', type=str, default='./data/right.jpg', 
        help='path to 2nd image')
    parser.add_argument(
        '--output', type=str, default='./output/result.png', 
        help='path to result image to be saved')
    parser.add_argument(
        '--detail', type=bool, default=True, 
        help='show detailed info on fundamental matrix')
    args = parser.parse_args()
    print("===Arguments===")
    print(args)
    print("===============")

    main()


