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
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import math

### for local
df = pd.read_excel('actions/db.xlsx')

### for production
# df = pd.read_excel('/app/actions/db.xlsx')
# df = df.dropna()
df.fillna('nan', inplace = True)
df.module_name=df.module_name.str.rstrip().str.lstrip()
df.module_leader=df.module_leader.str.rstrip().str.lstrip()

# from .helpers import slot_return
class ValidateModuleForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_module_form"

    # def required_slots(
    #     self,
    #     slots_mapped_in_domain: List[Text],
    #     dispatcher: "CollectingDispatcher",
    #     tracker: "Tracker",
    #     domain: "DomainDict",
    # ) -> Optional[List[Text]]:
    #     required_slots = slots_mapped_in_domain + ["module_name"]
    #     return required_slots
        
    def validate_module_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: DomainDict
    )-> Dict[Text, Any]:
        lst = []
        print("slot_value in module name", slot_value)
        if type(slot_value)==list:
            slot = slot_value[0].lower()
        else:
            slot = slot_value.lower()

        # if math.isnan(slot_value):
        #     return {
        #         "module_name":"nan"
        #     }

        # if slot_value=="Artificial Intelligence":
        #     return {
        #     "module_name": ["Artificial Intelligence"]
        #     }

        # module_name_dict = [mod[0] for mod in process.extract(slot, list(df.module_name), limit=5) if mod[1]>90]
        # if len(module_name_dict)==1:
        #     df_mod_name = df.query(f"module_name=='{module_name_dict[0]}'")
        #     return {"db_id": str(df_mod_name.index[0]),
        # "module_name": df_mod_name['module_name'].item(),
        # "module_code": df_mod_name['module_code'].item(),
        # "module_leader": df_mod_name['module_leader'].item(),
        # "leader_email": df_mod_name['leader_email'].item(),
        # "credits": df_mod_name['credits'].item(),
        # "assg": df_mod_name['assg'].item(),
        # "assg_weight": df_mod_name['assg_weight'].item()
        #     }
        
        module_name_lst = [mod[0] for mod in process.extract(slot, list(df.module_name.unique()), limit=5) if mod[1]>85]
        if slot == 'artificial intelligence':
            module_name_lst.append([i for i in list(df.module_name.unique()) if 'ai' in i.lower().split()][0])
        print("module_name_lst:00 ",module_name_lst)
        if len(module_name_lst)>=1:
            df_mod_name = df.query(f"module_name==@module_name_lst")
            print("dfmodname",df_mod_name)
            if len(list(df_mod_name['module_name']))==1:
                print('insideiff')
                return {"db_id": str(df_mod_name.index[0]),
                        "module_name": df_mod_name['module_name'].item(),
                        "module_code": df_mod_name['module_code'].item(),
                        "module_leader": df_mod_name['module_leader'].item(),
                        "leader_email": df_mod_name['leader_email'].item(),
                        "credits": df_mod_name['credits'].item(),
                        "assg": df_mod_name['assg'].item(),
                        "assg_weight": df_mod_name['assg_weight'].item()
                            }
                
            elif len(list(df_mod_name['module_name']))>1:
                print('insideeelif')
                return {"db_id": list(df_mod_name.index.astype('str')),
                        "module_name": list(df_mod_name['module_name']),
                        "module_code": list(df_mod_name['module_code']),
                        "module_leader": list(df_mod_name['module_leader']),
                        "leader_email": list(df_mod_name['leader_email']),
                        "credits": list(df_mod_name['credits']),
                        "assg": list(df_mod_name['assg']),
                        "assg_weight": list(df_mod_name['assg_weight'])
                            }
        


#slot_return(self, slot_name='module_name', slot_dict = module_name_dict)
        # elif len(module_name_lst)>1:
        #     lst = ['Please select one module from', 
        #     'These are the available modules',
        #     'Your choices for modules are']
        #     buttons = []
        #     module_lst = [mod[0] for mod in process.extract(slot, list(df.module_name.unique()), limit=5) if mod[1]>40]
        #     for mnd in module_lst:
        #         buttons.append({"payload": f"/{mnd}", "title": f"{mnd}"})
        #     dispatcher.utter_message(text = random.choice(lst) + ':\n')
        #     dispatcher.utter_message(buttons = buttons)
        #     return {
        #     "module_name": None
        #     }
        # elif len(module_name_lst)>1:
        #     lst = ['Please select one module from', 
        #     'These are the available modules',
        #     'Your choices for modules are']
        #     buttons = []
        #     for mnd in [mod[0] for mod in process.extract(slot, list(df.module_name), limit=5) if mod[1]>40]:
        #         buttons.append({"payload": f"/{mnd}", "title": f"{mnd}"})
        #     dispatcher.utter_message(text = random.choice(lst) + ':\n')
        #     dispatcher.utter_message(buttons = buttons)
        #     return {
        #     "module_leader": None
        #     }
        else:
            dispatcher.utter_message(text = "Can't find anyone with that name in the database...")
            return {
            "module_leader": None
            }
        


    def validate_module_code(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: DomainDict
    ) -> Dict[Text, Any]:
        lst = []
        print("slot_value in module code", slot_value)
        
        if type(slot_value)==list:
            slot = slot_value[0].lower()
        else:
            slot = slot_value.lower()

        # if slot_value in ['.nan','nan']:
        #     return {
        #         "module_code":"nan"
        #     }

        module_code_lst = [mod[0] for mod in process.extract(slot, list(df.module_code.unique()), limit=5) if mod[1]>90]

        if len(module_code_lst)==1:
            df_mod_name = df.query(f"module_code=='{module_code_lst[0]}'")
            return {"db_id": str(df_mod_name.index[0]),
        "module_name": df_mod_name['module_name'].item(),
        "module_code": df_mod_name['module_code'].item(),
        "module_leader": df_mod_name['module_leader'].item(),
        "leader_email": df_mod_name['leader_email'].item(),
        "credits": df_mod_name['credits'].item(),
        "assg": df_mod_name['assg'].item(),
        "assg_weight": df_mod_name['assg_weight'].item()
            }
