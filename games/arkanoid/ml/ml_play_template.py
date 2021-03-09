"""
The template of the main script of the machine learning process
"""
import math

class MLPlay:
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

        old_x = 0
        old_y = 0 
        m = 0
        predict_x = 0
        predict_y = 0
        #先計算會不會撞到牆 然後算撞到牆後的落點修正 然後重新算斜率 然後再預測落點
        #先算低一個地圖

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_RIGHT"
            old_x,old_y = scene_info["ball"] 
        else:
            x,y = scene_info["ball"]
            if y>60 :
                if x-old_x != 0:
                    m = (y - old_y)/(x - old_x)
                    #3/4 斜率不知為啥一直是正的
                    if m > 0:      #to the right
                        #predict_y = math.floor(200*m - 5)
                        predict_y = math.floor((200-x)*m + y -5)
                        predict_x = 195 
                    elif m < 0:    #to rhe left
                        print("hello")
                        predict_x = 0
                        predict_y = (-x)*m + y -5
            old_x = x
            old_y = y
            if x >= 195 or x ==0:
               print(predict_y,y,predict_x,x)
            #print(old_x,old_y,x,y,m)
            #print(x)
            
            command = "MOVE_LEFT"
            #print(scene_info)

        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
