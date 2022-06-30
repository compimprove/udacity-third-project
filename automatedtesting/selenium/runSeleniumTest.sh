export vm_public_ip=(../../terraform/main/test/terraform output -raw vm_public_ip_address)
scp login.py adminuser@$vm_public_ip:~/selenium-testing/login.py
ssh -o StrictHostKeyChecking=no adminuser@$vm_public_ip "python3 ~/selenium-testing/login.py; sudo cp ~/logfile.log /var/log/logfile.log"