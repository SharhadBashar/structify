# Structify Take-Home Question

## Task
Please write an algorithm to complete the question below in a language of your choice and write a README.md with a brief explanation of your algorithm and how to run it. Include your estimation of the big-O runtime in the README.md

## Question
Given a list of chords in a circle, count the number of intersections, if any. For simplicity's sake, assume all starting and ending points are unique.

## Input
Two lists: one being an identifier of the chord and the other being the radian measure. The identifiers are denoted `s_x` and `e_x`, where `s` is the starting point of the chord, and `e` is the end point of the chord.<br>
The values themselves are radians and sorted in ascending order. Look below for more clarity:

1. Focus on optimizing big-O runtime, but don't worry about system level optimizations
2. Only intersections that happen inside the circle count as intersections, as chords don't continue outside of the circle.
3. For simplicity, assume no intersections will occur at the same point and inputs are constrained `[0, 2*pi)`
4. Any language is acceptable, though we suggest Rust, Python, C+t, C, or Javascript

## Example
Input: `[(0.78, 1.47, 1.77, 3.92), ("s1", "s2", "e1", “e2”)]`<br>
Output: `1 Intersection`<br>
Explanations: Given the far right point of the circle is 0, there are two lines, as denoted by `s_1` and `s_2`. The lines intersect once inside the circle, and thus the answer is `1 Intersection`.<br> 
The image below shows the inputs and the intersection in the circle.

![Image of example](/example.JPG)

## How to run
(Optional) Before running, run `pip install -r requirments.txt` to install requirments
There are 2 ways to run:
1. Jupyter Notebook: Simply open `chords.ipynb` and run all the cells. Third last cell has the input lists. You can modify those as needed. The first thing will be a diagram with all the lines and the intersections in the circle. Then you can see the results in the following two cells of the 2 methods I will describe below
2. Python: Simply run `python main.py`. It will run all the methods as well as draw  a diagram with all the lines and the intersections in the circle. First will be the diagram. Then the results of the 2 methods.

## Big O Time Complexity
Both method takes `O(n^2)` time to run, because of the double for loops

## Explanation
I did 2 methods.<br>

### Method 1: Mathematical approach
This is in the functions `chord_mathematical` in the class `Chords` in `chord.py` file<br><br>
1. When I first looked at the problem, the first thing that came to my mind was getting the equations of the lines and seeing where they intersect.<br>
2. Since we are given the start and end radians of each line, we can find the corresponding `(x, y)` coordinates. See the image below<br>
`x = cos(theta)`<br>
`y = sin(theta`<br>
3. Doing this for each lines start and end point, we get 2 points for each line.<br>
4. Once we have the points, we can calculate the slope and intercept for each line and we can represent each line in the format `y = m*x + b`<br>
5. Finally, after we have the equations of the lines, we can compare each line with others to see where they intersect.<br>
6. Once we have a list of intersections, we also have to make sure that each intersections take place inside the circle. I assume we are working with a unit circle, but that can be passed in as an argument.<br>
7. I use pythagorean theorem to make sure each set of intersections is within the radius of the circle, and if it is, I count that and return the final count as an output<br>
![x, y from radians](https://i.stack.imgur.com/snoUq.png)

### Method 1: Programatic approach
This is in the functions `chord_intersection` in the class `Chords` in `chord.py` file<br>
