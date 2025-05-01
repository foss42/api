---
method: post
title: User Logout
desc: Invalidates the user's current session/token.
path: auth/logout
---

This API endpoint logs out the currently authenticated user, typically by invalidating their access token on the server-side.

## Request Headers

| Header          | Required | Description                                      |
| :-------------- | :------- | :----------------------------------------------- |
| `Authorization` | Yes      | Bearer token for authentication (e.g., `Bearer <access_token>`) |

## Request Body

No request body is required.

## HTTP Response Codes

| Status Code | Description                                  |
| :---------- | :------------------------------------------- |
| 200         | Successful Logout                            |
| 401         | Unauthorized (Invalid or missing token)      |
| 500         | Internal Server Error (Logout failed)        |

## Sample Usage

### Example #1: Successful Logout

#### API Request

```http
POST {{ site_api }}/{{ path }}
Authorization: Bearer <your_access_token>
```

#### cURL Request

```bash
curl -X 'POST' \
  '{{ site_api }}/{{ path }}' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <your_access_token>'
```

#### Response (200 OK)

```json
{
  "data": "Successfully logged out"
}
```

### Example #2: Unauthorized

#### API Request

```http
POST {{ site_api }}/{{ path }}
```

#### cURL Request

```bash
curl -X 'POST' \
  '{{ site_api }}/{{ path }}' \
  -H 'accept: application/json'
```

#### Response (401 Unauthorized)

```json
{
  "detail": "Not authenticated"
}
```