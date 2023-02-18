---
method: get
title: Kebab Case to Lower Case
desc: Converts the provided text in kebab case to lower case.
path: case/kebab2lower
---

This API converts kebab case to lower case.

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
curl "{{ site_api }}/{{ path }}?text=grass-is-green"
```

#### Response

```
{
  "data": "grass is green"
}
```
