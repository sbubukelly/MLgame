"""
The template of the main script of the machine learning process
"""
import math

class MLPlay:

    old_x = 0
    old_y = 0
    m = 0
    predict_x = 0
    predict_y = 0

    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        
        #先計算會不會撞到牆 然後算撞到牆後的落點修正 然後重新算斜率 然後再預測落點
        #先算低一個地圖

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_RIGHT"  
            self.old_x,self.old_y = scene_info["ball"] 
        else:
            x,y = scene_info["ball"]
            #if x == 0:
            #   print(x,y,self.old_x,self.old_y)
            if y>60 and  y - self.old_y > 0:
                if x-self.old_x != 0:
                    self.m = (y - self.old_y)/(x - self.old_x)
                    #print("m:",m)
                    if self.m > 0:      #to the right
                        #predict_y = math.floor(200*m - 5)
                        self.predict_y = math.floor((200-x)*self.m + y -5)
                        self.predict_x = 195 
                    elif self.m < 0:    #to the left
                        self.predict_x = 0
                        self.predict_y = (0-x)*self.m + y
                #if (x == 0 or x == 195):
                #    print(self.predict_x,self.predict_y,x,y,self.m)
            self.old_x = x
            self.old_y = y
           
            #print(self.predict_x,self.predict_y,x,y)
            
            if(scene_info["platform"][0] >= self.predict_x):
                command = "MOVE_LEFT"
            else:
                command = "MOVE_RIGHT"
            #print(scene_info)

        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
