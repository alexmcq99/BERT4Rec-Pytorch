from .base import AbstractDataset

import pandas as pd

from datetime import date


class BooksDataset(AbstractDataset):
    @classmethod
    def code(cls):
        return 'books'

    @classmethod
    def url(cls):
        return ''
        
    @classmethod
    def zip_file_content_is_folder(cls):
        return False

    @classmethod
    def all_raw_file_names(cls):
        return ['books_factorized.csv']

    def load_ratings_df(self):
        folder_path = self._get_rawdata_folder_path()
        file_path = folder_path.joinpath('books_factorized.csv')
        df = pd.read_csv(file_path, header=None)
        df.columns = ['uid', 'sid', 'rating', 'timestamp']
        return df