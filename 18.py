from cowin_api import CoWinAPI
from playsound import playsound
import time
import smtplib

cowin = CoWinAPI()

while(True):
# 21

	state_id = '21'
	dist_id = '364'
	date = '07-05-2021'
	available_centers = cowin.get_availability_by_district(dist_id,date)

	#exclude these
	ex = ['AWAGHATE BAL RUGNALAYA','Tandali Bu Sub Center']	

	for i in (available_centers['centers']):
		for j in i['sessions']:
			if(j['available_capacity'] > 0 and j['min_age_limit'] == 45 and i['name'] not in ex):

				s = smtplib.SMTP('smtp.gmail.com', 587)
				# start TLS for security
				s.starttls()
				
				# Authentication
				s.login("mail", "password")
				
				# message to be sent   
				SUBJECT = "Book ASAP"   
				TEXT = "THIS UPDATE IS FOR 45+ ONLY \nCenter Available: "+ i['name'] + "\n Address: " +i['address']+"\n Block Name: "+i['block_name']+"\n pincode: "+str(i['pincode'])+"\n Available Seats: "+str(j['available_capacity'])

				message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
				
				# sending the mail
				s.sendmail("mailIdOfSender", '''add receivers mail''' , message)
				
				# terminating the session
				s.quit()
				print("SENT")
				print("Still waiting")
				time.sleep(60)
				'''
				print("Book ASAP")
				print(i['name'])
				while(True):
					playsound('song.mp3')
				'''
				'''
			elif(j['available_capacity'] > 0 and j['min_age_limit'] == 18):
				s = smtplib.SMTP('smtp.gmail.com', 587)
				# start TLS for security
				s.starttls()
				
				# Authentication
				s.login("mailID", "password")
				
				# message to be sent   
				SUBJECT = "Book ASAP"   
				TEXT = "THIS UPDATE IS FOR 18+ ONLY \nCenter Available: "+ i['name'] + "\n Address: " +i['address']+"\n Block Name: "+i['block_name']+"\n pincode: "+str(i['pincode'])+"\n Available Seats: "+str(j['available_capacity'])

				message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
				
				# sending the mail
				s.sendmail("Sender Email",''add receivers mail'', message)
				
				# terminating the session
				s.quit()
				print("SENT")
				print("still waiting")
				time.sleep(60)
				'''
			else:
				print("Not Yet")
				time.sleep(10)
					
