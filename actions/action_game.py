import requests
from typing import Dict, Text, Any, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ActionGame(Action):

    def name(self) -> Text:
        return "action_game"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        games = [
            {"name": "Chess", "link": "https://www.chess.com/"},
            {"name": "Monopoly", "link": "https://www.gameflare.com/online-game/monopoly-online/"},
            {"name": "Slither.io", "link": "https://slither.io/"},
            {"name": "Uno", "link": "https://www.crazygames.com/game/uno-online"}
        ]
        
        message = "Here are some games you can play:\n"
        buttons = []
        for game in games:
            # message += f"- {game['name']}\n"
            buttons.append({"title": game["name"], "payload": game["link"]})
            
        
        dispatcher.utter_message(text=message, buttons=buttons)

        return []