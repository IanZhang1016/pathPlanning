# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:57:33 2018

@author: Group 5
"""


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
        self.coordnate_tuple = coordinate_tuple
        self.init_init_position = init_position
        self.rendezvous_point = rendezvous_point
        self.path = []
    
    
    def find_path(self):
        """Find the path of current robot from the initial psotion to the rendezvous point
        
        In this method, we will use the instance variables to find a path. We will save the 
        path in the instacne variable, self.path
        
        Args:
            None
            
        Returns:
            None
        """
        pass
    
    
    def print_path(self):
        """Print the path
        
        In this method, we will output the path in the standard format
        
        Args:
            None
        
        Returns:
            None
        """
        pass
    
    
def read_info(path):
    """Read the information from the txt file
    
    In this function, we will get the information of the museum and return the results
    
    Args:
        path: the file path
        
    Return:
        num_robot: the number of the robot
        init_position_tuple:  a tuple save the initial postion of the all robots
        rendezvous_point: the coordiante of the rendezvous point
        coordinate_tuple: A tuple save all coordinates
        
    Note:All coordinates in the text 
le are expressed as Cartesian coordinates 
         in the plane. So we need to convert it to a normal coordinate system.
    """
    pass


def init_all(file_path = 'test.txt'):
    num_robot, init_position_tuple, rendezvous_point, coordinate_tuple = read_info(file_path)  
    
    robot_list = []
    for init_postion in init_position_tuple:
        robot = Robot(coordinate_tuple, init_postion, rendezvous_point)
        robot.find_path()
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
