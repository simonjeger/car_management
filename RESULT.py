import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta
import plotly.figure_factory as ff
import TASK
import ORDER
import CALENDAR


class result:
    def __init__(self):

        self.path = 'car_management/timeplan'
        os.makedirs(self.path, exist_ok=True)

        ORDER.set_date()

        self.name = []
        self.type = []
        self.date_start = []
        self.date_end = []



        for task in TASK.my_task:
            self.name = self.name + [task.name]
            self.type = self.type + [task.type]
            self.date_start = self.date_start + [task.start]
            self.date_end = self.date_end + [task.end]

        self.color = {  'eng (all_0)': (0.2, 0.2, 0.2),
                        'int (all_0)': (0.6, 0.0, 0.0),
                        'ext (all_0)': (0.0, 0.4, 0.8),
                        'eng (jag_0)': (0.4, 0.4, 0.4),
                        'int (jag_0)': (0.8, 0.0, 0.0),
                        'ext (jag_0)': (0.0, 0.6, 1.0),
                        'eng (jag_1)': (0.6, 0.6, 0.6),
                        'int (jag_1)': (1.0, 0.0, 0.0),
                        'ext (jag_1)': (0.2, 0.6, 1.0),
                        'eng (vwb_0)': (0.8, 0.8, 0.8),
                        'int (vwb_0)': (1.0, 0.2, 0.0),
                        'ext (vwb_0)': (0.6, 0.8, 1.0)
                      }

    def list(self):
        result = ''
        for task in TASK.my_task:
            result = result + str(task.start)[:10] + ' - ' + str(task.end)[:10] + ' (' + str(task.duration)[:2] + ' d): ' + task.type + ' - ' + task.name + '\n'

        #file = open("list.txt", "w", exist_ok=True)
        file = open(self.path + "/list.txt", "w")
        file.close()
        file = open(self.path + "/list.txt", "w")

        # Write file
        file = open(self.path + "/list.txt", "w")
        file.write(result)
        file.close()

    def stem(self):
        ORDER.order_stem()

        # Choose some nice level
        level_max = 20
        level_raw = np.linspace(1, level_max * 2 + 1, level_max + 1)
        level = []
        for i in level_raw:
            level = level + [i] + [-i]
        level = np.tile(level, int(np.ceil(len(self.date_end) / 3)))[:len(self.date_end)]

        # Create figure and plot a stem plot with the date_end
        fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=False)
        ax.set(title="project car")

        for i in range(len(self.date_end)):
            markerline, stemline, baseline = ax.stem([self.date_end[i]], [level[i]], basefmt="k-", use_line_collection=True)
            plt.setp(markerline, color=(self.color[self.type[i]]))
            plt.setp(stemline, color=(self.color[self.type[i]]))

        # Add the y = 0 line in the middle
        markerline, stemline, baseline = ax.stem([np.min(self.date_start), np.max(self.date_end)], [0, 0], basefmt="k-", use_line_collection=True)
        plt.setp(markerline, mec="k", mfc="w", zorder=4)
        plt.setp(baseline, mec="k", mfc="w", zorder=3)

        # Label
        font = {#'family': 'normal',
                'weight': 'normal',
                'size': 5}
        matplotlib.rc('font', **font)

        vert = np.array(['top', 'bottom'])[(level > 0).astype(int)]
        for d, l, r, va in zip(self.date_end, level, self.name, vert):
            #ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3), textcoords="offset points", va=va, ha="right")
            ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3), textcoords="offset points", va='center', ha="right")
            ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3), textcoords="offset points", va='center', ha="right")

        # Format x_axis
        #ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))  # 4 month interval
        ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%d %b %Y"))

        ax_min = np.min(self.date_start)
        ax_max = np.max(self.date_end)
        ax_delta = ax_max - ax_min
        ax_min = np.min(self.date_start) - 0.1 * ax_delta
        ax_max = np.max(self.date_end) + 0.1 * ax_delta

        ax.set_xlim([ax_min, ax_max])
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

        # Remove y axis and spines
        ax.get_yaxis().set_visible(False)
        for spine in ["left", "top", "right"]:
            ax.spines[spine].set_visible(False)

        ax.margins(y=0.1)
        plt.savefig(self.path + '/stem.png')


    def gantt(self):
        ORDER.order_type()
        df = []
        for i in range(len(self.name)):
            df = df + [dict(Task=self.name[i], Start=self.date_start[i], Finish=self.date_end[i], Resource=self.type[i])]

        fig = ff.create_gantt(df, colors=self.color, index_col='Resource', show_colorbar=True)
        fig.show()

my_result = result()
my_result.list()
my_result.stem()
my_result.gantt()
