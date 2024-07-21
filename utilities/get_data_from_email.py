import imaplib
import email
import re
from email.header import decode_header
from bs4 import BeautifulSoup


def get_latest_otp(user, password, imap_url):
    def get_body(msg):
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True)
                elif part.get_content_type() == "text/html":
                    return part.get_payload(decode=True)
        else:
            return msg.get_payload(decode=True)
        return None

    def search(key, value, con):
        result, data = con.search(None, key, '"{}"'.format(value))
        return data

    def get_emails(result_bytes, con):
        msgs = []
        for num in result_bytes[0].split():
            typ, data = con.fetch(num, '(RFC822)')
            msgs.append(data)
        return msgs

    def extract_number_after_text(full_text, constant_text):
        escaped_text = re.escape(constant_text.strip())
        pattern = escaped_text + r"\s*(\d+)"
        match = re.search(pattern, full_text)
        if match:
            return match.group(1)
        else:
            return None

    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user, password)
    con.select('Inbox')

    subject_to_search = "One Time Passcode for your Twikkie Account"

    msgs = get_emails(search('SUBJECT', subject_to_search, con), con)

    if msgs:
        latest_email_data = msgs[-1]

        for response_part in latest_email_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                # Decode the email subject
                email_subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(email_subject, bytes):
                    email_subject = email_subject.decode(encoding if encoding else "utf-8")

                # Get the email body
                email_body = get_body(msg)
                if email_body:
                    email_body = email_body.decode()

                    # If the email body is in HTML, parse and extract text
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/html":
                                email_body = part.get_payload(decode=True)
                                soup = BeautifulSoup(email_body, "html.parser")
                                email_body = soup.get_text()

                    # Extract OTP
                    constant_text = "To authenticate, please use this One Time Password (OTP):"
                    otp_code = extract_number_after_text(email_body, constant_text)

                    if otp_code:
                        print(otp_code)
                    else:
                        print("Number not found after the constant text.")
                else:
                    print("Could not find body in the email.")
    else:
        print("No emails found with the specified subject.")

    con.logout()
    print(otp_code)
    return otp_code


def get_latest_email(user, password, imap_url):
    def get_body(msg):
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True)
                elif part.get_content_type() == "text/html":
                    return part.get_payload(decode=True)
        else:
            return msg.get_payload(decode=True)
        return None

    def search(key, value, con):
        result, data = con.search(None, key, '"{}"'.format(value))
        return data

    def get_emails(result_bytes, con):
        msgs = []
        for num in result_bytes[0].split():
            typ, data = con.fetch(num, '(RFC822)')
            msgs.append(data)
        return msgs

    def extract_link(full_text):
        pattern = r"https?://[^\s]+"
        match = re.search(pattern, full_text)
        if match:
            return match.group(0)
        else:
            return None

    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user, password)
    con.select('Inbox')

    subject_to_search = "Forgot Password Twikkie Account"

    msgs = get_emails(search('SUBJECT', subject_to_search, con), con)

    if msgs:
        latest_email_data = msgs[-1]

        for response_part in latest_email_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                # Decode the email subject
                email_subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(email_subject, bytes):
                    email_subject = email_subject.decode(encoding if encoding else "utf-8")

                # Print the email subject
                # print("Subject:", email_subject)

                # Get the email body
                email_body = get_body(msg)
                if email_body:
                    email_body = email_body.decode()

                    # If the email body is in HTML, parse and extract text
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/html":
                                email_body = part.get_payload(decode=True)
                                soup = BeautifulSoup(email_body, "html.parser")
                                email_body = soup.get_text()

                    # Extract Link
                    link = extract_link(email_body)

                    if link:
                        print(link)
                    else:
                        print("Link not found in the email body.")
                else:
                    print("Could not find body in the email.")
    else:
        print("No emails found with the specified subject.")

    con.logout()
    return link
