import numpy as np
import math


class Node:
    signal_type = -1
    signal_time = -1
    fid = -1
    x = 0
    y = 0

    def __init__(self, stype, stime, fid, x, y):
        self.signal_time = stime
        self.signal_type = stype
        self.fid = fid
        self.x = x
        self.y = y


class FingerprintSequence:
    category = 0
    signal_type = None
    fids = None
    uploader = None
    nodes_time = None
    nodes_location = None
    nodes_rssi = None
    feature_location = None
    feature_avg = None
    feature_std = None
    feature_max = None
    confidence = None

    def __init__(self, fid, x, y, signal_time, signal_type, uploader):
        self.signal_type = signal_type
        self.uploader = uploader
        self.fids = [fid]
        self.nodes_location = [[x, y]]
        self.nodes_time = [signal_time]
        # self.feature_location = np.array([0, 0])
        # self.feature_avg = np.array([])
        # self.feature_std = np.array([])
        # self.feature_max = np.array([])
        return

    def add_node(self, fid, x, y, signal_time):
        self.fids.append(fid)
        self.nodes_time.append(signal_time)
        self.nodes_location.append([x, y])
        return

    def feature_extraction(self):
        self.feature_location = np.mean(self.nodes_location, 0)
        self.feature_max = np.max(self.nodes_rssi, 0)
        self.feature_avg = np.array([None] * len(self.feature_max))
        self.feature_std = np.array([None] * len(self.feature_max))
        for i in range(len(self.nodes_rssi[0])):
            rssi_list = []
            for j in range(len(self.nodes_rssi)):
                if self.nodes_rssi[j][i] > -100:
                    rssi_list.append(self.nodes_rssi[j][i])
            if len(rssi_list) > 0:
                self.feature_avg[i] = np.mean(rssi_list)
                self.feature_std[i] = np.std(rssi_list)
            else:
                self.feature_avg[i] = -100
                self.feature_std[i] = 0

    def __len__(self):
        return len(self.fids)

    @staticmethod
    def distance_loc(f1, f2):
        return np.sqrt(np.sum(np.square(f1.feature_location-f2.feature_location)))

    @staticmethod
    def distance_rssi(f1, f2):
        avg_d = np.sqrt(np.sum(np.square(f1.feature_avg - f2.feature_avg)))
        std_d = np.sqrt(np.sum(np.square(f1.feature_std - f2.feature_std)))
        max_d = np.sqrt(np.sum(np.square(f1.feature_max - f2.feature_max)))
        return avg_d + std_d + max_d


class Category:
    type = None
    data = None
    grids = None

    def __init__(self, data):
        self.data = data
        self.grids = {}
        for i in range(len(data)):
            current_seq = data[i]
            x = current_seq.feature_location[0]
            y = current_seq.feature_location[1]
            ceil_x = math.ceil(x)
            ceil_y = math.ceil(y)
            floor_x = math.floor(x)
            floor_y = math.floor(y)
            self.grids[str(ceil_x) + ' '+ str(ceil_y)] = 1
            self.grids[str(ceil_x) + ' ' + str(floor_y)] = 1
            self.grids[str(floor_x) + ' ' + str(ceil_y)] = 1
            self.grids[str(floor_x) + ' ' + str(floor_y)] = 1

    def __len__(self):
        return len(self.data)

    def matched(self, fingerprint_sequence):
        x = fingerprint_sequence.feature_location[0]
        y = fingerprint_sequence.feature_location[1]
        ceil_x = math.ceil(x)
        ceil_y = math.ceil(y)
        floor_x = math.floor(x)
        floor_y = math.floor(y)
        loc = 0
        if str(ceil_x) + ' ' + str(ceil_y) in self.grids:
            loc = 1
        elif str(floor_x) + ' ' + str(ceil_y) in self.grids:
            loc = 1
        elif str(ceil_x) + ' ' + str(floor_y) in self.grids:
            loc = 1
        elif str(floor_x) + ' ' + str(floor_y) in self.grids:
            loc = 1
        if loc > 0:
            return self.rssi_match(fingerprint_sequence)
        else:
            return False

    def rssi_match(self, seq):
        dist = []
        nei_count = 0
        for i in range(len(self.data)):
            d = FingerprintSequence.distance_rssi(self.data[i], seq)
            if d < np.sqrt(len(seq.feature_avg)) * 3:
                nei_count += 1
                dist.append(d)
        dist.sort()
        if(len(dist)) >= 3:
            return np.mean([1/(1+dist[i]/np.sqrt(len(seq.feature_avg))) for i in range(3)])
        return False








