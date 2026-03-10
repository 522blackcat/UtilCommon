import datetime

import rule_engine
from numbers import Number
from rule_engine import Rule, Context, type_resolver_from_dict

# context = Context(type_resolver=rule_engine.type_resolver_from_dict({
#     "a": rule_engine.DataType.STRING,
#     'b': rule_engine.DataType.FLOAT,
#     'c': rule_engine.DataType.FLOAT
# }))
#
# rule = Rule(
#     'a in ["1", "2", "3", "4"] and  b >= 1 and c < 10',
#     context=context
# )
#
# result = rule.matches({'a': "1", 'b': 1, "c": 20})
# print(result)
#
#
# context = Context(type_resolver=rule_engine.type_resolver_from_dict({
#     "rtm": rule_engine.DataType.STRING,
#     "business_type": rule_engine.DataType.STRING,
#     "lob": rule_engine.DataType.STRING,
#     "sub_lob": rule_engine.DataType.STRING,
#     "fph_level": rule_engine.DataType.FLOAT,
#     "remarks": rule_engine.DataType.STRING,
#     "instock_target": rule_engine.DataType.FLOAT
# }))
# a = "business_type != null and business_type != '' and rtm in ['Mono','Carrier','Multi','Online'] and sub_lob in ['Mono','Carrier','Multi','Online'] and instock_target > 50 and instock_target <= 70"
#
# rule = Rule(a, context=context)
#
#
# context = Context(type_resolver=rule_engine.type_resolver_from_dict({
#     "a": rule_engine.DataType.STRING
# }))
#
# rule1 = Rule(
#     'a =~ "((((19|20)(([02468][048])|([13579][26]))-02-29)|((20[0-9]{2}|19[0-9]{2})-((0[13578]|1[02])-(0[1-9]|[12]\d|3[01])|(0[469]|11)-(0[1-9]|[12]\d|30)|02-(0[1-9]|1\d|2[0-8])))))\s([01]\d|2[0-3]):[0-5]\d:[0-5]\d"',
#     context=context
# )
#
#
#
# result = rule1.matches({"a": '2000-02-29 11:11:11'})
# print("rule1:", result)


# rule2 = Rule(
#     '',
#     context=context
# )


context = Context(type_resolver=rule_engine.type_resolver_from_dict({
    "a": rule_engine.DataType.STRING
}))
rule3 = Rule("a=~'.*'", context=context)
result = rule3.matches({"a": None})
print(result)