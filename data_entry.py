class DataEntry:
    time = 0
    curr_speed = 0
    dir = 0

    def __init__(self, time, curr_speed, dir):
        self.time = time
        self.curr_speed = curr_speed
        self.dir = dir

    def get_time(self):
        return self.time
    
    def get_curr_speed(self):
        return self.curr_speed

    def get_dir(self):
        return self.dir