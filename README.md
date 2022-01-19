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
1.   [Software Requirements Specification]()
2.   [Software Architecture Document]()
3.   [Software Design Document]()
4.   [User Guide]()
5.   [Source Code]()
6.   [Executable (Deployment Link)](https://www.ntustsers.xyz)
7.   [Presentation Slides]()
8.   [Presentation Video](https://youtu.be/LAXDKqn0O7o)
## Deployment
Our System is currently being deployed at https://www.ntustsers.xyz with full functionality available.
