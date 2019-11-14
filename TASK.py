from datetime import datetime
from datetime import timedelta



class task:

    def __init__(self, name, type, start, duration, deadline, reserve_margin, responsible, dependency, dependency_type):

        # Initialize
        self.name = name
        self.type = type
        self.duration = timedelta(days = duration)
        if start != '':
            self.start = datetime.strptime(start, "%Y-%m-%d")
            self.end = self.start + self.duration
        else:
            self.start = 0
            self.end = 0
        self.reserve = timedelta(days = duration * reserve_margin)
        self.deadline = deadline
        self.responsible = responsible
        self.dependency = dependency
        if dependency_type == '':
            self.dependency_type = type[5:10]
        else:
            self.dependency_type = dependency_type
        self.percentage = 0

    def progress(self, percentage):
        self.percentage = percentage



my_task = []

# Pre start
my_task = my_task + [task('kaufen', 'ext (jag_0)', '2019-08-21', 82, '', 0, '', '', '')]
my_task = my_task + [task('kaufen', 'ext (jag_1)', '2019-12-05', 82, '', 0, '', '', '')]
my_task = my_task + [task('vorführen', 'ext (jag_0)', '', 10, '', 0.1, '', 'kaufen', '')]
my_task = my_task + [task('vorführen', 'ext (jag_1)', '', 10, '', 0.1, '', 'kaufen', '')]

# Start intern
my_task = my_task + [task('Motor ausbauen', 'ext (jag_0)', '', 10, '', 0.1, '', 'vorführen', '')]
my_task = my_task + [task('Motor ausbauen', 'ext (jag_1)', '', 10, '', 0.1, '', 'vorführen', '')]
my_task = my_task + [task('Motor ausbauen', 'int (vwb_0)', '2019-11-20', 10, '', 0.1, '', '', '')]
my_task = my_task + [task('transportieren', 'int (jag_0)', '', 1, '', 0.1, '', 'Motor ausbauen', '')]
my_task = my_task + [task('transportieren', 'int (jag_1)', '', 1, '', 0.1, '', 'Motor ausbauen', '')]
my_task = my_task + [task('Tank ausbauen', 'int (jag_0)', '', 2, '', 0.1, '', 'transportieren', '')]
my_task = my_task + [task('Tank ausbauen', 'int (jag_1)', '', 2, '', 0.1, '', 'transportieren', '')]
my_task = my_task + [task('Tank ausbauen', 'int (vwb_0)', '', 2, '', 0.1, '', 'Tank ausbauen', 'jag_0')]
my_task = my_task + [task('Chassis putzen', 'int (jag_0)', '', 7, '', 0.1, '', 'Tank ausbauen', 'vwb_0')]
my_task = my_task + [task('Chassis putzen', 'int (jag_1)', '', 7, '', 0.1, '', 'Tank ausbauen', '')]
my_task = my_task + [task('Chassis putzen', 'int (vwb_0)', '', 7, '', 0.1, '', 'Chassis putzen', 'jag_0')]

# Start engineering
my_task = my_task + [task('Scannen & overall CAD', 'eng (all_0)', '', 10, '', 0.1, '', 'Tank ausbauen', 'jag_0')]
my_task = my_task + [task('Batterien auswählen & detailed CAD', 'eng (all_0)', '', 7, '', 0.1, '', 'Scannen & overall CAD', '')]
my_task = my_task + [task('Antriebsstrang kaufen', 'ext (all_0)', '', 30, '', 0.1, '', 'Batterien auswählen & detailed CAD', '')]

