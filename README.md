# Introduction

This repository implements models from the following two papers, but for CSE 6240, we're only concerned with BERT4Rec:

> **BERT4Rec: Sequential Recommendation with BERT (Sun et al.)**  

> **Variational Autoencoders for Collaborative Filtering (Liang et al.)**  

# FOR THE TAs: Usage for CSE 6240

## Overall

Run `main.py` with arguments to train and/or test you model. There are predefined templates for all models.

You can use the `--template` argument to choose which model to train, as in the examples below.

For the dataset, you can choose which dataset to run using the `--dataset_code` argument.  The three datasets used for this project were `video_games` and `movies_and_tv`.

On running `main.py`, if you did not define a dataset code, it asks you with command line input which dataset to use.

## BERT4Rec

To run BERT4Rec on the `video_games` dataset:
```bash
python main.py --template train_bert --dataset_code video_games
```
To change the dataset, simply replace `video_games` with `movies_and_tv`