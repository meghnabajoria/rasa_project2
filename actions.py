# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import re
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionLastIntent(Action):

    def name(self) -> Text:
        return "action_last_intent"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        what = tracker.events_after_latest_restart()
              
        listToStr = ' '.join([str(elem) for elem in what])
        ini_str=listToStr           
        ### TO FIND USER ###

        substr="user"
        occurrence=2
        inilist=[m.start() for m in re.finditer(r"user",ini_str)]
        user_counter=inilist[occurrence-1]
        ini_str=ini_str[user_counter:]
        #print(ini_str)

        #-- TO FIND NAME ---
        substr2="name"
        occurrence2=1
        inilist2=[m.start() for m in re.finditer(r"name",ini_str)]
        name_counter=inilist2[occurrence2-1]
        ini_str=ini_str[name_counter:]
        #print(ini_str)

        #^^^ FIND CONFIDENCE ^^^

        substr3="confidence"
        occurrence3=1
        inilist3=[m.start() for m in re.finditer(r"confidence",ini_str)]
        confidence_counter=inilist3[occurrence3-1]
        ini_str=ini_str[:confidence_counter]
        #print(ini_str)

        #=== REMOVE FEW CHAR ===

        ini_str=ini_str[8:]
        ini_str=ini_str[:12]
        #print(ini_str)       
         
        #if what is not None:
        #   dispatcher.utter_message("The last intetnt is {}".format(what))
        #else:
        #   dispatcher.utter_message("I couldn't tell what!")
            
        dispatcher.utter_message(ini_str)

        return []