#slot_return(self, slot_name='module_code', slot_dict = module_code_lst)
        elif len(module_code_lst)>1:
            lst = ['Please select one module code from', 
            'These are the available module codes',
            'Your choices for modules codes are']
            buttons = []
            for mnd in [mod[0] for mod in process.extract(slot, list(df.module_code), limit=5) if mod[1]>40]:
                buttons.append({"payload": f"/{mnd}", "title": f"{mnd}"})
            dispatcher.utter_message(text = random.choice(lst) + ':\n')
            dispatcher.utter_message(buttons = buttons)
            return {
            "module_code": None
            }


    def validate_module_leader(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: DomainDict
    ) -> Dict[Text, Any]:
        lst = []
        print("slot_value in module leader name", slot_value)
        print("value of moduleleader:", tracker.get_slot('module_leader'))
        if type(slot_value)==list:
            slot = slot_value[0].lower()
        else:
            slot = slot_value.lower()
        
        # if slot_value in ['.nan','nan']:
        #     return {
        #         "module_leader":"nan"
        #     }

        module_leader_lst = [mod[0] for mod in process.extract(slot, list(df.module_leader.unique()), limit=5) if mod[1]>90]
        print("module_leader_lst:00 ",module_leader_lst)
        if len(module_leader_lst)>=1:
            df_mod_leader = df.query(f"module_leader=='{module_leader_lst[0]}'")
            if len(list(df_mod_leader['module_name']))==1:
                return {"db_id": str(df_mod_leader.index[0]),
                        "module_name": df_mod_leader['module_name'].item(),
                        "module_code": df_mod_leader['module_code'].item(),
                        "module_leader": df_mod_leader['module_leader'].item(),
                        "leader_email": df_mod_leader['leader_email'].item(),
                        "credits": df_mod_leader['credits'].item(),
                        "assg": df_mod_leader['assg'].item(),
                        "assg_weight": df_mod_leader['assg_weight'].item()
                            }
                
            elif len(list(df_mod_leader['module_name']))>1:
                return {"db_id": list(df_mod_leader.index.astype('str')),
                        "module_name": list(df_mod_leader['module_name']),
                        "module_code": list(df_mod_leader['module_code']),
                        "module_leader": list(df_mod_leader['module_leader']),
                        # [:1:].item(),
                        "leader_email": list(df_mod_leader['leader_email']),
                        # [:1:].item(),
                        "credits": list(df_mod_leader['credits']),
                        "assg": list(df_mod_leader['assg']),
                        "assg_weight": list(df_mod_leader['assg_weight'])
                            }
#slot_return(self, slot_name='module_code', slot_dict = module_name_lst)
        # elif len(module_leader_lst)>1:
        #     lst = ['Please select one module leader from', 
        #     'These are the available module leader',
        #     'Your choices for modules leader are']
        #     buttons = []
        #     for mnd in [mod[0] for mod in process.extract(slot, list(df.module_leader), limit=5) if mod[1]>40]:
        #         buttons.append({"payload": f"/{mnd}", "title": f"{mnd}"})
        #     dispatcher.utter_message(text = random.choice(lst) + ':\n')
        #     dispatcher.utter_message(buttons = buttons)
        #     return {
        #     "module_leader": None
        #     }
        else:
            dispatcher.utter_message(text = "Can't find anyone with that name in the database...")
            return {
            "module_leader": None
            }

# class ActionResetModuleName(Action):
#     def name(self):
#         return 'action_reset_module_name'

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ):
        
#         return SlotSet("module_name", None)

# class ActionResetModuleNum(Action):
#     def name(self):
#         return 'action_reset_module_num'

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ):
        
#         return SlotSet("module_num", None)


