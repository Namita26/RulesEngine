# RulesEngine

This project is hosted on AWS free instance with public IP `54.244.160.6`.

Taking assignment into consideration, I have created a REST API for listening events triggered by any clients.

I have used python flask restful for implementing RESTful apis and mysql as teh database for storing the events. Also, sqlalchemy
for ORM layer.

The flask server is running on port `5000` thus, request url for api is `http://54.244.160.6`

## Input format for sending events

## API Endpoint

> POST api/rules

## Sample Request Payload

```json
{
	"noun": "bill",
	"userid": 178765,
	"ts": "20170315 134850",
	"latlong": "19.07,72.87",
	"verb": "pay",
	"timespent": 72,
	"properties": {
		"bank": "hdfc",
		"merchantid": 234,
		"value": 139.5,
		"mode": "netbank"
	}
}
```

## Sample curl payload

```
curl -X POST \
  http://localhost:5000/api/rules \
  -H 'cache-control: no-cache' \
  -H 'postman-token: 71ea91e6-63bd-5691-02da-91024369f153' \
  -d '{
	"noun": "bill",
	"userid": 178765,
	"ts": "20170315 134850",
	"latlong": "19.07,72.87",
	"verb": "pay",
	"timespent": 72,
	"properties": {
		"bank": "hdfc",
		"merchantid": 234,
		"value": 139.5,
		"mode": "netbank"
	}
}'
```
