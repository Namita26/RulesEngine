from rules.rule import Rule, RulesEngine

from models.events import Event

class FirstBillPayment(Rule):

  def has_condition_met(self, event):

    # query db or any storage to this user's payment records.
    previous_event_records = Event.query.filter_by(
      userid=event.get("userid"),
      noun=event.get("noun"),
      verb=event.get("verb")
    ).all()

    if previous_event_records:
      return False

    return True

  def execute(self, event):

    print "[Rule #1 FirstBillPayment Executed] Sending alert of the 1st payment"

RulesEngine.register_rule(FirstBillPayment())
