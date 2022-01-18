from datetime import date, datetime
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import json
import pygsheets
import numpy as np
import string
import random
import requests
#from google.oauth2 import id_token
#from google.auth.transport import requests
from oauth2client import client

# CLIENT_ID and CLIENT_SECRET for Google OAuth, this may be replaced by yours ID and secret. 
CLIENT_ID = "317495594650-racsmtup6d4bd9ur8esrkarfulqch1fl.apps.googleusercontent.com"
CLIENT_SECRET = "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"

gc = pygsheets.authorize(service_file='key.json')
sheet_lists = gc.open_by_url('https://docs.google.com/spreadsheets/d/16oMw0JkQYiEXWYRdE2IsWO8nWhyA9GfkEm4KwRaNJPQ/edit#gid=0')

#get sheets in google sheet
userSheet = sheet_lists.worksheet_by_title("User Info")
groupSheet = sheet_lists.worksheet_by_title("Group")
groupMemberSheet = sheet_lists.worksheet_by_title("Group Member")
reservation_sheet = sheet_lists.worksheet_by_title("Reservation")
time_sheet = sheet_lists.worksheet_by_title("Reservation Time")
#generate group ID
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def addCalendar(title, date, startTime, endTime, emails):
    #print(title, date, startTime, endTime, emails)
    url = 'https://script.google.com/macros/s/AKfycbxj3pxYzZ5VtbWwi-SRInhFtuYK_WxTgTh1rSxwxKHBYbY4n6g3sBBHQkyB6oeCh-EG/exec?title='+title+'&date='+date+'&startTime='+startTime+'&endTime='+endTime+'&emails='+emails
    requests.get(url)
def sendEmail(title, date, startTime, endTime, emails, room, name):
    #print(title, date, startTime, endTime, emails, room, name)
    url = 'https://script.google.com/macros/s/AKfycbwYDu8vC4PoDxX58Zbd3KsdZYDHPyz2rC56L4KVqluBiEQApKu8kkHPbcPSRo66271E/exec?title='+title+'&date='+date+'&startTime='+startTime+'&endTime='+endTime+'&emails='+emails+'&room='+room+'&name='+name
    requests.get(url)

@app.route("/api/test", methods=['GET'])
def test():
    print("TEST")
    return {"HI": "hey"}

@app.route("/api/reserveOneTime", methods=['POST'])
def reserveOneTime():
    reservation_id, group_ID, user_ID, user_emails_string, title, date, times, room, description = reservation_sheet.rows, request.json['group_ID'], request.json['user_ID'], request.json['user_ID'], request.json['title'], request.json['date'], request.json['time'], request.json['room'], request.json['description']

    times = [[int(t.split(':')[0]), int(t.split(':')[1])] for t in times]
    times.sort(key=lambda row: (row[0], row[1]))
    times = [str(t[0])+':'+str(t[1]) if t[1]!=0 else str(t[0])+':00' for t in times]

    # 提取 user name
    user_name = userSheet.cell((userSheet.find(user_ID, matchCase = True ,matchEntireCell = True, cols = (1, 1))[0].row, 3)).value

    # 提取 users
    user_list = groupMemberSheet.find(group_ID, matchCase = True ,matchEntireCell = True, cols = (1, 1))
    for user in user_list:
        user_emails_string += ' ' + groupMemberSheet.cell((user.row, 2)).value
    
    # 確認時間 avaliable
    same_room_rsvs = reservation_sheet.find(room, matchCase = True ,matchEntireCell = True, cols = (7, 7))
    reservation_list = []
    if len(same_room_rsvs) > 0:
        reservation_list = reservation_sheet.get_values('A2', 'H' + str(same_room_rsvs[-1].row))
    time_list = time_sheet.get_values('A2', 'B' + str(time_sheet.rows))

    for i in reservation_list:
        if i[3] != date or i[6] != room or i[7] == 'TRUE':
            continue
        #print(i)
        for time in time_list: 
            if time[0] == i[0] and time[1] in times:
                return {"success": False}
            #print(time)
            
    # 寫入 time sheet
    for time in times:
        time_sheet.insert_rows(1 ,1, [[str(reservation_id), time]])

    # 寫入 reservation sheet
    reservation_sheet.insert_rows(1 ,1, [[str(reservation_id), str(user_ID), str(group_ID), date, title, description, room, False]])

    # 寄信
    sendEmail(title, date, times[0], times[-1], user_emails_string, room, user_name)
    
    # 加入日曆
    addCalendar(title, date, times[0], times[-1], user_emails_string)
    
    return {"success": True, "reservation_id": reservation_id}

