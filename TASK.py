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
my_task = my_task + [task('kaufen', 'ext (jag_1)', '2019-11-25', 82, '', 0, '', '', '')]
my_task = my_task + [task('vorführen', 'ext (jag_0)', '', 30, '', 0.1, '', 'kaufen', '')]
my_task = my_task + [task('vorführen', 'ext (jag_1)', '', 30, '', 0.1, '', 'kaufen', '')]

# Start
my_task = my_task + [task('Motor kaufen', 'ext (all_0)', '2019-11-22', 30, '', 0.1, '', '', '')]
my_task = my_task + [task('Motor, Tank ect. ausbauen', 'ext (jag_0)', '', 2, '', 0.1, '', 'vorführen', '')]
my_task = my_task + [task('Motor, Tank ect. ausbauen', 'ext (jag_1)', '', 2, '', 0.1, '', 'vorführen', '')]
my_task = my_task + [task('Motor, Tank ect. ausbauen', 'int (vwb_0)', '2019-11-20', 1, '', 0.1, '', '', '')]
my_task = my_task + [task('transportieren & Chassis waschen', 'int (jag_0)', '', 1, '', 0.1, '', 'Motor, Tank ect. ausbauen', '')]
my_task = my_task + [task('transportieren & Chassis waschen', 'int (jag_1)', '', 1, '', 0.1, '', 'Motor, Tank ect. ausbauen', '')]
my_task = my_task + [task('Flansch (& Halterung) zeichnen', 'eng (all_0)', '', 4, '', 0.1, '', 'Motor kaufen', 'all_0')]
my_task = my_task + [task('Flansch (& Halterung) kaufen', 'ext (all_0)', '', 30, '', 0.1, '', 'Flansch (& Halterung) zeichnen', '')]

# Nach Prüfungsphase
my_task = my_task + [task('Motor (& Halterung) & Flansch einbauen', 'int (all_0)', '2020-02-17', 1, '', 0.1, '', '', '')]
my_task = my_task + [task('Batterienauswahl', 'eng (all_0)', '', 1, '', 0.1, '', 'Motor (& Halterung) & Flansch einbauen', '')]
my_task = my_task + [task('Batteriegehäuse zeichnen', 'eng (all_0)', '', 7, '', 0.1, '', 'Batterienauswahl', '')]
my_task = my_task + [task('Batteriegehäuse kaufen', 'ext (all_0)', '', 30, '', 0.1, '', 'Batteriegehäuse zeichnen', '')]
my_task = my_task + [task('Kabellänge bestimmen', 'eng (all_0)', '', 3, '', 0.1, '', 'Batteriegehäuse zeichnen', '')]
my_task = my_task + [task('Batterien & Kabel kaufen', 'eng (all_0)', '', 30, '', 0.1, '', 'Kabellänge bestimmen', '')]
my_task = my_task + [task('Research Heizung', 'eng (all_0)', '', 1, '', 0.1, '', 'Kabellänge bestimmen', 'vwb_0')]
my_task = my_task + [task('Heizung kaufen', 'ext (all_0)', '', 30, '', 0.1, '', 'Research Heizung', '')]
my_task = my_task + [task('Research Licht', 'eng (all_0)', '', 1, '', 0.1, '', 'Research Heizung', '')]
my_task = my_task + [task('Licht kaufen', 'ext (all_0)', '', 30, '', 0.1, '', 'Research Licht', '')]
my_task = my_task + [task('Batterie, Kabel & Gehäuse einbauen', 'int (all_0)', '', 5, '', 0.1, '', 'Batterien & Kabel kaufen', '')]
my_task = my_task + [task('Probefahrt', 'int (all_0)', '', 1, '', 0.1, '', 'Batterie, Kabel & Gehäuse einbauen', '')]
my_task = my_task + [task('Heizung einbauen', 'int (all_0)', '', 1, '', 0.1, '', 'Batterie, Kabel & Gehäuse einbauen', '')]
my_task = my_task + [task('Licht einbauen', 'int (all_0)', '', 1, '', 0.1, '', 'Heizung einbauen', '')]

# Details
my_task = my_task + [task('Reserve', 'int (all_0)', '', 50, '', 0.1, '', 'Licht einbauen', '')]
my_task = my_task + [task('vorführen', 'ext (all_0)', '', 1, '', 0.1, '', 'Reserve', '')]