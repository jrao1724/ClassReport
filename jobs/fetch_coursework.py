from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

# remember to delete token.pickle if you change these
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly', 
          'https://www.googleapis.com/auth/classroom.coursework.me']

def main(credential_file):
    """
    Fetches all active classes the user is currently a part of. From those courses,
    all coursework is retrieved and is then placed into a coursework.json data structure.
    """
    creds = None
    
    # this will be created when initially run
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credential_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])
    
    course_work_dict = {}

    if not courses:
        print("No courses were returned.")
        exit
    else:
        for course in courses:
            course_id = course['id']
            if course['courseState'] == 'ACTIVE':
                course_work = service.courses().courseWork().list(courseId=course_id).execute()
                course_work_dict.update(
                    {course['name']: course_work}
                )
                
    with open('coursework.json', 'w', encoding='utf-8') as f:
        json.dump(course_work_dict, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
    