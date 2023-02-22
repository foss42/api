---
method: get
title: Text to 1337 (leet)
desc: Returns the 1337 version of a text.
path: convert/leet
---

This API returns the Leet (1337) version of the text. Leet is a system of modified spellings used primarily by Internet users to get around keyword bans in forums. It replaces characters with numbers or symbols and uses character replacements in ways that play on the similarity of their glyphs either via reflection or some other resemblance.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| `text` | `string` | Yes | | The input text  |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### Example #1

Below is an example API usage for the `text` query parameter provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `text` | `universe` | `universe` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?text=universe
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?text=universe"
```

#### Response

```
{
  "data": "บи!V3®$3"
}
```

In this example, the input text supplied to the API was "universe" and the result returned is "บи!V3®$3".
