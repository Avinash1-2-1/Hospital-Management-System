### Hospital Management System
### Created by: Avinash Acharya,Pulkit Gupta,Vihan Gouda Class XII-B


print()
print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome to Hospital Management System                  *")
print("*                                                                          *")
print("****************************************************************************")

# this is the password for the administrator of HMS	
admin_pass = "@RooYu5"	

# flag to keep track of number of wrong attempts to gain access to admin mode
num_tries = 0
tries_flag = ""

while tries_flag != "Close the program" :
				
        print("-----------------------------------------")
        print("|Enter 1 for Admin mode			|")
        print("|Enter 2 for User mode			|")
        print("|Enter Q to quit HMS			|")
        print("-----------------------------------------")
		
        Admin_user_mode = input("Enter your mode : ") 
		
        if Admin_user_mode == "1" :     #Admin mode
                print("*****************************************\n|         Welcome to admin mode         |\n*****************************************")
                e_Password = input("Please enter the admin password : ")
                while True :
                        if e_Password == admin_pass :
                                print("-----------------------------------------")
                                print("|Enter 1 to manage patients  		|")
                                print("|Enter 2 to manage doctors 	 	|")
                                print("|Enter 3 to manage appointments  	|")
                                print("|Enter B to go back			|")
                                print("-----------------------------------------")
			
                                AdminOptions = input ("Enter your choice : ")
                                AdminOptions = AdminOptions.upper()
						
                                if AdminOptions == "1" :        #Admin mode --> Patients Management				
                                        print("# write code for Patients Management")			
											
                                elif AdminOptions == "2" :	#Admin mode --> Doctors Management
                                        print("# write code for Doctors Management")
											
                                elif AdminOptions == "3" :	#Admin mode --> Appointment Management
                                        print("# write code for Appointment Management")

                                elif AdminOptions == "B" :	#Go Back
                                        break

                                else :                          #Wrong choice entered
                                        print("Please enter a correct choice")	
                        else :
                                if num_tries < 2 :
                                        e_Password = input("\nPassword incorrect, please try again : ")
                                        num_tries += 1
                                else :
                                        print("\nIncorrect password, no more tries. Program Aborting!\n")
                                        tries_flag = "Close the program"
                                        break
				
					
					
        elif Admin_user_mode == "2" :	#User mode

                print("****************************************\n|         Welcome to user mode         |\n****************************************")

                while True :
                        print("\n-----------------------------------------")
                        print("|Enter 1 to view hospital's departments  |")
                        print("|Enter 2 to view hospital's doctors      |")
                        print("|Enter 3 to view patient's details       |")
                        print("|Enter 4 To view doctor's appointments   |")
                        print("|Enter B to go back                      |")
                        print("-----------------------------------------")

                        UserOptions = input("Enter your choice : ")
                        UserOptions = UserOptions.upper()
				
                        if   UserOptions == "1" :       #User mode --> view hospital's departments
                                print("# write code to view hospital's departments")		

                        elif UserOptions == "2" :	#User mode --> view hospital's doctors
                                print("# write code to view hospital's doctors")					

                        elif UserOptions == "3" :	#User mode --> view patient's details
                                print("# write code to view patient's details")				

                        elif UserOptions == "4" :	#User mode --> view doctor's appointments
                                print("# write code to view doctor's appointments")

                        elif UserOptions == "B" :	#Go Back
                                break
					
                        else :
                                print("Please enter a correct choice")

        elif Admin_user_mode.upper() == "Q" :	#Quit program
                print("\nThank you for using HMS!\n")
                break
					
        else : # Wrong mode entered
                print("Please enter a correct choice")
