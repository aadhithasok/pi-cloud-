# PiCloud

PiCloud is a secure and lightweight web-based file management system built using Flask, designed specifically for Raspberry Pi. It provides users with a modern, responsive interface to upload, download, and manage their files. The project supports remote access via port forwarding, making it a versatile personal cloud solution.

## Features

### User Authentication
- Secure login and logout with session management.

### File Management
- Upload files to your personal cloud storage.
- View and manage uploaded files from the dashboard.
- Download or delete files with ease.

### Responsive Design
- A modern, user-friendly interface accessible on all devices.

### Remote Accessibility
- Remotely access your cloud from anywhere using port forwarding.

### Scalable Setup
- Local storage on Raspberry Pi with potential for future enhancements like cloud storage integration.

## Technology Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (Custom Styling with `style.css`)
- **Authentication:** Flask-Login
- **File Storage:** Local filesystem (`~/PrivCloud` on Raspberry Pi)

## Setup Instructions

### Hardware and OS Setup

1. Use a Raspberry Pi (any model with sufficient storage).
2. Install the latest Raspberry Pi OS (Lite or Desktop).
3. Set up Wi-Fi and enable SSH:
   ```bash
   sudo raspi-config
   ```
   - Enable SSH for remote access.
   - Configure the network (Wi-Fi or Ethernet).

### Project Setup on Raspberry Pi

#### Create the Required Folder
The project stores files in a folder named `PrivCloud` in the Raspberry Pi's home directory. Create this folder:

```bash
mkdir ~/PrivCloud
```

#### Install Required Software
Update and upgrade system packages:

```bash
sudo apt update && sudo apt upgrade -y
```

Install Python and Git:

```bash
sudo apt install python3 python3-pip python3-venv git -y
```

#### Clone the Repository
Clone the project repository to your Raspberry Pi:

```bash
git clone https://github.com/your-username/PiCloud.git
cd PiCloud
```

#### Set Up a Virtual Environment
Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Install Dependencies
Install the required Python packages:

```bash
pip install flask flask-login python-dotenv gunicorn
```

### Running the Project

Navigate to the project directory and activate the virtual environment:

```bash
cd ~/PiCloud
source venv/bin/activate
```

Start the Flask application:

```bash
python app.py
```

Open your browser and navigate to:

```bash
http://127.0.0.1:5000
```

### Enable Remote Access via Port Forwarding

#### Check Your Local IP Address
Find the Raspberry Pi's local IP address:

```bash
hostname -I
```

#### Configure Port Forwarding on Your Router
Access your router’s admin page (usually `http://192.168.x.x`). Locate the Port Forwarding section and create a new rule:

- **Internal IP:** Raspberry Pi’s local IP (e.g., `192.168.1.10`)
- **Internal Port:** `5000`
- **External Port:** Any available port (e.g., `8000`)
- **Protocol:** TCP

Save the settings.

#### Access the Application Remotely
Find your public IP address by visiting [WhatIsMyIP](https://whatismyipaddress.com/). Access the application remotely using:

```bash
http://<your-public-ip>:<external-port>
```

## Folder Structure

```
PiCloud/
├── app.py           # Main Flask application
├── static/
│   └── style.css    # Custom CSS styles
├── templates/
│   ├── index.html   # Dashboard template
│   └── login.html   # Login page template
├── README.md        # Project documentation
```

## Future Enhancements

1. **Database Integration:** Migrate from local folder-based storage to database or cloud-based storage.
2. **Enhanced User Roles:** Add multi-user functionality with role-based access control.
3. **File Previews:** Support previews for images, documents, and videos.
4. **Deployment:** Deploy the application to platforms like Heroku, AWS, or Azure.
5. **File Encryption:** Implement secure file encryption for enhanced privacy.

