# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:57:33 2018

@author: Group 5
"""
import numpy as np


class Robot(object):
    def __init__(self, coordinate_tuple, init_position, rendezvous_point):
        """Init a instance of Robot class
        
        In this method, we will initialize all instance variables
        
        Args:
            coordinate_tuple:A tuple save all coordinates(This coordinate system is normal.)
            init_position: A list save the coordinate of the initial position, like[2, 8]
            rendezvous_point: A list save the coordinate of the initial position, like[4, 7]
        
        Returns:
            None
        """
        self.coordinate_tuple = coordinate_tuple
        self.init_position = init_position
        self.rendezvous_point = rendezvous_point
        self.path = []
    
    
    def find_path(self):
        """Find the path of current robot from the initial psotion to the rendezvous point
        
        In this method, we will use the instance variables to find a path. We will save the 
        path in the instacne variable, self.path
        
        Args:
            None
            
        Returns:
            False: means didn't find path
            path: means find path
        
        Note: We will use the instance variable coordinate_tuple. This variable stores 
              information in a normal coordinate system, not Cartesian coordinates. 
              This point is very important.
        """
        closed_list = []
        open_list = [self.init_position]
        pred = np.full((len(self.coordinate_tuple),len(self.coordinate_tuple[0])),None)
        g_score = np.zeros((len(self.coordinate_tuple),len(self.coordinate_tuple[0])))
        h_score = np.zeros((len(self.coordinate_tuple),len(self.coordinate_tuple[0])))
        f_score = np.zeros((len(self.coordinate_tuple),len(self.coordinate_tuple[0])))
        
        
        def heuristic_estimate_of_distance(point,sec_point=self.rendezvous_point):
            return np.linalg.norm(np.array(point) - np.array(sec_point))

                
        def construct_path():
            path = []
            index = self.rendezvous_point
            while index != self.init_position:
                path.append(index)
                index = pred[index[0],index[1]]
            path.append(self.init_position) 
            return path
            
            
        h_score[self.init_position[0], self.init_position[1]] = heuristic_estimate_of_distance(self.init_position)
        
        
        while open_list:
            x = open_list[0]
            if x == self.rendezvous_point:
                return construct_path()

            open_list.pop(0)
            closed_list.append(x)
            
            neigh_list = []

            #The robot can only move to up, down, left, right
            for i in range(-1, 2):
                if x[0] + i > 0 and x[0] + i < len(self.coordinate_tuple):
                    for j in range(-1, 2):
                        if x[1] + j < len(self.coordinate_tuple[0]) and abs(i) != abs(j):
                            if x[1] + j > 0 and x != [x[0] + i, x[1] + j] and self.coordinate_tuple[x[0] + i][x[1] + j] == 0:                        
                                neigh_list.append([x[0] + i,x[1] + j])

# =============================================================================
#             #The robot can move to north, west, south, east, northwest, northeast, southwest, southeast
#             for i in range(-1, 2):
#                 if x[0] + i > 0 and x[0] + i < len(self.coordinate_tuple):
#                     for j in range(-1, 2):
#                         if x[1] + j < len(self.coordinate_tuple[0]):
#                             if x[1] + j > 0 and x != [x[0] + i, x[1] + j] and self.coordinate_tuple[x[0] + i][x[1] + j] == 0:                        
#                                 neigh_list.append([x[0] + i,x[1] + j])
# =============================================================================
                    
            for y in neigh_list:
                if y in closed_list:
                    continue
                tentative_g_score = g_score[x[0],x[1]] + heuristic_estimate_of_distance(x,y)
                
                if y not in open_list:
                    open_list.append(y)
                    tentative_is_better = True
                elif tentative_g_score < g_score[y[0],y[1]]:
                    tentative_is_better = True
                else:
                    tentative_is_better = False
                
                if tentative_is_better:
                    pred[y[0],y[1]] = x
                    g_score[y[0],y[1]] = tentative_g_score
                    h_score[y[0],y[1]] = heuristic_estimate_of_distance(y)
                    f_score[y[0],y[1]] = g_score[y[0],y[1]] + h_score[y[0],y[1]]
                    sorted(open_list, key = lambda x: f_score[x[0], x[1]])
        return False
    
    def print_path(self):
        """Print the path
        
        In this method, we will output the path in the standard format
        
        Args:
            None
        
        Returns:
            None
        """
        f = open('output.txt','a')
        print(self.path)
        f.write('One robot path:\n')
        for point in reversed(self.path):
            f.write('(' + str(point[0]) + ',' +str(point[1]) + ')')
        f.write('\n')
        f.close()
        
    def set_path(self):
        self.path = self.find_path()
            
    
    
def read_info(path):
    """Read the information from the txt file
    
    In this function, we will get the information of the museum and return the results
    
    Args:
        path: the file path
        
    Return:
        init_position_tuple:  a tuple save the initial postion of the all robots
        rendezvous_point: the coordiante of the rendezvous point
        coordinate_tuple: A tuple save all coordinates
        
    Note:All coordinates in the text are expressed as Cartesian coordinates 
         in the plane. So we need to convert it to a normal coordinate system.
    """
    info = []
    init_position_tuple = ()
    init_position_list = []
    
    with open(path, 'r') as file:
        for line in file.readlines():
            info.append(line)
            
        num_robot = int(info[1][0])
        temp = []
        for i in range(2+int(info[1][0])+1):
            temp.append(info[i].split())
        
        for index in range(num_robot):
            point = [int(temp[2+index][0]),int(temp[2+index][1])]
            init_position_list.append(point)
        init_position_tuple = tuple(init_position_list)
        
        rendezvous_point = [int(temp[num_robot + 2][0]), int(temp[num_robot + 2][1])]
        
        def str2int(items):
            new_items = []
            for item in items:
                new_items.append(int(item))
            return new_items
        
        matrix = info[num_robot+3:] 
        matrix[:] = map(str2int,zip(*matrix[::-1]))
        matrix = tuple(matrix)
        
    return init_position_tuple, rendezvous_point, matrix
        
        
        
def init_all(file_path = 'test4.txt'):
    """Create instances of class Robot, and create a list save all robot instances
    
    Args:
        file_path: A file path save the information file, and the default value is 'test.txt'
        
    Return:
        robot_list: The list save all robot instances
    """
    init_position_tuple, rendezvous_point, coordinate_tuple = read_info(file_path)  
    
    robot_list = []
    for init_postion in init_position_tuple:
        robot = Robot(coordinate_tuple, init_postion, rendezvous_point)
        robot.set_path()
        robot_list.append(robot)
    
    return robot_list


def get_result(robot_list):
    """Using a loop to invoke the print_path method
    
    Args:
        roobot_list: A list save the all instances of Class Robot
        
    Return:
        None    
    """
    for robot in robot_list:
        robot.print_path()

    
def main():
    robot_list = init_all() ##need input the information file path
    get_result(robot_list)
    

if __name__ == '__main__':
    main()
