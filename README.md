# Project: Automated Load Testing & Network Monitoring in a Dockerized Environment

## Description  
This project automates **performance testing and network monitoring** of a Dockerized web application using **Jenkins, k6, and TShark**. The pipeline ensures that every new deployment undergoes load testing while capturing network traffic for further analysis.  

---

## Workflow  

1️⃣ **Jenkins triggers the pipeline** (manually or on code changes).  
2️⃣ **Build & Deploy**:  
   - Jenkins builds the Docker image.  
   - Runs the containerized web application.  
3️⃣ **Start Network Capture**:  
   - TShark starts in the background, monitoring HTTP traffic on the Docker network.  
4️⃣ **Load Testing**:  
   - k6 simulates high traffic to test app performance.  
5️⃣ **Stop Network Capture & Archive Results**:  
   - TShark stops and saves the `.pcap` file.  
   - k6 test results and network logs are archived in Jenkins for analysis.  
