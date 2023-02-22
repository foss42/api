---
method: get
title: Text to Kebab Case
desc: Converts the provided text into kebab case.
path: case/kebab
---

This API converts the input text to kebab case. Kebab case is also known as skewer case, spinal case, param case, dash case or LISP case.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| text | string | Yes | | The input text  |


**HTTP Response Codes**

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

### 1. Basic Usage

Below is an example of the api usage with the text param. 

### Request

```
curl "{{ site_api }}/{{ path }}?text=Grass%20is%20Green"
```

### Response

```
{
  "data": "grass-is-green"
}
```
