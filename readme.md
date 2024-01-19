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