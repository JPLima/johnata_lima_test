# The Application 

<h2>Before start deploy</h2>
Before start to running the application you need install some things. Follow bellow the commands:
<b>Ansible using Python3</b>
<p><b>$</b>sudo python3 pip install ansible</p>
<p><b>Install boto and boto3</b></p>
<p>$sudo pip3 install boto</p>
<p>$sudo pip3 install boto3</p>
<p><b>You need to create the file ~/.aws/credentials or set aws_secret_access_key and aws_access_key_id</b></p>

<h2>Playbooks</h2>
<p>The project is divided in two playbooks that calls task in the folder task/</p>
<h3>Infrasctructure</h2>
<p>The first playbook that must to be deployed to create the infrastructure from the application is main.yml</p>
The <b>main.yml</b> playbook import tasks network.yml, rds.yml and instances.yml
<b>network.yml</b> - Must be deployed first at all. This task will create all network enviromment on aws(VPC,SG, LB, IGW) and create the <i>infonetwork.json</i> the save necessary network information to other deploy without the need to run it again. 
<b>rds.yml</b> - It will create the subnet_group to RDS and the RDS instance. Get credentials from ./files/credentials.json that must to be set before run the playbook.
<b>instances.yml</b> - This playbook generete the key pair to access the ec2 instance and create the VM, also add the instance to host.txt file(if not exist, it will be created) and save the access key if does not exist. 

<h3>Application</h3>
The application's playbook is deploy_app.yml that import the installreq.yml, createdb.yml and app.yml
<p><b>installreq.ym</b> - This task install all dependences that the application require.</p>
<p><b>createdb.ym</b> -  Create the database "demo" on RDS. This task can only be deployed from the VM because there is no external access to RDS.
<p><b>app.yml</b> - This is the task that run the application flask. </p>

<h2>Run the playbooks</h2>


