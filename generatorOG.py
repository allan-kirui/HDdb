from faker import Faker
from faker.providers import BaseProvider
from faker_music import MusicProvider
from datetime import datetime
from paths import Paths

import pandas as pd
import os
import random
import csv

NUMBER_OF_SONGS = 30
LABEL_TITLE_ROW = ['LabelID', 'LabelName', 'MainGenre', 'NumberOfSongs', 'CreationDate', 'ContractStart', 'ContractEnd',
                   'NumberOfArtists', 'CostOfContract']
SONG_TITLE_ROW = ['SongID', 'LabelID', 'SongName', 'PublicationDate', 'Artist', 'Writer', 'Producer', 'Genre',
                  'DurationOfSong', 'Streams']
USER_TITLE_ROW = ['UserID', 'Username', 'email', 'SongID']
SONG_LOG_TITLE_ROW = ['SongID', 'UserID', 'StartTimeStamp', 'EndTimeStamp', 'MethodOfSelection']
TIME_LOG_TITLE_ROW = ['LogID', 'UserID', 'SessionStart', 'SessionEnd']


class MethodOfSelectionProvider(BaseProvider):
    def method_of_selection(self):
        return random.choice(['AI-suggestion', 'Search'])


faker = Faker()
faker.add_provider(MusicProvider)
faker.add_provider(MethodOfSelectionProvider)


def get_uuid():
    return faker.uuid4()


def get_label_name():
    return (faker.company()).replace(",", "")


def get_person_name():
    return faker.name()


def get_user_name():
    return faker.user_name()


def get_email():
    return faker.company_email()


def get_song_genre():
    return (faker.music_genre()).replace(",", "")


def capitalize(word):
    return word.capitalize()


def get_song_name():
    words = faker.words()
    capitalized_words = list(map(capitalize, words))
    return ' '.join(capitalized_words)


def get_number(endRange, floatType):
    if not floatType:
        return random.randrange(1, endRange)
    else:
        return round(random.uniform(1, endRange), 2)


def get_datetime(start_datetime=datetime(1960, 1, 1, 1, 1, 1), end_datetime=datetime(2022, 1, 1, 1, 1, 1)):
    return faker.date_time_ad(start_datetime=start_datetime, end_datetime=end_datetime)


def get_timestamp():
    return faker.time()


def get_method_of_selection():
    return faker.method_of_selection()


def avoid_repeating_values(path_to_file, col_ID):
    unique_id = get_uuid()
    if os.path.exists(path_to_file) and os.path.getsize(path_to_file) > 0:
        df = pd.read_csv(path_to_file)
        while not df.empty and unique_id in df[col_ID].values:
            unique_id = get_uuid()
    return unique_id


# LabelID,LabelName,MainGenre,NumberOfSongs,CreationDate,ContractStart,ContractEnd,NumberOfArtists,CostOfContract
def generate_labels():
    unique_id = avoid_repeating_values(path_to_file=paths.label_orig_path, col_ID="LabelID")
    return [unique_id, get_label_name(), get_song_genre(), get_number(6000, False), get_datetime(), get_datetime(),
            get_datetime(), get_number(700, False), get_number(60000, True)]


# SongID,LabelID,SongName,PublicationDate,Artist,Writer,Producer,Genre,DurationOfSong,Streams
def generate_songs():
    unique_id = avoid_repeating_values(path_to_file=paths.song_orig_path, col_ID="SongID")
    return [unique_id, "", get_song_name(), get_datetime(), get_person_name(), get_person_name(), get_person_name(),
            get_song_genre(), get_number(60, True), get_number(1000, False)]


# UserID,Username,email,SongID
def generate_users():
    unique_id = avoid_repeating_values(path_to_file=paths.user_orig_path, col_ID="UserID")
    return [unique_id, get_user_name(), get_email(), ""]


# LogID,UserID,SessionStart,SessionEnd
def generate_time_logs():
    unique_id = avoid_repeating_values(path_to_file=paths.timeLog_orig_path, col_ID="LogID")
    return [unique_id, "", get_timestamp(), get_timestamp()]


# SongID,UserID,StartTimeStamp,EndTimeStamp,MethodOfSelection
def generate_song_logs():
    return ["", "", get_datetime(start_datetime=datetime(2005, 7, 31, 1, 24, 38)),
            get_datetime(start_datetime=datetime(2005, 7, 31, 1, 24, 38)), get_method_of_selection()]


def generateDataAndWriteToCSV(filename, titleRow, generator, amount):
    if os.path.exists(filename):
        action = 'a'
    else:
        action = 'w+'
    with open(filename, action, newline='', encoding='utf8') as file:
        writer = csv.writer(file)
        if action != 'a':
            writer.writerow(titleRow)
        for i in range(1, amount + 1):
            writer.writerow(generator())


paths = Paths()
paths.checkAndCreateDirs()

generateDataAndWriteToCSV(paths.label_orig_path, LABEL_TITLE_ROW, generate_labels, 10)
generateDataAndWriteToCSV(paths.song_orig_path, SONG_TITLE_ROW, generate_songs, 20)
generateDataAndWriteToCSV(paths.user_orig_path, USER_TITLE_ROW, generate_users, 9)
generateDataAndWriteToCSV(paths.timeLog_orig_path, TIME_LOG_TITLE_ROW, generate_time_logs, 17)
generateDataAndWriteToCSV(paths.songLog_orig_path, SONG_LOG_TITLE_ROW, generate_song_logs, 11)
