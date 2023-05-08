PRO4

Prerequisites

Before starting make sure you have the following programs installed.
* git
* docker
* pip
* python3-virtualenv

Installation

Clone this repository using:
```
git clone https://github.com/VladimirFogel/PRO4.git
```
Navigate to the cloned directory using:
```
cd PRO4
```
Install the required packages using:
```
pip install -r requirements.txt
```
Usage

Start the application using:
```
python app.py
```
Open your web browser and go to http://localhost:8000

Dockerization

To run the application in a Docker container, follow these steps:

Build the Docker image using:
```
docker build -t pro4 .
```
Run the Docker container using:
```
docker run -p 5000:5000 pro4
```
Note that you can replace pro4 with any name you want to give your Docker container.

To make sure that your Git commits are properly attributed to you, you should set your Git name, email, and safe directory using the following commands:
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global --add safe.directory /path/to/PRO4
```
Make sure to replace "Your Name", "you@example.com", and "/path/to/PRO4" with your own name, email address, and the path to the PRO4 directory.

If you are still having issues, try setting the SSH URL for your Git remote manually by running the command:
```
git remote set-url origin git@github.com:Mrgoodwill/PRO4.git 
```
(replace "Mrgoodwill" and "PRO4" with your own GitHub username and repository name).

Check that your SSH key is being used by Git. To do this, run the command:
```
ssh -T git@github.com
```
This should return a message that starts with
"Hi username! You've successfully authenticated...". If you see an error message instead, it means that your SSH key is not being used by Git.


Zeitdokumentation:
* https://docs.google.com/spreadsheets/d/1mwbqgdCWlFgcgNUbmIdQwrI29UEeELdBSZa5vNcmR4U/edit?usp=sharing

Jira Board:
* https://pro4projektmanagement.atlassian.net/jira/software/projects/PRO4/boards/1

SSH Schwachstellen Template:
* https://forms.gle/CfSYcY2WqVsZDadf7
