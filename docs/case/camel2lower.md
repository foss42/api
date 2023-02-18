---
method: get
title: Camel Case to Lower Case
desc: Converts the provided text in camel case to lower case.
path: case/camel2lower
---

This API converts camel case to lower case.

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
curl "{{ site_api }}/{{ path }}?text=grassIsGreen"
```

#### Response

```
{
  "data": "grass is green"
}
```
