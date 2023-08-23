import numpy as np
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#--------------------------------------
# Database Setup
#--------------------------------------

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect= True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#--------------------------------------
# Flask Setup
#--------------------------------------

app = Flask(__name__)

#--------------------------------------
# Flask Routes
#--------------------------------------

@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"Note: To access values between a start and end date enter both dates using the format: yyy-mm-dd/yyy-mm-dd"
    )

# Create a route that queries precipiation levels and dates and returns a dictionary using date as key and precipation as value
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create session from Python to the DB
    session = Session(engine)

    """list of all Precipitation Data"""
    # Query Precipitation data
    precip_results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= "2016-08-23").\
        all()

    session.close()

    # Convert list to dictionary
    precip_all = []
    for date,prcp  in precip_results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
               
        precip_all.append(prcp_dict)

    return jsonify(precip_all)


# Create a route that returns a JSON list of stations from the database
@app.route("/api/v1.0/stations")
def stations():
    # Create session from Python to the DB
    session = Session(engine)

    """List of all Stations"""
    # Query Stations
    sel = [Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation]
    station_results = session.query(*sel).all()

    session.close()

    stations_all = []
    for station,name,lat,lon,el in station_results:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Lat"] = lat
        station_dict["Lon"] = lon
        station_dict["Elevation"] = el
        stations_all.append(station_dict)

    return jsonify(stations_all)

# Create a route that queries the dates and temp observed for the most active station for the last year of data and returns a JSON list of the temps observed for the last year
@app.route("/api/v1.0/tobs")
def tobs():
    # Create session from Python to the DB
    session = Session(engine)

    """List of all tobs"""
    # Query tobs
    tobs_results = session.query(Measurement.date,  Measurement.tobs, Measurement.station).\
        filter(Measurement.date >= '2016-08-23').\
        filter(Measurement.date <= '2017-08-23').\
        filter(Measurement.station == "USC00519281").\
        order_by(Measurement.date).all()

    session.close()

    # Convert list to dictionary
    tobs_all = []
    for date, tobs, station in tobs_results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_dict["station"] = station
        
        tobs_all.append(tobs_dict)

    return jsonify(tobs_all)

# Define function, set start date entered by user as parameter for start_date decorator 
@app.route("/api/v1.0/<start>")
def start_date(start):
    session = Session(engine) 

    # Create query for minimum, average, and max tobs where query date is greater than or equal to the date the user submits in URL
    # Return a list of min, avg and max tobs for a start date
    tobs_results_start = session.query(*[func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]).\
                filter(Measurement.date >= start).all()
    
    session.close() 

 # Create dictionary from the row of data and append to a list of start_date_tobs
    start_date_tobs = []
    for min, avg, max in tobs_results_start:
        start_date_tobs_dict = {}
        start_date_tobs_dict["min_temp"] = min
        start_date_tobs_dict["avg_temp"] = avg
        start_date_tobs_dict["max_temp"] = max

        start_date_tobs.append(start_date_tobs_dict)
    
    return jsonify(start_date_tobs)

# Define function, set start and end dates entered by user as parameters for start_end_date decorator
@app.route("/api/v1.0/<start>/<end>")
def Start_end_date(start, end):
    session = Session(engine)

    # Create query for minimum, average, and max tobs where query date is greater than or equal to the start date and less than or equal to end date user submits in URL
    # Return a list of min, avg and max tobs for start and end dates
    tobs_results_end = session.query(*[func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]).\
                filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()
  
    # Create a dictionary from the of row data and append to a list of start_end_date_tobs
    start_end_tobs = []
    for min, avg, max in tobs_results_end:
        start_end_tobs_dict = {}
        start_end_tobs_dict["min_temp"] = min
        start_end_tobs_dict["avg_temp"] = avg
        start_end_tobs_dict["max_temp"] = max

        start_end_tobs.append(start_end_tobs_dict)
    
    return jsonify(start_end_tobs)

# app.run statement
if __name__ == "__main__":
    app.run(debug=True)