# After winterbreak
my_task = my_task + [task('Motorentest', 'int (all_0)', '2020-02-20', 3, '', 0.1, '', '', '')]
my_task = my_task + [task('Batteriegehäuse zeichnen', 'eng (all_0)', '', 7, '', 0.1, '', 'Motorentest', '')]
my_task = my_task + [task('Batteriegehäuse kaufen', 'ext (all_0)', '', 30, '', 0.1, '', 'Batteriegehäuse zeichnen', '')]
my_task = my_task + [task('Batterie & Gehäuse einbauen', 'int (jag_0)', '', 5, '', 0.1, '', 'Batteriegehäuse kaufen', 'all_0')]
my_task = my_task + [task('Batterie & Gehäuse einbauen', 'int (jag_1)', '', 5, '', 0.1, '', 'Batterie & Gehäuse einbauen', 'jag_0')]
my_task = my_task + [task('Batterie & Gehäuse einbauen', 'int (vwb_0)', '', 5, '', 0.1, '', 'Batterie & Gehäuse einbauen', 'jag_1')]
my_task = my_task + [task('Flansch zeichnen', 'eng (all_0)', '', 5, '', 0.1, '', 'Batteriegehäuse zeichnen', '')]
my_task = my_task + [task('Flansch kaufen', 'ext (all_0)', '', 30, '', 0.1, '', 'Flansch zeichnen', '')]
my_task = my_task + [task('Motor & Flansch einbauen', 'int (jag_0)', '', 5, '', 0.1, '', 'Batterie & Gehäuse einbauen', 'vwb_0')]
my_task = my_task + [task('Motor & Flansch einbauen', 'int (jag_1)', '', 5, '', 0.1, '', 'Motor & Flansch einbauen', 'jag_0')]
my_task = my_task + [task('Motor & Flansch einbauen', 'int (vwb_0)', '', 5, '', 0.1, '', 'Motor & Flansch einbauen', 'jag_1')]

# Final
my_task = my_task + [task('Research Heizung', 'eng (all_0)', '', 3, '', 0.1, '', 'Motor & Flansch einbauen', 'vwb_0')]
my_task = my_task + [task('Heizung kaufen', 'ext (all_0)', '', 30, '', 0.1, '', 'Research Heizung', '')]
my_task = my_task + [task('Research Licht', 'eng (all_0)', '', 3, '', 0.1, '', 'Research Heizung', '')]
my_task = my_task + [task('Licht kaufen', 'ext (all_0)', '', 30, '', 0.1, '', 'Research Licht', '')]
my_task = my_task + [task('Kabel ziehen', 'int (jag_0)', '', 5, '', 0.1, '', 'Research Licht', 'all_0')]
my_task = my_task + [task('Kabel ziehen', 'int (jag_1)', '', 5, '', 0.1, '', 'Kabel ziehen', 'jag_0')]
my_task = my_task + [task('Kabel ziehen', 'int (vwb_0)', '', 5, '', 0.1, '', 'Kabel ziehen', 'jag_1')]
my_task = my_task + [task('Probefahrt', 'int (jag_0)', '', 5, '', 0.1, '', 'Kabel ziehen', 'vwb_0')]
my_task = my_task + [task('Probefahrt', 'int (jag_1)', '', 5, '', 0.1, '', 'Probefahrt', 'jag_0')]
my_task = my_task + [task('Probefahrt', 'int (vwb_0)', '', 5, '', 0.1, '', 'Probefahrt', 'jag_1')]

# Details
my_task = my_task + [task('Heizung einbauen', 'int (jag_0)', '', 5, '', 0.1, '', 'Heizung kaufen', 'all_0')]
my_task = my_task + [task('Heizung einbauen', 'int (jag_1)', '', 5, '', 0.1, '', 'Heizung einbauen', 'jag_0')]
my_task = my_task + [task('Heizung einbauen', 'int (vwb_0)', '', 5, '', 0.1, '', 'Heizung einbauen', 'jag_1')]
my_task = my_task + [task('Licht einbauen', 'int (jag_0)', '', 5, '', 0.1, '', 'Heizung einbauen', 'vwb_0')]
my_task = my_task + [task('Licht einbauen', 'int (jag_1)', '', 5, '', 0.1, '', 'Licht einbauen', 'jag_0')]

# Finish
my_task = my_task + [task('vorführen', 'ext (all_0)', '', 30, '', 0.1, '', 'Licht einbauen', 'jag_1')]