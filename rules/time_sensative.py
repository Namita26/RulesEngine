import datetime

from rules.rule import Rule, RulesEngine

from models.events import Event

class TimeSensativePayment(Rule):

  def has_condition_met(self, event):

    previous_event_records = Event.query.filter_by(
      userid = event.get("userid"),
      noun = event.get("noun"),
      verb = event.get("verb")
    ).all()

    records_last_5_mins = filter(
      lambda x: x.ts >= datetime.datetime.now()-datetime.timedelta(minutes=5),
      previous_event_records
    )

    bill_amounts = map(lambda x: x.properties.get("value"), records_last_5_mins)
    final_bill_amount = sum(bill_amounts)

    if final_bill_amount > 20000:
      return True

    return False

  def execute(self, event):

    print "[Rule #2 TimeSensativePayment executed] Sending alert for 5 or more bill pay events of total value >= 20000 happened within 5 minutes"

RulesEngine.register_rule(TimeSensativePayment())
