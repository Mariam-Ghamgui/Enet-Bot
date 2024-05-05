# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import psycopg2

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        dispatcher.utter_message(text="Hi! I am your Enet'Bot assistant!")

        button_resp = [
            {
                "title": "English",
                "payload": "English"
            },
            {
                "title": "French",
                "payload": "French"
            }
        ]
        dispatcher.utter_message(text="Please choose a language", buttons=button_resp)
        return []


class ActionHandleLanguageChoice(Action):
    def name(self) -> Text:
        return "action_handle_language_choice"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        language_choice = tracker.latest_message['text']  # Get the user's choice

        # Handle different contact choices
        if language_choice == "English":
            dispatcher.utter_message(text="How can i assist you?")
        elif language_choice == "French":
            dispatcher.utter_message(text="Coment je peux vous aider?")
        
        else:
            dispatcher.utter_message(text="Invalid choice. Please choose a valid contact type.")

        return []

# actions.py
import psycopg2

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List




class ActionSendOrientationPlanImage(Action):
    def name(self) -> Text:
        return "action_send_orientation_plan_image"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the image URL for the orientation plan of ENET'Com
        image_url = "https://enetcom.rnu.tn/userfiles/images/orientation%20R_D_page-0001.jpg"

        # Send the image message as a response
        dispatcher.utter_message(text="Here is the Plan d'orientation de l'ENET'Com", image=image_url)
        return []


class ActionSendUniversityVideo(Action):
    def name(self) -> Text:
        return "action_send_university_video"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the YouTube video link
        image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7XFaHTfSx83J-PZNmsugWKvLzWsxSP1269g&usqp=CAU"

        

        # Send the video message as a response
        dispatcher.utter_message(text="Check this video about ENET'Com", image=image_url)
        return []
    
class ActionSendPdfAttachment(Action):
    def name(self) -> Text:
        return "action_send_pdf_attachment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the PDF data
        pdf_data = {
            "title": "Internal Regulations 2023/2024",
            "payload": "pdf_attachment",
            "url": "https://enetcom.rnu.tn/userfiles/files/AU_2023-2024/R%C3%A8glement%20Int%C3%A9rieur%20Ing%C3%A9nieur%202023%202024%20.pdf"
        }
        # Send the PDF attachment response
        dispatcher.utter_message(text="Here are the internal regulations for 2023/2024:")
        dispatcher.utter_message(json_message=pdf_data)
        return []
 

   



class ActionSendDepartmentsCollapsible(Action):
    def name(self) -> Text:
        return "action_send_departments_collapsible"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the data for departments with English titles and descriptions
        data = [
            {
                "title": "Data Engineering and Decision Support Systems",
                "description": "The Data Engineering and Decision Support Systems (DEDS) program aims to meet the needs of companies operating in data-related sectors. This program introduces high-quality training in cutting-edge technologies related to data science and business intelligence. You can find the study plan in the following link https://enetcom.rnu.tn/userfiles/files/Plan-Etudes/IDSD_23-24.pdf"
            },
            {
                "title": "Telecommunications Engineering",
                "description": "Since the establishment of ENET’Com in 2014, the Telecommunications department has been involved in training high-level engineers in various activities related to the Telecommunications field. related sectors. You can find the study plan in the following link https://enetcom.rnu.tn/userfiles/files/Plan-Etudes/GT_23-24.pdf"
            },
            {
                "title": "Industrial Computer Engineering",
                "description": "The Industrial Computer Engineering (ICE) program at ENET’Com aims to meet the needs of manufacturing companies in terms of highly skilled professionals in the fields of computer engineering and industrial computing. You can find the study plan in the following link https://enetcom.rnu.tn/userfiles/files/Plan-Etudes/GII_23-24.pdf"
            },
            {
                "title": "Electronic Communication Systems Engineering",
                "description": "The Electronic Communication Systems Engineering (ECSE) program at ENET’Com aims to train high-level engineers in various activities in the field of Electronics and Embedded Systems. You can find the study plan in the following link https://enetcom.rnu.tn/userfiles/files/Plan-Etudes/GEC_23-24.pdf"
            }
        ]

        # Create the message payload with the collapsible data
        message = {
            "payload": "collapsible",
            "data": data
        }

        # Send the collapsible message as a response
        dispatcher.utter_message(text="Here are the departments at ENET’Com:", json_message=message)
        return []


