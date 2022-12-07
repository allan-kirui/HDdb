CREATE DATABASE SpotifyDB
GO

USE SpotifyDB
GO

CREATE TABLE MusicLabel
(
	LabelID varchar(100) PRIMARY KEY,
	LabelName varchar(100) CHECK (LEN(LabelName) >= 1),
	MainGenre varchar(100) CHECK (LEN(MainGenre) >= 1),
	NumberOfSongs INTEGER,
	CreationDate DATETIME,
	ContractStart DATETIME,
	ContractEnd DATETIME,
	NumberOfArtists INTEGER,
	CostOfContract FLOAT,
)
GO

CREATE TABLE Song
(
    SongID varchar(100) CHECK (LEN(SongID) >= 1) PRIMARY KEY,
	LabelID varchar(100) REFERENCES MusicLabel,
	SongName varchar(100) CHECK (LEN(SongName) >= 1),
	PublicationDate DATETIME,
	Artist varchar(100) CHECK (LEN(Artist) >= 1),
	Writer varchar(100) CHECK (LEN(Writer) >= 1),
	Producer varchar(100) CHECK (LEN(Producer) >= 1),
	Genre varchar(100) CHECK (LEN(Genre) >= 1),
	DurationOfSong FLOAT CHECK (DurationOfSong <= 60.0),
	streams INTEGER,
)
GO

CREATE TABLE SpotifyUser
(
    UserID varchar(100) PRIMARY KEY,
	Username varchar(100) CHECK (LEN(username) >= 1),
	email varchar(100) CHECK (LEN(email) >= 1), 
	SongID varchar(100) REFERENCES Song,
)
GO



CREATE TABLE TimeLog
(
	LogID varchar(100) PRIMARY KEY,
	UserID varchar(100) REFERENCES SpotifyUser,
	SessionStart DATETIME,
	SessionEnd DATETIME
	/*TimeSpent FLOAT CHECK (TimeSpent <= 24.0),*/
)
GO

CREATE TABLE SongLog
(
	SongID varchar(100) REFERENCES Song,
	UserID  varchar(100) REFERENCES SpotifyUser,
	StartTimeStamp DATETIME,
	EndTimeStamp DATETIME,
	MethodOfSelection varchar(50) check (MethodOfSelection = 'AI-suggestion' OR MethodOfSelection='Search'),
	PRIMARY KEY (SongID, UserID, StartTimeStamp, EndTimeStamp)
)
GO