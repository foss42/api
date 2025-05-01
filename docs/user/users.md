---
method: get
title: Get All Users
desc: Retrieves a list of all users.
path: /users
---

This API endpoint returns a list containing details of all registered users.

## HTTP Response Codes

| Status Code | Description                               |
| :---------- | :---------------------------------------- |
| 200         | Successful Response                       |
| 500         | Internal Server Error (Could not fetch users) |

## Sample Usage

### Example #1: Get All Users

#### API Request

```http
GET {{ site_api }}/{{ path }}
```

#### cURL Request

```bash
curl -X 'GET' \
  '{{ site_api }}/{{ path }}' \
  -H 'accept: application/json'
```

#### Response (200 OK)

*(Note: The actual response depends on the user data structure and number of users)*

```json
[
	{
		"id": "1",
        "name": "Travis Barber",
		"phone": "1-288-119-0313",
		"email": "travisbarber@apidash.in",
		"country": "United States"
	},
	{
		"id": "2",
        "name": "Hollee Fuller",
		"phone": "(313) 241-5941",
		"email": "holleefuller340@apidash.in",
		"country": "Philippines"
	},
	{
		"id": "3",
        "name": "Naomi Love",
		"phone": "1-112-492-6137",
		"email": "naomilove5709@apidash.in",
		"country": "Poland"
	},
	{
		"id": "4",
        "name": "Craig Espinoza",
		"phone": "1-155-458-4723",
		"email": "craigespinoza6358@apidash.in",
		"country": "Austria"
	},
	{
		"id": "5",
        "name": "Vaughan Mayer",
		"phone": "1-443-823-2236",
		"email": "vaughanmayer@apidash.in",
		"country": "Australia"
	}
]
```