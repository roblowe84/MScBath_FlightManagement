import sqlite3
import pytest

# To run in codespace in Terminal type pytest -q

from FlightManagementDB_queries import addnewFlight, update_specificflight, update_PilotAllocation
@pytest.fixture
def sample_db():
    #Setup sample table for purposes of testing addnewFlight
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

    # Send test data to addnewFlight function
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

    # Update table with sample data
    query = '''INSERT INTO Flight VALUES
    ('FL9999','Pending','09:00','11:00','Thursday','DUB005','AMS006','B737_001')'''
    cursor.execute(query)
    sample_db.commit()

    # Test update_specificflight by passing in a change in flight status
    update_specificflight(cursor,'FL9999', 'Cancelled')
    sample_db.commit()
    query = '''SELECT FlightStatus FROM Flight WHERE FlightID = "FL9999"'''

    cursor.execute(query)
    test_flightstatus = cursor.fetchone()[0]
  
    assert test_flightstatus == 'Cancelled'

def test_updated_PilotAllocation(sample_db):
    cursor = sample_db.cursor()

    # Create sample Assigned Table
    query = ''' CREATE TABLE Assigned (
                PilotID VARCHAR (10),
                FlightID VARCHAR (10),
                PilotRole VARCHAR (10),
                PRIMARY KEY (PilotID, FlightID))'''
    cursor.execute(query)

    # Insert initial assignment
    query = '''INSERT INTO Assigned (PilotID, FlightID, PilotRole)
                VALUES ('PILOT001','FL1001','Lead')'''
    cursor.execute(query)
    sample_db.commit()

    # Update the Assignment
    update_PilotAllocation(cursor,FlightID='FL1002', Role = 'Deputy', PilotID='PILOT001')
    sample_db.commit()

    query = '''SELECT PilotiD, FlightID, PilotRole FROM Assigned'''
    cursor.execute(query)
    row = cursor.fetchone()

    assert row == ('PILOT001', 'FL1002', 'Deputy')