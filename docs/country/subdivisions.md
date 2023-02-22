---
method: get
title: Get Country Subdivisions (states, territories, etc.) from Country Code
desc: Fetches the country subdivision details (states, territories, etc.) for an Alpha-3 or Alpha-2 country code.
path: country/subdivisions
---

This API fetches the country subdivision details (states, territories, etc.) for the given two letter (Alpha-2) or three letter (Alpha-3) ISO 3166-1 country code. 

Currently, the following countries are supported:

| Country | ISO Alpha-2 Code | ISO Alpha-3 Code|
| ----------- | ----------- | -----------  |
| Australia | `AU` | `AUS` |
| Canada | `CA` | `CAN` |
| China | `CN` | `CHN` |
| India | `IN` | `IND` |
| Japan | `JP` | `JPN` |
| South Korea | `KR` | `KOR` |
| United States of America | `US` | `USA` |

**To add support for a new country please raise an issue in the project repository.**

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| `code` | `string` | Yes | | ISO Alpha-2 or Alpha-3 country code.  |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

### Example #1: ISO Alpha-2 code input

Below is an example API usage for the `code` query parameter value provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `code` | `AU` | `AU` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?code=AU
```

#### cURL Request

Making the API request via cURL command line tool.

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

### Example #2: ISO Alpha-3 code input

Below is an example API usage for the `code` query parameter value provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `code` | `KOR` | `KOR` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?code=KOR
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl -X 'GET' \
  '{{ site_api }}/{{ path }}?code=KOR' \
  -H 'accept: application/json'
```

#### Response

```
{
  "data": [
    {
      "code": "26",
      "name": "Busan",
      "category": "metropolitan city"
    },
    {
      "code": "27",
      "name": "Daegu",
      "category": "metropolitan city"
    },
    {
      "code": "30",
      "name": "Daejeon",
      "category": "metropolitan city"
    },
    {
      "code": "29",
      "name": "Gwangju",
      "category": "metropolitan city"
    },
    {
      "code": "28",
      "name": "Incheon",
      "category": "metropolitan city"
    },
    {
      "code": "31",
      "name": "Ulsan",
      "category": "metropolitan city"
    },
    {
      "code": "43",
      "name": "Chungbuk",
      "category": "province"
    },
    {
      "code": "44",
      "name": "Chungnam",
      "category": "province"
    },
    {
      "code": "42",
      "name": "Gangwon",
      "category": "province"
    },
    {
      "code": "41",
      "name": "Gyeonggi",
      "category": "province"
    },
    {
      "code": "47",
      "name": "Gyeongbuk",
      "category": "province"
    },
    {
      "code": "48",
      "name": "Gyeongnam",
      "category": "province"
    },
    {
      "code": "45",
      "name": "Jeonbuk",
      "category": "province"
    },
    {
      "code": "46",
      "name": "Jeonnam",
      "category": "province"
    },
    {
      "code": "11",
      "name": "Seoul",
      "category": "special city"
    },
    {
      "code": "50",
      "name": "Sejong",
      "category": "special self-governing city"
    },
    {
      "code": "49",
      "name": "Jeju",
      "category": "special self-governing province"
    }
  ]
}
```
