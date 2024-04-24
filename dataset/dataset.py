import room_setup

class Dataset(object):
    def __init__(self,
                room_setup: room_setup.RoomSetup,
                preprocess_dir: str
                ):
        self.room_setup = room_setup
        self.preprocess_dir = preprocess_dir