---
method: post
title: User Login
desc: Authenticates a user and returns an access token.
path: auth/login
---

This API endpoint authenticates a user based on their username and password and returns a JWT access token upon successful authentication.

## Request Body

The request body must contain the user's credentials.

| Attribute | Data Type | Required | Description        |
| :-------- | :-------- | :------- | :----------------- |
| `username`| `string`  | Yes      | The user's username |
| `password`| `string`  | Yes      | The user's password |

**Example:**

```json
{
  "username": "jhon",
  "password": "jhoniscool"
}
```

## HTTP Response Codes

| Status Code | Description             |
| :---------- | :---------------------- |
| 200         | Successful Response     |
| 400         | Invalid Credentials     |
| 422         | Validation Error        |

## Sample Usage

### Example : Successful Login

#### API Request

```http
POST {{ site_api }}/{{ path }}
Content-Type: application/json

{
  "username": "jhon",
  "password": "jhoniscool"
}
```

#### cURL Request

Making the API request via cURL command line tool.

```bash
curl -X 'POST' \
  '{{ site_api }}/{{ path }}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "jhon",
  "password": "jhoniscool"
}'
```

#### Response (200 OK)

```json
{
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
  }
}
```