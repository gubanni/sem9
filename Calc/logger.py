from datetime import datetime as dt
from time import time

def calc_logger(data):
    time = dt.now().strftime('%D. %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; {}\n'
                    .format(time, data))