class ActionSendTrainingCarousel(Action):
    def name(self) -> Text:
        return "action_send_training_carousel"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the data for the carousel
        carousel_data = {
            "payload": "cardsCarousel",
            "data": [
                {
                    "image": "https://i.postimg.cc/rmyZkQW1/Engineering.png",
                    "title": "Engineering",
                    "ratings": "4.5",
                },
                {
                    "image": "https://i.postimg.cc/T1fdf80k/License.png",
                    "title": "Unified Bachelor's",
                    "ratings": "4.0",
                },
                {
                    "image": "https://i.postimg.cc/jqM0LJSq/Masters.png",
                    "title": "Master's",
                    "ratings": "4.0",
                },
                {
                    "image": "https://i.postimg.cc/pdJc4g9V/Phd.png",
                    "title": "Phd in STIC",
                    "ratings": "4.0",
                }
            ]
        }

        # Send the carousel response
        dispatcher.utter_message(json_message=carousel_data)
        return []

class ActionSendProfessorsChart(Action):
    def name(self) -> Text:
        return "action_send_professors_chart"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the chart data for professors
        data = {
            "title": "Professors at ENET’Com (2023/2024)",
            "labels": ["Professeurs", "Maîtres de Conférences", "Maîtres Assistants", "Assistants", "PES"],
            "backgroundColor": ["#36a2eb", "#ffcd56", "#ff6384", "#4caf50", "#c45850"],
            "chartsData": [14, 12, 86, 8, 9],  # Update with actual data
            "chartType": "pie",
            "displayLegend": "true"
        }

        # Create the message payload with the chart data
        message = {
            "payload": "chart",
            "data": data
        }

        # Send the chart as a response
        dispatcher.utter_message(text="Here is the chart showing the distribution of professors at ENET’Com (2023/2024):", json_message=message)
        return []

class ActionSendInfrastructureChart(Action):
    def name(self) -> Text:
        return "action_send_infrastructure_chart"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the chart data for infrastructure
        data = {
            "title": "Infrastructure at ENET’Com",
            "labels": [
                "Salles d'enseignements",
                "Amphi",
                "Laboratoires (TP)",
                "Salle de projet",
                "Salle de réunion",
                "Centre 4C",
                "Salle de lecture",
                "Laboratoires de recherche",
                "Salle socioculturelle",
                "Salle de thèse",
                "Unité de santé",
                "Magasin",
                "Buvette",
                "Bureaux d’enseignants",
                "Bureaux administratifs",
                "Bibliothèque",
                "Espaces verts"
            ],
            "backgroundColor": [
                "#36a2eb", "#ff6384", "#ffcd56", "#4caf50", "#c45850",
                "#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#f39c12",
                "#2ecc71", "#34495e", "#16a085", "#e67e22", "#2980b9", "#1abc9c"
            ],
            "chartsData": [
                20, 1, 33, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 35, 12, 1, 1
            ],  # Update with actual data
            "chartType": "bar",
            "displayLegend": "true"
        }

        # Create the message payload with the chart data
        message = {
            "payload": "chart",
            "data": data
        }

        # Send the chart as a response
        dispatcher.utter_message(text="Here is the chart showing the infrastructure at ENET’Com:", json_message=message)
        return []
 

class ActionSendContactQuickReplies(Action):
    def name(self) -> Text:
        return "action_send_contact_quick_replies"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the data for quick replies about contact info
        data = [
            {
                "title": "Phone",
                "payload": "phone"
            },
            {
                "title": "Fax",
                "payload": "fax"
            },
            {
                "title": "Email",
                "payload": "email"
            }
        ]

        # Create the message payload with quick replies
        message = {
            "payload": "quickReplies",
            "data": data
        }

        # Send the quick replies message as a response
        dispatcher.utter_message(text="Please choose a contact type:", json_message=message)
        return []
    


class ActionHandleContactChoice(Action):
    def name(self) -> Text:
        return "action_handle_contact_choice"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        contact_choice = tracker.latest_message['text']  # Get the user's choice

        # Handle different contact choices
        if contact_choice == "phone":
            dispatcher.utter_message(text="Phone: 74 863 047 / 74 862 500")
        elif contact_choice == "email":
            dispatcher.utter_message(text="Email: contact@enetcom.usf.tn")
        elif contact_choice == "fax":
            dispatcher.utter_message(text="Fax: 74 863 037")
        else:
            dispatcher.utter_message(text="I can't understand what you're asking for. Can you please rephrase?")

        return []


import geopy.distance

