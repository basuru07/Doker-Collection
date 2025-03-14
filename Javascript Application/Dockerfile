# Use the official Node.js image as the base
FROM node:22.12.0

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files into the container
COPY . .

# Expose multiple ports for the application
EXPOSE 3000 4000

# Define the command to run the application
CMD ["node", "index.js"]
