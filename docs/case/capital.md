---
method: get
title: Text to Capital Case
desc: Converts the provided text into capital case.
path: case/capital
---

This API converts the input text to capital case, wherein for each word in the string the first character is uppercased and the remaining characters are lowercased.

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
| `text` | `grass is green` | `grass%20is%20green` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?text=grass%20is%20green
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?text=grass%20is%20green"
```

#### Response

```
{
  "data": "Grass Is Green"
}
```

In the output, the first character for each word of the input `text` has been uppercased whereas the remaining characters are in lowercase .

### Example #2

Below is another example API usage for the `text` query parameter provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `text` | `from the highest heights to the lowest depths, in photographs` | `from%20the%20highest%20heights%20to%20the%20lowest%20depths,%20in%20photographs` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?text=from%20the%20highest%20heights%20to%20the%20lowest%20depths,%20in%20photographs
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?text=from%20the%20highest%20heights%20to%20the%20lowest%20depths,%20in%20photographs"
```

#### Response

```
{
  "data": "From The Highest Heights To The Lowest Depths, In Photographs"
}
```

### Example #3

Below is another example API usage for the `text` query parameter provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `text` | `'Ford v Ferrari' finishes first at the box office` | `%27Ford%20v%20Ferrari%27%20finishes%20first%20at%20the%20box%20office` | 

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?text=%27Ford%20v%20Ferrari%27%20finishes%20first%20at%20the%20box%20office
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?text=%27Ford%20v%20Ferrari%27%20finishes%20first%20at%20the%20box%20office"

```

#### Response

```
{
  "data": "'Ford V Ferrari' Finishes First At The Box Office"
}
```
