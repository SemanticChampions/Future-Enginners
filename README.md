# WRO FUTURE ENGINEERS

## ROBOT DESIGN PROCESS

## Table of Content

1. Aim and objective of the bot
2. Research and Brainstorming
3. Build a Prototype
4. Build a Robot
5. Competition Strategy
6. Robot Testing

## ROBOT AIM and OBJECTIVES
Aim
The aim of the robot is to swiftly maneuver its environment or parkour.
This involves

**Objectives**

1. Detect obstacles in the environment.
2. Avoid obstacles in the environment.
3. Perform (1) and (2) while self driving.
4. Detect state and auto-correct when crashed or in error.
### Constraints
1. Time
2. Motor
3. Drive train
4. Cannot use too common ideas from the internet
5. Dimensions

## RESEARCH and BRAINSTORMING
Practical Functions of the Robot
Using a rear-wheel drive system the bot will be able to perform the follow (the following list is in order of priority)

### PRACTICAL FUNCTIONS OF ROBOT
● Moving in all directions
  
● Lane following
  
● Acceleration and deceleration
  
● Braking
  
● Color Detection
  
● Turning
  
● Crash handling
  
● Orientation detection
  
● Obstacle detection
  
● Obstacle avoidance
  
● Light adjustment
  
### ELABORATION OF PRACTICAL FUNCTIONS DETAILS
**COLOR DETECTION BY THE ROBOT:**  
With the OpenCV library, the robot will be programmed to detect color using the following.

**The HSV format**:

1. The video frame is read correctly.
2. Each frame is converted from BGR to HSV.
3. A mask is created using the inRange() method on the image with the image and the color to be detected as the arguments.
4. After doing the above, a threshold image is created by the mask. This blacks out every other item in the image leaving only the pixels that match the mask. This creates a black background with a white range of detection.
5. This shows that the color has been detected

## Energy Source for the Robot

The robot uses a 9V adapter that has an output of 2.5A or more.


## Intelligence (How does the robot think):

The bot uses deep learning models alongside computer vision, Kalman filtering and concepts of Advanced Driver Assistance Systems(ADAS) all made with C++ and python.
Using Computer vision and Kalman filtering to make itself aware of itself and  environment and how to react to changes in the environment.
Sketching
This is where the AutoCAD(Fusion360) squad come in.
Building a Prototype


### Competition Strategy
Since the competition is a time attack race time of completion is very essential to everything. Therefore all ideas should be developed to the point where it makes the robot do things faster.
Current Strategy

Motion:
For the first lap the robot learns about [//the environment and positions of all the red and green bars on the mat. – Why is this the first thing to do?
Using that data, the robot adapts itself increasing to maximum speeds and turn rates at various points during the second and last laps of the round and possibly drifting

**To be able to do this:** 

1. The first step is to be able to move around the game mat as possible while no obstacles on the mat.
2. Then moving while detecting obstacles and avoiding obstacles.
3. Performing (2) flawlessly.
4. Gather information on the current mat
5. Moving with pre-recorded information
6. Speeding up.
7. Drifting (optional. We would really love to be able to drift) – Do you know the essence of drifiting?

## Robot Testing
