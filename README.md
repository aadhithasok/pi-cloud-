PiCloud
PiCloud is a simple, lightweight, and secure personal cloud system built using Flask and designed to run smoothly on a Raspberry Pi. 
Instead of depending on third-party cloud services, PiCloud lets you store and manage your own files on your own device. 
It gives you a clean and responsive web interface where you can upload, download, and organize files easily. With optional port forwarding, 
you can even access your files remotely from anywhere.

What PiCloud Offers
Secure Login
PiCloud includes user authentication with session management, ensuring that only authorized users can access the dashboard. 
Your personal files stay protected at all times.
Easy File Management
You can upload files directly to your Raspberry Pi, view everything from a simple dashboard, and download or delete files whenever needed. 
The system is designed to feel straightforward and hassle-free.
Works on Any Device
The interface is modern and responsive, making it comfortable to use on desktops, tablets, and mobile phones without any issues.

Access from Anywhere
If you set up port forwarding on your router, PiCloud allows remote access to your personal storage. This means you can manage your files even when you're away from home.

Built to Grow
Files are stored locally at ~/PrivCloud on the Raspberry Pi, but the structure of the project allows for future improvements—such as integrating external cloud storage or supporting multiple users.

Technology Stack
Backend: Flask (Python)
Frontend: HTML and CSS (custom styling with style.css)
Authentication: Flask-Login
File Storage: Local filesystem on the Raspberry Pi
