---
method: get
title: Country Code to Popular Name
desc: Fetches the name by which a country is popularly know as, for the given Alpha-3 or Alpha-2 country code.
path: country/name
---

This API fetches the name by which a country is popularly know as, for the given Alpha-3 or Alpha-2 country code.

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
  '{{ site_api }}/{{ path }}?code=VN' \
  -H 'accept: application/json'
```

#### Response

```
{
  "data": "Vietnam"
}
```
