import numpy as np
import operator
import TASK



def set_date():
    # Set start and end depending on dependency
    for task in TASK.my_task:
        if task.dependency != '':
            dependency = task.dependency
            for predecessor in TASK.my_task:
                if (predecessor.name == dependency) & (predecessor.type[5:10] == task.dependency_type):
                    start = predecessor.end + predecessor.reserve
            task.start = start
            task.end = task.start + task.duration

def order_stem():
    TASK.my_task.sort(key=operator.attrgetter('end'))

def order_type():
    # Reverse order for Gantt chart
    TASK.my_task.reverse()

    # Group in terms of task
    result_all_0_intern = []
    result_all_0_extern = []
    result_all_0_engineering = []
    result_jag_0_intern = []
    result_jag_0_extern = []
    result_jag_0_engineering = []
    result_jag_1_intern = []
    result_jag_1_extern = []
    result_jag_1_engineering = []
    for task in TASK.my_task:
        if task.type == 'eng (all_0)':
            result_all_0_engineering = result_all_0_engineering + [task]
        if task.type == 'int (all_0)':
            result_all_0_intern = result_all_0_intern + [task]
        if task.type == 'ext (all_0)':
            result_all_0_extern = result_all_0_extern + [task]
        if task.type == 'eng (jag_0)':
            result_jag_0_engineering = result_jag_0_engineering + [task]
        if task.type == 'int (jag_0)':
            result_jag_0_intern = result_jag_0_intern + [task]
        if task.type == 'ext (jag_0)':
            result_jag_0_extern = result_jag_0_extern + [task]
        if task.type == 'eng (jag_1)':
            result_jag_1_engineering = result_jag_1_engineering + [task]
        if task.type == 'int (jag_1)':
            result_jag_1_intern = result_jag_1_intern + [task]
        if task.type == 'ext (jag_1)':
            result_jag_1_extern = result_jag_1_extern + [task]
        if task.type == 'eng (vwb_0)':
            result_jag_0_engineering = result_jag_0_engineering + [task]
        if task.type == 'int (vwb_0)':
            result_jag_0_intern = result_jag_0_intern + [task]
        if task.type == 'ext (vwb_0)':
            result_jag_0_extern = result_jag_0_extern + [task]

    TASK.my_task = result_all_0_intern + result_all_0_extern + result_all_0_engineering + result_jag_0_intern + result_jag_0_extern + result_jag_0_engineering + result_jag_1_intern + result_jag_1_extern + result_jag_1_engineering