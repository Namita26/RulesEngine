from rules.rule import Rule, RulesEngine


class FeedbackPostedPayment(Rule):

  def has_condition_met(self, event):

    # query db or any storage to this user's payment records with event name as feedback and bill pay.
    # if bill pay event is done but correspoding feedback event is not there then execute this

    # if records:
    #   return False

    # return True

    return False

  def execute(self, event):

    print "sending alert for feedback email not gone after bill paid, send alert to cube team."

RulesEngine.register_rule(FeedbackPostedPayment())