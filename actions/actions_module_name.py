# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Dict, Text, List, Optional, Any

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.interfaces import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import random
import math
# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process

#df = pd.read_excel('db.xlsx')
#df.module_name=df.module_name.str.rstrip()
#df.module_leader=df.module_leader.str.rstrip()

class ActionsLeaderName(Action):
    def name(self) -> Text:
        return "actions_module_name"

    def run(
        self,
#        slot_value: Any,
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        print("\nAction Module Name:")
        # slot_value = tracker.get_slot('module_name')
        module_name = tracker.get_slot('module_name')
        print("slot value in action mod leader",module_name)
        module_leader = tracker.get_slot('module_leader')
        if module_name:
            # print("in slotvalue")
            # print(type(module_name))
            
            if isinstance(module_name, str):
                # print('Im in stg')
                dispatcher.utter_message(text = f"{module_leader} teaches {module_name}."
                    # response = "utter_module_name"
                    )
            elif isinstance(module_name, list):
                # print('Im in list')
                msg = f"The followng modules are being taught by {module_leader}:"
#                dispatcher.utter_message(text=msg)
                for msnum, mg in enumerate(module_name):
                    #msg = msg +
                    #msg = f"{msnum+1}. {mg}"
                    msg = msg + "\n" + str(msnum+1) + " " + str(mg) + "\n"
#                    dispatcher.utter_message(text=msg)
                print(msg)
                dispatcher.utter_message(text=msg)
        elif module_name is None or math.isnan(module_name):
            dispatcher.utter_message(text = "Can't find the module name in the database please contact support.")
        else:
            dispatcher.utter_message(text = "Can't find the module name in the database please contact support.")

        
