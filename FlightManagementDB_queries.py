import sqlite3

def view_flights(cursor):
    query = '''SELECT FlightID, FlightStatus FROM Flight'''
    cursor.execute(query)
    return cursor.fetchall()

def view_pilotschedule(cursor, viewpilotID):
    query = '''
        SELECT 
            Flight.FlightID,
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
    query = '''SELECT AirportLocation FROM Airport'''
    cursor.execute(query)
    return cursor.fetchall()

def view_departureinformation(cursor, departureairport):

    query = ''' SELECT
                Airport.AirportStatus,
                Flight.FlightID,
                Flight.FlightStatus,
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

    query = ''' SELECT
                Airport.AirportStatus,
                Flight.FlightID,
                Flight.FlightStatus,
                Flight.ArrivalTime,
                Flight.AircraftID,
                Assigned.PilotID
                FROM Flight
                JOIN Airport
                    ON Flight.EndAirportID = Airport.AirportID
                LEFT JOIN Assigned
                    ON Assigned.FlightID = Flight.FlightID
                    AND Assigned.PilotRole = 'Lead'
                WHERE Airport.AirportLocation = ?'''
    cursor.execute(query, (arrivalairport,))
    rows = cursor.fetchall()

