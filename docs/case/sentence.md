---
method: get
title: Text to Sentence Case
desc: Converts the provided text into sentence case.
path: case/sentence
---

This API converts the input text into sentence case wherein the first character is capitalized and rest all characters are lowercased. It doesn't capitalize names or places.

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
curl "{{ site_api }}/{{ path }}?text=grass%20is%20green"
```

#### Response

```
{
  "data": "Grass is green"
}
```

### 2. Basic Usage

Below is another example of the api usage with the text param. 

#### Request

```
curl "{{ site_api }}/{{ path }}?text=grass%20is%20greener%20in%20California%20with%20Tim"
```

#### Response

```
{
  "data": "Grass is greener in california with tim"
}
```
