import json
import datetime

from flask import request
from flask_restful import Resource

from rules.rule import RulesEngine

from models.events import Event

from flask import current_app as app


class RulesAPIHandler(Resource):
  
  def post(self):

    json_data = request.get_data()
    json_data = json.loads(json_data)
    json_data = json.loads(json_data)

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

    event.save()

    RulesEngine().execute(json_data)

    return ""