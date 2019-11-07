import numpy as np
import TASK



def order():
    # Set start and end depending on dependency
    for task in TASK.my_task:
        if task.dependency != '':
            dependency = task.dependency
            for search in TASK.my_task:
                if search.name == dependency:
                    start = search.end
            task.start = start
            task.end = start + task.duration