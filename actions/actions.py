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

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# class ActionRest(Action):

#     def name(self) -> Text:
#         return "action_rest"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         data_file = pd.read_excel("menus.xlsx",sheet_name="RestCoff")
#         # data = pd.DataFrame(data=({'RegID':data_file['Registration Id'],'Age':data_file['Age Years'],'Gender':data_file['Gender Name'], 'RDW':data_file['RDW'],'MCH':data_file['MCH'], \
#         #                    'MCHC':data_file['MCHC'],'MCV':data_file['MCV'],'RCC':data_file['Red cell count'], 'HB': data_file['Hemoglobin'],'Ferritin':data_file['Ferritin In Serum']}),index=None)
#         data_file = data_file[data_file['Rtype']=='Restaurant']
#         rests = data_file.Rname.unique()
#         message = "قائمة المطاعم هي\n"
#         for rest in rests:
#             message += "-  " + rest + "\n"
        
#         # message +="\nبإمكانك اختيار اي منها لعرض المنيو الخاصة به"
#         message +="\nأي منها ترغب في زيارته ! "

#         # print(message)
#         # dispatcher.utter_message(text="Restaurant Enq!")
#         dispatcher.utter_message(text=message)

#         return []

class ActionCoff(Action):

    def name(self) -> Text:
        return "action_coff"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        data_file = pd.read_excel("menus.xlsx",sheet_name="RestCoff")
        # data = pd.DataFrame(data=({'RegID':data_file['Registration Id'],'Age':data_file['Age Years'],'Gender':data_file['Gender Name'], 'RDW':data_file['RDW'],'MCH':data_file['MCH'], \
        #                    'MCHC':data_file['MCHC'],'MCV':data_file['MCV'],'RCC':data_file['Red cell count'], 'HB': data_file['Hemoglobin'],'Ferritin':data_file['Ferritin In Serum']}),index=None)
        data_file = data_file[data_file['Rtype']=='Cafe']
        rests = data_file.Rname.unique()
        message = "قائمة المقاهي هي\n"
        for rest in rests:
            message += "- " + rest + "\n"
        
        message +="\nبإمكانك اختيار اي منها لعرض المنيو الخاصة به"

        # print(message)
        # dispatcher.utter_message(text="Restaurant Enq!")
        dispatcher.utter_message(text=message)

        return []

class ActionRest(Action):

    def name(self) -> Text:
        return "action_rest"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data_file = pd.read_excel("menus.xlsx",sheet_name="Rests")
        cuisine_type = tracker.slots.get('cuisine')
        ord_items = tracker.slots.get('ord_items')
        #print("Slot: ", ord_items)

        # print(cuisine_type)
        
        if cuisine_type is None:
            dispatcher.utter_message(response="utter_Rest_Enquiry")
        
        else:
            if ord_items == None:
                #ord_items = cuisine_type
                print("noneeee")
                SlotSet("ord_items",cuisine_type)
            else:
                ord_items = ord_items + ' __ ' + cuisine_type
                #print(ord_items)
                [SlotSet("ord_items",ord_items)]
                print(tracker.slots.get('ord_items'))



            #ord_items = "1- " + str(cuisine_type)
            #SlotSet("ord_items",ord_items)
            #print("solot set")
            #print(cuisine_type)
            rests = data_file[data_file['cuisine'] == cuisine_type]
            #print(len(rests))
            # rests = data_file
            message = "هذه قائمة بالمطاعم التي توفر " + cuisine_type + ": \n"
            
            #print(tracker.slots.get('ord_items'))

            for index, rest in rests.iterrows():
                message += " \n "
                message += rest['RName'] + "\n"
                message += "-  العنوان: " + rest['address'] + "\n"
                message += "-  الموقع:" + rest['location'] + "\n\n"
            
            message += "\nاكتب اسم المطعم إذا كنت تريد الحجز لديه"
            dispatcher.utter_message(text=message)


        #####################################################
        # data_file = data_file[data_file['Rtype']=='Restaurant']
        # rests = data_file.Rname.unique()
        # message = "قائمة المطاعم هي\n"
        # for rest in rests:
        #     message += "-  " + rest + "\n"
        return [SlotSet("ord_items",ord_items)]

class ActionBook(Action):

    def name(self) -> Text:
        return "action_book_table"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data_file = pd.read_excel("menus.xlsx",sheet_name="Rests")
        rest_name = tracker.slots.get('rest_name')

        # print(cuisine_type)
        
        if rest_name is not None:
            # dispatcher.utter_message(response="utter_Rest_Enquiry")
            message = "لقد تم الحجز في "
            message += rest_name
            dispatcher.utter_message(text=message)


        return []