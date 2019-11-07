import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import TASK
import ORDER
import CALENDAR



class timeline:

    def __init__(self):

        ORDER.order()
        name = []
        for task in TASK.my_task:
            name = name + [task.name]

        date_start = []
        for task in TASK.my_task:
            date_start = date_start + [task.start]

        date_end = []
        for task in TASK.my_task:
            date_end = date_end + [task.end]

        # Convert date_end strings (e.g. 2014-10-18) to datetime
        #date_end = [datetime.strptime(d, "%Y-%m-%d") for d in date_end]

        # Choose some nice levels
        levels = np.tile([1, 3, 5],
                         int(np.ceil(len(date_end) / 3)))[:len(date_end)]

        # Create figure and plot a stem plot with the date_end
        fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
        ax.set(title="project car")

        markerline, stemline, baseline = ax.stem(date_start, levels, linefmt="C3-", basefmt="k-", use_line_collection=True)
        markerline, stemline, baseline = ax.stem(date_end, levels, linefmt="C3-", basefmt="k-", use_line_collection=True)

        plt.setp(markerline, mec="k", mfc="w", zorder=3)

        # Shift the markers to the baseline by replacing the y-data by zeros.
        markerline.set_ydata(np.zeros(len(date_end)))

        # annotate lines
        vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
        for d, l, r, va in zip(date_end, levels, name, vert):
            ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3), textcoords="offset points", va=va, ha="right")

        # format xaxis with 4 month intervals
        #ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))
        ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%d %b %Y"))
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

        # remove y axis and spines
        ax.get_yaxis().set_visible(False)
        for spine in ["left", "top", "right"]:
            ax.spines[spine].set_visible(False)

        ax.margins(y=0.1)
        plt.show()


my_timeline = timeline()