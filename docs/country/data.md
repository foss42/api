---
method: get
title: Country Code to World Bank Data
desc: Fetch some world bank data of a country provided its ISO Alpha-2 or Alpha-3 country code.
path: country/data
---

This API fetches some world bank data of a country given by its ISO Alpha-2 or Alpha-3 country code.

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
| `code` | `US` | `US` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?code=US
```

#### cURL Request

Making the API request via cURL command line tool.

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

### Example #2: ISO Alpha-3 code input

Below is an example API usage for the `code` query parameter value provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `code` | `IND` | `IND` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?code=IND
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl -X 'GET' \
  '{{ site_api }}/{{ path }}?code=IND' \
  -H 'accept: application/json'
```

#### Response

```
{
  "data": {
    "area": 3287260.0,
    "population": 1407563842
  }
}
```
