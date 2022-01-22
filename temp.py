from cowin_api import CoWinAPI
from playsound import playsound
import time
import smtplib

cowin = CoWinAPI()

while(True):
# 21
	state_id = '21'
	dist_id = '364'
	date = '22-05-2021'
	available_centers = cowin.get_availability_by_district(dist_id,date)

	#exclude these
	ex = ['AWAGHATE BAL RUGNALAYA','Tandali Bu Sub Center']	
	print("Still empty")
	print(available_centers)
	if(available_centers == {'centers': []}):
		time.sleep(10)

	for i in (available_centers['centers']):
		for j in i['sessions']:
			if(j['available_capacity'] > 0 and j['min_age_limit'] == 45 and i['name'] not in ex):
				s = smtplib.SMTP('smtp.gmail.com', 587)
				# start TLS for security
				s.starttls()
				
				# Authentication
				s.login("mailId", "Password")
				
				# message to be sent   
				SUBJECT = "Do you booking ASAP"   
				TEXT = "THIS UPDATE IS FOR 45+ ONLY \nCenter Available: "+ i['name'] + "\n Address: " +i['address']+"\n Block Name: "+i['block_name']+"\n pincode: "+str(i['pincode'])+"\n Available Seats: "+str(j['available_capacity'])

				message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
				
				# sending the mail
				s.sendmail("mailIdOfSender", "mailIdOfReciever", message)
				
				# terminating the session
				s.quit()
				print("IN FOR 2")
				print("SENT")
				print("Still waiting")
				time.sleep(60)
				print("Book ASAAPPP")
				print(i['name'])
				while(True):
					playsound('song.mp3')

			else:
				print("Not Yet")
				time.sleep(10)
