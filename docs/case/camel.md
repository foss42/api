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
| `text` | `string` | Yes | | The input text  |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

### Example #1

Below is an example API usage for the `text` query parameter provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `text` | `Grass is Green` | `Grass%20is%20Green` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?text=Grass%20is%20Green
```

#### cURL Request

Making the API request via cURL command line tool.

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
