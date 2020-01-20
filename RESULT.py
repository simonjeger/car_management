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

        ORDER.set_date_day()

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
        for my_task in TASK.my_task:
            result = result + str(my_task.start)[:10] + ' - ' + str(my_task.end)[:10] + ' (' + str(my_task.duration)[:2] + ' d): ' + my_task.type + ' - ' + my_task.name + '\n'

        #file = open("list.txt", "w", exist_ok=True)
        file = open(self.path + "/list.txt", "w")
        file.close()
        file = open(self.path + "/list.txt", "w")

        # Write file
        file = open(self.path + "/list.txt", "w")
        file.write(result)
        file.close()

    def stem(self):
        task = ORDER.order_end()

        name = []
        type = []
        date_start = []
        date_end = []

        for my_task in task:
            name = name + [my_task.name]
            type = type + [my_task.type]
            date_start = date_start + [my_task.start]
            date_end = date_end + [my_task.end]

        # Choose some nice level
        level_max = 30
        level_raw = np.linspace(1, level_max * 2 + 1, level_max + 1)
        level = []
        for i in level_raw:
            level = level + [i] + [-i]
        level = np.tile(level, int(np.ceil(len(date_end) / 3)))[:len(date_end)]

        # Create figure and plot a stem plot with the date_end
        fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=False)
        ax.set(title="project_car deadlines")

        for i in range(len(date_end)):
            markerline, stemline, baseline = ax.stem([date_end[i]], [level[i]], basefmt="k-", use_line_collection=True)
            plt.setp(markerline, color=(self.color[type[i]]))
            plt.setp(stemline, color=(self.color[type[i]]))

        # Add the y = 0 line in the middle
        markerline, stemline, baseline = ax.stem([np.min(date_start), np.max(date_end)], [0, 0], basefmt="k-", use_line_collection=True)
        plt.setp(markerline, mec="k", mfc="w", zorder=4)
        plt.setp(baseline, mec="k", mfc="w", zorder=3)

        # Label
        font = {#'family': 'normal',
                'weight': 'normal',
                'size': 4}
        matplotlib.rc('font', **font)

        vert = np.array(['top', 'bottom'])[(level > 0).astype(int)]
        for d, l, r, va in zip(date_end, level, name, vert):
            #ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3), textcoords="offset points", va=va, ha="right")
            ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3), textcoords="offset points", va='center', ha="right")
            ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3), textcoords="offset points", va='center', ha="right")

        # Format x_axis
        #ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))  # 4 month interval
        ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%d %b %Y"))

        ax_min = np.min(date_start)
        ax_max = np.max(date_end)
        ax_delta = ax_max - ax_min
        ax_min = np.min(date_start) - 0.1 * ax_delta
        ax_max = np.max(date_end) + 0.1 * ax_delta

        ax.set_xlim([ax_min, ax_max])
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        plt.gcf().subplots_adjust(bottom=0.25)

        # Remove y axis and spines
        ax.get_yaxis().set_visible(False)
        for spine in ["left", "top", "right"]:
            ax.spines[spine].set_visible(False)

        ax.margins(y=0.1)
        plt.savefig(self.path + '/stem.png')


    def gantt(self):
        #task = ORDER.order_start()
        task = TASK.my_task

        df = []
        for i in range(len(task)):
            df = df + [dict(Task=task[i].name, Start=task[i].start, Finish=task[i].end, Resource=task[i].type)]

        fig = ff.create_gantt(df, colors=self.color, index_col='Resource', show_colorbar=True)
        fig.show()

my_result = result()
my_result.list()
my_result.stem()
my_result.gantt()