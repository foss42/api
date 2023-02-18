---
method: get
title: Text to 1337 (leet)
desc: Returns the 1337 version of a text.
path: convert/leet
---

This API returns the 1337 version of the text. The 1337 version or Leet is a system of modified spellings used primarily by Internet users. It replaces characters with numbers or symbols and uses character replacements in ways that play on the similarity of their glyphs either via reflection or some other resemblance.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| text | string | Yes | | The input text  |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Examples

### 1. Basic Usage

Below is an example of the api usage with the text param. 

#### Request

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
