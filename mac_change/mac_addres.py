import subprocess


def mac_changer():
    subprocess.run(
        "ifconfig", shell=True, text=True,check=True,capture_output=True
    )
    print("Your config shows above ")


    subprocess.run(
        " ifconfig eth0 down", shell=True, text=True, check=True,capture_output=True
    )

 

    subprocess.run(
        "ifconfig eth0 down", shell=True, text=True, check=True,capture_output=True
    )


    
    subprocess.run(
        "ifconfig eth0 hw ether 04:03:01:a2:a5:a6",shell=True,text=True,check=True,capture_output=True
    )

    subprocess.run(
        "ifconfig eth0 up",shell=True,text=True,check=True,capture_output=True
    )
    
    print("succes change the mac adress let boom it")