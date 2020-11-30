Hi. We are a group from Advanced Programming SMJE4383, with 3 members, which are Chen Bao Hui (A17MJ0028), Nurshazwani binti Mizaini (A17MJ0221) and Puteri Noor Iffah binti Ahmad Jalani (A17MJ0172). This is a repository to where all our project work are kept. 

The web-based project we do is a To-Do list with some basic functions such as adding, editing, skrikethrough and delete tasks. We have the codings, video demonstration, and report in this repository. 


Below are some steps to run the server:
git clone https://github.com/puteriffah/SMJE4383-assignment1.git
cd SMJE4383-assignment1
source asgt1/bin/activate
cd django
cd todo
python manage.py runserver

*note that the server may not be able to run nicely as the file locations varies.
For example, at the file 'django/todo/todo/setting.py' line 58, we have to change the file location or else an error of 'TemplateDoesNotExist at ...' will occur.