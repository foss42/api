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
curl "{{ site_api }}/{{ path }}?text=grass%20is%20greener"
```

#### Response

```
{
  "data": "Grass Is Greener"
}
```

In the output, the first character for each word of the input `text` has been uppercased whereas the remaining characters are in lowercase .

### 2. Basic Usage

Below is another example of the api usage with the text param. 

#### Request

```
curl "{{ site_api }}/{{ path }}?text=from%20the%20highest%20heights%20to%20the%20lowest%20depths,%20in%20photographs"
```

#### Response

```
{
  "data": "From The Highest Heights To The Lowest Depths, In Photographs"
}
```

### 3. Basic Usage

Below is another example of the api usage with the text param. 

#### Request

```
curl "{{ site_api }}/{{ path }}?text=Ford%20v%20Ferrari%27%20finishes%20first%20at%20the%20box%20office"

```

#### Response

```
{
  "data": "Ford V Ferrari' Finishes First At The Box Office"
}
```
