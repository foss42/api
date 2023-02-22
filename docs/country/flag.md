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
| `code` | `IN` | `IN` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?code=IN
```

#### cURL Request

Making the API request via cURL command line tool.

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

### Example #2: ISO Alpha-3 code input

Below is an example API usage for the `code` query parameter value provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `code` | `USA` | `USA` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?code=USA
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl -X 'GET' \
  '{{ site_api }}/{{ path }}?code=USA' \
  -H 'accept: application/json'
```

#### Response

```
{
  "data": "🇺🇸"
}
```
