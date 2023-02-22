---
method: get
title: Number to Social
desc: Converts a number into a human readable form as seen in social media counts (followers, shares, likes).
path: humanize/social
---

This API returns a human readable version of social media numbers like number of followers, shares, likes, etc.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| num | integer | Yes | | Refers to the number of social media numbers which will be turned into a human readable version. Hence should always be >= 0 |
| digits | integer | No | `1` | Specifies the maximum number of digits after the decimal |
| system | string | No | `NA` | Determines when to switch between US abbreviation ("K", "M", "B", "T"), UK abbreviation ("k", "m", "bn", "tn") or Short Scale , SS system ("thousand", "million", "billion", "trillion). See examples for more details. |
| add_space | boolean | No | `false` | Specifies whether space should be added between the number and the unit. See examples for more details |
| trailing_zeros | boolean | No | `false` | Indicates whether all trailing zeros to the right of the decimal point should be removed or not. See examples for more details |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

### 1. Basic Usage

Below is a basic usage of the api with just the `num` param. 

#### Request

```
curl "{{ site_api }}/{{ path }}?num=5567"
```

#### Response

```
{
  "data": "5.6K"
}
```

In the example, `num` is equal to 5567 and the output returned is 5.6K

### 2. Basic with digit

`digits` specify the max. number of digits after the decimal. The default value of digits is `1`. If the digit parameter is set to 2, 2 significant digits after the decimal point is displayed. Let us see that via an example.

#### Request

```
curl "{{ site_api }}/{{ path }}?num=5567&digits=2"
```

#### Response

```
{
  "data": "5.57K"
}
```

Here, as you can see since `digits` is set as `2`, we can see 2 significant digits after the decimal point. Hence, the result returned is 5.57K

### 3. Basic with add space

`add_space` is used to specify whether a space should be added between the number and the unit (1 K or 1K). The default value for add_space is set as `false` which means by default no space is added between the number and the unit. Let us see an example to understand it better.

#### Request

```
curl "{{ site_api }}/{{ path }}?num=5567&add_space=true"
```

#### Response

```
{
  "data": "5.6 K"
}
```

Since `add_space` is set as `true`, you can observe a space between the number 2 and the unit K.

### 4. Basic with system

`system` determines when to switch between US abbreviation ("K", "M", "B", "T"), UK abbreviation ("k", "m", "bn", "tn") or Short Scale , SS system ("thousand", "million", "billion", "trillion) system). By default, the value of `system` is `NA` which stands for North America and returns the US abbreviation. Thus, the permitted values for `system` is `NA`, `UK` and `SS`.  

#### Request

```
curl "{{ site_api }}/{{ path }}?num=5567&system=UK"
```

#### Response

```
{
  "data": "5.6k"
}
```

In the above example, since `system` is set as `UK`, the output returned is 5.6k which is the UK abbreviation.

### 5. Basic with trailing zeros

When `trailing_zeros` is `false`, all trailing zeros to the right of the decimal point are removed. By default, `trailing_zeros` is set as `false`.

#### Request

```
curl "{{ site_api }}/{{ path }}?num=5567&digits=4&trailing_zeros=true"
```

#### Response

```
{
  "data": "5.5670K"
}
```

In the above example, since `trailing_zeros` is set to `true` and `digits` is `4`, we can see 4 digits after the decimal point and a trailing zero as well.

### 6. Complete request

In this example, we will see all the parameters in action

#### Request

```
curl "{{ site_api }}/{{ path }}?num=8700000&digits=3&system=SS&add_space=true&trailing_zeros=true"
```

#### Response

```
{
  "data": "8.700 million"
}
```

Here, in this example, since `digits` is equal to `3` we can see 3 digits after the decimal point. Since `system` is `SS` we can see the short scale system ("thousand", "million", "billion", "trillion). Since, `add_space` is set as `true`, there is a space between 8.700 and million. Also, we can see 2 trailing zeros 8.700 as `trailing_zeros` is set to `true`.

### 7. Basic example 

Even if `num` is greater than trillion, it will be specified in trillions no matter how large the amount. Let us see an example.

#### Request

```
curl "{{ site_api }}/{{ path }}?num=2900000000000000000"
```

#### Response

```
{
  "data": "2900000T"
}
```

Now let us see some examples where we can encounter the **response_code** `422`.

### 8. When num has text value

#### Request

```
curl "{{ site_api }}/{{ path }}?num=foss42"
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

### 9. When num is less than 0

#### Request

```
curl "{{ site_api }}/{{ path }}?num=-31"
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
