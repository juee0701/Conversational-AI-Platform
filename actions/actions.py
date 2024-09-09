import datetime as dt
import yake
from typing import Any, Text, Dict, List
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from difflib import SequenceMatcher

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # data=[{"label":" Personal Loan EMI Calculator","value":"/inform{'slot_name':'option1'}"},{"label":"Car Loan EMI Calculator","value":"/inform{'slot_name':'option2'}"},{"label":"Home Loan EMI Calculator","value":"/inform{'slot_name':'option3'}"}]
        # message={"payload":"dropDown","data":data}
        # dispatcher.utter_message(text="Choose your EMI Calculator:"  ,json_message=message)
        dispatcher.utter_message("  Custom action is running!")
        doc = tracker.latest_message['text']
        details = doc.split(",")
        p=float(details[0])
        n=float(details[1])*12
        r=float(details[2])/1200
        EMI = ((p * r * ((1 + r)**n))/((1 + r)**n - 1))
        dispatcher.utter_message("EMI per month:")
        dispatcher.utter_message(text=f"{EMI}")    
       
                

        return []
    
class ActionLoan(Action):
    
    def name(self) -> Text:
        return "action_loan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("  Custom action is running!")
        doc = tracker.latest_message['text']
        details = doc.split(",")
        age=int(details[0])
        job=int(details[1])
        curr=int(details[2])
        sal = int(details[3])
        if (age>=18 and age<=60) and (job>=2) and (curr>=1) and (sal>=25000):
            dispatcher.utter_message("Yes, you are eligible to apply for a loan.")
        else:
            dispatcher.utter_message("Sorry, you are not eligible to apply for a loan.")  
       
                

        return []


