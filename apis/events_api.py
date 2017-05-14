import json
import datetime

from flask import request
from flask_restful import Resource

from rules.rule import RulesEngine

from models.events import Event

from flask import current_app as app


from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):

  def default(self, obj):
  
    if isinstance(obj.__class__, DeclarativeMeta):
      
      fields = {}
      for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
        data = obj.__getattribute__(field)
        try:
          json.dumps(data)
          fields[field] = data
        except TypeError:
          fields[field] = None
      
      return fields

    return json.JSONEncoder.default(self, obj)


class RulesAPIHandler(Resource):
  
  def post(self):

    payload = request.get_data()

    json_data = json.loads(payload)

    event = Event(
      json_data.get("id"),
      json_data.get("userid"),
      json_data.get("noun"),
      datetime.datetime.now(),
      json_data.get("latlong"),
      json_data.get("verb"),
      json_data.get("timespent"),
      json_data.get("properties")
    )

    xx = event.save()

    RulesEngine().execute(json_data)

    xx = json.dumps(event, cls=AlchemyEncoder)

    return {"response": json.loads(xx), "status": "success"}