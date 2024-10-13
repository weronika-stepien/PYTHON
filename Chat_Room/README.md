<div align="center">

# Chat Room
#### Join or create multiple chat rooms for real-time messaging


![Preview](/Images/chat.gif)

![Version](https://img.shields.io/badge/version-1.0-blue?style=for-the-badge&labelColor=black) ![Static Badge](https://img.shields.io/badge/3-blue?style=for-the-badge&logo=python&logoColor=blue&label=python&labelColor=black) ![Static Badge](https://img.shields.io/badge/flask-black?style=for-the-badge&logo=Flask&logoColor=blue) ![HTML Badge](https://img.shields.io/badge/HTML-5-blue?style=for-the-badge&logo=html5&logoColor=blue&label=HTML&labelColor=black) ![CSS Badge](https://img.shields.io/badge/CSS-3-blue?style=for-the-badge&logo=css3&logoColor=blue&label=CSS&labelColor=black) ![Static Badge](https://img.shields.io/badge/windows%20%7C%20macOs%20%7C%20linux-blue?style=for-the-badge&label=platform&labelColor=black)










------------


![Static Badge](https://img.shields.io/badge/Table%20%20%20%20%20%20%20%20%20%20%20of%20%20%20%20%20%20%20%20%20%20Contents-blue?style=for-the-badge&logoColor=darkviolet)

**| [Overview](#overview) | [Key Features](#key-features) | [User Manual](#user-manual) | [Ongoing Improvements and Known Bugs](#ongoing-improvements-and-known-bugs) | [Found a Bug?](#found-a-bug) |**





------------



## Overview
Built with `Flask` and `Python`, the Chat Room App offers real-time group conversations in a browser environment. Users can create and join rooms, engage in instant messaging, and receive real-time updates. The cross-platform compatibility ensures smooth usage across Windows, macOS, and Linux.


------------



## Key Features
##### Real-time Messaging
###### Instantly send and receive messages in chat rooms with no delays.
##### Multiple Chat Rooms
######  Create and join multiple chat rooms to organize conversations by topics or groups.
##### Room Management
######  Users can easily create and manage chat rooms.
##### Flask Backend
###### Built on Flask, a lightweight Python framework that ensures efficient communication.
##### Chat History
###### Users can access past messages even after refreshing or rejoining the chat room.


------------



## User Manual
</div>

####  Requirements
###### Python Version
The game requires `Python 3` or higher to run. You can check your  version by running below command:
```bash
$ python -version
```
###### Dependencies
Install the required Python packages:
```bash
$ pip install -r requirements.txt
```

#### Getting Started
###### To run a program, you need to:
- Clone this repository
 ```bash
$ git clone <repository_url>
```
###### If you're using Docker:
This section will guide you through the steps to build and run a Docker container for the Chatroom application using the provided Dockerfile.

1. Build the Docker Image or pull it from the DockerHub:

###### DockerHub
Use the following command to pull the image from DockerHub:

```bash
$ docker pull weronikastepien/chat-room
```

And to run the container:

```bash
$ docker run -p 5000:5000 chat-room:web-app
```
Open your browser and go to:
[http://127.0.0.1:5000](http://127.0.0.1:5000 "Chatroom application")

###### Docker

If you prefer build the Docker image from the Dockerfile use this command instead:
```bash
$ docker build -t chatroom-app .
```
-  `-t chatroom-app` assigns a name/tag to your Docker image. You can replace `chatroom-app` with your preferred name.
- `.` specifies that the Dockerfile is in the current directory.

2. Run the Docker Container
   Once the image is built, you can create and run a container from that image using the command below:
```bash
$ docker run -d -p 5000:5000 --name chatroom-app-container chatroom-app
```
- `-d` runs the container in detached mode.
- `-p 5000:5000` maps port `5000` on your local machine to port `5000` on the container.
- `--name chatroom-app-container` assigns a custom name to the running container.
- `chatroom-app` is the name of the image created earlier.

3. Open your browser and go to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000 "Chatroom application")

###### If you're using the executable file:
- Navigate to the repository's `releases` folder where the executable file is located.
- Double-click the executable file (`Chat.jar`) to launch the game.
- If the executable does not open via double-click, run the following command from the terminal/command prompt:
```bash
$  python Chat.jar
```

###### If you're running from Source Code
- Start the Flask-based chat room app locally:
```bash
$ python main.py
```
- Access the application via your web browser at:
```bash
http://127.0.0.1:5000
```

#### Customization
###### Configuring Flask Settings
You can modify the Flask application’s behavior by changing settings in the main.py file or adding environment variables. By default, the app runs in production mode. To enable debug mode, set the FLASK_ENV variable to development:

**Steps to make the change:**
```bash
export FLASK_ENV=development  # Linux/macOS
set FLASK_ENV=development  # Windows
```

###### Change Listening Port
The default port is 5000. To change this, open main.py and modify the main.run() line:
```python
main.run(host="0.0.0.0", port=8080)  # Example for changing to port 8080
```

------------
<div align="center">

## Ongoing Improvements and Known Bugs

| # | Name                     | Type | Description                                                                                                                      |
|---|--------------------------|------|----------------------------------------------------------------------------------------------------------------------------------|
| 1 | Emoji Support            | Bug  | Some emoji characters do not render properly in the chat room due to font compatibility issues.                                  |
| 2 | Flask Debug Mode Warning | Bug  | Users running the app in debug mode (`FLASK_ENV=development`) might see some warning messages related to WebSocket connections.  |






------------

## Found a bug?

If you encounter any issues or bugs while using this project, please feel free to open an issue in the Issues section of the repository. Make sure to describe the bug in detail, providing steps to reproduce, expected behavior, and any relevant logs or screenshots.

If you'd like to contribute a fix for the issue, you're welcome to submit a pull request (PR). When submitting a PR, please reference the issue number and provide a description of the changes made.


------------

</div>





