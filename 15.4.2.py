import json

with open('file_json.json', 'r') as js:
    data = json.load(js)

error = []
var1 = r"http://"
var2 = r"https://"


#Проверка поля timestamp
if (isinstance(data[0]['timestamp'], int)):
     True
else: error.append(f"Тип данных timestamp {type(data[0]['timestamp'])}")

#Проверка поля item_price
if (isinstance(data[0]['item_price'], int)):
     True
else: error.append(f"Тип данных item_price {type(data[0]['item_price'])}")


#Проверка поля remoteHost
if (isinstance(data[0]['remoteHost'], str)):
     True
else: error.append(f"Тип данных remoteHost {type(data[0]['remoteHost'])}")


#Проверка поля partyId
if (isinstance(data[0]['partyId'], str)):
     True
else: error.append(f"Тип данных partyId {type(data[0]['partyId'])}")


#Проверка поля sessionId
if (isinstance(data[0]['sessionId'], str)):
     True
else: error.append(f"Тип данных sessionId {type(data[0]['sessionId'])}")


#Проверка поля pageViewId
if (isinstance(data[0]['pageViewId'], str)):
     True
else: error.append(f"Тип данных pageViewId {type(data[0]['pageViewId'])}")


#Проверка поля item_id
if (isinstance(data[0]['item_id'], str)):
     True
else: error.append(f"Тип данных item_id {type(data[0]['item_id'])}")


#Проверка поля basket_price
if (isinstance(data[0]['basket_price'], str)):
     True
else: error.append(f"Тип данных basket_price {type(data[0]['basket_price'])}")


#Проверка поля userAgentName
if (isinstance(data[0]['userAgentName'], str)):
     True
else: error.append(f"Тип данных userAgentName {type(data[0]['userAgentName'])}")


#Проверка поля eventType
if (data[0]['eventType']) == 'itemBuyEvent' or 'itemViewEvent' :
     True
else: error.append(f"В поле eventType должно содержаться только 2 значения: 'itemBuyEvent' or 'itemViewEvent' ")


#Проверка поля detectedDuplicate
if (isinstance(data[0]['detectedDuplicate'], bool)):
     True
else: error.append(f"Тип данных detectedDuplicate {type(data[0]['detectedDuplicate'])}")


#Проверка поля detectedCorruption
if (isinstance(data[0]['detectedCorruption'], bool)):
     True
else: error.append(f"Тип данных detectedCorruption {type(data[0]['detectedCorruption'])}")


#Проверка поля firstInSession
if (isinstance(data[0]['firstInSession'], bool)):
     True
else: error.append(f"Тип данных firstInSession {type(data[0]['firstInSession'])}")


#Проверка поля referer 7 and 8
if (data[0]['referer']).find(var1, 0, 7) != -1 or (data[0]['referer']).find(var2, 0, 8) != -1:
     True
elif (data[0]['referer']).find(var1, 0, 7) == -1:
     error.append(r"Строка 'referer' должная начинаться с 'http://' или 'https://'")


#Проверка поля location 7 and 8
if (data[0]['location']).find(var1, 0, 7) != -1 or (data[0]['location']).find(var2, 0, 8) != -1:
     True
elif (data[0]['location']).find(var1, 0, 7) == -1:
     error.append(r"Строка 'location' должная начинаться с 'http://' или 'https://'")


#Проверка поля item_url 7 and 8
if (data[0]['item_url']).find(var1, 0, 7) != -1 or (data[0]['item_url']).find(var2, 0, 8) != -1:
     True
elif (data[0]['item_url']).find(var1, 0, 7) == -1:
     error.append(r"Строка 'item_url' должная начинаться с 'http://' или 'https://'")

if error == []:
    print('Pass')
else: print(error)


