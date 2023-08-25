# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all of the available api routes."""
    return ("""
Available Routes:<br/>
<br/>
- Returns Preciptation analysis: <a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>
<br/>
- Returns available Stations data: <a href='/api/v1.0/stations'>/api/v1.0/stations</a><br/>
<br/>
- Returns Temperature data: <a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>
<br/>
- Returns Minimum, Maximum, Average Temperature starting from a certain date: /api/v1.0/YYYY-MM-DD<br/>
<br/>            
- Returns Minimum, Maximum, Average Temperature between two dates (start date provided in the API is the first date and the end data is the second one): /api/v1.0/YYYY-MM-DD/YYYY-MM-DD<br/>
Note: latest date in dataset is '2017-08-23'
""")

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Performs query to get the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()

    # Converts query results from your precipitation analysis to dictionary
    prcp_analysis = []
    for date, prcp in results:
        prcp_dict = {date: prcp}
        prcp_analysis.append(prcp_dict) 

    # Closing Session
    session.close()
    
    # Returns jsonified output
    return jsonify(prcp_analysis)

@app.route("/api/v1.0/stations")
def stations():
    # Performs query to retrieve stations id from measurement table and joins it with station table to get the station names
    stations = session.query(Measurement.station, Station.name).join(Station, Measurement.station == Station.station).distinct().all()

    # Converts query results to a dictionary
    stations_list = []
    for station, name in stations:
        stations_dict = {station: name}
        stations_list.append(stations_dict)

    # Closing Session
    session.close()
    
    # Returns jsonified output
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    # Uses the most active station id, to query tobs data for the only latest year
    tobs_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2016-08-23')\
        .filter(Measurement.station == 'USC00519281').all()

    # Converts query results to a dictionary
    tobs_list = []
    for date, tobs in tobs_data:
        tobs_dict = {date: tobs}
        tobs_list.append(tobs_dict)
    
    # Closing Session
    session.close()
    
    # Returns jsonified output
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>") # Defines api route when start date only is given
@app.route("/api/v1.0/<start>/<end>") # Defines route when both start and end dates are given 
def start_end(start,end='2017-08-23'): # Uses the latest date in the data as a default ending date
    # Query to return Max, Min and Avg Temperature starting from a certain date to the default ending date
    tobs_info = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs))\
            .filter(Measurement.date >= start).all()
    
    # if another end date is provided, perform this query instead
    if end: 
        tobs_info = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs))\
            .filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Stores the outputs from the query results
    TMIN = tobs_info[0][0]
    TMAX = tobs_info[0][1]
    TAVG = tobs_info[0][2]
    
    # Closing Session
    session.close()

    # Returns text using the outputs
    return f"""The Minimum Temperature is {TMIN},<br/>
        The Maximum Temperature is {TMAX},<br/>
        The Average Temperature is {TAVG}"""

# Defines the main behavior
if __name__ == '__main__':
    app.run(debug=True)