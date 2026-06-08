import sqlite3
import pytest

# To run in codespace in Terminal type pytest -q

from FlightManagementDB_queries import addnewFlight, update_specificflight
@pytest.fixture
def sample_db():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    query = '''CREATE TABLE Flight (
    FlightID VARCHAR (10) NOT NULL,
    FlightStatus VARCHAR (10) NOT NULL,
    ArrivalTime VARCHAR (10),
    DepartureTime VARCHAR (10),
    DepartureDay VARCHAR (10),
    StartAirportID VARCHAR (10),
    EndAirportID VARCHAR (10),
    AircraftID VARCHAR (10) NOT NULL,
    PRIMARY KEY (FlightID));'''

    cursor.execute(query)

    conn.commit()
    return conn

def test_addnewFlight_inserts_rows_correctly(sample_db):
    cursor = sample_db.cursor()

    rows = addnewFlight(cursor,
                        FlightID="FL9999",
                        FlightStatus="Pending",
                        DepartureTime="09:00",
                        ArrivalTime="11:00",
                        departureDay="Thursday",
                        StartAirportID="DUB005",
                        EndAirportID="AMS006",
                        AircraftID="B737_001")
    # Check function adds the row to the table
    assert len(rows)==1

    # Check function adds the correct values
    inserted = rows[0]
    assert inserted[0] =="FL9999"
    assert inserted[1] =="Pending"
    assert inserted[2] =="09:00"
    assert inserted[3] =="11:00"
    assert inserted[4] =="Thursday"
    assert inserted[5] =="DUB005"
    assert inserted[6] =="AMS006"
    assert inserted[7] =="B737_001"

def test_FlightUpdateFunctionality(sample_db):
    cursor = sample_db.cursor()

    query = '''INSERT INTO Flight VALUES
    ('FL9999','Pending','09:00','11:00','Thursday','DUB005','AMS006','B737_001')'''
    cursor.execute(query)
    sample_db.commit()

    update_specificflight(cursor,'FL9999', 'Cancelled')
    sample_db.commit()
    query = '''SELECT FlightStatus FROM Flight WHERE FlightID = "FL9999"'''

    cursor.execute(query)
    test_flightstatus = cursor.fetchone()[0]
  
    assert test_flightstatus == 'Cancelled'
    