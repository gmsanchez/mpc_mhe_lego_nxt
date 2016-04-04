import matplotlib
font = {'size': 9}
matplotlib.rc('font', **font)
import matplotlib.pyplot as plt
import numpy as np
import csv

data_idx = {'t': 0, 'ul': 1, 'ur': 2, 'battery': 3, 'mot_l': 4, 'mot_r': 5, 'ax': 6, 'ay': 7, 'az': 8,
                         'gyro': 9, 'compass': 10, 'not_used_01': 11, 'sonar': 12}


class DataScaler():
    def __init__(self, data_dim):
        self.data = np.zeros(data_dim)
        self.compass_log = np.zeros(10)

    def update(self, _data):
        _data = _data.astype(float, copy=True)
        deg2rad = np.pi/180.0
        cm2mm = 10.0
        acc_scale = (9.81*1000.0)/200.0

        _data[[6, 7, 8]] *= acc_scale
        _data[[4, 5, 9, 10]] *= deg2rad
        _data[[12]] *= cm2mm

        unwrapped_compass_meas = self.unwrap_compass(_data[10])
        _data[10] = unwrapped_compass_meas

        self.data = _data

    def unwrap_compass(self, data):
        # print "unwrap: ", data
        self.compass_log = np.roll(self.compass_log, -1)
        self.compass_log[-1] = data
        self.compass_log = np.unwrap(self.compass_log, 0)
        return self.compass_log[-1]

    def get_scaled_data(self):
        return self.data

    def get_plot_data(self):
        return self.data[:, [0, 1, 2, 4, 5, 6, 7, 9, 10, 12]]


class DataLogger():
    def __init__(self, nsamples, data_dim):
        self.nsamples = nsamples
        if self.nsamples == 0:
            self.data = np.zeros((1, data_dim))
        else:
            self.data = np.zeros((self.nsamples, data_dim))
        self.csv_header = ["t", "ul", "ur", "battery", "mot_l", "mot_r", "ax", "ay", "az", "gyro", "compass", "none", "sonar"]
        self.data_scaler = DataScaler(data_dim)

    def update(self, newdata):
        # self.data_scaler.update(newdata)
        # self.data[-1] = self.data_scaler.get_scaled_data()
        if self.nsamples == 0:
            self.data = np.append(self.data, newdata, axis=0)
        else:
            self.data = np.roll(self.data, -1, axis=0)
            self.data[-1] = newdata

    def get_data(self):
        return self.data

    def get_plot_data(self):
        """ Return data ready for plotting. """
        return self.data[:, [0, 1, 2, 4, 5, 6, 7, 9, 10, 12]]

    def save_csv(self, file_name):
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.csv_header)
            writer.writerows(self.data)


