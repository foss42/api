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
  "data": "uǝǝɹ⅁ sᴉ ssɐɹ⅁"
}
```

In this example, with the input text being equal to `"Grass is Green"` the upside down output is `"uǝǝɹ⅁ sᴉ ssɐɹ⅁"`.
