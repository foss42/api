---
method: get
title: Number to Rank (Ordinal)
desc: Converts a number into its ordinal form.
path: humanize/rank
---

This API converts a number provided into its ordinal form that indicates the exact position or rank in a leaderboard.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| `num` | `integer` | Yes | | The number provided to be converted into a rank or the exact position in a leaderboard |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

### Example #1

Below is an example API usage for the `num` query parameter provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `3` | `3` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=3
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?num=3"
```

#### Response

```
{
  "data": "3rd"
}
```

In the example, num is equal to `3` and the output returned is `3rd`.
