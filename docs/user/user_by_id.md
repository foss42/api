---
method: get
title: Get User by ID
desc: Retrieves the details of a specific user by their ID.
path: /users/{user_id}
---

This API endpoint returns the details for a specific user identified by their unique `user_id`.

## Path Parameters

| Parameter | Data Type | Required | Description        |
| :-------- | :-------- | :------- | :----------------- |
| `user_id` | `integer` | Yes      | The ID of the user to retrieve |

## HTTP Response Codes

| Status Code | Description                               |
| :---------- | :---------------------------------------- |
| 200         | Successful Response                       |
| 404         | User Not Found                            |
| 422         | Validation Error (e.g., non-integer ID)   |
| 500         | Internal Server Error (Could not fetch user) |

## Sample Usage

### Example #1: Get User with ID 2

#### API Request

```http
GET {{ site_api }}/user/users/2
```

#### cURL Request

```bash
curl -X 'GET' \
  '{{ site_api }}/user/users/2' \
  -H 'accept: application/json'
```

#### Response (200 OK)

*(Note: The actual response depends on the user data structure)*

```json
{
    "id": "1",
    "name": "Travis Barber",
	"phone": "1-288-119-0313",
	"email": "travisbarber@apidash.in",
	"country": "United States"
}
```

### Example #2: User Not Found (ID 99)

#### API Request

```http
GET {{ site_api }}/user/users/99
```

#### cURL Request

```bash
curl -X 'GET' \
  '{{ site_api }}/user/users/99' \
  -H 'accept: application/json'
```

#### Response (404 Not Found)

```json
{
  "detail": "User with ID 99 not found"
}
```