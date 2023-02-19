---
method: get
title: Get Country Subdivisions (states, territories, etc.) from Country Code
desc: Fetches the country subdivision details (states, territories, etc.) for an Alpha-3 or Alpha-2 country code.
path: country/subdivisions
---

This API fetches the country subdivision details (states, territories, etc.) for the given two letter (Alpha-2) or three letter (Alpha-3) ISO 3166-1 country code. 

Currently, the following countries are supported:
- `AU` (Australia)
- `US` (USA)
- `CN` (China)
- `JP` (Japan)
- `IN` (India)
- `KR` (South Korea) 
- `CA` (Canada)

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
  '{{ site_api }}/{{ path }}?code=AU' \
  -H 'accept: application/json'
```

#### Response

```
{
  "data": [
    {
      "code": "ACT",
      "name": "Australian Capital Territory",
      "category": "territory"
    },
    {
      "code": "NSW",
      "name": "New South Wales",
      "category": "state"
    },
    {
      "code": "NT",
      "name": "Northern Territory",
      "category": "territory"
    },
    {
      "code": "QLD",
      "name": "Queensland",
      "category": "state"
    },
    {
      "code": "SA",
      "name": "South Australia",
      "category": "state"
    },
    {
      "code": "TAS",
      "name": "Tasmania",
      "category": "state"
    },
    {
      "code": "VIC",
      "name": "Victoria",
      "category": "state"
    },
    {
      "code": "WA",
      "name": "Western Australia",
      "category": "state"
    }
  ]
}
```