@app.route("/api/cancelReservation", methods=['POST'])
def cancelReservation():
    rsv = reservation_sheet.find(str(request.json['meeting_ID']), matchCase = True ,matchEntireCell = True, cols = (1, 1))
    if len(rsv)==0: 
        return {"success": False}
    reservation_sheet.update_values((rsv[0].row, 8), [[True]])
    return {"success": True}

@app.route("/api/getDailyReservation", methods=['POST'])
def getDailyReservation():
    date = request.json['date']
    room = request.json['room_number']
    reservationDict = {}
    rsvs = reservation_sheet.find(date, matchCase = True ,matchEntireCell = True, cols = (4, 4))
    reservation_list = []
    if len(rsvs) > 0:
        reservation_list = reservation_sheet.get_values('A2', 'H' + str(rsvs[-1].row))
    time_list = time_sheet.get_values('A2', 'B' + str(time_sheet.rows))

    for i in reservation_list:
        if i[7] == 'TRUE' or i[3] != date or i[6] != room:
            continue
        for timeCell in time_list:
            if timeCell[0] == i[0]:
                reservationDict[timeCell[1]] = True
        
    '''
    for rsv in rsvs:
        idx = 9
        while 1:
            time = reservation_sheet.cell((rsv.row, idx)).value
            if time == '':
                break
            reservationDict[time] = True
            idx += 1     
    '''

    for i in range(8, 21):
        time = str(i)+':00'
        if not time in reservationDict.keys():
            reservationDict[time] = False
        time = str(i)+':30'
        if not time in reservationDict.keys():
            reservationDict[time] = False
    return {"success": True, "dailyReservation": reservationDict}

@app.route("/api/getAllReservations", methods=['POST'])
def getAllReservations():

    rsvs = reservation_sheet.find(str(request.json['user_ID']), matchCase = True ,matchEntireCell = True, cols = (2, 2))
    reservation_list = reservation_sheet.get_values('A2', 'H' + str(rsvs[-1].row))

    reservation_past = []
    reservation_future = []

    for rsv in reservation_list:
        if rsv[1] == str(request.json['user_ID']) and rsv[-1] != 'TRUE':

            res_date = datetime.strptime(rsv[3], '%Y-%m-%d').date()
            dt = datetime.today()
            only_date = dt.date()
            if res_date < only_date:
                reservation_past += [[rsv[0], rsv[4], rsv[5] ]]
            else:
                reservation_future += [[rsv[0], rsv[4], rsv[5] ]]

    

    return {"success": True, "allReservations": {"reservation_past": reservation_past, "reservation_future": reservation_future}}
    

