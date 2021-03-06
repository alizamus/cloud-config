#!/usr/bin/python

#executing this command:
#./config add network user1-net --ipam ipam-default --subnet 10.1.3.0/29 --route-target 65050:10050
#based on the user and data center nummber
import sys
import os
import getopt

def main(argv):
	try:                                
		opts, args = getopt.getopt(argv, "hu:d:r:s:", ["help", "user=","datacenter=","r_target=","start_user="])
	except getopt.GetoptError:                                
		sys.exit(2)
	for opt, arg in opts:       
		if opt in ("-h", "--help"):                         
			sys.exit()                                   
		elif opt in ("-u", "--user"): 
			username = arg
		elif opt in ("-d", "--datacenter"):
			data_num = arg
		elif opt in ("-r", "--r_target"):
			target = arg
		elif opt in ("-s", "--start_user"):
			start_user = arg
	
	subnet = "10.1." + str(data_num) +"."+str(((int(username))-int(start_user))*8)+"/29"
	
	command = "/root/code/config" + " " + "--username user" + username + " --password user" + username + " --tenant sandbox"+ username + " --api-server 127.0.0.1 " + "add network public-user" + username + "-net " + "--ipam ipam-default --subnet " + subnet + " --route-target " + target
	
	os.system(command)
if __name__ == "__main__":
    main(sys.argv[1:])
