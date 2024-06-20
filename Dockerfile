FROM node:latest

# Copy files
ADD /node-server /code/node-server
ADD /client /code/client

# Build React app
WORKDIR /code/client
RUN npm install
RUN npm run build

# Build server
WORKDIR /code/node-server
RUN npm install
RUN npm run build

# Start server
RUN npm start