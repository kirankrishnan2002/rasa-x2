from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction

import random

class AskForVegetarianAction(Action):
    def name(self) -> Text:
        return "action_ask_question"

    # @staticmethod
    # def ques_db() -> Dict[Text]:
    #     """Database of questions"""

    #     return {'modules_tod':'What modules did you have today',
    #             'lec_tod':'How was your lecture',
    #             'eng_sess':'Was your tutorial session engaging',
    #             'hobbies':'What are your hobbies',
    #             'future_end':'What are your future endeavours',
    #             'fav_mov':'What is your favourite movie',
    #             'fav_pizza':'What is your favourite pizza topping',
    #             'extra_cirr':'Do you take part in any extracurricular activities',
    #             'fav_sport':'What is your favourite sport',
    #             'cs_field':'Which field of computer science would you like to specialise in future',
    #             'year_of_Study':'Which year of study are you in',
    #             'passion':'What are you most passionate about',
    #             'ambitions':'What are ambitions for the future',
    #             'talents':'Do you have any hidden talents',
    #             'emojis':'What emoji do you use the most when messaging other people',
    #             'dream_holiday':'Where is your dream holiday destination',
    #             'weekend_plans':'What are your plans for the weekend',
    #             'hoiday_plan':'Any plans for the holidays',
    #             'superpower':'If you had a super power what would it be',
    #             'best_event':'What is the best event you have ever attended?',
    #             'inspiration':'Who is your inspiration'}
    
    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        ques = {'modules_tod':'What modules did you have today',
                'lec_tod':'How was your lecture',
                'eng_sess':'Was your tutorial session engaging',
                'hobbies':'What are your hobbies',
                'future_end':'What are your future endeavours',
                'fav_mov':'What is your favourite movie',
                'fav_pizza':'What is your favourite pizza topping',
                'extra_cirr':'Do you take part in any extracurricular activities',
                'fav_sport':'What is your favourite sport',
                'cs_field':'Which field of computer science would you like to specialise in future',
                'year_of_Study':'Which year of study are you in',
                'passion':'What are you most passionate about',
                'ambitions':'What are ambitions for the future',
                'talents':'Do you have any hidden talents',
                'emojis':'What emoji do you use the most when messaging other people',
                'dream_holiday':'Where is your dream holiday destination',
                'weekend_plans':'What are your plans for the weekend',
                'hoiday_plan':'Any plans for the holidays',
                'superpower':'If you had a super power what would it be',
                'best_event':'What is the best event you have ever attended?',
                'inspiration':'Who is your inspiration',
                'game':"Would you like to play a game and have some fun?\nYou have following options:\n"}
        # self.ques_db()
        typ, ques_msg = random.choice(list(ques.items()))

        if typ == 'lec_tod':
            buttons=[
                {"title": "Good", "payload": "/affirm"},
                {"title": "Bad", "payload": "/deny"}
            ]
        if typ == 'eng_sess':
            buttons=[
                {"title": "Yes", "payload": "/affirm"},
                {"title": "No", "payload": "/deny"}
            ]
        if typ == 'game':
            buttons = [
                {"title": "Chess", "payload": "https://www.chess.com/"},
                {"title": "Monopoly", "payload": "https://www.gameflare.com/online-game/monopoly-online/"},
                {"title": "Slither.io", "payload": "https://slither.io/"},
                {"title": "Uno", "payload": "https://www.crazygames.com/game/uno-online"},
            ]

        if typ in ['lec_tod', 'eng_sess', 'game']:
            dispatcher.utter_message(text=ques_msg,
                                 buttons=buttons)
        else:
            dispatcher.utter_message(text=ques_msg)

        return [SlotSet("dq_type",typ)]
    


class ValidateRestaurantForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_dynamic_form"

    def validate_question(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[Dict[Text, Any]]:#Dict[Text:, Any]:
        """Validate question value."""
        
        required_slots = ["question"]
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot", slot_name)]

        # all slots filled, perform action
        return self.submit(tracker, dispatcher, domain)

    def submit(
            self,
            tracker: Tracker,
            dispatcher: CollectingDispatcher,
            domain: Dict[Text, Any],
        ) -> List[EventType]:
            # question = tracker.get_slot("question")
            intent = tracker.latest_message["intent"].get("name")

            if intent in ['deny']:
                dispatcher.utter_message(text='Oh no')
                return [FollowupAction("action_listen"), SlotSet("requested_slot", None)]
            else:
                dispatcher.utter_message(text='Okay Great')
                return [FollowupAction("action_listen"), SlotSet("requested_slot", None)]
            # return [SlotSet("question", None), SlotSet("requested_slot", None)]
        