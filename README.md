# Room Reservation System
### 110-1 CS3025 Software Engineering Group 6
#### B10732012 Jun-Yu (Andrew) Chen, B10832004 Shu-Yan Cheng, B10832008 Yun-Hsuan Tsai, B10832018 Hao Kuan, B10832021 Wei Chen

## Introduction
The main goal of the system's design is to improve the user experience of the current NTUST library room reservation system with a total redesign. To achieve this, we added some new concepts and functions into our system:
- **Grouping system:**

     We introduced a new concept called "Group" into the reservation system. Users are able to add team members into a group so personnel in the meeting could be tracked, reminder-related functionality is also based on grouping.
     
- **Email/Calendar notice:**

     We use Google API to send email and add the schedule into Google Calendar. After you reserve a meeting. The system will automatically send an e-mail to all the members in the group. The schedule will also be added to members' calendar.
     
- **Simple and Intuitive UI/UX:**
     
     We simplify the user flow for room reservation. Several clicks are all you need when reserving a meeting room.
     
[![Landing](https://user-images.githubusercontent.com/64970325/150075022-592d76ca-3046-4818-b7c5-65a1a1dd3fa6.png)](https://www.ntustsers.xyz)

## How To Build
- **Frontend**: 
     1. Install npm and run ``npm install`` in ``/frontend``. 
     2. Run ``npm run serve`` in ``/frontend`` to start a development server. 
     3. Open a browser and direct to ``http://localhost:8080``. 
     4. Now you are good to go. 
     
     ___Note: This frontend will still call api to our server instead of the one you run locally.___
- **Backend**: 
     1. Install ``python`` and ``virtualenv``. 
     2. Create a virtual environment using ``virtualenv virtualEnv``. (virtualEnv can be replaced by whatever you want)
     3. If you are using Linux, activate your virtual environment using ``source virtualEnv/bin/activate``. 
     4. Run ``pip install -r requirement.txt`` in ``/backend`` to install all necessary dependencies. 
     5. Run ``python app.py`` in ``/backend`` to start your backend server. 
     6. Now you are good to go. 
    
     ___Note: If you want to use this backend server as your api server, replace every___ ``https://ntustsers.xyz/api/`` ___with___ ``http://localhost:5000/api``___.___
## Documents & Links (In Google Drive)
__For raw files please refer to the [Releases](https://github.com/albert9052/software-engineering-project/releases) tab of this repository or download manually from given Google Drive links.__
-   [Software Requirements Specification](https://drive.google.com/file/d/1DSfeUkJNkMURLOl2SYgnMg1yWLoZbjlP/view?usp=sharing)
-   [Software Architecture Document](https://drive.google.com/file/d/10NRchKQRNI0Tl6I3UEFTmREwld-A03Kd/view?usp=sharing)
-   [Software Design Document](https://drive.google.com/file/d/1HUiTWgxCEUIvl7nRt6rXkVnR1ef_rZeR/view?usp=sharing)
-   [User Guide](https://drive.google.com/file/d/1iHDFlv9bDNhnJba4uo35CiqX6c3FvGFM/view?usp=sharing)
-   [Source Code](https://drive.google.com/file/d/1iJRG6AtXlG-mD2v1rybPZWL8eD-Y3DlX/view?usp=sharing)
-   [Executable (Deployment Link)](https://www.ntustsers.xyz)
-   [Presentation Slides](https://drive.google.com/file/d/18hik6miEUCfGkMzL2BDHSZeRJXDF0JDL/view?usp=sharing)
-   [Presentation Video](https://youtu.be/LAXDKqn0O7o)
## Deployment
Our System is currently being deployed at https://www.ntustsers.xyz with full functionality available.
