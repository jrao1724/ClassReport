import argparse

from jobs import fetch_coursework, generate_html, send_email

def main():
    """
    Wrapper to run the jobs in succession. Requires credentials.json and config.yaml as arguments.
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