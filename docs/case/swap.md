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
  "data": "gRASS IS gREEN"
}
```

You can see that the case of the input text has been toggled, i.e., lowercase characters becomes uppercase and uppercase characters become lowercase.
