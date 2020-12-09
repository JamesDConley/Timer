import time
import logging

# Setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Timer:
    def __init__(self, log=True):
        self.log = log
    def start(self, task='Unnamed Task'):
        """Starts the timer .

        Args:
            task (str, optional): Name of the task to use for logging. Defaults to 'Unnamed Task'.
        """
        self.laps = []
        self.lap_diffs = []
        self.total_tile = 0
        self.start_time = time.time()
        self.task = task
        if self.log:
            logger.info(f"{self.task} started")
    def lap(self):
        #TODO : WIP
        now = time.time()
        # Get the time since last lap
        if len(self.laps) == 0:
            time_since_last_lap = now - self.start_time
        else:
            time_since_last_lap = now - self.laps[-1]
        self.laps.append(now)
        self.lap_diffs.append(time_since_last_lap)
    
    def stop(self):
        """Stops returns the time elapsed since timer was last started, logging the time if self.log is True .

        Returns:
            float: seconds elapsed since last timer start
        """
        self.total_time = time.time() - self.start_time
        if self.total_time > 3600:
            units = 'hours'
            divisor = 3600
        elif self.total_time > 60:
            units = 'minutes'
            divisor = 60
        else:
            units = 'seconds'
            divisor = 1
        if log:
            logger.info(f"{self.task} finished after {round(self.total_time/divisor, 2)} {units}")
        return self.total_time
    
