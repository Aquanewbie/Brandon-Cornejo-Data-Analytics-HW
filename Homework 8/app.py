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
    return (
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs"
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

if __name__ == '__main__':
    app.run(debug=True)




