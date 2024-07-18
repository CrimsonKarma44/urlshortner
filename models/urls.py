class Url():
   '''Url model class'''
   def __init__(self, url:str, alias:str) -> None:
      self.url = url
      self.alias = alias

   def constructJson(self) -> dict:
      '''
      arranges the data as dictonary
      '''
      data = {
         "url": self.url.lower(),
         "alias": self.alias.lower()
      }
      return data
   

