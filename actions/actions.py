# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd

class ActionRest(Action):

    def name(self) -> Text:
        return "action_option"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        selected_number = tracker.slots.get('selected_number')
        
        selected_options = selected_options + selected_number + '-'
        [SlotSet("selected_options",selected_options)]

        print(selected_options)


        ###############################################################################
        
        # if cuisine_type is None:
        #     dispatcher.utter_message(response="utter_Rest_Enquiry")
        
        # else:
        #     if ord_items == None:
        #         #ord_items = cuisine_type
        #         print("noneeee")
        #         SlotSet("ord_items",cuisine_type)
        #     else:
        #         ord_items = ord_items + ' __ ' + cuisine_type
        #         #print(ord_items)
        #         [SlotSet("ord_items",ord_items)]
        #         print(tracker.slots.get('ord_items'))


        dispatcher.utter_message(text=selected_options)

        return [SlotSet("ord_items",ord_items)]
