import argparse

import generate_html
import fetch_coursework
import send_email

def main():
    """
    Must pass in config.yaml and credentials.json. 
    """
    parser = argparse.ArgumentParser(description='pass in arguments for sending class reports.')
    parser.add_argument('credentials', help='credentials for accessing Classroom API')
    parser.add_argument('config', help='yaml config file for email configuration')
    
   
    args = parser.parse_args()
    name = input("Enter the student's name: ")
    print("Fetching coursework...")
    fetch_coursework.main(args.credentials)
    print("Generating email body...")
    generate_html.main(name)
    print("Sending email...")
    send_email.main(args.config, name)
    print("Email successfully sent!")
        
if __name__ == '__main__':
    main()