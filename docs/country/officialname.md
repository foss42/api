---
method: get
title: Country Code to Official Name
desc: Fetches the official (ISO) country name for an Alpha-3 or Alpha-2 country code.
path: country/officialname
---

This API fetches the official (ISO) country name for an Alpha-3 or Alpha-2 country code.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| code | string | Yes | | ISO Alpha-2 or Alpha-3 country code.  |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Example

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
  "data": "Viet Nam"
}
```
