---
method: get
title: Phone to Numeric
desc: Converts a phone number with letters into its numeric equivalent.
path: convert/phone2numeric
---

This API converts a phone number with letters into its numeric equivalent.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| text | string | Yes | | The text supplied to be converted into a numeric phone number |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Examples

### 1. Basic Usage
Below is a basic usage of the api with just the text param. 

#### Request

```
curl "{{ site_api }}/{{ path }}?text=1-800-GOT-JUNK"
```

#### Response

```
{
  "data": "1-800-468-5865"
}
```

In this example, input `text` is "1-800-GOT-JUNK". The result returned is the numeric version of this phone number which is "1-800-468-5865".
