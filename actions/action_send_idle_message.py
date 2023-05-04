from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ActionExecuted, UserUtteranceReverted, ConversationPaused, ReminderScheduled
from datetime import datetime, timedelta
import random
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import SlotSet


class SendIdleMessage(Action):
    def name(self) -> Text:
        return "action_send_idle_message"

    # def run(self, dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    #     now = datetime.now()
    #     datetime.datetime.now() + datetime.timedelta(seconds=5)
    #     last_active_time = tracker.latest_message_time
    #     idle_time = now - last_active_time

    #     if idle_time > timedelta(seconds=5):
    #         # User is idle for more than 5 seconds, send a message
    #         dispatcher.utter_message("Hey there, are you still there?")
        
    #     return []
    
    # def supported_events(self) -> List[Text]:
    #     return [ConversationPaused().type_name]
    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List[Dict[Text, Any]]:
        # now = datetime.now()
        # last_active_time = tracker.latest_message_time
        # idle_time = now - last_active_time

        date = datetime.now() + timedelta(seconds=5)
        entities = tracker.latest_message.get("entities")

        # if idle_time > timedelta(seconds=5):
        # dispatcher.utter_message(f"Starting idle timer now")

        # User is idle for more than 5 seconds, schedule a reminder to send a message
        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time=date,
            entities=entities,
            name="user_idle",
            kill_on_user_message=True
        )

        return [reminder]

        # return []

class ActionReactToReminder(Action):
    """Reminds the user to call someone."""

    def name(self) -> List[Dict[Text, Any]]:
        return "action_react_to_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # name = next(tracker.get_slot("PERSON"), "someone")
        
        # dispatcher.utter_message()
        return [SlotSet("question", None), FollowupAction("dynamic_form")]

        # return [FollowupAction("dynamic_form"),
        #         SlotSet("question":None)]