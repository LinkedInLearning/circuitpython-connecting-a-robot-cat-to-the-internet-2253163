# CircuitPython: Connecting a Robot Cat to the Internet
This is the repository for the LinkedIn Learning course CircuitPython: Connecting a Robot Cat to the Internet. The full course is available from [LinkedIn Learning][lil-course-url].

![CircuitPython: Connecting a Robot Cat to the Internet][lil-thumbnail-url] 

While many Internet of Things projects send data to the cloud, sometimes you want a physical indication of an event from the internet. In this course, Charlyn Gonda shows you how to use CircuitPython—a version of Python specifically for microcontrollers—to program a robot cat that reacts to events while connected to the internet. Charlyn shows how to code for common hardware devices like LEDs and servos, and explains a common messaging protocol for IoT projects called message queue telemetry transport, or MQTT. If you’re looking for an internet cat video that actually teaches you something useful, join Charlyn as she shows how to program this robot cat.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"

## Installing
1. To use these exercise files, you must copy and paste `firmware/code.py` into a file named `code.py` on your CircuitPython compatible board (the course uses the "Adafruit Metro M4 Express Airlift Lite" board).
2. (Optional) Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree.

### Instructor

Charlyn Gonda 
                            


                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/charlyn-gonda).

[lil-course-url]: https://www.linkedin.com/learning/circuitpython-connecting-a-robot-cat-to-the-internet
[lil-thumbnail-url]: https://cdn.lynda.com/course/2253163/2253163-1635874806475-16x9.jpg
