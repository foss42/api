---
method: get
title: Swap Case of Text
desc: Converts all uppercase characters into lowercase and all lowercase characters into uppercase.
path: case/swap
---

This API converts all the uppercase characters of the input text to lowercase and all the lowercase characters to uppercase. Swap case is also known as toggle case.

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
curl "http://127.0.0.1:8000/case/swap?text=Grass%20is%20Green"
```

#### Response

```
{
  "data": "gRASS IS gREEN"
}
```

You can see that the case of the input text has been toggled, i.e., lowercase characters becomes uppercase and uppercase characters become lowercase.
