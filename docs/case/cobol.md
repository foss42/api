---
method: get
title: Text to Cobol Case
desc: Converts the provided text into cobol case.
path: case/cobol
---

This API converts the input text to cobol case where every word is capitalised. Cobol case is also known as upper train case or screaming kebab case.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| text | string | Yes | | The input text  |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

### 1. Basic Usage

Below is an example of the api usage with the text param. 

#### Request

```
curl "{{ site_api }}/{{ path }}?text=Grass%20is%20Green"
```

#### Response

```
{
  "data": "GRASS-IS-GREEN"
}
```
