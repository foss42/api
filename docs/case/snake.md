---
method: get
title: Text to Snake Case
desc: Converts the provided text into snake case.
path: case/snake
---

This API converts the input text to snake case. Snake Case is also known as pothole case. In snake case, each space is replaced by an `_` underscore character and all letters are in lowercase. Snake case is often used for creating variable and method names and is also a good choice for naming files, as it makes filenames readable.

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
curl "http://127.0.0.1:8000/case/snake?text=Grass%20is%20Green"
```

#### Response

```
{
  "data": "grass_is_green"
}
```

As evident in the example above, the snake case version for the input "Grass is Green" is "grass_is_green". All the spaces in the output have been replaced by underscore and the first letter of each word is in lowercase.

### 2. Basic Usage

Below is another example of the api usage with the text param. 

#### Request

```
curl "http://127.0.0.1:8000/case/snake?text=GRASS%20IS%20GREEN"
```

#### Response

```
{
  "data": "grass_is_green"
}
```
