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
| `code` | `VN` | `VN` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?code=VN
```

#### cURL Request

Making the API request via cURL command line tool.

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

### Example #2: ISO Alpha-3 code input

Below is an example API usage for the `code` query parameter value provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `code` | `CIV` | `CIV` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?code=CIV
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl -X 'GET' \
  '{{ site_api }}/{{ path }}?code=CIV' \
  -H 'accept: application/json'
```

#### Response

```
{
  "data": "Ivory Coast"
}
```
