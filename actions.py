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
        #print(what)
        #print("++++++++++++++++++++++++++++++++++++++")
        length_of_list_what=len(what)
        #print(length_of_list_what)
        complete_list_items=length_of_list_what-4
        occurrence=complete_list_items/4
        occurrence=int(occurrence)
        #print("occurrence is")
        #print(occurrence)
		
        print("====ITEMS ARE====")
        #print(str(what))
        #print(*what, sep = "\n\n\n")
              
        listToStr = ' '.join([str(elem) for elem in what])
        ini_str=listToStr           
        ### TO FIND USER ###

        substr="user"       
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
        #ini_str=ini_str[:12]
        ini_str = ini_str.partition("'")[0]
        #print(ini_str)       
                   
        dispatcher.utter_message(ini_str)
		
		#print("always")
        if ini_str=='site':
            dispatcher.utter_message("The pain is in my right knee.")
        elif ini_str=="exacerbating_factors":
            dispatcher.utter_message("No doctor, the pain is nt reducing, I tried rubbing medicinal creams and even did hot compression yet no improvement.")
        elif ini_str=="associated_factors":
            dispatcher.utter_message("I haven't noticed any symptoms. It starts anytime when I walk alot.")
        elif ini_str=="character":
            dispatcher.utter_message("The pain is really sharp and at times unbearable. I have to do hot compression in order to provide a little relief.")
        elif ini_str=="problem_start":
            dispatcher.utter_message("The pain started like almost a week back, I can't remember the exact date but I am sure that it hasn't been more than a week.")
        elif ini_str=="what_problem":
            dispatcher.utter_message("Doctor my knee hurts. It's usually the right knee that always pains.")
        elif ini_str=="radiation":
            dispatcher.utter_message("The pain is everywhere in my knee. It doesn't subsides or moves anywhere else.")
        elif ini_str=="severity":
            dispatcher.utter_message("It's quite severe doctor. I am unable to walk even for five minutes once the pain starts. It escalates very quickly.")
        elif ini_str=="movements":
            dispatcher.utter_message("I do a lot of running and other cardio exercises. I also lift heavy weights.")
        elif ini_str=="problem_before":
            dispatcher.utter_message("No ! I haven't experianced this pain ever before.")
        elif ini_str=="name":
            dispatcher.utter_message("I am 22 years old and I have a very active and healthy lifestyle. I don't have any history of diseases or bone problems.")
        elif ini_str=="medications":
            dispatcher.utter_message("I have paracetamol as pain killer at times since the pain is unbearable. When pain killers are not needed I apply some pain reducing cream.")
        else:
            dispatcher.utter_message("Not matched to any intent")

        return []
