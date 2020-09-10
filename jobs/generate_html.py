import datetime
import json
import os
from collections import OrderedDict

def main(name):
    """
    Generates the HTML from the coursework data structure that gets created from
    fetch_coursework.py. It's messy but it works. 
    """
    today = datetime.datetime.today().strftime("%B %d, %Y")
    body_text = """
        <html>
        <head>
            <style type = text/css>
                @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

                #assignments {
                    font-family: 'Roboto', sans-serif;
                    border-collapse: collapse;
                    width: 100%;
                }
                #assignments td, #assignments th {
                    border: 1px solid #ddd;
                    padding: 8px;
                }
                #assignments tr:nth-child(even) {
                    background-color: #f2f2f2;
                }
                #assignments tr:hover {
                    background-color: #ddd;
                }
                #assignments th {
                    padding-top: 12px;
                    padding-bottom: 12px;
                    text-align: left;
                    background-color: #78acff;
                    color: black;
                }
                
                body {
                    font-family: 'Open Sans', sans-serif;
                }
            </style>
        </head>

        """
    body_text += f"""
        <body>
            <h1>{name}'s Homework for {today}</h1>"""


    coursework_dict = {}
    with open('coursework.json') as f:
        coursework_dict = json.load(f)
        
    
    for course, coursework in coursework_dict.items():
        body_text += f"""<h2>Assignments for {course}:</h2>"""
        
        for key, value in coursework.items():
            body_text += """
                            <table id="assignments">
                                <tr>
                                    <th>Assignment</th>
                                    <th>Due Date</th>
                                </tr>
                         """
            sorted_classes = sorted(value, key = lambda x: x['updateTime'], reverse=False)
            for items in sorted_classes:
                date = ""
                if 'dueDate' in items:
                    present = datetime.datetime.now()
                    date = str(items['dueDate']['year']) + "-" + str(items['dueDate']['month']) + "-" + str(items['dueDate']['day'])
                    due_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                    if due_date.date() > present.date():
                        body_text += f"""
                                        <tr>
                                            <td><a href="{items['alternateLink']}">{items['title']}</a></td>
                                            <td>{due_date.strftime("%B %d, %Y")}</td> 
                                        </tr>
                                     """
                    else:
                        try:
                            datetime_obj = datetime.datetime.strptime(items['creationTime'], "%Y-%m-%dT%H:%M:%SZ")
                        except:
                            datetime_obj = datetime.datetime.strptime(items['creationTime'], "%Y-%m-%dT%H:%M:%S.%fZ")
                        if (datetime.datetime.now() - datetime_obj).days < 7:
                            due_date = ""
                            body_text += f"""
                                            <tr>
                                                <td><a href="{items['alternateLink']}">{items['title']}</a></td>
                                                <td>N/A</td> 
                                            </tr>"""
            body_text += """</table>"""
            
    body_text += """</body></html>"""
    
    with open('email.html', 'w') as email_html:
        email_html.write(body_text)
        
    os.remove('coursework.json')
    
if __name__ == '__main__':
    main()