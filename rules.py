

RULES = []

class Rule(object):

  # two methods which will be executed

  def has_condition_met(self, event):
    pass

  def execute(self, event):
    pass


class RulesEngine(Rule):

  # set of all rules

  # def __init__(self):
    

  @staticmethod
  def register_rule(rule):
    RULES.append(rule)


  def execute(self, event):

    for rule in RULES:

      if rule.has_condition_met(event):

        rule.execute(event)


class FirstBillPayment(Rule):

  def has_condition_met(self, event):

    # query db or any storage to this user's payment records.

    # if records:
    #   return False

    # return True

    return True

  def execute(self, event):

    print "sending alert of the 1st payment"

RulesEngine.register_rule(FirstBillPayment())


class TimeSensativePayment(Rule):

  def has_condition_met(self, event):

    # query db or any storage to this user's payment records.
    # get all user's records in last 5 mins
    # if not (5 or more records found )
    # return False
    # else take a total of all of them, if it exceeds 20000, then
    # send alert.

    # if records:
    #   return False

    # return True

    return True

  def execute(self, event):

    print "sending alert for 5 or more bill pay events of total value >= 20000 happened within 5 minutes"

RulesEngine.register_rule(TimeSensativePayment())


class FeedbackPostedPayment(object):

  def has_condition_met(self, event):

    # query db or any storage to this user's payment records with event name as feedback and bill pay.
    # if bill pay event is done but correspoding feedback event is not there then execute this

    # if records:
    #   return False

    # return True

    return True

  def execute(self, event):

    print "sending alert for feedback email not gone after bill paid, send alert to cube team."

RulesEngine.register_rule(FeedbackPostedPayment())


if __name__ == "__main__":

  print "\n===================\n"
  print RulesEngine().execute({"name": "namita"})
  print "\n===================\n"

