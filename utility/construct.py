def construct(url:str, alias:str) -> dict:
   '''
   arranges the data as dictonary
   '''
   data = {
      "url": url.lower(),
      "alias": alias.lower()
   }
   return data