---
method: get
title: Text to Upper Case
desc: Converts the provided text into upper case.
path: case/upper
---

This API converts all cased characters of the input text to upper case.

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
curl "http://127.0.0.1:8000/case/upper?text=Grass%20is%20Green"
```

#### Response

```
{
  "data": "GRASS IS GREEN"
}
```

In this example, all the characters of the input text have been converted into upper case characters.
