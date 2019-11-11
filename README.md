# reddePy
<img src="https://www.reddeonline.com/assets/images/redde-logo.png" width=400>


# redde-nodejs-sdk
Python3 SDK that allows merchants to receive, send, check transaction status, and perform lots of payment transactions.

Before you can have access to APIs you need to register and create an [Account](https://app.reddeonline.com/register) on reddeonline. Header for all request should have {"apikey": "string"}: and this API key will be sent to merchant when their app configuration is setup for them by Wigal.

For more information on documentation go to developers.reddeonline.com

* [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)

## Installation
To use this library you'll need to have created a [Redde account](https://app.reddeonline.com/register).                     To install this package and use in your project, we recommend using Npm.

```
npm i redde-python-sdk                                                                                        
```


## Usage

Importing **redde-python-sdk** package

```js
const Redde = require('redde-nodejs-sdk');

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

```js
const request = require('request');
const Redde = require('redde-nodejs-sdk');
var express = require("express");
var myParser = require("body-parser");
var app = express();

app.use(myParser.json({ extended: true }));


app_id = ""; //Enter Your App ID Here
api_key = ""; //Enter Your Api Key Here

//Instantiate ReddeApi class
const redde = new Redde(api_key, app_id);


//Generating Random Client Reference
var ref = redde.clientRef(6);

//Generating Random Client ID
var clientid = redde.clientID(6);

//Calling Receive Function 
var receive = redde.receiveMoney(1, "MTN", 233240000004, ref, clientid);

//Sending a request to redde endpoint
request.post(receive, (err, res, body) => {
    if (err) {
        return console.log(err);
    }
    console.log(JSON.parse(JSON.stringify(body)));
});

//Callback Url Endpoint
app.post("/payment", function (req, res) {
    var data = req.body;
    res.send(data);

});


app.listen(8080);
```


#### Sending money to a Customer or Client

To use the API to send money to a customer, the sendMoney() method will be used which takes takes 5 required arguments which are: **amount, network type(MTN, AIRTELTIGO, VODAFONE), phone number, client reference, and client id** respectively.

```js
const request = require('request');
const Redde = require('redde-nodejs-sdk');
var express = require("express");
var myParser = require("body-parser");
var app = express();

app.use(myParser.json({ extended: true }));


app_id = ""; //Enter Your App ID Here
api_key = ""; //Enter Your Api Key Here

//Instantiate ReddeApi class
const redde = new Redde(api_key, app_id);


//Generating Random Client Reference
var ref = redde.clientRef(6);

//Generating Random Client ID
var clientid = redde.clientID(6);

//Calling Receive Function 
var receive = redde.sendMoney(1, "MTN", 233240000004, ref, clientid);

//Sending a request to redde endpoint
request.post(receive, (err, res, body) => {
    if (err) {
        return console.log(err);
    }
    console.log(JSON.parse(JSON.stringify(body)));
});

//Callback Url Endpoint
app.post("/payment", function (req, res) {
    var data = req.body;
    res.send(data);

});


app.listen(8080);
```

## Callbacks
Most APIs implement callbacks for easy tracking of api transactions so we have shown you how to implement. Check it out in the code below.

```js

//Callback Url Endpoint
app.post("/payment", function (req, res) {
    var data = req.body;
    res.send(data);

});
```

# License
This library is released under the MIT License
