import json
import re
import discord
import datetime
from timeboxIssueController import create_timebox_issue
from issueController import create_issue
from issueController import update_issue

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def find_date(input_string):
    if not isinstance(input_string, str):
        return 'Error: input must be a string.'

    yyyy_mm_dd_pattern = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
    matches = yyyy_mm_dd_pattern.findall(input_string)

    if not matches:
        return 'Error: No date found in the input string.'

    return matches[0]

def find_waktu(input_hour):
    if input_hour in range(0, 10):
        return 'Pagi'
    elif input_hour in range(10, 15):
        return 'Siang'
    elif input_hour in range(15, 18):
        return 'Sore'
    elif input_hour in range(18, 24):
        return 'Malam'
    else:
        return 'Invalid hour'

def find_hour(input_string):
    hour_minute_format_pattern = re.compile(r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\b')
    matches = hour_minute_format_pattern.findall(input_string)
    return matches[0]

def find_project(channel_id):
    try:
        with open('projects.json', 'r') as file:
            project_json = json.load(file)
    except (FileNotFoundError, PermissionError) as e:
        return f'Error: Could not open the JSON file. {str(e)}'

    return project_json.get(str(channel_id), 'Error: Could not find project in the JSON data.')

def get_response(message: str, channel_id :str, author :str, attachment) -> str:
    p_message = message
    attachmentLinks = []
    for att in attachment:
        attachmentLinks.append(att.url)
    print(attachmentLinks)
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    current_hour = datetime.datetime.now().hour

    response_msg = ">>> "
    prefix = p_message[:2]
    waktu = find_waktu(current_hour)
    if '!report' in p_message:
        report_index = p_message.find('!report')
        report_message = p_message[report_index + len('!report'):].strip()

        body = {
        'created_at' : "",
        'created_by' : "338",
        'duedate' : "",
        'feature_issue' :  "",
        'is_accept_review' : "",
        'is_review': "1",
        'm_project_id' : "2",
        'm_project_status' : "1",
        'name' : f"Laporan {author} {current_time} {waktu}",
        'point' : 0,
        'type' : "0",
        'user_acceptance_id' : 44,
        'user_auth_id' : 338,
        }
        id_issue = create_issue(body)
        attachmentValue = ""
        for link in attachmentLinks:
                attachmentValue += f'<p><a target="_blank" rel="noopener noreferrer" href="{link}">Attachment</a></p> '
            
        
        update_body = {
        'background' : f"{report_message}",
        'id' : id_issue
        }
        update_body['background'] += attachmentValue
        print(update_body)
        update_issue(update_body)
        return f'{waktu} Kak {author},\nTerimakasih atas reportnya.\n\nKeluhan Kakak sudah masuk dalam antrian task dan menunggu untuk dicek oleh tim kami. Kami mengusahakan yang terbaik untuk kakak.\n\nMohon ditunggu untuk informasi selanjutnya kak.'
    
    if prefix == '!s':
        if p_message == prefix + " " + 'hello':
            return 'hey there'
        if p_message == prefix:
            return 'need help ?'
        
        
        if prefix + ' ' + 'tb' in p_message:

            timebox_index = p_message.find("timebox")
            pipe_index = p_message.find("|")
            issue_name = p_message[timebox_index + len("timebox"):pipe_index].strip()
            p_index = p_message.find("P")
            point = p_message[p_index + 1:].split()[0]    
            dates = find_date(p_message)
            hour = find_hour(p_message)
            
            project_data = find_project(channel_id)
            if isinstance(project_data, dict):
                project = project_data['m_project_id']
                project_name = project_data['project_name']
            else:
                return project_data
            
            point = int(point)
            print(f"channel id : {channel_id}")
            print(f"point : {point}")
            print(f"dates : {dates}")
            print(f"hour : {hour}")
            print("issue name : " + issue_name)
            print(f"m_project_id : {project}")
            print(f"project name : {project_name}")
            
            if point > 8:
                response_msg = "Point tidak boleh lebih dari 8"
            if p_index == -1:
                response_msg = "invalid point format"

            body = {'name': issue_name, 'duedate':f"{dates} {hour}",'type_repetition':'', 'user_auth_id' : '76', 'm_project_id':f'{project}', 'description':'desc test', 'point':point, 'status':'1', 'created_by':'76'}

            req = create_timebox_issue(body)
            print(req.text)
            if req.status_code == 200:
                response_msg = f">>> Issue berhasil dibuat!\n{issue_name}\nPoint : {point}\nDuedate : {dates} {hour}\nProject : {project_name}"
            else:
                response_msg = f"Error: Received status code {req.status_code}."
                if req.status_code == 400:
                    response_msg += " Bad Request. Please check your request body."
                elif req.status_code == 401:
                    response_msg += " Unauthorized. Please check your authentication."
                elif req.status_code == 404:
                    response_msg += " Not Found. The requested resource could not be found."
                elif req.status_code == 500:
                    response_msg += " Internal Server Error. The server encountered an unexpected condition."
            return response_msg