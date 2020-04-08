## path 1
* greet
  - action_check_intent
  - utter_greet
* what_problem
  - action_check_intent
  - utter_what_problem
* follow_up
  - action_check_intent
  - action_last_intent
* problem_start
  - action_check_intent
  - utter_problem_start
* associated_factors
  - action_check_intent
  - utter_associated_factors
* radiation
  - action_check_intent
  - utter_radiation
* severity
  - action_check_intent
  - utter_severity
* movements
  - action_check_intent
  - utter_movements
* goodbye
  - action_check_intent
  - utter_goodbye
  
## custom last_intent
* follow_up
  - action_last_intent
