# pathPlanning
Problem defination
Path Planning
The purpose of this CP468 term project is to design and implement an A?-based algorithm to solve a path
planning problem. You can use the programming language of your choice.
Project Description
Consider a Museum room that is patrolled by N robots at night. At a pre-determined time, the robots are
supposed to rendezvous at a given point R in the room. The robots move inside the room, and the room contains
obstacles, such as chairs and benches for the visitors, paintings, sculptures etc. The robots are supposed to
know the locations of the obstacles in the room.
Implement an A?-based algorithm to compute the path of each robot, from its initial position to the given
rendezvous point R.
Technical details
The location of the obstacles in the room will be given in the form of a text le. The text le will contain
the dimensions of the room, the number of robots N, the initial position of each robot, the given rendezvous
point R as well as the locations of the obstacles in the room. All coordinates in the text le are expressed as
Cartesian coordinates in the plane.
Here is an example of an input text le: ( 0 means vacant point, 1 means obstacle point)
8 10 // the room has dimensions 8 by 10
2 // there are N = 2 robots
2 1 // 1st robot initial position: point (2,1)
8 2 // 2nd robot initial position: point (8,2)
4 7 // the rendezvous point R has coordinates (4,7)
1000000001 // room points (0,7), (1,7), ... (9,7)
1100000011
0000000000
1000110001
1001111001
0001111000
0000110000 // room points (0,1), (1,1), ... (9,1)
1100000011 // room points (0,0), (1,0), ... (9,0)

Goals:
Implement A* algorithm
