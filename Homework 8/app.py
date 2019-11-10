import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from datetime import datetime
import statistics as st

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
#* `/api/v1.0/precipitation`

#  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

#  * Return the JSON representation of your dictionary.

#* `/api/v1.0/stations`

#  * Return a JSON list of stations from the dataset.

#* `/api/v1.0/tobs`
#  * query for the dates and temperature observations from a year from the last data point.
#  * Return a JSON list of Temperature Observations (tobs) for the previous year.

@app.route("/")
def welcome():
    """List all available api routes."""
    breakline=("_________________________________________________________________________________________________________________________________<br/>")
    return (
        f"/api/v1.0/precipitation<br/>"
        f"{breakline}"
        f"/api/v1.0/stations<br/>"
        f"{breakline}"
        f"/api/v1.0/tobs<br/>"
        f"{breakline}"
        f"Input a Start Date (Format: YYYY-MM-DD) <start> and an End Date (Format: YYYY-MM-DD) in <end> to retrieve Temperature ranges info <br/>"
        f"  <br/>"
        f"/api/v1.0/YYYY-MM-DD/YYYY-MM-DD<br/>"
        f"{breakline}"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
    # Query all passengers
    results = session.query(Measurement.prcp, Measurement.date).all()

    session.close()

    precipitationlist = []
    for prcp, date in results:
        precipitation_dict = {date: prcp}
        precipitationlist.append(precipitation_dict)

    return jsonify(precipitationlist)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
    # Query all passengers
    results = session.query(Station.station).all()

    session.close()

    stationlist = []
    for station in results:
        stationlist.append(station)

    return jsonify(stationlist)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Query for the dates and temperature observations from a year from the last data point
    # Query all passengers
    
    #Find Last Date
    Results = session.query(Measurement.date)
    LastDate=Results[-1]

    session.close()

    Lastdate_object = dt.datetime.strptime(LastDate[0], '%Y-%m-%d')
    Twelvemonths = Lastdate_object - dt.timedelta(days=365)
    Twelvemonthsago = Twelvemonths.strftime('%Y-%m-%d')
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= Twelvemonthsago)

    session.close()

    templist = []
    for date, tobs in results:
        tobs_dict = {date: tobs}
        templist.append(tobs_dict)
        
    return jsonify(templist)

  
@app.route("/api/v1.0/<start>")
def starttofalseend(start):
    """When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date."""
    #Convert Given Date to a Date Python Can use to Calculate
    Startdate = dt.datetime.strptime(start, '%Y-%m-%d')
     #Find Last Date
    session = Session(engine)
    Results = session.query(Measurement.date)
    LastDate=Results[-1]
    session.close()
    
    Timespan = session.query(func.min(Measurement.tobs),
                             func.avg(Measurement.tobs),
                             func.max(Measurement.tobs)).filter(Measurement.date >= Startdate).all()
    print(Timespan)

    session.close()
    return (
        f"Only given a start date <br/>"
        f"Temperature ranges between {start} and the default last date of {LastDate[0]}: <br/>"
        f"Temperature Minimum: {Timespan[0][0]} ° F<br/>"
        f"Temperature Average: {Timespan[0][1]} ° F<br/>"
        f"Temperature Maximum: {Timespan[0][2]} ° F<br/>"
    )

  # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  # When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  # When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
 # `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
@app.route("/api/v1.0/<start>/<end>")
def starttoend(start,end):
    """When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive."""
    Startdate = dt.datetime.strptime(start, '%Y-%m-%d')
    Enddate = dt.datetime.strptime(end, '%Y-%m-%d')
    session = Session(engine)
    Timespan = session.query(func.min(Measurement.tobs),
                             func.avg(Measurement.tobs),
                             func.max(Measurement.tobs)).filter(Measurement.date >= Startdate).filter(Measurement.date <= Enddate).all()
    session.close()
    
    return(
        f"Temperature ranges between {start} and {end}:<br/>"
        f"Temperature Minimum: {Timespan[0][0]} ° F<br/>"
        f"Temperature Average: {Timespan[0][1]} ° F<br/>"
        f"Temperature Maximum: {Timespan[0][2]} ° F<br/>"
    )
if __name__ == '__main__':
    app.run(debug=True)




