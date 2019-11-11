# reddePy
<img src="https://www.reddeonline.com/assets/images/redde-logo.png" width=400>


# reddepy-sdk
Python3 SDK that allows merchants to receive, send, check transaction status, and perform lots of payment transactions.

Before you can have access to APIs you need to register and create an [Account](https://app.reddeonline.com/register) on reddeonline. Header for all request should have {"apikey": "string"}: and this API key will be sent to merchant when their app configuration is setup for them by Wigal.

For more information on documentation go to developers.reddeonline.com

* [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)

## Installation
To use this library you'll need to have created a [Redde account](https://app.reddeonline.com/register).                     To install this package and use in your project, we recommend using Npm.

```
python3 -m pip install reddepy

or 

pip install reddepy
```


## Usage

Importing **redde python sdk** package

```python

from reddepy.redde import ReddeApi

```

Import **redde-python-package** at the top of your js file as shown above. Enter your API key and App ID which was provided to you by the Redde Team:

```python

app_id = ""  # Enter App ID Here
api_key = ""  # Enter Api Key Here


#Instantiate ReddeApi Class
redde = ReddeApi(api_key, app_id)

client_ref = redde.clientReferenceNumber(6)
client_id = redde.randomClientID(6)


``` 


## Examples

#### Receiving money from Customer or Client

To use the API to recieve money from a customer, the receiveMoney() method will be used which takes takes 5 required arguments which are: **amount, network type(MTN, AIRTELTIGO, VODAFONE), phone number, client reference, and client id** respectively.

```python

from reddepy.redde import ReddeApi


app_id = ""  # Enter App ID Here
api_key = ""  # Enter Api Key Here


#Instantiate ReddeApi Class
redde = ReddeApi(api_key, app_id)

client_ref = redde.clientReferenceNumber(6)
client_id = redde.randomClientID(6)



#Call receiveMoney Function 
recieve = redde.receiveMoney(1, 233240000004, client_ref, client_id, "MTN")
print(recieve)

```


#### Sending money to a Customer or Client

To use the API to send money to a customer, the sendMoney() method will be used which takes takes 5 required arguments which are: **amount, network type(MTN, AIRTELTIGO, VODAFONE), phone number, client reference, and client id** respectively.

```python

from reddepy.redde import ReddeApi


app_id = ""  # Enter App ID Here
api_key = ""  # Enter Api Key Here


#Instantiate ReddeApi Class
redde = ReddeApi(api_key, app_id)

client_ref = redde.clientReferenceNumber(6)
client_id = redde.randomClientID(6)



#Call receiveMoney Function 
send = redde.sendMoney(1, 233240000004, client_ref, client_id, "MTN")
print(send)

```

## Callbacks

You need to setup your callback URL for the apps we create for you on Redde

1. Login to your Redde account
2. Click on the Apps link on the navigation bar
3. You will see your list of apps in a table. Click on the modify button
4. Add your callback url(s) for both the Receive Callback URL and Cash Out Callback URL
5. Apply changes and you are all set.

Most APIs implement callbacks for easy tracking of api transactions so try and implement it to keep track of the API transactions.
```python

//Callback Url Endpoint

```

# License
This library is released under the MIT License
