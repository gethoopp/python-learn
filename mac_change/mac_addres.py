import subprocess

#this function define to change mac adrres
def mac_changer():
    #handle input interface 
    interface = input("input the interface >");
    #mac_addres = " 04:03:01:a2:a5:a6";
    #handel input new mac addres
    mac_addres = input("Input the new addres >");
    subprocess.run(
        "ifconfig", shell=True, text=True,check=True,capture_output=True
    )
    print("Your config shows above ")


    subprocess.run(
        f" ifconfig {interface} down", shell=True, text=True, check=True,capture_output=True
    )

 

    subprocess.run(
        f"ifconfig {interface} down", shell=True, text=True, check=True,capture_output=True
    )


    
    subprocess.run(
        f"ifconfig {interface} hw ether {mac_addres}",shell=True,text=True,check=True,capture_output=True
    )

    subprocess.run(
        f"ifconfig {interface} up",shell=True,text=True,check=True,capture_output=True
    )
    
    print("succes change the mac adress let boom it")