# -*- coding: utf-8 -*-
"""
Created on Thu Apr 03 15:50:12 2014

@author: hannah
"""
import datetime
import numpy as np
import scipy.stats as st

from matplotlib import figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


DCOLOR = "#336699"
def run_sequence_plot(ax, dates, data):
    xt = [d for d in dates if d.month==1 and d.day==1 and d.year%2==0]
    years = [d for d in dates if d.month==1 and d.day == 1 and d.year%2==0]
    ax.set_title("Run Sequence Plot")
    ax.set_ylabel('Precipitation')
    ax.vlines(years, data.min(), data.max(),
              linestyle=':', linewidth=1, color='grey')
    ax.plot(dates, data,'-',
                 linewidth=3, color=DCOLOR)
    print years
    yrtk = [d for d in years]
    ax.set_xticks(yrtk)
    yrlabs = [y.strftime('%Y') for y in yrtk]
    ax.set_xticklabels(yrlabs, weight='ultralight')

    ax.set_ylim((data.min(), data.max()))
    ax.autoscale(tight=True)
    return

def lag_plot(ax, data):
    ax.set_title("Lag Plot")

    print data[1:].shape, data[:-1].shape
    ax.scatter(data[1:], data[0:-1], color=DCOLOR,
               edgecolor='k', s=50)
    ax.grid(True)
    ax.set_ylim(data.min(), data.max())
    ax.set_xlim(data.min(), data.max())
    ax.set_ylabel('Precipitation(t+1)')
    ax.set_xlabel('Precipitation(t)')
    return

def histogram(ax,data):
    ax.set_title("Histogram")
    ax.set_xlabel('Precipitation')
    ax.set_ylabel('Number of Observations')
    sp = 3
    _, bins = np.histogram(data)
    ax.hist(data, color=DCOLOR, edgecolor='k',
            range=(bins[0], bins[sp]))
    ax.set_xlim((bins[0], bins[sp]))
    return

def norm_prob(ax,data):
    ax.set_title("Normal Probability Plot")
    y = np.sort(data)
    x = st.norm.pdf(y)
    ax.set_ylabel("Ordered Precipitation")
    ax.set_xlabel("N(0,1) Stat Medians")
    ax.scatter(x,y, color=DCOLOR, marker='x', s=50)
    ax.set_xlim((x.min(), x.max()))
    ax.set_ylim((y.min(), y.max()))

def four_plot(dates, values):
    fig = figure.Figure(figsize=(30,30))
    canvas = FigureCanvas(fig)
    #fig.suptitle("Precipitation in \n the Amazon River Delta")
    ax1 = fig.add_subplot(2,2,1)
    run_sequence_plot(ax1, dates, values)
    ax2 = fig.add_subplot(2,2,2)
    lag_plot(ax2, values)
    ax3 = fig.add_subplot(2,2,3)
    histogram(ax3, values)
    ax4 = fig.add_subplot(2,2,4)
    norm_prob(ax4, values)
    fig.tight_layout()
    canvas.print_figure('figures/fplot.png', bbox_inches='tight', pad_inches=0.1)



if __name__ == '__main__':
    ndays = 1000
    index = [datetime.datetime.today() - datetime.timedelta(days=n) for n in range(ndays)][::-1]
    values = np.random.rand((ndays))
    runseq= ['runseq', run_sequence_plot, [index, values]]
    lag = ['lag', lag_plot, [values]]
    hist = ['hist', histogram, [values]]
    norm = ['norm', norm_prob, [values]]
    runs = [runseq, lag, hist, norm]
    for (fn, f, args) in runs:
        if 'runseq' in fn:
            fg = (12,4)
        else:
            fg = (12,12)
        fig = figure.Figure(figsize=fg)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(1,1,1)
        f(ax, *args)
        canvas.print_figure("figures/fourplot_{}.png".format(fn),
		                     bbox_inches='tight', pad_inches=0.1)

    four_plot(index, values)
