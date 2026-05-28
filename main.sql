CREATE TABLE Pilot (
    PilotID VARCHAR (10) NOT NULL,
    PilotStatus VARCHAR (10) NOT NULL,
    Rank VARCHAR (10) NOT NULL,
    PRIMARY KEY (PilotID));

CREATE TABLE Assigned (
    PilotID VARCHAR (10) NOT NULL REFERENCES Pilot,
    FlightID VARCHAR (10) NOT NULL REFERENCES Flight,
    PilotRole VARCHAR (10) NOT NULL,
    PRIMARY KEY (PilotID,FlightID));

CREATE TABLE Flight (
    FlightID VARCHAR (10) NOT NULL REFERENCES Assigned,
    FlightStatus VARCHAR (10) NOT NULL,
    Departure VARCHAR (10),
    Arrival VARCHAR (10),
    StartAirportID VARCHAR (10),
    EndAirportID VARCHAR (10),
    AircraftID VARCHAR (10) NOT NULL,
    PRIMARY KEY (FlightID));

CREATE TABLE Airport (
    AirportID VARCHAR (10) NOT NULL,
    AirportStatus VARCHAR (10) NOT NULL,
    AirportLocation VARCHAR (10) NOT NULL,
    PRIMARY KEY (AirportID));

INSERT INTO Pilot (PilotID, PilotStatus, Rank)
VALUES
('PILOT001','Available','Captain'),
('PILOT002','Available','Officer'),
('PILOT003','Unavailable','Captain'),
('PILOT004','Available','Officer'),
('PILOT005','Training','Officer'),
('PILOT006','Available','Captain'),
('PILOT007','Unavailable','Officer'),
('PILOT008','Available','Captain'),
('PILOT009','Available','Officer'),
('PILOT010','Training','Officer'),
('PILOT011','Available','Captain'),
('PILOT012','Available','Officer');

INSERT INTO Assigned (PilotID, FlightID, PilotRole)
VALUES
('PILOT001','FL1001','Lead'),
('PILOT002','FL1001','Deputy'),
('PILOT003','FL1002','Lead'),
('PILOT004','FL1002','Deputy'),
('PILOT005','FL1003','Lead'),
('PILOT006','FL1004','Lead'),
('PILOT007','FL1005','Lead'),
('PILOT008','FL1006','Lead'),
('PILOT009','FL1007','Lead'),
('PILOT010','FL1008','Lead'),
('PILOT011','FL1009','Lead'),
('PILOT012','FL1010','Lead');

INSERT INTO Airport (AirportID, AirportStatus, AirportLocation)
VALUES
('LHR001','Open','London'),
('MAN002','Open','Manchester'),
('EDI003','Open','Edinburgh'),
('GLA004','Open','Glasgow'),
('DUB005','Open','Dublin'),
('AMS006','Open','Amsterdam'),
('FRA007','Open','Frankfurt'),
('MAD008','Open','Madrid'),
('LIS009','Open','Lisbon'),
('CDG010','Open','Paris'),
('BCN011','Open','Barcelona'),
('ROM012','Open','Rome');

INSERT INTO Flight (FlightID, FlightStatus,Departure,Arrival,StartAirportID,EndAirportID,Aircraft)
VALUES
('FL1001','Scheduled','06:00','08:00','LHR001','AMS006','B737_001'),
('FL1002','Scheduled','07:30','10:00','AMS006','FRA007','A320_001'),
('FL1003','Scheduled','11:00','13:00','FRA007','CDG010','A319_001'),
('FL1004','Delayed','15:00','18:00','CDG010','BCN011','A320_002'),
('FL1005','Cancelled','09:00','11:00','BCN011','ROM012','A321_001'),
('FL1006','Scheduled','12:00','14:00','ROM012','DUB005','B737_002'),
('FL1007','Scheduled','16:00','18:00','DUB005','EDI003','A320_003'),
('FL1008','Scheduled','19:00','21:00','EDI003','GLA004','A319_002'),
('FL1009','Scheduled','08:00','10:00','GLA004','MAN002','A320_004'),
('FL1010','Scheduled','13:00','15:00','MAN002','LHR001','A321_002');

SELECT * FROM Pilot;
SELECT * FROM Assigned;
SELECT * FROM Flight;
SELECT * FROM Airport;