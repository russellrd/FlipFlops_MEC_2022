class DataEntry:
    time = 0
    curr_vel = 0
    dir = 0

    def __init__(self, time, curr_vel, dir):
        self.time = time
        self.curr_vel = curr_vel
        self.dir = dir

    def get_time(self):
        return self.time
    
    def get_curr_vel(self):
        return self.curr_vel

    def get_dir(self):
        return self.dir