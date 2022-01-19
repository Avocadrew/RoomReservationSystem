# Room Reservation System
### 110-1 CS3025 Software Engineering Group 6
#### Jun-Yu (Andrew) Chen, Shu-Yan Cheng, Yun-Hsuan Tsai, Ethan Kuan, Wei Chen

## Introduction
The main goal we design the system is to improve the user experience of current library meeting room reservation system. To achieve this, we added some new concepts and functions into our system:
- **Grouping system:**

     We introduce a new concept "Group" into the reservation system. Add your team members into your own group so you can easily track who is in the meeting, and also convenient to remind them of the following meeting.
     
- **Email/Calendar notice:**

     We use Google API to send email and add the schedule into Google Calendar.  After you reserve a meeting. The system will automatically send an e-mail to all the members in the group. The schedule will also be added to members' calendar.
     
- **Simple and Intuitive UI/UX:**
     
     We simplify the user flow for reserving meeting. All you need is several click to reserve a meeting room.

![Landing](https://user-images.githubusercontent.com/64970325/150075022-592d76ca-3046-4818-b7c5-65a1a1dd3fa6.png)

## How To Build
- **Frontend**: 
     1. Install npm and run ``npm install`` in ``/frontend``. 
     2. Run ``npm run serve`` in ``/frontend`` to start a development server. 
     3. Open a browser and direct to ``http://localhost:8080``. 
     4. Now you are good to go. 
     
     ___Note: This frontend will still call api to our server, instead of the one you run locally.___
- **Backend**: 
     1. Install ``python`` and ``virtualenv``. 
     2. Create a virtual environment using ``virtualenv virtualEnv``. (virtualEnv can be replaced by whatever you want)
     3. If you are using Linux, activate your virtual environment using ``source virtualEnv/bin/activate``. 
     4. Run ``pip install -r requirement.txt`` in ``/backend`` to install all necessary dependencies. 
     5. Run ``python app.py`` in ``/backend`` to start your backend server. 
     6. Now you are good to go. 
    
     ___Note: If you want to use this backend server as your api server, replace every___ ``https://ntustsers.xyz/api/`` ___with___ ``http://localhost:5000/api``___.___
## Documents & Links
-   [Software Requirements Specification](https://drive.google.com/file/d/16P3u-TN29-a_zdGoybNxbZJS0BSj8QMu/view?usp=sharing)
-   [Software Architecture Document](https://drive.google.com/file/d/1u8kIYB3H1p1x4A8SMqJynv2mRLd7J2Jz/view?usp=sharing)
-   [Software Design Document](https://drive.google.com/file/d/1WpE52fKBgNV14rL6fBHWNQ9GAAQQ2PTi/view?usp=sharing)
-   [User Guide](https://drive.google.com/file/d/1a1CDlHIwFV-G35-sFf2DcpUd0SS1DqOy/view?usp=sharing)
-   [Source Code](https://drive.google.com/file/d/1y2fEyNlyEN3SeHiuH0cuWj57fDhghAc3/view?usp=sharing)
-   [Executable (Deployment Link)](https://www.ntustsers.xyz)
-   [Presentation Slides](https://drive.google.com/file/d/1uNfKhgFXfIXfwSGeXhlK35-MhsRvUbMY/view?usp=sharing)
-   [Presentation Video](https://youtu.be/LAXDKqn0O7o)
## Deployment
Our System is currently being deployed at https://www.ntustsers.xyz with full functionality available.