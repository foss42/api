---
method: get
title: Text to Camel Case
desc: Converts the provided text into camel case.
path: case/camel
---

This API converts the provided text to camel case. Camel case is also known as dromedary case. 

Here, the words are written without any spaces or punctuations with first letter of the every word, excluding the first word being capitalized. 

It is commonly used in Java, JavaScript, and TypeScript for creating variable, function, and method names.

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
  "data": "grassIsGreen"
}
```

As evident in the example above, the camel case version for the input "Grass is Green" is "grassIsGreen". In the output, the spaces are removed and the first letter of every word apart from the first word is capitalized.
