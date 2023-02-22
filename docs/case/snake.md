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
  "data": "grass_is_green"
}
```

As evident in the example above, the snake case version for the input "Grass is Green" is "grass_is_green". All the spaces in the output have been replaced by underscore and the first letter of each word is in lowercase.

### Example #2

Below is another example API usage for the `text` query parameter provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `text` | `GRASS IS GREEN` | `GRASS%20IS%20GREEN` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?text=GRASS%20IS%20GREEN
```

#### cURL Request

Making the API request via cURL command line tool.

```
{{ site_api }}/{{ path }}?text=GRASS%20IS%20GREEN
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?text=GRASS%20IS%20GREEN"
```

#### Response

```
{
  "data": "grass_is_green"
}
```
