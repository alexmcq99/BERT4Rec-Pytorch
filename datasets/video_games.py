from .base import AbstractDataset

import pandas as pd

from datetime import date


class VideoGamesDataset(AbstractDataset):
    @classmethod
    def code(cls):
        return 'video_games'

    @classmethod
    def url(cls):
        return ''
        
    @classmethod
    def zip_file_content_is_folder(cls):
        return False

    @classmethod
    def all_raw_file_names(cls):
        return ['video_games.txt']

    def load_ratings_df(self):
        folder_path = self._get_rawdata_folder_path()
        file_path = folder_path.joinpath('video_games.txt')
        df = pd.read_csv(file_path, sep=" ", header=None)
        df.columns = ['uid', 'sid', 'rating', 'timestamp']
        return df