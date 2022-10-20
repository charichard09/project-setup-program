#  Simple script to create a project folder for web developement.
#  Need to pip install pyperclip

import pyperclip

def mkProject():
  directory_name = input("What is the project name?\n")
  print(f"Copied to clipboard:\nmkdir {directory_name} {directory_name}/ss {directory_name}/js\n")
  pyperclip.copy(f"mkdir {directory_name} {directory_name}/css {directory_name}/js")
  input("Please press enter when finished.\n")
  print(f"Copied to clipboard:\ntouch index.html {directory_name}/css/styles.css {directory_name}/js/scripts.js")
  pyperclip.copy(f"touch {directory_name}/README.md {directory_name}/index.html {directory_name}/css/styles.css {directory_name}/js/scripts.js")


mkProject()