@app.route("/api/checkReservation", methods=['POST'])
def checkReservation():
    reservation, rsv_ID = {}, request.json['meeting_ID']
    reservation['time'] = []
    rsv_fnd, time_fnd = reservation_sheet.find(str(rsv_ID), matchCase = True ,matchEntireCell = True, cols = (1, 1)), time_sheet.find(str(rsv_ID), matchCase = True ,matchEntireCell = True, cols = (1, 1))
    
    time_list = time_sheet.get_values('A2', 'B' + str(time_fnd[-1].row))
    for row in time_list:
        if row[0] == str(rsv_ID):
            reservation['time'] += [row[1]]
    #print(row_index)
    reservation_information = reservation_sheet.get_values('A' + str(rsv_fnd[0].row), 'G' + str(rsv_fnd[0].row))
    reservation['group_ID'] = reservation_information[0][2]
    reservation['date'] = reservation_information[0][3]
    reservation['title'] = reservation_information[0][4]
    reservation['description'] = reservation_information[0][5]
    reservation['room number'] = reservation_information[0][6]
    #reservation['group_ID'] = reservation_sheet.cell((rsv_fnd[0].row, 3)).value
    #reservation['date'] = reservation_sheet.cell((rsv_fnd[0].row, 4)).value
    #reservation['title'] = reservation_sheet.cell((rsv_fnd[0].row, 5)).value
    #reservation['description'] = reservation_sheet.cell((rsv_fnd[0].row, 6)).value
    #reservation['room number'] = reservation_sheet.cell((rsv_fnd[0].row, 7)).value
    return {"success": True, "reservation": reservation}

#--------------------------------------------------------------------------------

@app.route("/api/signIn", methods=['POST'])
def signIn():
    auth_code = request.json['token']
    #print("Verifying auth_code...")
    #print(auth_code)
    id_token, user_info = {}, {'is_registered':True}
    try: 
        credentials = client.credentials_from_code(CLIENT_ID, CLIENT_SECRET, scope='profile email', code=auth_code)
        id_token = credentials.id_token
    except client.FlowExchangeError as e: 
        print(e)
        return {"success": False, 'error': 'Invalid auth token'}
    else:
        user_ID = id_token['email']
        fnd = userSheet.find(user_ID, matchCase = True, matchEntireCell = True, cols = (1, 1))
        if len(fnd) == 0:
            user_info['is_registered'] = False
            user_info['user_ID'] = user_ID 
            userSheet.insert_rows(1, 1, [user_ID])
        elif userSheet.cell((fnd[0].row, 2)).value=='':
            user_info['user_ID'] = user_ID 
            user_info['is_registered'] = False
        else:            
            user_info['user_ID'] = user_ID 
            user_info['gender'] = userSheet.cell((fnd[0].row, 2)).value
            user_info['name'] = userSheet.cell((fnd[0].row, 3)).value
            user_info['job_title'] = userSheet.cell((fnd[0].row, 4)).value
            user_info['phone'] = userSheet.cell((fnd[0].row, 5)).value[1:]
    return {"success": True, "userInfo": user_info}
    
@app.route("/api/saveDetailedUserInformation", methods=['POST'])
def saveDetailedUserInformation():
    try:
        UserID, gender, name, jobTitle, phone = request.json['UserID'], request.json['gender'], request.json['name'], request.json['jobTitle'], request.json['phone']

        print(UserID)
        fnd = userSheet.find(UserID, matchCase = True ,matchEntireCell = True, cols = (1, 1))
        #if user id exist, return false
        if len(fnd) == 0:
            return {"success": False}
        
        #input value
        userDetail = [[UserID, gender, name, jobTitle, "-"+str(phone)]]
        userSheet.update_values('A'+str(fnd[0].row)+':E'+str(fnd[0].row), userDetail)
        return {"success": True}
    except:
        print('Exeption occur!!')
        return {"success": False}

    

@app.route("/api/getDetailedUserInformation", methods=['POST'])
def getDetailedUserInformation():
    try:
        UserID = request.json['UserID']
        data = userSheet.find(UserID, matchCase = True, matchEntireCell = True, cols = (1, 1))
        if len(data) == 0 :
            print('User not found')
            return {"success": False}
        
        index = data[0].row
        returnList = userSheet.get_row(index, include_tailing_empty = False)
        returnList[4] = returnList[4][1:]
        return {"success": True, "detailedUserInformation": returnList}
    except: 
        print('Exeption occur!!')
        return {"success": False}

    
