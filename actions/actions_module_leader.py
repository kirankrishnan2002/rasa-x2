# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Dict, Text, List, Optional, Any

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.interfaces import Action
# from rasa_sdk.events import SlotSet
# import pandas as pd
# import random
import math
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#df = pd.read_excel('db.xlsx')
#df.module_name=df.module_name.str.rstrip()
#df.module_leader=df.module_leader.str.rstrip()

class ActionsModuleLeader(Action):
    def name(self) -> Text:
        return "actions_module_leader"

    def run(
        self,
#        slot_value: Any,
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: DomainDict #Dict[Text, Any]
    )  -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(text='me')
        
        module_leader = tracker.get_slot('module_leader')
        module_name = tracker.get_slot('module_name')
        print("ModuleLeaderValue in action module_leader:", module_leader, "module_name:",module_name)
        print(module_leader)
        if module_leader:
            print('in modled loop')
            # dispatcher.utter_message(response = "utter_module_leader")
            if isinstance(module_leader, str):
                print('Im in stg module_leader')
                dispatcher.utter_message(text = f"{module_name} is taught by {module_leader}.")
            elif isinstance(module_leader, list):
                print('Im in list module_leader')
                if isinstance(module_name, list):
                    msg = f"The followng modules are being taught:"
                    msnum = 1
                    for moduleLeader, moduleName in zip(module_leader,module_name):
                        print(moduleLeader)
                        
                        if moduleLeader == "nan":
                            msg = msg + "\n" + str(msnum) + " No module leader name found for " + str(moduleName)
                        if moduleName == "nan":
                            msg = msg + "\n" + str(msnum) + " No module name found for " + str(moduleLeader)
                        if isinstance(moduleLeader, str) and not moduleLeader == "nan" and not moduleName == "nan":
                            msg = msg + "\n" + str(msnum) + " " + str(moduleLeader) + " teaches " + str(moduleName)
                            
                        msnum +=1

                    print(msg)
                    dispatcher.utter_message(text=msg)
        elif module_leader is None or math.isnan(module_leader):
            dispatcher.utter_message(text = "Can't find the name of the module leader in the database please contact support.")
        else:  
            dispatcher.utter_message(text = "Can't find the name of the module leader in the database please contact support.")
        return []
        
