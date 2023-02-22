---
method: get
title: Country Code to Country Flag
desc: Fetch Emoji Country Flag corresponding to an ISO Alpha-2 or Alpha-3 country code.
path: country/flag
---

This API fetches the emoji country flag corresponding to an ISO Alpha-2 or Alpha-3 country code.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| code | string | Yes | | ISO Alpha-2 or Alpha-3 country code.  |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

Below is an example of the api usage. 

#### Request

```
curl -X 'GET' \
  '{{ site_api }}/{{ path }}?code=IN' \
  -H 'accept: application/json'
```

#### Response

```
{
  "data": "🇮🇳"
}
```
