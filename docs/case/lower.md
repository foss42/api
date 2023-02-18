---
method: get
title: Text to Lower Case
desc: Converts the provided text into lower case.
path: case/lower
---

This API converts all cased characters of the input text to lower case.

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
  "data": "grass is green"
}
```

In this example, all the characters of the input `text` have been converted into lower case characters.
