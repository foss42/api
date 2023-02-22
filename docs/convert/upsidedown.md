---
method: get
title: Text to Upside Down
desc: Convert a text into its upside down version like Stranger Things.
path: convert/upsidedown
---

This API returns the upside down version of the input text.

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
  "data": "uǝǝɹ⅁ sᴉ ssɐɹ⅁"
}
```

In this example, with the input text being equal to "Grass is Green" the upside down output is "uǝǝɹ⅁ sᴉ ssɐɹ⅁".
