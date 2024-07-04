# To-Do List Application Migration to AWS

This guide provides step-by-step instructions to migrate a to-do list application to AWS, utilizing various AWS services such as EC2, RDS, and IAM.

## Prerequisites

- AWS Account
- Basic knowledge of AWS services
- Familiarity with Django and PostgreSQL

## Services Used

- Amazon EC2
- Amazon RDS
- Amazon IAM

## Step-by-Step Implementation

### Setting up AWS Environment

#### EC2 Instances

1. **Launch EC2 Instance**
   - Go to the AWS Management Console, choose `Services`, and click on `EC2`.
   - In the EC2 dashboard, select `Launch instance`.
   - Configure the instance:
     - **Name:** `MyServer1`
     - **AMI:** Ubuntu Server 24.04 LTS (HVM)
     - **Instance Type:** t2.micro
     - **Key Pair:** No key pair
     - **Network Settings:** Create Security Group, Allow SSH traffic from `0.0.0.0/0`
   - Wait until the instance state and status checks are running and passed.
   - Select `Connect` at the top right corner.
   - Click on the `Connect` button to access the EC2 Instance Connect.

2. **Setup Django Environment**
   - Update package lists:
     ```bash
     sudo apt-get update
     ```
   - Clone the project repository:
     ```bash
     git clone https://github.com/jasonsongjiajain/Dbassignment2.git
     cd Dbassignment2
     ```
   - Install Python pip and Django:
     ```bash
     sudo apt install python3-pip -y
     pip3 install --break-system-packages django
     ```

3. **Configure Security Groups**
   - Go to Security Groups and Inbound Rules.
   - Select `Edit inbound rules`.
   - Add a rule:
     - **Type:** Custom TCP
     - **Port Range:** 8000
     - **Source:** Anywhere IPv4 `0.0.0.0/0`

4. **Run the Django Application**
   - Open the `settings.py` file and update `ALLOWED_HOSTS`:
     ```python
     ALLOWED_HOSTS = ['<EC2_Public_IP>', 'localhost', '127.0.0.1']
     ```
   - Run the following commands to start the Django server:
     ```bash
     python3 manage.py makemigrations
     python3 manage.py migrate
     python3 manage.py runserver 0.0.0.0:8000
     ```

5. **Test the Application**
   - Open an Incognito tab and enter the EC2 public IPv4 address followed by `:8000` in the URL.

#### RDS

1. **Create PostgreSQL Database**
   - In the AWS Management Console, choose `Services` and click on `RDS`.
   - Select `Create database`.
   - Configure the database:
     - **Database Creation Method:** Standard Create
     - **Engine Type:** PostgreSQL
     - **Templates:** Free Tier
     - **DB Cluster Identifier:** `MyDatabase1`
     - **Credentials Settings:** `MyUser1` / `mysuperuser`
     - **Public Access:** Yes
     - **Initial Database Name:** `MyDatabase1`
   - Click `Create Database`.

2. **Configure Security Groups for RDS**
   - Go to Databases, click on `mydatabase1`, and select the VPC security group.
   - Click on the Security Group ID and select `Edit Inbound Rules`.
   - Add rules:
     - **Rule 1:**
       - **Type:** Custom TCP
       - **Port Range:** 5432
       - **Source:** Anywhere IPv4 `0.0.0.0/0`
     - **Rule 2:**
       - **Type:** Custom TCP
       - **Port Range:** 5432
       - **Source:** Anywhere IPv6 `::/0`

3. **Connect Django to RDS**
   - Install PostgreSQL adapter:
     ```bash
     pip3 install --break-system-packages psycopg2-binary
     ```
   - Open `settings.py` and update the `DATABASES` settings:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'MyDatabase1',
             'USER': 'MyUser1',
             'PASSWORD': 'mysuperuser',
             'HOST': '<RDS_Endpoint>',
             'PORT': '5432',
         }
     }
     ```
   - Save the changes (`ctrl + o`, `enter`, `ctrl + x`).

4. **Apply Migrations**
   - Run the following commands to migrate the database:
     ```bash
     python3 manage.py makemigrations
     python3 manage.py migrate
     python3 manage.py runserver 0.0.0.0:8000
     ```

#### IAM

1. **Create IAM User**
   - In the AWS Management Console, choose `Services` and click on `IAM`.
   - Select `Users` and click `Create User`.
   - Enter the user name and attach the required policies.
   - Click `Create User`.

2. **Assign Permissions**
   - Note: Permission settings may fail due to limitations in the sandbox environment.

### Security Measures

- **Access Control:** Assign an IAM user to generate an access key.
- **Security Group:** Set inbound rules for EC2 and RDS connections to ensure robust security practices.

### Application Testing

- **Insert a New Entry:** Test adding a new task.
- **Delete an Entry:** Test deleting an existing task.
- **Insert Another New Entry:** Test adding another task to verify functionality.

## Conclusion

By following these steps, you can successfully migrate and set up a to-do list application on AWS, ensuring scalability, security, and high availability.

## References

- [GitHub Repository](https://github.com/jasonsongjiajain/Dbassignment2.git)
- [YouTube Presentation](https://youtu.be/1AbD97eD2WM)
