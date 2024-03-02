<h1 align="center">Simple Client-Server Application</h1>

This repository contains two Python scripts, `client.py` and `server.py`, implementing a basic client-server interaction using sockets.

## Usage

### Server (`server.py`)

The `server.py` script acts as a server and listens for incoming connections from clients. Upon connection, it receives data from the client, processes it, and sends a response back.

To run the server, type: python server.py

The server will start listening for connections on port 12000.

## Client (client.py)
The `client.py` script acts as a client and connects to the server to send data and receive a response.

To run the client, type: python client.py

The client will prompt you to input a number from 1 to 100 and your name. It then sends this data to the server and waits for a response. The response received from the server will be printed to the console.

## Files
client.py: Python script for the client application.

server.py: Python script for the server application.
