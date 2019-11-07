from datetime import datetime
from datetime import timedelta



class task:

    def __init__(self, name, type, start, duration, deadline, responsible, dependency):

        # Initialize
        self.name = name
        self.type = type
        self.duration = timedelta(days=duration)
        if start != '':
            self.start = datetime.strptime(start, "%Y-%m-%d")
            self.end = self.start + self.duration
        else:
            self.start = 0
            self.end = 0
        self.deadline = deadline
        self.responsible = responsible
        self.dependency = dependency
        self.percentage = 0

    def progress(self, percentage):
        self.percentage = percentage



my_task = []
my_task = my_task + [task('order jaguar', 'buying', '2019-08-21', 64, '', 'Felix', '')]
my_task = my_task + [task('take measurements', 'working', '', 1, '', 'Andreas', 'order jaguar')]
my_task = my_task + [task('order drive train', 'buying', '', 2, '', 'Simon', 'take measurements')]