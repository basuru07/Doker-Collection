# Use an official Node.js runtime as a parent image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json to the container (for docker volume purpose)
COPY package*.json ./

# Install dependencies  (for docker volume purpose)
RUN npm install

# Copy the rest of your application files
COPY . .

# Build the React app for production
RUN npm run build

# Expose the port the app will run on
EXPOSE 3000

# Serve the app using a simple static server (You can use a production server like nginx, but we use 'serve' here)
RUN npm install -g serve

# Run the app when the container starts
CMD ["serve", "-s", "build", "-l", "3000"]
