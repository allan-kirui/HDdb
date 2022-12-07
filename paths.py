import pandas as pd
import os


class Paths:
    def __init__(self):
        self.songLog = None
        self.timeLog = None
        self.user = None
        self.song = None
        self.label = None

        self.csvs_orig = 'csvs-orig'
        self.csvs_fin = 'csvs-fin'
        self.csvs_bulk = 'csvs-bulk'

        self.label_csv = 'label.csv'
        self.song_csv = 'song.csv'
        self.user_csv = 'user.csv'
        self.timeLog_csv = 'timelog.csv'
        self.songLog_csv = 'songLog.csv'

        self.label_bulk = 'label.bulk'
        self.song_bulk = 'song.bulk'
        self.user_bulk = 'user.bulk'
        self.timelog_bulk = 'timeLog.bulk'
        self.songLog_bulk = 'songLog.bulk'

        self.label_fin_csv = 'label-fin.csv'
        self.song_fin_csv = 'song-fin.csv'
        self.user_fin_csv = 'user-fin.csv'
        self.timeLog_fin_csv = 'timelog-fin.csv'
        self.songLog_fin_csv = 'songLog-fin.csv'

        self.label_orig_path = os.path.join(self.csvs_orig, self.label_csv)
        self.song_orig_path = os.path.join(self.csvs_orig, self.song_csv)
        self.user_orig_path = os.path.join(self.csvs_orig, self.user_csv)
        self.timeLog_orig_path = os.path.join(self.csvs_orig, self.timeLog_csv)
        self.songLog_orig_path = os.path.join(self.csvs_orig, self.songLog_csv)

        self.label_fin_path = os.path.join(self.csvs_orig, self.label_csv)
        self.song_fin_path = os.path.join(self.csvs_orig, self.song_csv)
        self.user_fin_path = os.path.join(self.csvs_orig, self.user_csv)
        self.timeLog_fin_path = os.path.join(self.csvs_orig, self.timeLog_csv)
        self.songLog_fin_path = os.path.join(self.csvs_orig, self.songLog_csv)

        self.label_bulk_path = os.path.join(self.csvs_bulk, self.label_bulk)
        self.song_bulk_path = os.path.join(self.csvs_bulk, self.song_bulk)
        self.user_bulk_path = os.path.join(self.csvs_bulk, self.user_bulk)
        self.timelog_bulk_path = os.path.join(self.csvs_bulk, self.timelog_bulk)
        self.songLog_bulk_path = os.path.join(self.csvs_bulk, self.songLog_bulk)

    def checkAndCreateDirs(self):
        """
        Creates the directories if they don't exist
        :return None:
        """
        os.makedirs(self.csvs_orig, exist_ok=True)
        os.makedirs(self.csvs_fin, exist_ok=True)
        os.makedirs(self.csvs_bulk, exist_ok=True)

    def readFiles(self):
        self.label = pd.read_csv(self.label_orig_path, sep=',', parse_dates=False)
        self.song = pd.read_csv(self.song_fin_path, sep=',', parse_dates=False)
        self.user = pd.read_csv(self.user_fin_path, sep=',', parse_dates=False)
        self.timeLog = pd.read_csv(self.timeLog_fin_path, sep=',', parse_dates=False)
        self.songLog = pd.read_csv(self.songLog_fin_path, sep=',', parse_dates=False)
