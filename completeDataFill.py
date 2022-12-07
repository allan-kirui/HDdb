import random
import os
from paths import Paths

paths = Paths()
paths.readFiles()

# SONG
songs_labelID = []
for i in range(len(paths.song['SongID'])):
    songs_labelID.append(random.choice(paths.label['LabelID']))
paths.song['LabelID'] = songs_labelID
paths.song.to_csv(os.path.join(paths.csvs_fin, paths.song_fin_csv), index=False)

# USER
users_songID = []
for i in range(len(paths.user['UserID'])):
    users_songID.append(random.choice(paths.song['SongID']))
paths.user['SongID'] = users_songID
paths.user.to_csv(os.path.join(paths.csvs_fin, paths.user_fin_csv), index=False)

# TIMELOG
timelogs_userID = []
for i in range(len(paths.timeLog['LogID'])):
    timelogs_userID.append(random.choice(paths.user['UserID']))
paths.timeLog['UserID'] = timelogs_userID
paths.timeLog.to_csv(os.path.join(paths.csvs_fin, paths.timeLog_fin_csv), index=False)

# SONGLOG
songlogs_songID = []
songlogs_userID = []
for i in range(len(paths.songLog['SongID'])):
    songlogs_songID.append(random.choice(paths.song['SongID']))
paths.songLog['SongID'] = songlogs_songID

for i in range(len(paths.songLog['UserID'])):
    songlogs_userID.append(random.choice(paths.user['UserID']))
paths.songLog['UserID'] = songlogs_userID

paths.songLog.to_csv(os.path.join(paths.csvs_fin, paths.songLog_fin_csv), index=False)


def createBulkFile(csv_filename, bulk_filename):
    with open(csv_filename, 'r', newline='', encoding='utf8') as csvfile, open(bulk_filename, 'w+', newline='',
                                                                               encoding='utf8') as bulkfile:
        next(csvfile)
        for line in csvfile:
            bulkfile.write(line)


createBulkFile(paths.label_orig_path, paths.label_bulk_path)
createBulkFile(paths.song_fin_path, paths.song_bulk_path)
createBulkFile(paths.user_fin_path, paths.user_bulk_path)
createBulkFile(paths.timeLog_fin_path, paths.timelog_bulk_path)
createBulkFile(paths.songLog_fin_path, paths.songLog_bulk_path)
