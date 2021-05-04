"""
The template of the script for the machine learning process in game pingpong
"""
import math

class MLPlay:
    frame_count = 0
    old_x = 0
    old_y = 0
    m = 0
    predict_x = 0
    predict_y = 0
    is_first = 1
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = side

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if self.side == "1P":
            if scene_info["status"] != "GAME_ALIVE":
                return "RESET"

            if not self.ball_served:
                self.ball_served = True
                return "SERVE_TO_LEFT"

            else:
                x,y = scene_info["ball"]
                if y - self.old_y > 0 :
                    if x-self.old_x != 0:
                        self.m = (y - self.old_y)/(x - self.old_x)
                        self.predict_x = math.floor((415-y+self.m*x)/self.m)
                        if(self.predict_x >= 195):
                            # print("hit right wall")
                            self.predict_y = math.floor((195-x)*self.m + y )      #撞牆壁時的y
                            self.predict_x = (415-self.predict_y+(-self.m)*195)/(-self.m)
                            # print(self.predict_x)
                        if(self.predict_x <= 0):
                            # print("hit left wall")
                            self.predict_y = math.floor((0-x)*self.m + y )      #撞牆壁時的y
                            self.predict_x = (415-self.predict_y+(-self.m)*0)/(-self.m)
                            # print(self.predict_x)
                        
                        
                            #self.predict_x = (395-y+self.m*x)/self.m
                    
                        #print(self.predict_x,self.predict_y,x,y)
                    
                if(scene_info["platform_1P"][0] + 20 > math.floor(self.predict_x)):
                            if(scene_info["platform_1P"][0]+20-math.floor(self.predict_x)<5):
                                command = "NONE"
                            else:
                                command = "MOVE_LEFT"
                elif(scene_info["platform_1P"][0] + 20 < math.floor(self.predict_x)):
                            if(math.floor(self.predict_x)-scene_info["platform_1P"][0]+20<5):
                                command = "NONE"
                            else:
                                command = "MOVE_RIGHT"
                else:
                    command = "NONE"
                #print(scene_info)
                self.old_x = x
                self.old_y = y
            

            return command
        elif self.side == "2P":
            if scene_info["status"] != "GAME_ALIVE":
                return "RESET"

            if not self.ball_served:
                self.ball_served = True
                return "SERVE_TO_LEFT"

            else:
                x,y = scene_info["ball"]
                if y - self.old_y < 0 :
                    if x-self.old_x != 0:
                        self.m = (y - self.old_y)/(x - self.old_x)
                        self.predict_x = math.floor((80-y+self.m*x)/self.m)
                        if(self.predict_x >= 195):
                            # print("hit right wall")
                            self.predict_y = math.floor((195-x)*self.m + y )      #撞牆壁時的y
                            self.predict_x = (80-self.predict_y+(-self.m)*195)/(-self.m)
                            # print(self.predict_x)
                        if(self.predict_x <= 0):
                            # print("hit left wall")
                            self.predict_y = math.floor((0-x)*self.m + y )      #撞牆壁時的y
                            self.predict_x = (80-self.predict_y+(-self.m)*0)/(-self.m)
                            # print(self.predict_x)
                        
                            #self.predict_x = (395-y+self.m*x)/self.m
                    
                        #print(self.predict_x,self.predict_y,x,y)
                    
                if(scene_info["platform_2P"][0] + 20 > math.floor(self.predict_x)):
                            if(scene_info["platform_2P"][0]+20-math.floor(self.predict_x)<5):
                                command = "NONE"
                            else:
                                command = "MOVE_LEFT"
                elif(scene_info["platform_2P"][0] + 20 < math.floor(self.predict_x)):
                            if(math.floor(self.predict_x)-scene_info["platform_2P"][0]+20<5):
                                command = "NONE"
                            else:
                                command = "MOVE_RIGHT"
                else:
                    command = "NONE"
                #print(scene_info)
                self.old_x = x
                self.old_y = y
            

            return command


    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
