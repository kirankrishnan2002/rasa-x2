from typing import Dict, Text, List, Optional, Any

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.interfaces import Action
# from rasa_sdk.events import SlotSet

class ActionsModuleLeader(Action):
    def name(self) -> Text:
        return "action_ovr_prog_leader"

    def run(
        self,
#        slot_value: Any,
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: DomainDict #Dict[Text, Any]
    )  -> List[Dict[Text, Any]]:
        
        usr_msg = tracker.latest_message.get('text')
        module_leader = tracker.get_slot('module_leader')
        module_name = tracker.get_slot('module_name')

        msg = f'Susan Atwood is the overall programme leader you can email her at: s.c.attwood@herts.ac.uk'
        print(msg)
        dispatcher.utter_message(text=msg)
        return []
        