@app.route("/api/addGroup", methods=['POST'])
def addGroup():
    try:
        groupName = request.json['groupName']
        emails = request.json['emails']
        description = request.json['description']
        userID = request.json['userID']
        if(len(groupName) == 0):
            print('Group name should not be empty !')
            return {"success": False}
        
        #generate a random ID
        groupID = id_generator(6, '1234567890ABCDEFGH')
        #be sure groupID is the only one
        while len(groupSheet.find(groupID, matchCase = True ,matchEntireCell = True, cols = (1, 1))) != 0:
            groupID = id_generator(6, '1234567890ABCDEFGH')
            
        #input value
        group = [[groupID,groupName, description, userID, False]]
        
        #input group member information
        for i in range(0, len(emails)):
            groupMemberSheet.insert_rows(1, 1, [[groupID, emails[i]]])
        
        groupSheet.insert_rows(1, 1, group)
        return {"success": True, "groupID": groupID}
        
    except Exception as e:
        print('Exeption occur!!')
        print(e)
        return {"success": False}
    

@app.route("/api/saveGroup", methods=['POST'])
def saveGroup():
    try:
        groupID, groupName, emails, description, userID = request.json['groupID'], request.json['groupName'], request.json['emails'], request.json['description'], request.json['userID']
        #modify group page
        fnd = groupSheet.find(groupID, matchCase = True ,matchEntireCell = True, cols = (1, 1))
        if(len(fnd) != 0):
            groupSheet.update_values('A'+str(fnd[0].row)+'D'+str(fnd[0].row), [[groupID,groupName, description, userID]])
        else:
            print("groupID not found")
            return {"success": False}
        
        #modify group member page
        fnd = groupMemberSheet.find(groupID, matchCase = True ,matchEntireCell = True, cols = (1, 1))
        
        for i in range(len(fnd)-1, -1, -1):
            groupMemberSheet.delete_rows(fnd[i].row ,1)

        #then add members again
        for i in range(0, len(emails)):
            array = [groupID ,emails[i]]
            groupMemberSheet.insert_rows(1 ,1 ,array)

        return {"success": True}
        
    except Exception as e:
        print(e)
        return {"success": False}
    
@app.route("/api/getGroupList", methods=['POST'])
def getGroupList():
    try:
        userID = request.json['userID']
        
        reList = []
        fnd = groupSheet.find(userID, matchCase = True ,matchEntireCell = True, cols = (4,4))
        if len(fnd)==0:
            return {"success": True, "groupList": []}
        groupList = groupSheet.get_values('A' + str(fnd[0].row), 'E' + str(fnd[-1].row))
        
        offset = fnd[0].row
        memberList = groupMemberSheet.get_values('A2', 'B' + str(groupMemberSheet.rows))
        
        for f in fnd:
            if groupList[f.row - offset][4] == 'TRUE':
                continue
            groupID, emails = groupList[f.row - offset][0], []
            for i in memberList:
                if i[0] == groupID:
                    emails += [i[1]]
            reList += [{'groupID':groupID, 'GroupName':groupList[f.row - offset][1], 'Description':groupList[f.row - offset][2], 'emails': emails}]
        return {"success": True, "groupList": reList}
    except Exception as e:
        print(e)
        return {"success": False}
    
    
@app.route("/api/deleteGroup", methods=['POST'])
def deleteGroup():
    try:
        userID = request.json['userID']
        groupID = request.json['groupID']
        fnd = groupSheet.find(groupID, matchCase = True ,matchEntireCell = True, cols = (1,1))
        if(len(fnd) == 0):
            print('GroupID not found')
            return {"success": False}
        
        if(groupSheet.get_value('D' + str(fnd[0].row)) == userID):
            groupSheet.update_value('E'+str(fnd[0].row), True)
            return {"success": True}
        else:
            print('You cannot delete the group')
            return {"success": False}
    except Exception as e:
        print(e)
        return {"success": False}
    

app.run(debug=True)
