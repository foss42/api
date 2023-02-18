---
method: get
title: Text to Title Case
desc: Converts the provided text into title case.
path: case/title
---

This API converts the input text to title case, also known as headline case. It formats text with a proper title case for article/publication headlines. 

The rules are based on style guides from APA, The Chicago Manual of Style, and other modern conventions.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| text | string | Yes | | The input text  |


**HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |



## Examples

### 1. Basic Usage

Below is an example of the api usage with the text param. 

#### Request

```
curl "http://127.0.0.1:8000/case/title?text=grass%20is%20green"
```

#### Response

```
{
  "data": "Grass Is Green"
}
```

### 2. Basic Usage

Below is another example of the api usage with the text param. 

#### Request

```
curl "http://127.0.0.1:8000/case/title?text=from%20the%20highest%20heights%20to%20the%20lowest%20depths,%20in%20photographs"
```

#### Response

```
{
  "data": "From the Highest Heights to the Lowest Depths, in Photographs"
}
```

### 3. Basic Usage

Below is another example of the api usage with the text param. 

#### Request

```
curl "http://127.0.0.1:8000/case/title?text=Ford%20vs.%20Ferrari%27%20finishes%20first%20at%20the%20box%20office"
```

#### Response

```
{
  "data": "Ford vs. Ferrari' Finishes First at the Box Office"
}
```
