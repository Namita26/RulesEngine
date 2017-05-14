RULES = []

class Rule(object):

  # two methods which will be executed
  def has_condition_met(self, event):
    pass

  def execute(self, event):
    pass


class RulesEngine(Rule):

  # set of all rules
  @staticmethod
  def register_rule(rule):
    RULES.append(rule)

  def execute(self, event):

    for rule in RULES:
      if rule.has_condition_met(event):
        rule.execute(event)