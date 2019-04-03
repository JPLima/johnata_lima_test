# challenge
This simple project buil an application and deploy on aws
there are three playbook to ruim
<p><b>#1</b> - create_infra.yml, create the network enviroment(VPC,SG, LB, IGW...) and deploy the EC2 instance </p>
<p><b>#2</b> - create_rds.yml, create a RDS MySQL Instance and generate de credentials.json file </p>
<p><b>#3</b> - deploy_app.yml, move the files with the application and run it. Install de requeriments too</p>

<h1> The Application</h1>
<h2> How to deploy</h2>
<h2> Pre installation </h2>
To run the deploy you need install some requeriments, follow below the commands:
   <p> Install ansible with python3</p>
        $sudo python3 pip install ansible 
    <p>Install boto and boto3</p>
        <p>$sudo pip3 install boto</p>
        <p>$sudo pip3 install boto3</p>

<h1>Deploy</h1>
<h2>The deployment from this application is divided in three steps:</h2>
    <p><b>Step 1</b> Run ansible-playbook to create de infrastructure </p>
            $ansible-playbook create_infra.yml
            <p>Here, the playbook will edit the ./file/template/index.html to put the load balancer public DNS and the host.txt file with the user and public name from EC2</p>
    <p><b>Step 2</b> Run playbook to deploy the RDS</p>
            $ansible-playbook create_rds.yml
            <p>At this point, the playbook will create the credentials.json file and send to ./file folder</p>
    <p><b>Step 3</b> Run playbook to install dependecies and run the application</p>
            $ansible-playbook -i host.txt deploy_app.yml

<p><h2>You need to create the file ~/.aws/credentials or set aws_secret_access_key  and aws_access_key_id</h2></p>
