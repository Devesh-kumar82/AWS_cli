import speech_recognition as sr
import os
import pyttsx3
import getpass
#import pywhatkit


os.system("cls")
print("\n\n\t\t\t\t\t\t   WELCOME TO MY AMAZON WEBSERVER")
print("---------------------------------------------------------------------------------------------------------------------------------------")
pyttsx3.speak("hello, How are you,   I am your voice assistant.  WELCOME TO MY AMAZON WEBSERVER. , Pleace enter the password, Before access the AWS.")

#w=input(" ENTER to Enter Your ")
w="pass"
for w in "pass":
	password=getpass.getpass("Enter your Password :--   ")
	if password=="aws@1":		
		print("\n\nWhat can i do for you !!!.....{----These are my list which i've providing...----}")
		pyttsx3.speak("What's can i do for you,   These are my list...! which i've providing.")
		print("--------------------------------------------------------------------------------------------------------------------------------------")

		print("\n\t\t\t\t\t\t1). Create a key pair.\n\t\t\t\t\t\t2). Create a security group.\n\t\t\t\t\t\t3). Launch an EC2 instance.")
		print("\t\t\t\t\t\t4). Create an EBS volume of 1 GB.")
		print("\t\t\t\t\t\t5). Attach EBS volume with instance.")
		print("--------------------------------------------------------------------------------------------------------------------------------------")

		
	
		while True:
			r=sr.Recognizer()
			pyttsx3.speak("\nWhat's can i do for you,  Plese tell me...\n")
			print("--------------------------------------------------------------------------------------------------------------------------------------")
			print("What's your recure,  Plese Tell me...")
			print("--------------------------------------------")
			with sr.Microphone() as source:
				print('Listening.....')
				pyttsx3.speak("start say")
				audio=r.listen(source)
				print('speech done...')
				pyttsx3.speak("speech done")

			x=r.recognize_google(audio)
			print(x)
			if ("create" in x) and ("key" in x) and ("pair" in x):
				pyttsx3.speak("Creating a key pair")
				pyttsx3.speak("plz input the key name")
				k=input("\nInput key name :- ")
				pyttsx3.speak("Creating a key pair in aws with the name {}".format(k))
				os.system("aws ec2 create-key-pair --key-name {}".format(k))
				pyttsx3.speak("  Key pair has been created ")





		
			elif ("create security group" in x) or ("security group" in x):
				pyttsx3.speak("Creating a security group")
				pyttsx3.speak("plz input the security group name and description name")
				k=input("Input security group name :-  ")
				z=input("\nInput description name :-  ")
				pyttsx3.speak("Creating a security group  in aws with the name {}".format(k))
				os.system("aws ec2 create-security-group --group-name {} --description {}".format(k,z))
				pyttsx3.speak(" Security group has been created ")




		
			
			elif ("launch instance" in x) or ("launch an instance" in x): 
				pyttsx3.speak("Choose an Amazon Machine Image.  These are the list")
				print("\t\t\t1). Amazon Linux 2 AMI.")
				print("\t\t\t2). Amazon Linux AMI 2018.03.0 .")
				print("\t\t\t3). Red Hat Enterprise Linux 8 .")
				print("\t\t\t4). Ubuntu Server 20.04 LTS.")
				print("\t\t\t5). Microsoft Windows Server 2019 Base.")
				a=input("\nEnter the number :- ")
				if int(a)==1:
					pyttsx3.speak("Which zone do you want to create a instance. These are the list.")
					print("\t\t\t1). ap-south-1a ")
					print("\t\t\t2). ap-south-1b ")
					print("\t\t\t3). ap-south-1c ")
					k=input("input key name :- ")
					if int(k)==1:
						sub="subnet-c4d9d0ac" 
						pyttsx3.speak(" Your choice is  Amazon Linux 2 AMI. And ap south 1a zone. ")
						img="ami-0e306788ff2473ccb"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Amazon Linux 2, has lounched.")


					elif int(k)==2:
						sub="subnet-a5225ce9" 
						pyttsx3.speak(" Your choice is  Amazon Linux 2 AMI. And ap south 1b zone ")
						img="ami-0e306788ff2473ccb"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Amazon Linux 2, has lounched.")



					elif int(k)==3:
						sub="subnet-a028a9db" 
						pyttsx3.speak(" Your choice is  Amazon Linux 2 AMI. And ap south 1c zone")
						img="ami-0e306788ff2473ccb"
						pyttsx3.speak("Launching an instance,")
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Amazon Linux 2, has lounched.")



					else:
						pyttsx3.speak("Invalid input. Pleace input valide number.")
						print("Invalid input. Pleace input valide number.")
			

				elif int(a)==2:
					pyttsx3.speak("Which zone do you want to create a instance. These are the list.")
					print("\t\t\t1). ap-south-1a ")
					print("\t\t\t2). ap-south-1b ")
					print("\t\t\t3). ap-south-1c ")
					k=input("\ninput key name :- ")
					if int(k)==1:
						sub="subnet-c4d9d0ac" 
						pyttsx3.speak(" Your choice is Amazon Linux AMI 2018.03.0, And ap south 1a zone.")
						img="ami-03cfb5e1fb4fac428"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Amazon Linux , has lounched.")



					elif int(k)==2:
						sub="subnet-a5225ce9" 
						pyttsx3.speak(" Your choice is Amazon Linux AMI 2018.03.0 , And ap south 1b zone.")
						img="ami-03cfb5e1fb4fac428"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Amazon Linux , has lounched.")



					elif int(k)==3:
						sub="subnet-a028a9db" 
						pyttsx3.speak(" Your choice is Amazon Linux AMI 2018.03.0 , And ap south 1c zone.")
						img="ami-03cfb5e1fb4fac428"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Amazon Linux , has lounched.")



					else:
						pyttsx3.speak("Invalid input. Pleace input valide number.")
						print("Invalid input. Pleace input valide number.")



				elif int(a)==3:
					pyttsx3.speak("Which zone do you want to create a instance. These are the list.")
					print("\t\t\t1). ap-south-1a ")
					print("\t\t\t2). ap-south-1b ")
					print("\t\t\t3). ap-south-1c ")
					k=input("\ninput key name :- ")
					if int(k)==1:
						sub="subnet-c4d9d0ac" 
						pyttsx3.speak(" Your choice is Red Hat Linux version 8. And ap south 1a zone. ")
						img="ami-052c08d70def0ac62"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id  :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Red Hat Linux version 8, has lounched.")



					elif int(k)==2:
						sub="subnet-a5225ce9" 
						pyttsx3.speak(" Your choice is Red Hat Linux version 8. And ap south 1b zone. ")
						img="ami-052c08d70def0ac62"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id  :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Red Hat Linux version 8, has lounched")

					elif int(k)==3:
						sub="subnet-a028a9db" 
						pyttsx3.speak(" Your choice is Red Hat Linux version 8. And ap south 1c zone. ")
						img="ami-052c08d70def0ac62"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id  :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Red Hat Linux version 8, has lounched.")


					else:
						pyttsx3.speak("Invalid input. Pleace input valide number.")
						print("Invalid input. Pleace input valide number.")





				elif int(a)==4:
					pyttsx3.speak("Which zone do you want to create a instance. These are the list.")
					print("\t\t\t1). ap-south-1a ")
					print("\t\t\t2). ap-south-1b ")
					print("\t\t\t3). ap-south-1c ")
					k=input("\ninput key name :- ")
					if int(k)==1:
						sub="subnet-c4d9d0ac" 
						pyttsx3.speak(" Your choice is Ubuntu Server 20.04 LTS. And ap south 1a zone ")
						img="ami-0cda377a1b884a1bc"
						pyttsx3.speak("Launching an instance,")
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id :-  ")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Ubuntu Server 20.04, has lounched.")

					elif int(k)==2:
						sub="subnet-a5225ce9" 
						pyttsx3.speak(" Your choice is Ubuntu Server 20.04 LTS. And ap south 1b zone ")
						img="ami-0cda377a1b884a1bc"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id  :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Ubuntu Server 20.04, has lounched.")


					elif int(k)==3:
						sub="subnet-a028a9db" 
						pyttsx3.speak(" Your choice is Ubuntu Server 20.04 LTS. And ap south 1c zone ")
						img="ami-0cda377a1b884a1bc"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id  :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Ubuntu Server 20.04, has lounched.")


					else:
						pyttsx3.speak("Invalid input. Pleace input valide number.")
						print("Invalid input. Pleace input valide number.")




				elif int(a)==5:
					pyttsx3.speak("Which zone do you want to create a instance. These are the list.")
					print("\t\t\t1). ap-south-1a ")
					print("\t\t\t2). ap-south-1b ")
					print("\t\t\t3). ap-south-1c ")
					k=input("\nInput key name :- ")
					if int(k)==1:
						sub="subnet-c4d9d0ac" 
						pyttsx3.speak(" Your choice is Microsoft Windows Server 2019 Base. And ap south 1a zone ")
						img="ami-0b2f6494ff0b07a0e"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Microsoft Windows Server 2019 Base, has lounched.")
			


					elif int(k)==2:
						sub="subnet-a5225ce9" 
						pyttsx3.speak(" Your choice is Microsoft Windows Server 2019 Base. And ap south 1b zone ")
						img="ami-0b2f6494ff0b07a0e"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group name :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Microsoft Windows Server 2019 Base, has lounched.")


					elif int(k)==3:
						sub="subnet-a028a9db" 
						pyttsx3.speak(" Your choice is Microsoft Windows Server 2019 Base. And ap south 1c zone")
						img="ami-0b2f6494ff0b07a0e"
						pyttsx3.speak(" Please input key name and security group id name")
						k=input("\nInput key name :- ")
						sec=input("\nEnter security group id :-  ")
						pyttsx3.speak("Launching an instance,")
						os.system("aws ec2 run-instances --image-id {}  --instance-type t2.micro  --count 1  --key-name {}  --subnet-id {} --security-group-ids {}".format(img,k,sub,sec)) #--tag-specifications {}
						pyttsx3.speak("Microsoft Windows Server 2019 Base, has lounched.")


					else:
						pyttsx3.speak("Invalid input. Pleace input valide number.")
						print("Invalid input. Pleace input valide number.")



				else:
					pyttsx3.speak("Opssssssss!!!!!!!!!  please enter valid number")
					print("------------Oopssssss!!!!!!!!!  please enter valid number----------------------")
	
			elif ("create EBS volume" in x) or ("Create  EBS volume" in x) or ("create ebs volume" in x) or ("create volume" in x) :#or ("EBS volume" in x): 
				#name=input("Enter volume name:- ")
				pyttsx3.speak("Which zone do you want to create a volume. These are the list.")
				print("\t\t\t1). ap-south-1a ")
				print("\t\t\t2). ap-south-1b ")
				print("\t\t\t3). ap-south-1c ")
				k=input("\nEnter the zone between 1 to 3 :- ")
				if int(k)==1:
					zone="ap-south-1a" 
					pyttsx3.speak("Input the volume size")
					siz=input("\nEnter the volume size :- ")					
					pyttsx3.speak("creating EBS volume of {}GB in ap south 1a zone".format(siz))
					os.system("aws ec2 create-volume --volume-type gp2 --size {}  --availability-zone {} ".format(siz,zone))
					pyttsx3.speak(" EBS volume of {}GB creatated successful ".format(siz))

				elif int(k)==2:
					zone="ap-south-1b" 
					pyttsx3.speak("Input the volume size")
					siz=input("\nEnter the volume size :- ")
					pyttsx3.speak("creating EBS volume of {}GB in ap south 1b zone ".format(siz))
					os.system("aws ec2 create-volume --volume-type gp2 --size 1  --availability-zone {} ".format(siz,zone))
					pyttsx3.speak(" EBS volume of {}GB creatated successful ".format(siz))

				elif int(k)==3:
					zone="ap-south-1c" 
					pyttsx3.speak("Input the volume size")
					siz=input("\nEnter the volume size :- ")
					pyttsx3.speak("creating EBS volume of {}GB in ap south 1c zone".format(siz))
					os.system("aws ec2 create-volume --volume-type gp2 --size 1  --availability-zone {} ".format(siz,zone))
					pyttsx3.speak(" EBS volume of {}GB creatated successful ".format(siz))

				else:
					pyttsx3.speak("Invalid input. Pleace input valide number. ")
					print("Invalid input. Pleace input valide number.")

			elif ("attach EBS volume with instance" in x) or ("attach ebs volume with instance" in x) or ("attach volume" in x) or ("Attach EBS volume" in x) or ("attach EBS volume" in x): 
				pyttsx3.speak("Attaching EBS volume with instance")
				pyttsx3.speak("Input the volume id and instance id.  which you have creatated")
				k=input("\nInput the volume id name :- ") 
				ins=input("\nInput the instance id name :- ")
				os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf ".format(k,ins))
				pyttsx3.speak(" EBS volume of 1GB attachted successful ")


			elif("thank" in x) and ("you" in x):
				pyttsx3.speak("It's my pleasure for helping you.")
				print("It's my pleasure for helping you.")


			elif ("exit" in x) or ("close" in x):
        		       exit()

			else:
				print("not valid")
				pyttsx3.speak("not valid")




	else:
		pyttsx3.speak("You have entered wrong password,  Pleace reenter the password ")
		













		
		
			
