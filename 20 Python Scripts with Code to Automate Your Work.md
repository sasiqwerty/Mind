---
aliases: 
tags: 
date created: Monday, September 4th 2023, 10:11:55 am
date modified: Monday, September 4th 2023, 10:21:44 am
---
In this article, we’ll explore 20 Python scripts along with their code that can help you automate various tasks and boost your productivity. Whether you’re a developer, data analyst, or just someone looking to simplify their workflow, these scripts have got you covered.

## Table of Contents

1. [Introduction](#Introduction)
2. [1. Automating File Management](#1.%20Automating%20File%20Management)
	1. [1. 1 — Sorting Files in a Directory](#1.%201%20%E2%80%94%20Sorting%20Files%20in%20a%20Directory)
	2. [1. 2 — Removing Empty Folders](#1.%202%20%E2%80%94%20Removing%20Empty%20Folders)
	3. [1.3 — Renaming Multiple Files](#1.3%20%E2%80%94%20Renaming%20Multiple%20Files)
3. [Python Script to Rename Multiple Files in a Directory](#Python%20Script%20to%20Rename%20Multiple%20Files%20in%20a%20Directory)
4. [2. Web Scraping with Python](#2.%20Web%20Scraping%20with%20Python)
	1. [2. 1 — Extracting Data from a Website](#2.%201%20%E2%80%94%20Extracting%20Data%20from%20a%20Website)
5. [Python Script for Web Scraping to Extract Data from a Website](#Python%20Script%20for%20Web%20Scraping%20to%20Extract%20Data%20from%20a%20Website)
6. [Your Code here to Extract Relevant Data from the Website](#Your%20Code%20here%20to%20Extract%20Relevant%20Data%20from%20the%20Website)
	1. [2.2 — Downloading Images in Bulk](#2.2%20%E2%80%94%20Downloading%20Images%20in%20Bulk)
7. [Python Script to Download Images in Bulk from a Website](#Python%20Script%20to%20Download%20Images%20in%20Bulk%20from%20a%20Website)
	1. [2.3 — Automating Form Submissions](#2.3%20%E2%80%94%20Automating%20Form%20Submissions)
8. [Python Script to Automate Form Submissions on a Website](#Python%20Script%20to%20Automate%20Form%20Submissions%20on%20a%20Website)
9. [Your Code here to Handle the Response after Form Submission](#Your%20Code%20here%20to%20Handle%20the%20Response%20after%20Form%20Submission)
10. [3. Text Processing and Manipulation](#3.%20Text%20Processing%20and%20Manipulation)
	1. [3. 1 — Counting Words in a Text File](#3.%201%20%E2%80%94%20Counting%20Words%20in%20a%20Text%20File)
	2. [3.2 Finding and Replacing Text](#3.2%20Finding%20and%20Replacing%20Text)
	3. [3.3 Generating Random Text](#3.3%20Generating%20Random%20Text)
11. [4. Automating Emails](#4.%20Automating%20Emails)
	1. [4. 1 — Sending Personalized Emails](#4.%201%20%E2%80%94%20Sending%20Personalized%20Emails)
	2. [4.2 Emailing File Attachments](#4.2%20Emailing%20File%20Attachments)
	3. [4.3 Automatic Email Reminder](#4.3%20Automatic%20Email%20Reminder)
12. [5. Automating Excel Spreadsheets](#5.%20Automating%20Excel%20Spreadsheets)
	1. [5. 1 — Reading & Writing to Excel](#5.%201%20%E2%80%94%20Reading%20&%20Writing%20to%20Excel)
	2. [5.2 Data Analysis and Visualization](#5.2%20Data%20Analysis%20and%20Visualization)
	3. [5.3 Merging Multiple Sheets](#5.3%20Merging%20Multiple%20Sheets)
13. [6. Interacting with Databases](#6.%20Interacting%20with%20Databases)
	1. [6. 1 Connecting to a Database](#6.%201%20Connecting%20to%20a%20Database)
	2. [6.2 Executing SQL Queries](#6.2%20Executing%20SQL%20Queries)
	3. [6.3 Data Backup and Restore](#6.3%20Data%20Backup%20and%20Restore)
14. [7. Social Media Automation](#7.%20Social%20Media%20Automation)
	1. [7. 1 Posting on Twitter and Facebook](#7.%201%20Posting%20on%20Twitter%20and%20Facebook)
	2. [7.2 Automatic Social Media Sharing](#7.2%20Automatic%20Social%20Media%20Sharing)
15. [Scraping Social Media Data](#Scraping%20Social%20Media%20Data)
16. [8. Automating System Tasks](#8.%20Automating%20System%20Tasks)
	1. [8. 1 Managing System Processes](#8.%201%20Managing%20System%20Processes)
	2. [8.2 Scheduling Tasks with Cron](#8.2%20Scheduling%20Tasks%20with%20Cron)
17. [8.3 Monitoring Disk Space](#8.3%20Monitoring%20Disk%20Space)
18. [9. Automating Image Editing](#9.%20Automating%20Image%20Editing)
	1. [9. 1 Image Resizing and Cropping](#9.%201%20Image%20Resizing%20and%20Cropping)

## Introduction

Python is a popular programming language known for its simplicity and readability. It provides a vast collection of libraries and modules that make it an excellent choice for automating various tasks.

Let’s dive into the world of automation and discover 20 Python scripts that can simplify your work and save you time and effort.

## 1. Automating File Management

### 1. 1 — Sorting Files in a Directory

```python  
# Python script to sort files in a directory by their extension  
import os  
from shutil import move  
def sort_files(directory_path):  
for filename in os.listdir(directory_path):  
if os.path.isfile(os.path.join(directory_path, filename)):  
file_extension = filename.split('.')[-1]  
destination_directory = os.path.join(directory_path, file_extension)  
if not os.path.exists(destination_directory):  
os.makedirs(destination_directory)  
move(os.path.join(directory_path, filename), os.path.join(destination_directory, filename))  
```

**Description:**

This Python script organizes files in a directory by sorting them into subdirectories based on their file extensions. It identifies the file extension and moves the file to the appropriate subdirectory. This can be useful for decluttering your downloads folder or organizing files for a specific project.

### 1. 2 — Removing Empty Folders

```python  
# Python script to remove empty folders in a directory  
import os  
def remove_empty_folders(directory_path):  
for root, dirs, files in os.walk(directory_path, topdown=False):  
for folder in dirs:  
folder_path = os.path.join(root, folder)  
if not os.listdir(folder_path):  
os.rmdir(folder_path)  
```

**Description:**

This Python script searches for and deletes empty folders within a specified directory. It can help you maintain a clean and tidy folder structure, especially when dealing with large sets of data.

### 1.3 — Renaming Multiple Files

## Python Script to Rename Multiple Files in a Directory

```python
import os  
def rename_files(directory_path, old_name, new_name):  
for filename in os.listdir(directory_path):  
if old_name in filename:  
new_filename = filename.replace(old_name, new_name)  
os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
```

**Description:**

This Python script allows you to rename multiple files in a directory simultaneously. It takes the old name and the new name as inputs and replaces the old name with the new one for all the files that match the specified criteria.

## 2. Web Scraping with Python

### 2. 1 — Extracting Data from a Website

## Python Script for Web Scraping to Extract Data from a Website

```python
import requests  
from bs4 import BeautifulSoup  
def scrape_data(url):  
response = requests.get(url)  
soup = BeautifulSoup(response.text, 'html.parser')  
```

## Your Code here to Extract Relevant Data from the Website

**Description:**

This Python script utilizes the requests and BeautifulSoup libraries to scrape data from a website. It fetches the content of the webpage and uses BeautifulSoup to parse the HTML. You can customize the script to extract specific data like headlines, product information, or prices.

### 2.2 — Downloading Images in Bulk

## Python Script to Download Images in Bulk from a Website

```python
import requests  
def download_images(url, save_directory):  
response = requests.get(url)  
if response.status_code == 200:  
images = response.json() # Assuming the API returns a JSON array of image URLs  
for index, image_url in enumerate(images):  
image_response = requests.get(image_url)  
if image_response.status_code == 200:  
with open(f"{save_directory}/image_{index}.jpg", "wb") as f:  
f.write(image_response.content)
```

**Description:**

This Python script is designed to download images in bulk from a website. It assumes that the website provides a JSON API that returns an array of image URLs. The script then iterates through the URLs and downloads the images, saving them to the specified directory.

### 2.3 — Automating Form Submissions

## Python Script to Automate Form Submissions on a Website

```python
import requests  
def submit_form(url, form_data):  
response = requests.post(url, data=form_data)  
if response.status_code == 200:  
```

## Your Code here to Handle the Response after Form Submission

**Description:**

This Python script automates form submissions on a website by sending POST requests with the form data. You can customize the script by providing the URL and the necessary form data to be submitted.

## 3. Text Processing and Manipulation

### 3. 1 — Counting Words in a Text File

```python
# Python script to count words in a text file  
def count_words(file_path):  
with open(file_path, 'r') as f:  
text = f.read()  
word_count = len(text.split())  
return word_count  
```

**Description:**

This Python script reads a text file and counts the number of words it contains. It can be used to quickly analyze the content of text documents or to keep track of the word count in a writing project.

### 3.2 Finding and Replacing Text

```python  
# Python script to find and replace text in a file  
def find_replace(file_path, search_text, replace_text):  
with open(file_path, 'r') as f:  
text = f.read()  
modified_text = text.replace(search_text, replace_text)  
with open(file_path, 'w') as f:  
f.write(modified_text)  
```

**Description:**

This Python script searches for a specific text in a file and replaces it with the desired text. It can be helpful for batch-replacing certain phrases or correcting errors in large text files.

### 3.3 Generating Random Text

```python  
# Python script to generate random text  
import random  
import string  
def generate_random_text(length):  
letters = string.ascii_letters + string.digits + string.punctuation  
random_text = ''.join(random.choice(letters) for i in range(length))  
return random_text  
```

**Description:**

This Python script generates random text of a specified length. It can be used for testing and mocking purposes or even as a source of random content for creative writing.

## 4. Automating Emails

### 4. 1 — Sending Personalized Emails

```python  
# Python script to send personalized emails to a list of recipients  
import smtplib  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
def send_personalized_email(sender_email, sender_password, recipients, subject, body):  
server = smtplib.SMTP('smtp.gmail.com', 587)  
server.starttls()  
server.login(sender_email, sender_password)  
for recipient_email in recipients:  
message = MIMEMultipart()  
message['From'] = sender_email  
message['To'] = recipient_email  
message['Subject'] = subject  
message.attach(MIMEText(body, 'plain'))  
server.sendmail(sender_email, recipient_email, message.as_string())  
server.quit()  
```

**Description:**

This Python script enables you to send personalized emails to a list of recipients. You can customize the sender’s email, password, subject, body, and the list of recipient emails. Please note that for security reasons, you should use an application-specific password when working with Gmail.

### 4.2 Emailing File Attachments

```python  
# Python script to send emails with file attachments  
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email import encoders  
def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, file_path):  
server = smtplib.SMTP('smtp.gmail.com', 587)  
server.starttls()  
server.login(sender_email, sender_password)  
message = MIMEMultipart()  
message['From'] = sender_email  
message['To'] = recipient_email  
message['Subject'] = subject  
message.attach(MIMEText(body, 'plain'))  
with open(file_path, "rb") as attachment:  
part = MIMEBase('application', 'octet-stream')  
part.set_payload(attachment.read())  
encoders.encode_base64(part)  
part.add_header('Content-Disposition', f"attachment; filename= {file_path}")  
message.attach(part)  
server.sendmail(sender_email, recipient_email, message.as_string())  
server.quit()  
```

**Description:**

This Python script allows you to send emails with file attachments. Simply provide the sender’s email, password, recipient’s email, subject, body, and the path to the file you want to attach.

### 4.3 Automatic Email Reminder

```python  
# Python script to send automatic email reminders  
import smtplib  
from email.mime.text import MIMEText  
from datetime import datetime, timedelta  
def send_reminder_email(sender_email, sender_password, recipient_email, subject, body, reminder_date):  
server = smtplib.SMTP('smtp.gmail.com', 587)  
server.starttls()  
server.login(sender_email, sender_password)  
now = datetime.now()  
reminder_date = datetime.strptime(reminder_date, '%Y-%m-%d')  
if now.date() == reminder_date.date():  
message = MIMEText(body, 'plain')  
message['From'] = sender_email  
message['To'] = recipient_email  
message['Subject'] = subject  
server.sendmail(sender_email, recipient_email, message.as_string())  
server.quit()  
```

**Description:**

This Python script sends automatic email reminders based on a specified date. It is useful for setting up reminders for important tasks or events, ensuring you never miss a deadline.

## 5. Automating Excel Spreadsheets

### 5. 1 — Reading & Writing to Excel

```python  
# Python script to read and write data to an Excel spreadsheet  
import pandas as pd  
def read_excel(file_path):  
df = pd.read_excel(file_path)  
return df  
def write_to_excel(data, file_path):  
df = pd.DataFrame(data)  
df.to_excel(file_path, index=False)  
```

**Description:**

This Python script uses the pandas library to read data from an Excel spreadsheet and write data to a new Excel file. It allows you to work with Excel files programmatically, making data manipulation and analysis more efficient.

### 5.2 Data Analysis and Visualization

```python  
# Python script for data analysis and visualization with pandas and matplotlib  
import pandas as pd  
import matplotlib.pyplot as plt  
def analyze_and_visualize_data(data):  
# Your code here for data analysis and visualization  
pass  
```

**Description:**

This Python script uses pandas and matplotlib libraries to perform data analysis and visualization. It enables you to explore datasets, derive insights, and create visual representations of the data.

### 5.3 Merging Multiple Sheets

```python  
# Python script to merge multiple Excel sheets into a single sheet  
import pandas as pd  
def merge_sheets(file_path, output_file_path):  
xls = pd.ExcelFile(file_path)  
df = pd.DataFrame()  
for sheet_name in xls.sheet_names:  
sheet_df = pd.read_excel(xls, sheet_name)  
df = df.append(sheet_df)  
df.to_excel(output_file_path, index=False)  
```

**Description:**

This Python script merges data from multiple sheets within an Excel file into a single sheet. It’s handy when you have data split across different sheets but want to consolidate them for further analysis.

## 6. Interacting with Databases

### 6. 1 Connecting to a Database

```python  
# Python script to connect to a database and execute queries  
import sqlite3  
def connect_to_database(database_path):  
connection = sqlite3.connect(database_path)  
return connection  
def execute_query(connection, query):  
cursor = connection.cursor()  
cursor.execute(query)  
result = cursor.fetchall()  
return result  
```

**Description:**

This Python script allows you to connect to an SQLite database and execute queries. You can adapt it to work with other database management systems like MySQL or PostgreSQL by using the appropriate Python database drivers.

### 6.2 Executing SQL Queries

```python  
# Python script to execute SQL queries on a database  
import sqlite3  
def execute_query(connection, query):  
cursor = connection.cursor()  
cursor.execute(query)  
result = cursor.fetchall()  
return result  
```

**Description:**

This Python script is a generic function to execute SQL queries on a database. You can pass the query as an argument to the function along with the database connection object, and it will return the result of the query.

### 6.3 Data Backup and Restore

```python  
import shutil  
def backup_database(database_path, backup_directory):  
shutil.copy(database_path, backup_directory)  
def restore_database(backup_path, database_directory):  
shutil.copy(backup_path, database_directory)  
```

**Description:**

This Python script allows you to create backups of your database and restore them when needed. It’s a precautionary measure to protect your valuable data from accidental loss.

## 7. Social Media Automation

### 7. 1 Posting on Twitter and Facebook

```python  
# Python script to automate posting on Twitter and Facebook  
from twython import Twython  
import facebook  
def post_to_twitter(api_key, api_secret, access_token, access_token_secret, message):  
twitter = Twython(api_key, api_secret, access_token, access_token_secret)  
twitter.update_status(status=message)  
def post_to_facebook(api_key, api_secret, access_token, message):  
graph = facebook.GraphAPI(access_token)  
graph.put_object(parent_object='me', connection_name='feed', message=message)  
```

**Description:**

This Python script utilizes the Twython and facebook-sdk libraries to automate posting on Twitter and Facebook. You can use it to share updates, announcements, or content from your Python script directly to your social media profiles.

### 7.2 Automatic Social Media Sharing

```python  
# Python script to automatically share content on social media platforms  
import random  
def get_random_content():  
# Your code here to retrieve random content from a list or database  
pass  
def post_random_content_to_twitter(api_key, api_secret, access_token, access_token_secret):  
content = get_random_content()  
post_to_twitter(api_key, api_secret, access_token, access_token_secret, content)  
def post_random_content_to_facebook(api_key, api_secret, access_token):  
content = get_random_content()  
post_to_facebook(api_key, api_secret, access_token, content)  
```

**Description:**

This Python script automates sharing random content on Twitter and Facebook. You can customize it to fetch content from a list or database and share it periodically on your social media platforms.

## Scraping Social Media Data

```python  
# Python script for scraping data from social media platforms  
import requests  
def scrape_social_media_data(url):  
response = requests.get(url)  
# Your code here to extract relevant data from the response  
```

**Description:**

This Python script performs web scraping to extract data from social media platforms. It fetches the content of the provided URL and then uses techniques like BeautifulSoup to parse the HTML and extract the desired data.

## 8. Automating System Tasks

### 8. 1 Managing System Processes

```python  
# Python script to manage system processes  
import psutil  
def get_running_processes():  
return [p.info for p in psutil.process_iter(['pid', 'name', 'username'])]  
def kill_process_by_name(process_name):  
for p in psutil.process_iter(['pid', 'name', 'username']):  
if p.info['name'] == process_name:  
p.kill()  
```

**Description:**

This Python script uses the psutil library to manage system processes. It allows you to retrieve the list of running processes and kill a specific process by its name.

### 8.2 Scheduling Tasks with Cron

```python  
# Python script to schedule tasks using cron syntax  
from crontab import CronTab  
def schedule_task(command, schedule):  
cron = CronTab(user=True)  
job = cron.new(command=command)  
job.setall(schedule)  
cron.write()  
```

**Description:**

This Python script utilizes the crontab library to schedule tasks using cron syntax. It enables you to automate the execution of specific commands at regular intervals or at specific times.

## 8.3 Monitoring Disk Space

```python  
# Python script to monitor disk space and send an alert if it's low  
import psutil  
def check_disk_space(minimum_threshold_gb):  
disk = psutil.disk_usage('/')  
free_space_gb = disk.free / (230) # Convert bytes to GB  
if free_space_gb < minimum_threshold_gb:  
# Your code here to send an alert (email, notification, etc.)  
pass  
```

**Description:**

This Python script monitors the available disk space on your system and sends an alert if it falls below a specified threshold. It’s useful for proactive disk space management and preventing potential data loss due to insufficient disk space.

## 9. Automating Image Editing

### 9. 1 Image Resizing and Cropping

```python  
# Python script to resize and crop images  
from PIL import Image  
def resize_image(input_path, output_path, width, height):  
image = Image.open(input_path)  
resized_image = image.resize((width, height), Image.ANTIALIAS)  
resized_image.save(output_path)  
def crop_image(input_path, output_path, left, top, right, bottom):  
image = Image.open(input_path)  
cropped_image = image.crop((left, top, right, bottom))  
cropped_image.save(output_path)  
```

**Description:**

This Python script uses the Python Imaging Library (PIL) to resize and crop images. It can be helpful for preparing images for different display resolutions or specific use cases.