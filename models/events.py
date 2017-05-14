import json
import datetime
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import exc

db = SQLAlchemy()

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  userid = db.Column(db.Integer)
  noun = db.Column(db.String(80))
  ts = db.Column(db.DateTime())
  latlong = db.Column(db.String(200))
  verb = db.Column(db.String(80))
  timespent = db.Column(db.Integer)
  properties = db.Column(db.JSON())

  def __init__(self, id, userid, noun, ts, latlong, verb, timespent, properties):
    self.id = id
    self.userid = userid
    self.noun = noun
    self.ts = ts
    self.latlong = latlong
    self.verb = verb
    self.timespent = timespent
    self.properties = properties

  def save(self):

    try:
      db.session.add(self)
      db.session.commit()
    except exc.IntegrityError as e:
      print "[DUPLICATE EVENT] the input event is already in db!"
