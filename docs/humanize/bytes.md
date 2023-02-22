---
method: get
title: Bytes to Human
desc: Converts number of bytes into human readable format.
path: humanize/bytes
---

This API turns number of bytes (like `2345674`) into a human readable format (`2 MB`).

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| num | integer | Yes | | Refers to the number of bytes which will be turned into a human readable format. Hence should always be >= 0 |
| digits | integer | No | `0` | Specifies the maximum number of digits after the decimal |
| prefix | boolean | No | `false` | Indicates whether SI prefixes like kilobytes, megabytes, gigabytes etc. should be used or not. See examples for more details |
| add_space | boolean | No | `true` | Specifies whether space should be added between the number and the unit. See examples for more details |
| trailing_zeros | boolean | No | `false` | Indicates whether all trailing zeros to the right of the decimal point should be removed or not. See examples for more details |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

### 1. Basic Usage

Below is a basic usage of the api with just the num param. 

#### Request

```
curl "{{ site_api }}/{{ path }}?num=2345674"
```

#### Response

```
{
  "data": "2 MB"
}
```

In this example, `num` is equal to 2345674 and the output returned is 2 MB as 2345674/1048576 = 2.

### 2. Basic with digit

`digits` specify the max. number of digits after the decimal. The default value of digits is `0`. If the digit parameter is set to 2, 2 significant digits after the decimal point is displayed. 

Let us see that via an example

#### Request

```
curl "{{ site_api }}/{{ path }}?num=2345674&digits=2"
```

#### Response

```
{
  "data": "2.24 MB"
}
```

Here, as you can see since `digits` is set as `2`, we can see 2 significant digits after the decimal point. 2345674/(1024*1024) = 2.23700 MB which will then be returned as 2.24 MB as only 2 siginificant digits are allowed in this case.

### 3. Basic with add space

`add_space` is used to specify whether a space should be added between the number and the unit (1 MB or 1MB). The default value for `add_space` is set as `true` which means by default a space is added between the number and the unit. Let us see an example to understand it better.

#### Request

```
curl "{{ site_api }}/{{ path }}?num=2345674&add_space=false"
```

#### Response

```
{
  "data": "2MB"
}
```

Since `add_space` is set as `false`, you can observe that there is no space between the number 2 and the unit MB.

### 4. Basic with prefix

`prefix` determines when SI prefixes (kilobytes, megabytes, gigabytes, etc.) are used instead of the symbols. When `prefix` is set as `true` prefixes like kilobytes, megabytes, gigabytes etc. are used. By default, the value of prefix is `false` i.e. symbols (KB, MB etc.) are used by default.

#### Request

```
curl "{{ site_api }}/{{ path }}?num=2345674&prefix=true"
```

#### Response

```
{
  "data": "2 megabytes"
}
```

In the above example, since `prefix` is set as `true`, the output returned is SI prefix megabytes.

### 5. Basic with trailing zeros

When `trailing_zeros` is `false`, all trailing zeros to the right of the decimal point are removed. By default, `trailing_zeros` is set as False.

#### Request

```
curl "{{ site_api }}/{{ path }}?num=2345674&digits=4&trailing_zeros=true"
```

#### Response

```
{
  "data": "2.2370 MB"
}
```

In the above example, since `trailing_zeros` is set to `true` and `digits` is `4` we can see 4 digits after the decimal point and a trailing zero as well.

### 6. Complete request

In this example, we will see all the parameters in action

#### Request

```
curl "{{ site_api }}/{{ path }}?num=2345674&digits=4&prefix=true&add_space=true&trailing_zeros=true"
```

#### Response

```
{
  "data": "2.2370 megabytes"
}
```

Here, in this example, since `digits` is equal to `4` we can see 4 digits after the decimal point. Since `prefix` is `true` we can see megabytes instead of MB symbol. There is no space between the number 2.2370 and the prefix megabytes as `add_space` is set as `false`. Also, we can see a trailing zero 2.2370 as `trailing_zeros` is set to `true`.

Now, let us see some examples where we can encounter the **response_code** `422`.

### 7. When num is a string

#### Request

```
curl "{{ site_api }}/{{ path }}?num=ant"
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

Response status 422 is returned. For the api work, num must be an integer.

### 8. When num is less than 0

#### Request

```
curl "{{ site_api }}/{{ path }}?num=-2"
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
