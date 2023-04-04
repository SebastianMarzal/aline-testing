# How to start it
Run the following microservices on Docker:
* aline-user-microservice
* aline-underwriter-microservice
* aline-gateway
* mysql

# Import
Import the following classes:
* aline-atf.AlineInterface
* Applicants.ApplicantsInterface (only one done yet)
* Applications.ApplicationsInterface
* Users.UsersInterface
* Banks.BanksInterface

# To use it
1. Create an instance of the AlineInterface class with arguments: user ms port, username, password
2. Create an instance of the other Interfaces with arguments: previously created Aline Interface, and the microservice port
3. See docs for available methods. TL;DR: Basic CRUD methods mostly.