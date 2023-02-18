---
method: get
title: Text to Mirror
desc: Returns the mirror version of a text.
path: convert/mirror
---

This API returns the mirror version of the input text.

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
curl "{{ site_api }}/{{ path }}?text=Grass%20is%20Green"
```

#### Response

```
{
  "data": "nɘɘาᘐ ƨ𝗂 ƨƨ𐑇าᘐ"
}
```

In this example, with the input text being equal to "Grass is Green" the mirror version is "nɘɘาᘐ ƨ𝗂 ƨƨ𐑇าᘐ".
