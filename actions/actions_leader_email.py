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
import random, math
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#df = pd.read_excel('db.xlsx')
#df.module_name=df.module_name.str.rstrip()
#df.module_leader=df.module_leader.str.rstrip()

class ValidateLeaderEmail(Action):
    def name(self) -> Text:
        return "actions_leader_email"

    def run(
        self,
#        slot_value: Any,
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        slot_value = tracker.get_slot('leader_email')
        module_name = tracker.get_slot('module_name')

        if slot_value:
            if isinstance(module_name, str):
                dispatcher.utter_message(response = "utter_leader_email")
            if isinstance(module_name, list):
                msg = "Following are the module email:\n"
                for modnme, modeml in zip(module_name, slot_value):
                    msg = msg + str(modnme) + ": " + str(modeml) + "\n"
        elif slot_value is None or math.isnan(slot_value):
            dispatcher.utter_message(text = "Can't find the email in the database please contact support.")
        else:
            dispatcher.utter_message(text = "Can't find the email in the database please contact support.")

        
