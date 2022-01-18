# Room Reservation System

2. 組員
     B10732012 陳俊宇
     B10832004 程書彥
     B10832008 蔡芸軒
     B10832018 官澔
     B10832021 陳緯

3. 專案介紹
     The main goal we design the system is to improve the user experience of current library meeting room reservation system.
     To achieve this , we added some new concepts and functions into our new system :
     1.Grouping system : 
          We introduce a new concept "Group" into the reservation system. Add your team members into 
          your own group so you can easily track who is in the meeting, and also convenient to 
          remind them of the following meeting.
     2.Email/Calender notice : 
          We use Google API to send email and add the schedule into Google Calender. 
          After you reserve a meeting. The system will automatically send an e-mail to all the members in the group.
          The schedule will also be added to members' calender.
     3.Simple UI/UX : 
          We simplify the user flow for reserving meeting. All you need is several click to reserve a meeting room. 
     enjoy ^_^ ~

5. How to build frontend and backend locally
     Frontend: 
          1. Install npm and run "npm install" in "/frontend". 
          2. Run "npm run serve" in "/frontend" to start a development server. 
          3. Open a browser and direct to http://localhost:8080. 
          4. Now you are good to go. 
          (This frontend will still call api to our server, instead of the one you run locally.)
     Backend: 
          1. Install python and virtualenv. 
          2. Create a virtual environment using "virtualenv virtualEnv". (virtualEnv can be replaced by whatever you want)
          3. If you are using Linux, activate your virtual environment using "source virtualEnv/bin/activate". 
          4. Run "pip install -r requirement.txt" in "/backend" to install all necessary dependencies. 
          5. Run "python app.py" in "/backend" to start your backend server. 
          6. Now you are good to go. 
          (If you want to use this backend server as your api server, replace every "https://ntustsers.xyz/api/" with "http://localhost:5000/api".)

6. 部署的網站位置（ntustsers.xyz)
     https://www.ntustsers.xyz
