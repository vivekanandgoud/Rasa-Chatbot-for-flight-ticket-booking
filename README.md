
**Train Rasa NLU**
```
python3 -m rasa_nlu.train -c nlu_config.yml --data data/nlu.md -o models --fixed_model_name nlu --project current --verbose
```
**Run Rasa NLU**
```
python3 -m rasa_nlu.server --path ./models
```

**Train Rasa Core**
```
python3 -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue -c policy.yml
```
**To run the custom action**
```
python3 -m rasa_core_sdk.endpoint --actions actions
```

**Run Rasa Core**
```
python3 -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml
```
***Out Put*** 
```
Your input ->  hi Bot
Hey, HI I am Flight ticket booking chatbot  i can help you to book tickets.
127.0.0.1 - - [2019-05-31 00:04:28] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 243 0.023990
Your input ->  help me in booking flight tickets
Sure. Please let me know Depature location?.
127.0.0.1 - - [2019-05-31 00:04:42] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 212 0.028356
Your input ->  delhi
Sure. Please let me know To location??
127.0.0.1 - - [2019-05-31 00:04:48] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 206 0.064013
Your input ->  pune
Sure. Please let me know date of travel?.
127.0.0.1 - - [2019-05-31 00:04:57] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 209 0.027964
Your input ->  26/08/2019
please choose connection flight Yes or No?
127.0.0.1 - - [2019-05-31 00:05:03] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 210 0.023962
Your input ->  yes
available flight services:['1) Air India', '2) hello India', '3) Singapore Airlines', '4) Indigo', '5) Air India']
choose the flight number to confrim
127.0.0.1 - - [2019-05-31 00:05:07] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 319 1.047580
Your input ->  1
Congratulations **** Your Flight Booked succesfully.ref.No:43HL0004567600034"
127.0.0.1 - - [2019-05-31 00:05:11] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 246 0.039964
Your input ->
```
