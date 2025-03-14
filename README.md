# Containerizing Your Application with Docker

This section provides the steps to **containerize** your application using **Docker**. By following these steps, you can run your app in a containerized environment for easier deployment and portability.

---

## **Prerequisites**

Before proceeding, ensure the following tools are installed on your local system:

- **Docker**: [Download and install Docker](https://www.docker.com/products/docker-desktop)
- **Git**: [Download and install Git](https://git-scm.com/)
- **Application**: Your project should have a running application that can be containerized (e.g., Node.js, Python, etc.).

---

## **Steps to Containerize the Application**

### **1. Create a Dockerfile**

The `Dockerfile` is a script that contains instructions on how to build your Docker image. Below is a general structure of a `Dockerfile`.

#### **General Structure of Dockerfile**

```dockerfile
# Use an official image as a base image
FROM node:18

# Set the working directory in the container
WORKDIR /app


# Copy the rest of the application files into the container
COPY <source> <destination>
COPY . .

# Expose the port your app runs on
EXPOSE 3000

# Define the command to run the application
CMD ["Language", "Application name"]
```

### **2. Create a Dockerfile**
Once you have your `Dockerfile` and application ready, you need to build the Docker image. Run the following command in your project directory

```dockerfile
docker build -t <your-image-name> .

```
### **3. Run the Docker Container**
Once you have your `Dockerfile` and application ready, you need to build the Docker image. Run the following command in your project directory

```dockerfile
docker run -d -p <host-port>:<container-port> --name <container-name> <image-name>

```
### **4. Verify the Running Container**
To check if your container is running, use the following command

```dockerfile
docker ps

```
## **Examples**
- [Javascript Application](https://github.com/basuru07/Doker-Collection/tree/main/Javascript%20Application)
- [NodeJs Application](https://github.com/basuru07/Doker-Collection/tree/main/Node.js%20Application)
- [Python Application](https://github.com/basuru07/Doker-Collection/tree/main/Python%20Application)

## **Useful Docker Commands**

- **Build Docker Image**: 
  `docker build -t <image-name> .`

- **Run Docker Container**: 
  `docker run -d -p <host-port>:<container-port> --name <container-name> <image-name>`

- **List Running Containers**: 
  `docker ps`

- **Stop Container**: 
  `docker stop <container-name>`

- **Remove Container**: 
  `docker rm <container-name>`

- **Remove Image**: 
  `docker rmi <image-name>`
