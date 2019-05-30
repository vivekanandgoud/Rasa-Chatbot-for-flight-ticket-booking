from rasa_core_sdk import Action
import requests
import json


class ActionGetNewst(Action):
        
        # Read Json File
                       

	def name(self):
		return 'action_get_news'

	def run(self, dispatcher, tracker, domain):
                
		category = tracker.get_slot('category')
		print(category)
		print("hello")
		message = str(123)
		
		with open('ticket.json') as ticketfile:
                        
                        #TicketList = json.load(ticketfile)
                        #try:
                        TicketList = json.load(ticketfile)
                        #except:
                            #print("no json file loaded for finding Flights")

                        #print(TicketList)
                        #print("given attributes...:",From, Tos, Dates,Connection)
                        valu="Kochi"
                        valu1 ="1290,432,454545,667567,32312"
                        #FlightsFound = TicketList[1]["Airlines"]
                        FlightsFound = [str(i+1) + ") " + ticket["Airlines"]  for i, ticket in enumerate(filter(lambda ticket: ticket["From"] == valu , TicketList))]
                        Ref_no_flight = [str(i+1) + ") " + ticket["Ref_no"]  for i, ticket in enumerate(filter(lambda ticket: ticket["Ref_no"] == valu1 , TicketList))]
                        #Ref_no_flight = [sticket["Ref_no"]  for ticket in enumerate(TicketList)]
                        #print(FlightsFound)
                        message = str("available flight services:")+str(FlightsFound)+ "\n"+str("choose the flight number to confrim")
		dispatcher.utter_message(message)
		#BT=input()
		
                #print("\n Congratulations **** Your Flight:"+FlightsFound[(int(BT)-1)]+"Booked succesfully.")
		return []

class ActionGetFlights(Action):
        
        # Read Json File
                       

	def name(self):
		return 'action_get_Flights'

	def run(self, dispatcher, tracker, domain):
                
		category = tracker.get_slot('category')
		print(category)
		print("hello")
		message = str(123)
		
		with open('ticket.json') as ticketfile:
                        
                        #TicketList = json.load(ticketfile)
                        #try:
                        TicketList = json.load(ticketfile)
                        #except:
                            #print("no json file loaded for finding Flights")

                        #print(TicketList)
                        #print("given attributes...:",From, Tos, Dates,Connection)
                        valu="Kochi"
                        valu1 ="1290,432,454545,667567,32312"
                        #FlightsFound = TicketList[1]["Airlines"]
                        FlightsFound = [str(i+1) + ") " + ticket["Airlines"]  for i, ticket in enumerate(filter(lambda ticket: ticket["From"] == valu , TicketList))]
                        Ref_no_flight = [str(i+1) + ") " + ticket["Ref_no"]  for i, ticket in enumerate(filter(lambda ticket: ticket["Ref_no"] == valu1 , TicketList))]
                        #Ref_no_flight = [sticket["Ref_no"]  for ticket in enumerate(TicketList)]
                        #print(FlightsFound)
                        message = str("available flight services:")+str(FlightsFound)+ "\n"+str("choose the flight number to confrim")
		dispatcher.utter_message(message)
		#BT=input()
		
                #print("\n Congratulations **** Your Flight:"+FlightsFound[(int(BT)-1)]+"Booked succesfully.")
		return []

