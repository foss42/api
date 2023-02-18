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
| num | integer | Yes | | The number provided to be converted into a rank or the exact position in a leaderboard |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Examples

### 1. Basic Usage

Below is a basic usage of the api with just the `num` param. 

#### Request

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

Now let us see some examples where we can encounter the **response_code** `422`.

### 2. When num has text value

#### Request

```
curl "{{ site_api }}/{{ path }}?num=three"
```

#### Response

```
{
  "detail": [
    {
      "loc": [
        "query",
        "num"
      ],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

Response status 422 is returned. For this to work, num must be an integer

### 3. When num is less than 0

#### Request

```
curl "{{ site_api }}/{{ path }}?num=-5"
```

#### Response

```
{
  "detail": [
    {
      "loc": [
        "query",
        "num"
      ],
      "msg": "ensure this value is greater than or equal to 0",
      "type": "value_error.number.not_ge",
      "ctx": {
        "limit_value": 0
      }
    }
  ]
}
```

Response status 422 is returned as num has to be greater than equal to 0 for the api to successfully return a value.
