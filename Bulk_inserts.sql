use SpotifyDB
GO

BULK INSERT dbo.Musiclabel FROM 'D:\Education\Sem 5\HD\csvs-bulk\label.bulk' WITH (FIELDTERMINATOR=',', ROWTERMINATOR = '0x0a')
BULK INSERT dbo.Song FROM 'D:\Education\Sem 5\HD\csvs-bulk\song.bulk' WITH (FIELDTERMINATOR=',', ROWTERMINATOR = '0x0a')
BULK INSERT dbo.SpotifyUser FROM 'D:\Education\Sem 5\HD\csvs-bulk\user.bulk' WITH (FIELDTERMINATOR=',', ROWTERMINATOR = '0x0a')
BULK INSERT dbo.TimeLog FROM 'D:\Education\Sem 5\HD\csvs-bulk\timeLog.bulk' WITH (FIELDTERMINATOR=',', ROWTERMINATOR = '0x0a')
BULK INSERT dbo.SongLog FROM 'D:\Education\Sem 5\HD\csvs-bulk\songLog.bulk' WITH (FIELDTERMINATOR=',', ROWTERMINATOR = '0x0a')


