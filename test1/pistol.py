import time as t
class Gun:
    magazin = False
    twice = [3]
    auto_reset = True
    def Recharge():
        global magazin
        print("Recharge") ##########################
        for i in Gun.twice:
            t.sleep(150)
            print('.') #############################
        print("\n") ################################
        magazin = True
        print("FULL") ##############################

    def Reset():
        global magazin
        if magazin == False:
            Gun.Recharge()
        else:
            print("WAS FULL ") #####################
    
    def Auto_Reset_Shoot():
        global magazin
        if magazin == False:
            print("MAGAZIN IS NOT FULL") ###########
            if Gun.auto_reset == True:
                Gun.Recharge()
                Gun.Shoot()

    def Shoot():
        global magazin
        print("BOOM") ##############################
        for i in Gun.twice:
            t.sleep(100)
            print(" BOOM") #########################
        print("\n") ################################
        magazin = False


gun = Gun
command = input() ##################################
while True:
    if command == "s":
        gun.Auto_Reset_Shoot()
    elif command == "r":
        gun.Reset()
    elif command == "ar":
        if gun.auto_reset:
            gun.auto_reset = False
            print("AUTO Recharge off") ##############
        else:
            gun.auto_reset = True
            print("AUTO Recharge on") ###############
    command = input() ###############################