# Betsushi
Betsu (別), the japanese word meaning "another" and Shiharai (支払い) meaning "payment". Hence the name Betsushi was derived.

---
## Introduction

This is the backend for [Indi>Pe](https://github.com/SudodevsHQ/indipe-client) a submission for FTX Hackathon'21, an application that can provide Indian UPI (Unified Payments Interface) to the people of foreign nationality.

Team members:

Aayush Dongre (dankre#7878)
Anurag Patil (source#5843)
Ayush Singh (epinephrine69#4257)
Kunal Sharma (kunal#4839)
### Technologies used:

- [PostgreSQL ](https://www.postgresql.org/) for the database
- [Docker](https://www.docker.com/) to containerize the application for easy deployments
- [Python](https://www.python.org/) as the programming language of choice
- [Starlette](https://www.starlette.io/), the library used to build the REST and the websocket services
- [Firebase Admin](https://firebase.google.com/) to authorize the user, which was authorized by the client.
  
### Razorpay services used:

- RazorpayX Payouts
- Razorpay Smart Collect
- Razorpay International payment Gateway

### Deployment

#### Prerequisites:
- Should have created a Firebase Project
- A valid docker installation

1. Rename the file `.env.example` to `.env` and populate the file with valid values.
2. Change the following values in the `docker-compose.yaml` file to their respective valid values:
    - `GOOGLE_APPLICATION_CREDENTIALS` env variable in the service `app` to the correct path of the `service-account` json file
    - Proper values for environment variables in the service `postgres`
3. Spin up the containers
    ```sh
    sudo docker-compose up --build -d
    ```
    This will install all the necessary dependencies required for the python server as well as start a postgresql instance
4. Make a database called `indipe` in the postgresql instance and run the initial schema migrations from `schema/init.sql`
5. Voila! You are ready to go!

### Flow Diagrams:
<img width="924" alt="image" src="https://github.com/user-attachments/assets/ebcb3f70-1b2d-4dbf-817e-be991b18f1e8" />
![image](https://github.com/user-attachments/assets/825a3763-5c46-418f-a728-a4d600153d67)
![image](https://github.com/user-attachments/assets/52c599c7-3bef-497a-bf8c-47fb88c4e405)
![image](https://github.com/user-attachments/assets/4d3bf32e-194f-450c-8c29-58562e890936)


