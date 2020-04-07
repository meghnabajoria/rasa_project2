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

class IntetntRecognition(Action):
    def run()
        label_to_idx = {'age': 0,
    	'associated_Factors': 1,
    	'character': 2,
     	'closedQuestions': 3,
     	'concern': 4,
     	'dob': 5,
     	'drugHx': 6,
     	'exacerbating_Factors': 7,
     	'followup': 8,
     	'goodbye': 9,
     	'introduction': 10,
     	'name': 11,
     	'onset': 12,
     	'openQuestions': 13,
     	'pastMedicalHx': 14,
     	'pastSurgicalHx': 15,
     	'probelmStart': 16,
     	'problembefore': 17,
     	'radiation': 18,
     	'reassurance': 19,
     	'severity': 20,
     	'site': 21,
     	'summary': 22,
     	'timing': 23,
     	'transitionPoints': 24,
     	'whatProblem': 25,
    	'follow_up':26,
    	'greet':27}

    # Set to track intents
    intent_tracker = set()

    class ActionCheckIntent(Action):
        def name(self) -> Text:
            return “action_check_intent”

        def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            global label_to_idx, intent_tracker
            for item in reversed(tracker):
	
            if item["event"] == "user":
                intent_code = label_to_idx[item["parse_data"]["intent"]["name"]]
                if intent_code in intent_tracker:
                    dispatcher.utter_message("As I mentioned before")
            else:
                intent_tracker.add(intent_code)
            # Break because we only want the last user intent
            break



class ActionLastIntent(Action):

    def name(self) -> Text:
        return "action_last_intent"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        what = tracker.events_after_latest_restart()
        last_item=what[-5] 
        last_item=str(last_item)
		#print(last_item)
		
        substr0="name"       
        inilist0=[m.start() for m in re.finditer(r"name",last_item)]
        name_counter_lastelement=inilist0[0]
        last_item=last_item[name_counter_lastelement:]
        
        print(last_item)
    
        inilist4=[m.start() for m in re.finditer(r"confidence",last_item)]
        confidence_counter_lastelement=inilist4[0]
        last_item=last_item[:confidence_counter_lastelement]
        print(last_item)
		
        last_item=last_item[8:]
        last_item = last_item.partition("'")[0]
        print("  THE FINAL LAST_ITEM IS")
        print(last_item)
		
        if last_item=="follow_up":
            #print(*what,sep="\n\n\n")
            last_item=what[-9] 
            #print(last_item)
            last_item=str(last_item)
            #print(last_item)
            inilist0=[m.start() for m in re.finditer(r"name",last_item)]
            name_counter_lastelement=inilist0[0]
            last_item=last_item[name_counter_lastelement:]
       
            inilist4=[m.start() for m in re.finditer(r"confidence",last_item)]
            confidence_counter_lastelement=inilist4[0]
            last_item=last_item[:confidence_counter_lastelement]
        		
            last_item=last_item[8:]
            last_item = last_item.partition("'")[0]
            ini_str=last_item
            print("  THE INI_STR IS")
            print(ini_str)
            if ini_str=='site':
                dispatcher.utter_message("As I said earlier, the pain is in my right knee.")
            elif ini_str=="exacerbating_factors":
                dispatcher.utter_message("As mentioned before doctor, the pain is not subsiding, medicinal creams were also not helpfull.")
            elif ini_str=="associated_factors":
                dispatcher.utter_message("As I said earlier,I haven't noticed any symptoms. It starts when I walk alot.")
            elif ini_str=="character":
                dispatcher.utter_message("As I said earlier,The pain is really sharp and at times unbearable. I have to do hot compression in order to provide a little relief.")
            elif ini_str=="problem_start":
                dispatcher.utter_message("As I said earlier,The pain started almost a week back.")
            elif ini_str=="what_problem":
                dispatcher.utter_message("As I said earlier, my knee hurts. It's usually the right knee that always pains.")
            elif ini_str=="radiation":
                dispatcher.utter_message("As I said earlier,the pain is everywhere in my knee. It doesn't subsides or moves anywhere else.")
            elif ini_str=="severity":
                dispatcher.utter_message("As I said earlier,the pain is quite severe doctor. I am unable to walk even for five minutes once the pain starts. It escalates very quickly.")
            elif ini_str=="movements":
                dispatcher.utter_message("As I mentioned, I do a lot of running and other cardio exercises. I also lift heavy weights.")
            elif ini_str=="problem_before":
                dispatcher.utter_message("As I mentioned,I haven't experianced this pain ever before.")
            elif ini_str=="name":
                dispatcher.utter_message("As I mentioned,I am 22 years old and I have a very active and healthy lifestyle. I don't have any history of diseases or bone problems.")
            elif ini_str=="medications":
                dispatcher.utter_message("As I mentioned,I have paracetamol as pain killer at times since the pain is unbearable. When pain killers are not needed I apply some pain reducing cream.")
			
                   
        elif last_item=='site':
            dispatcher.utter_message("The pain is in my right knee.")
        elif last_item=="exacerbating_factors":
            dispatcher.utter_message("No doctor, the pain is nt reducing, I tried rubbing medicinal creams and even did hot compression yet no improvement.")
        elif last_item=="associated_factors":
            dispatcher.utter_message("I haven't noticed any symptoms. It starts anytime when I walk alot.")
        elif last_item=="character":
            dispatcher.utter_message("The pain is really sharp and at times unbearable. I have to do hot compression in order to provide a little relief.")
        elif last_item=="problem_start":
            dispatcher.utter_message("The pain started like almost a week back, I can't remember the exact date but I am sure that it hasn't been more than a week.")
        elif last_item=="what_problem":
            dispatcher.utter_message("Doctor my knee hurts. It's usually the right knee that always pains.")
        elif last_item=="radiation":
            dispatcher.utter_message("The pain is everywhere in my knee. It doesn't subsides or moves anywhere else.")
        elif last_item=="severity":
            dispatcher.utter_message("It's quite severe doctor. I am unable to walk even for five minutes once the pain starts. It escalates very quickly.")
        elif last_item=="movements":
            dispatcher.utter_message("I do a lot of running and other cardio exercises. I also lift heavy weights.")
        elif last_item=="problem_before":
            dispatcher.utter_message("No ! I haven't experianced this pain ever before.")
        elif last_item=="name":
            dispatcher.utter_message("I am 22 years old and I have a very active and healthy lifestyle. I don't have any history of diseases or bone problems.")
        elif last_item=="medications":
            dispatcher.utter_message("I have paracetamol as pain killer at times since the pain is unbearable. When pain killers are not needed I apply some pain reducing cream.")
        else:
            print(last_item)
				
        return []
 
