---
method: get
title: Text to Train Case
desc: Converts the provided text into train case.
path: case/train
---

This API converts the input text to train case where the first letter of each word is capitalized. Train Case is also known as HTTP Header Case.

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
curl "http://127.0.0.1:8000/case/train?text=Grass%20is%20Green"
```

#### Response

```
{
  "data": "Grass-Is-Green"
}
```
