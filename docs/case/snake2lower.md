---
method: get
title: Snake Case to Lower Case
desc: Converts the provided text in snake case to lower case
path: case/snake2lower
---

This API converts snake case to lower case.

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
curl "http://127.0.0.1:8000/case/snake2lower?text=grass_is_green"
```

#### Response

```
{
  "data": "grass is green"
}
```
