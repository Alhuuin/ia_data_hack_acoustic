import numpy as np

mic_height = 50.3125
feet = 12
y_tile = 23.5
x_tile = 11 +7/8

camera_origin_location = np.array([-6*x_tile-5.75, -y_tile, 45+13/16])*25.4

mic_1 = np.array([-11*x_tile - 1, -5*y_tile - 6-3/8, mic_height]) * 25.4 
mic_4= np.array([-11*x_tile + 1.25 + 1/16, 2.5*y_tile+3.75, mic_height]) * 25.4
mic_6 = np.array([5+3/8, 2+1/8, mic_height]) * 25.4
mic_9 = np.array([-3, -6*y_tile - 0.5, mic_height]) * 25.4


mic_xyzs = np.stack((mic_1,mic_4, mic_6, mic_9),axis=0)

SPEAKER_BOTTOM_RIGHT_Y = (1200.15 + 1196.975 + 1206.5)/ 3
SPEAKER_BOTTOM_RIGHT_X = (88.9 + 107.95 + 101.6) / 3
SPEAKER_BOTTOM_LEFT_Y = (1327.15 + 1311.55712764 + 1317.625) / 3
SPEAKER_BOTTOM_LEFT_X = - 76.98583188

speaker_xyz_bottom_right = np.array([SPEAKER_BOTTOM_RIGHT_X, SPEAKER_BOTTOM_RIGHT_Y, 44.5*25.4])
speaker_xyz_bottom_left = np.array([SPEAKER_BOTTOM_LEFT_X, SPEAKER_BOTTOM_LEFT_Y, 44.5*25.4])
speaker_xyz_top_right = np.array([SPEAKER_BOTTOM_RIGHT_X, SPEAKER_BOTTOM_RIGHT_Y, (44.5+17)*25.4])
speaker_xyz_top_left = np.array([SPEAKER_BOTTOM_LEFT_X, SPEAKER_BOTTOM_LEFT_Y, (44.5+17)*25.4])
speaker_xyz = (speaker_xyz_bottom_right+speaker_xyz_bottom_left+speaker_xyz_top_right+speaker_xyz_top_left)/4


walls = None
x_min = - 4000
x_max = 500
y_min = -4000
y_max = 2000

mic_xyzs_base = np.stack((mic_1, mic_4, mic_6, mic_9), axis=0)

class RoomSetup(object):
    def __init__(self,
                speaker_xyz,
                mic_xyzs,
                x_min: float,
                x_max: float,
                y_min: float,
                y_max: float,
                walls=None):

        self.speaker_xyz = speaker_xyz
        self.mic_xyzs = mic_xyzs
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.walls = walls
        self.n_mics = mic_xyzs.shape[0]

    def plot_room(self, centroid, levels=None, legend=True, camera_coords=True, vmax=0.3, vmin=0.1945841):


        c = centroid

        #Scatter Plot
        rcParams['figure.figsize'] = 8,8
        plt.scatter(self.speaker_xyz[0], self.speaker_xyz[1], label='Speaker', color='green')
        plt.scatter(self.mic_xyzs[:,0], self.mic_xyzs[:,1], label = 'Mics', color='orange')

        if levels is None:
            plt.scatter(c[:,0], c[:,1], label = 'Centroids', c ='green', s=4)
        else:
            plt.scatter(c[:,0], c[:,1], label = 'Human Locations', c=levels, cmap="bwr", s=9)

        if self.walls is not None:
            plt.plot(self.walls[:,0], self.walls[:,1] , marker = 'o', color='black', label = 'Walls')

        #plt.scatter(0, 0, label = 'Origin', c ='black')
        plt.xlim([self.x_min, self.x_max])
        plt.ylim([self.y_min, self.y_max])
        plt.axis('equal')

        if legend:
            plt.legend()

class Dataset(object):
    def __init__(self,
                room_setup: RoomSetup,
                preprocess_dir: str
                ):
        self.room_setup = room_setup
        self.preprocess_dir = preprocess_dir

PSEUDO_SAMPLE_RATE = 16000
