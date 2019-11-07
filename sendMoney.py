from reddeApi.redde import ReddeApi

app_id = "" #Enter App ID Here
api_key = "" #Enter Api Key Here

#Instantiate ReddeApi Class
redde = ReddeApi(api_key, app_id)
client_ref = redde.clientReferenceNumber(6)
client_id = redde.randomClientID(6)


#Call sendMoney Function
send = redde.sendMoney(1, 233500000604, client_ref, client_id, "MTN",)

print(send)