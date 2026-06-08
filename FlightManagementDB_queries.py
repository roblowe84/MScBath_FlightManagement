import sqlite3


def view_flights(cursor):
    # View all flights and their current status as per the database
    query = '''SELECT DepartureDay, FlightID, FlightStatus, AircraftID FROM Flight'''
    cursor.execute(query)
    return cursor.fetchall()

def view_specificflight(cursor, FlightID):
    # View all flights and their current status as per the database
    query = '''SELECT DepartureDay, FlightID, FlightStatus, AircraftID FROM Flight WHERE FlightID = ?'''
    cursor.execute(query, (FlightID,))
    return cursor.fetchall()

def update_specificflight(cursor, FlightID, FlightStatus):
    # Update the Status of a specific flight in the Flight table
    query = '''UPDATE Flight
    SET FlightStatus = ? WHERE FlightID = ?'''
    cursor.execute(query, (FlightStatus,FlightID))


def view_flights_byDepartureDay(cursor,selectedDepartureDay):
    # View flights on a selected departure day
    query = '''
        SELECT 
            DepartureDay,
            FlightID,
            FlightStatus,
            AircraftID
            FROM Flight
        WHERE DepartureDay = ?'''
    cursor.execute(query,(selectedDepartureDay,))
    return cursor.fetchall()

def view_flights_byAircraftID(cursor,selectedAircraftID):
    # View flights by selected AircraftID
    query = '''
        SELECT 
            DepartureDay,
            FlightID,
            FlightStatus,
            AircraftID
            FROM Flight
        WHERE AircraftID = ?'''
    cursor.execute(query,(selectedAircraftID,))
    return cursor.fetchall()

def view_pilotschedule(cursor, viewpilotID):
    # View the current pilots schedule based on PilotID
    query = '''
        SELECT 
            Flight.FlightID,
            Flight.DepartureDay,
            Flight.DepartureTime,
            Flight.ArrivalTime,
            Flight.StartAirportID,
            Flight.EndAirportID,
            Flight.FlightStatus
        FROM Assigned
        JOIN Flight ON Assigned.FlightID = Flight.FlightID
        WHERE Assigned.PilotID = ?'''
    cursor.execute(query, (viewpilotID,))
    return cursor.fetchall()

def return_allairports(cursor):
    # Return all airport locations in the database
    query = '''SELECT AirportLocation FROM Airport'''
    cursor.execute(query)
    return cursor.fetchall()

def return_allairportIDs(cursor):
    # Return all airport IDs which is used for validation routines
    query = '''SELECT AirportID FROM Airport'''
    cursor.execute(query)
    return cursor.fetchall()

def view_departureinformation(cursor, departureairport):
    # Show all departure information based on the departure airport
    query = ''' SELECT
                Airport.AirportStatus,
                Flight.FlightID,
                Flight.FlightStatus,
                Flight.DepartureDay,
                Flight.DepartureTime,
                Flight.AircraftID,
                Assigned.PilotID
                FROM Flight
                JOIN Airport
                    ON Flight.StartAirportID = Airport.AirportID
                LEFT JOIN Assigned
                    ON Assigned.FlightID = Flight.FlightID
                    AND Assigned.PilotRole = 'Lead'
                WHERE Airport.AirportLocation = ?'''
    cursor.execute(query, (departureairport,))
    return cursor.fetchall()

def view_arrivalinformation(cursor,arrivalairport):
    # Show all arrival information based on the arrival airport
    query = ''' SELECT
                Airport.AirportStatus,
                Flight.FlightID,
                Flight.FlightStatus,
                Flight.DepartureDay,
                Flight.ArrivalTime,
                Flight.AircraftID,
                Assigned.PilotID
                FROM Flight
                JOIN Airport
                    ON TRIM(Flight.EndAirportID) = TRIM(Airport.AirportID)
                LEFT JOIN Assigned
                    ON Assigned.FlightID = Flight.FlightID
                    AND Assigned.PilotRole = 'Lead'
                WHERE TRIM(Airport.AirportLocation) = TRIM(?)'''
    cursor.execute(query, (arrivalairport,))
    return cursor.fetchall()

def return_allaircraft(cursor):
    # Return all aircraft IDs which is used for validation routines
    query = '''SELECT AircraftID FROM Flight'''
    cursor.execute(query)
    return cursor.fetchall()

def return_allFlightIDs(cursor):
    # Return all Flight IDs which is used for validation routines
    query = '''SELECT FlightID FROM Flight'''
    cursor.execute(query)
    return cursor.fetchall()


def addnewFlight(cursor,FlightID,FlightStatus,DepartureTime,ArrivalTime,departureDay,StartAirportID,EndAirportID,AircraftID):
    # Add a new Flight based on User Input
    query = '''INSERT INTO Flight(FlightID,FlightStatus,DepartureTime,ArrivalTime,departureDay, StartAirportID, EndAirportID, AircraftID)
    VALUES(?,?,?,?,?,?,?,?)'''
    cursor.execute(query,(FlightID,FlightStatus,DepartureTime,ArrivalTime,departureDay,StartAirportID, EndAirportID,AircraftID))

    # Return the latest Flight Data so user can view the update made
    query = '''SELECT FlightID, FlightStatus, DepartureTime, ArrivalTime,departureDay, StartAirportID,EndAirportID, AircraftID FROM Flight'''
    cursor.execute(query)
    return cursor.fetchall()

def update_PilotAllocation(cursor, FlightID, Role, PilotID):
    # Update the Assigned table for Pilot
    query = '''UPDATE Assigned
    SET FlightID = ?, PilotRole = ? WHERE PilotID = ?'''
    cursor.execute(query,(FlightID, Role, PilotID))
