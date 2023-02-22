---
method: get
title: Text to Pascal Case
desc: Converts the provided text into pascal case.
path: case/pascal
---

This API converts the input text to pascal case. Pascal case is also known as upper camel case or studly case. 

Pascal Case is a naming convention wherein the first letter of each word in a variable is capitalized. Pascal Case is used for naming classes in most programming languages. It is similar to Camel Case except the fact that the first letter of the first word is also capitalized.

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
  "data": "GrassIsGreen"
}
```

As evident in the example above, the pascal case version for the input "Grass is Green" is "GrassIsGreen". The spaces are removed and the first letter of every word is capitalized.
