# InteractiveEpipolar

## What is this?
This is an interactive interface to experience the 8-points algorithm on Epipolar geometry.

## Requirements
Tested on
- Ubuntu 20.04
- Python 3.8.5
  - matplotlib      3.4.2
  - numpy           1.20.3
  - opencv-python   4.5.2.52
  

## Install & Run
### 1. Install libraries
```
cd ~/
git clone https://github.com/maronuu/InteractiveEpipolar.git
cd ~/InteractiveEpipolar
pipenv install -r requirements.txt
```
Of course, you can utilize another method than pipenv.

### 2. Run main.py
```
python3 main.py --img1 data/left.jpg --img2 data/right.jpg --output output/result.png [--detail]
```
Then, two windows will show up.

### 3. Click 8 correspondent points on each image ALTERNATELY.

![two images of the same object from different views](https://user-images.githubusercontent.com/63549742/120670048-fc48cf00-c4ca-11eb-803b-73f48c1b09a9.png)

You must do alternately, like

Input 1st point on view_1 -> Input 1st point on view_2 ->

Input 2nd point on view_1 -> Input 2nd point on view_2 ->

...

Input 8th point on view_1 -> Input 8th point on view_2

Then, a result will show up. It is to be saved to `InteractiveEpipolar/output/{picture_name}.png`

![result](https://user-images.githubusercontent.com/63549742/120671200-1df68600-c4cc-11eb-9b53-fba297430e54.png)

## Description
A detailed explanation of Epipolar Geometry is [here](https://docs.opencv.org/3.4/da/de9/tutorial_py_epipolar_geometry.html).

Note that this implementation is using an 8-points algorithm, which can solve it linearly, but it lacks robustness.
Actually, `output/result.png` falls short of accurate epilines.
For a more accurate calculation,
- Utilize extracted features to find matched points like [Flann-based matcher](https://docs.opencv.org/3.4/dc/de2/classcv_1_1FlannBasedMatcher.html).
- Get a far greater number of points (automatically).
