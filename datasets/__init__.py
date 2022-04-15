from datasets.books import BooksDataset
from datasets.movies_and_tv import MoviesAndTVDataset
from datasets.video_games import VideoGamesDataset
from .ml_1m import ML1MDataset
from .ml_20m import ML20MDataset

DATASETS = {
    ML1MDataset.code(): ML1MDataset,
    ML20MDataset.code(): ML20MDataset,
    VideoGamesDataset.code(): VideoGamesDataset,
    MoviesAndTVDataset.code(): MoviesAndTVDataset,
    BooksDataset.code(): BooksDataset
}


def dataset_factory(args):
    dataset = DATASETS[args.dataset_code]
    return dataset(args)