class BlitPlotter():

    def __init__(self, numsamples, datadim):

        self.datalogger = DataLogger(numsamples, datadim)

        self.t = np.arange(0, numsamples)

        self.f = plt.figure(num = 0, figsize = (12, 8))#, dpi = 100)
        self.f.suptitle("NXT Viewer", fontsize=12)

        self.ax00 = plt.subplot2grid((5, 3), (0, 0), rowspan=3, colspan=2)
        self.ax30 = plt.subplot2grid((5, 3), (3, 0))
        self.ax31 = plt.subplot2grid((5, 3), (3, 1))
        self.ax40 = plt.subplot2grid((5, 3), (4, 0))
        self.ax41 = plt.subplot2grid((5, 3), (4, 1))
        self.ax02 = plt.subplot2grid((5, 3), (0, 2))
        self.ax12 = plt.subplot2grid((5, 3), (1, 2))
        self.ax22 = plt.subplot2grid((5, 3), (2, 2))
        self.ax32 = plt.subplot2grid((5, 3), (3, 2))
        self.ax42 = plt.subplot2grid((5, 3), (4, 2))
        # self.ax42 = plt.subplot2grid((5, 3), (4, 2), xlim=(0, 500), ylim=(-1.0, 1.0), autoscale_on=False)

        self.line_axes = [self.ax30,  self.ax40, self.ax31, self.ax41, self.ax02,
                          self.ax12, self.ax22, self.ax32, self.ax42]

        for ax in self.line_axes:
            ax.set_xlim(0, numsamples)
            # ax.get_xaxis().set_animated(True)
            # ax.get_yaxis().set_animated(True)

        plt.ion()
        plt.show(False)
        self.f.canvas.draw()

        # self.mot_l = np.zeros(500)
        self.l30, = self.ax30.plot([], [], 'r-', label="mot_l")
        self.l31, = self.ax31.plot([], [], 'g-', label="u_l")
        self.l40, = self.ax40.plot([], [], 'b-', label="mot_r")
        self.l41, = self.ax41.plot([], [], 'b-', label="u_r")
        self.l02, = self.ax02.plot([], [], 'b-', label="ax")
        self.l12, = self.ax12.plot([], [], 'b-', label="ay")
        self.l22, = self.ax22.plot([], [], 'b-', label="gyro")
        self.l32, = self.ax32.plot([], [], 'b-', label="compass")
        self.l42, = self.ax42.plot([], [], 'b-', label="sonar")

        self.lines = [self.l30, self.l40, self.l31, self.l41, self.l02,
                          self.l12, self.l22, self.l32, self.l42]

        for line in self.lines:
            # line.axes.set_xlim(0,500)
            line.set_data(self.t, np.zeros(numsamples))

        # self.lines = [ax.plot([], [], 'b-', label="mot_l", styleanimated=True)[0] for ax in self.line_axes]

        self.line_backgrounds = [self.f.canvas.copy_from_bbox(ax.bbox) for ax in self.line_axes]


        # self.line_backgrounds = [self.f.canvas.copy_from_bbox(ax.get_figure().bbox) for ax in self.line_axes]

    def update_plot(self, plot_data):
        items = enumerate(zip(self.lines, self.line_axes, self.line_backgrounds), start=1)
        for j, (line, ax, background) in items:
            self.f.canvas.restore_region(background)

            ymax = np.max(plot_data[:, j])
            ymin = np.min(plot_data[:, j])
            # line.set_data(self.t, plot_data[:, j])
            line.set_ydata(plot_data[:, j])
            line.axes.set_ylim(ymin-1, ymax+1)

            ax.draw_artist(line)
            # ax.draw_artist(ax.get_xaxis())
            # ax.draw_artist(ax.get_yaxis())
            #
            self.f.canvas.blit(ax.bbox)
            # self.f.canvas.blit(ax.clipbox)

    def update(self, data):
        self.datalogger.update(data)
        plot_data = self.datalogger.get_plot_data()

        # self.f.canvas.restore_region(self.line_backgrounds[0])
        # self.mot_l = np.roll(self.mot_l, -1)
        # self.mot_l[-1] = data
        # self.l30.axes.set_xlim(0, 500)
        # self.l30.axes.set_ylim(-1, 1)
        # self.l30.set_data(t, self.mot_l)
        # self.ax30.draw_artist(self.l30)
        # self.ax30.draw_artist(self.ax30.get_xaxis())
        # self.ax30.draw_artist(self.ax30.get_yaxis())
        #
        # # self.f.canvas.blit(self.ax30.bbox)
        # self.f.canvas.blit(self.ax30.clipbox)

        # data_idx = [0, 4, 5, ]

        items = enumerate(zip(self.lines, self.line_axes, self.line_backgrounds), start=1)
        for j, (line, ax, background) in items:
            self.f.canvas.restore_region(background)

            ymax = np.max(plot_data[:, j])
            ymin = np.min(plot_data[:, j])
            # line.set_data(self.t, plot_data[:, j])
            line.set_ydata(plot_data[:, j])
            line.axes.set_ylim(ymin-1, ymax+1)

            ax.draw_artist(line)
            # ax.draw_artist(ax.get_xaxis())
            # ax.draw_artist(ax.get_yaxis())
            #
            # self.f.canvas.blit(ax.bbox)
            self.f.canvas.blit(ax.clipbox)

#
# for j, line in enumerate(lines, start=1):
#         ymax = np.max(data[:, j])
#         ymin = np.min(data[:, j])
#         line.set_data(np.arange(0, NUM_SAMPLES), data[:, j])
#         line.axes.set_ylim(ymin-1, ymax+1)


    def ion(self):
        plt.ion()

    def show(self):
        plt.show()
