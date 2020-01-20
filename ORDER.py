import numpy as np
import copy
import operator
import TASK



def set_date_day():
    # Set start and end depending on dependency
    for task in TASK.my_task:
        if task.dependency != '':
            dependency = task.dependency
            for predecessor in TASK.my_task:
                if (predecessor.name == dependency) & (predecessor.type[5:10] == task.dependency_type):
                    start = predecessor.end + predecessor.reserve
            print(task.name)
            task.start = start
            task.end = task.start + task.duration

def set_date_week():
    # Set start and end depending on dependency
    for task in TASK.my_task:
        if task.dependency != '':
            dependency = task.dependency
            for predecessor in TASK.my_task:
                if (predecessor.name == dependency) & (predecessor.type[5:10] == task.dependency_type):
                    start = predecessor.end + predecessor.reserve
            task.start = start
            task.end = task.start + task.duration

def order_start():
    task = copy.deepcopy(TASK.my_task)
    task.sort(key=operator.attrgetter('start'))
    return task

def order_end():
    task = copy.deepcopy(TASK.my_task)
    task.sort(key=operator.attrgetter('end'))
    return task

def order_type():
    task = copy.deepcopy(TASK.my_task)

    # Reverse order for Gantt chart
    task.reverse()

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
    for my_task in result:
        if my_task.type == 'eng (all_0)':
            result_all_0_engineering = result_all_0_engineering + [task]
        if my_task.type == 'int (all_0)':
            result_all_0_intern = result_all_0_intern + [task]
        if my_task.type == 'ext (all_0)':
            result_all_0_extern = result_all_0_extern + [task]
        if my_task.type == 'eng (jag_0)':
            result_jag_0_engineering = result_jag_0_engineering + [task]
        if my_task.type == 'int (jag_0)':
            result_jag_0_intern = result_jag_0_intern + [task]
        if my_task.type == 'ext (jag_0)':
            result_jag_0_extern = result_jag_0_extern + [task]
        if my_task.type == 'eng (jag_1)':
            result_jag_1_engineering = result_jag_1_engineering + [task]
        if my_task.type == 'int (jag_1)':
            result_jag_1_intern = result_jag_1_intern + [task]
        if my_task.type == 'ext (jag_1)':
            result_jag_1_extern = result_jag_1_extern + [task]
        if my_task.type == 'eng (vwb_0)':
            result_jag_0_engineering = result_jag_0_engineering + [task]
        if my_task.type == 'int (vwb_0)':
            result_jag_0_intern = result_jag_0_intern + [task]
        if my_task.type == 'ext (vwb_0)':
            result_jag_0_extern = result_jag_0_extern + [task]

    result = result_all_0_intern + result_all_0_extern + result_all_0_engineering + result_jag_0_intern + result_jag_0_extern + result_jag_0_engineering + result_jag_1_intern + result_jag_1_extern + result_jag_1_engineering
    return result