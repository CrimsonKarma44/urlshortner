import json
import os
import pyperclip

def JsonReader()-> list:
   '''Reads the json storage file'''
   file = os.getcwd() + "/storage/file.json"
   try:
      with open(file, "r") as file:
         data = json.load(file)
      return data
      
   except Exception as err:
      return err


def JsonSaver(newData:dict) -> str:
   '''Save new data into the json storage file'''
   file = os.getcwd() + "/storage/file.json"

   data = JsonReader()
   try:
      data.append(newData)
      json_string = json.dumps(data, indent=3)
      
      with open(file, "w") as file:
         file.write(json_string)
      return "saved"
   except Exception as err:
      return err


def jsonDelete(alias:str)->list:
   '''Deletes data from the json storage file'''
   file = os.getcwd() + "/storage/file.json"
   data = JsonReader()
   try:
      for count, i in enumerate(data):
         if i['alias'] == alias.lower():
            data.pop(count)
      json_string = json.dumps(data, indent=3)
         
      with open(file, "w") as file:
         file.write(json_string)
      return data
   except Exception as err:
      return err


def jsonCopy(alias):
   '''Copies to the clipboard'''
   data = JsonReader()
   try:
      for i in data:
         if i['alias'] == alias.lower():
            pyperclip.copy(i['url'])
      return "copied to clipboard"
   except Exception as err:
      return err