class ActionSendLocation(Action):
    def name(self) -> Text:
        return "action_send_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Coordinates of Enetcom University
        enetcom_coords = (34.8382270587061, 10.754945692549999)
        
        # Get user's location from tracker
        user_latitude = tracker.latest_message.get("latitude")
        user_longitude = tracker.latest_message.get("longitude")
        
        # Calculate distance between user and Enetcom University
        user_coords = (user_latitude, user_longitude)
        distance_km = geopy.distance.geodesic(user_coords, enetcom_coords).kilometers
        
        # Address of Enetcom University
        enetcom_address = "Route de Tunis, cité el Ons, Technopôle de Sfax - 3018 Sfax"
        
        # Create message with address and distance
        message = f"The address of Enetcom University is {enetcom_address}.\n"
        message += f"The distance between you and Enetcom University is approximately {distance_km:.2f} kilometers."
        
        dispatcher.utter_message(message)

        return []

   

class ActionSendRoleOptions(Action):
    def name(self) -> Text:
        return "action_send_role_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = [
            {"label": "Professor", "value": "Professor"},
            {"label": "Administrator", "value": "Administrator"},
            {"label": "Visitor", "value": "Visitor"},
            {"label": "Student", "value": "Student"}
        ]
        message = {"payload": "dropDown", "data": data}
        dispatcher.utter_message(text="Please indicate your role:", json_message=message)
        return []
    
class ActionStoreUserRole(Action):
    def name(self) -> Text:
        return "action_store_user_role"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_role = tracker.latest_message.get('text')
        if user_role not in ['Professor', 'Administrator', 'Visitor', 'Student']:
            dispatcher.utter_message("Please select a valid role.")
            return []

        try:
            # MongoDB connection string with the database name
            uri = "mongodb+srv://rasa:rasabot@cluster0.ukiftw4.mongodb.net/rasa_logs?retryWrites=true&w=majority&appName=Cluster0"

            # Create a new client and connect to MongoDB
            client = MongoClient(uri)

            # Access or create a database and collection
            db = client["rasa"]
            collection = db["Users_Role"]

            # Create a document to insert into the collection
            document = {
                "timestamp": datetime.datetime.now(),
                "user_id": tracker.sender_id,
                "user_role": user_role
            }

            # Insert the document into the collection
            collection.insert_one(document)

            dispatcher.utter_message("Thank you for your answer! GoodBye!")
        except ConnectionFailure as e:
            dispatcher.utter_message("There was a problem connecting to the database.")
            print(f"Connection error: {e}")

        return []

class QueryDatabase(Action):
    def name(self) -> Text:
        return "action_query_database"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="university_db",
            user="postgres",
            password="mariam",
            port="5432"
        )
        
        # Execute SQL query
        query = "SELECT event_name, event_date, location, description, organizer FROM events;"
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        
        # Close database connection
        cursor.close()
        conn.close()
        
        # Send response back to the user
        if results:
            for result in results:
                event_name, event_date, location, description, organizer = result
                message = f"Event: {event_name}\nDate: {event_date}\nLocation: {location}\nDescription: {description}\nOrganizer: {organizer}"
                dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="No events found.")

        return []



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import datetime

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the fallback message from the tracker
        fallback_message = tracker.latest_message.get("text", "")

        try:
            # MongoDB connection string with the database name
            uri = "mongodb+srv://rasa:rasabot@cluster0.ukiftw4.mongodb.net/rasa_logs?retryWrites=true&w=majority&appName=Cluster0"

            # Create a new client and connect to MongoDB
            client = MongoClient(uri)
            
            # Access or create a database and collection
            db = client["rasa"]
            collection = db["unknown_questions"]
            
            # Create a document to insert into the collection
            document = {
                "timestamp": datetime.datetime.now(),
                "unknown_questions": fallback_message,
                "sender_id": tracker.sender_id
            }
            
            # Insert the document into the collection
            collection.insert_one(document)
            
            dispatcher.utter_message("I'm sorry, I didn't understand that. Can you please rephrase?")
            
        except ConnectionFailure as e:
            dispatcher.utter_message("There was a problem connecting to the database.")
            print(f"Connection error: {e}")
            
        return []


#from typing import Any, Text, Dict, List
#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#
#class ActionDefaultFallback(Action):
#    def name(self) -> Text:
#        return "action_default_fallback"
#
#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        
#        # Get the fallback message from the tracker
#        fallback_message = tracker.latest_message.get("text", "")
#        
#        dispatcher.utter_message("I'm sorry, I didn't understand that. Can you please rephrase?")
#        
#        return []















