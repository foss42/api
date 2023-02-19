---
method: get
title: Country Code to World Bank Data
desc: Fetch some world bank data of a country provided its ISO Alpha-2 or Alpha-3 country code.
path: country/data
---

This API fetches some world bank data of a country provided its ISO Alpha-2 or Alpha-3 country code.

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
  '{{ site_api }}/{{ path }}?code=US' \
  -H 'accept: application/json'
```

#### Response

```
{
  "data": {
    "area": 9831510,
    "population": 331893745
  }
}
```
