---
method: get
title: Get User Profile
desc: Retrieves the profile information of the currently authenticated user.
path: /profile
---

This API endpoint returns a profile details of a user.

## Request Headers

| Header          | Required | Description                                      |
| :-------------- | :------- | :----------------------------------------------- |
| `Authorization` | Yes      | Bearer token for authentication (e.g., `Bearer <access_token>`) |

## HTTP Response Codes

| Status Code | Description                                  |
| :---------- | :------------------------------------------- |
| 200         | Successful Response                          |
| 401         | Unauthorized (Invalid or missing token)      |
| 500         | Internal Server Error (Could not fetch profile) |

## Sample Usage

### Example #1: Get Profile

#### API Request

```http
GET {{ site_api }}/{{ path }}
Authorization: Bearer <your_access_token>
```

#### cURL Request

```bash
curl -X 'GET' \
  '{{ site_api }}/{{ path }}' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <your_access_token>'
```

#### Response (200 OK)


```json
{
    "id": "1",
    "name": "Travis Barber",
	"phone": "1-288-119-0313",
	"email": "travisbarber@apidash.in",
	"country": "United States"
}
```

### Example #2: Unauthorized

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

#### Response (401 Unauthorized)

```json
{
  "detail": "Not authenticated"
}
```