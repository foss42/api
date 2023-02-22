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
| `num` | `integer` | Yes | | Refers to the number of bytes which will be turned into a human readable format. Hence should always be >= 0 |
| `digits` | `integer` | No | `0` | Specifies the maximum number of digits after the decimal |
| `prefix` | `boolean` | No | `false` | Indicates whether SI prefixes like kilobytes, megabytes, gigabytes, etc. should be used or not. See examples for more details |
| `add_space` | `boolean` | No | `true` | Specifies whether space should be added between the number and the unit. See examples for more details |
| `trailing_zeros` | `boolean` | No | `false` | Indicates whether all trailing zeros to the right of the decimal point should be removed or not. See examples for more details |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

### Example #1

Below is an example API usage with just the `num` query parameter provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `2345674` | `2345674` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=2345674
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?num=2345674"
```

#### Response

```
{
  "data": "2 MB"
}
```

In this example, `num` is equal to 2345674 and the output returned is `2 MB` as 2345674/1048576 = 2.

### Example #2: Max. no. of digits

Below is an example API usage with the `num` query parameter along with `digits` to specify the max. number of digits after the decimal. The default value of `digits` is `0`. If the digit parameter is set to `2`, `2` significant digits after the decimal point is displayed. 

The query parameter values are provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `2345674` | `2345674` |
| `digits` | `2` | `2` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=2345674&digits=2
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?num=2345674&digits=2"
```

#### Response

```
{
  "data": "2.24 MB"
}
```

Here, as you can see since `digits` is set as `2`, we can see 2 significant digits after the decimal point. 2345674/(1024*1024) = 2.23700 MB which will then be returned as `2.24 MB` as only 2 significant digits are allowed in this case.

### Example #3: Adding space in between the value and units

Below is an example API usage with the `num` query parameter along with `add_space` to specify whether a space should be added between the value and the unit (`1 MB` or `1MB`). The default value for `add_space` is set as `true` which means by default a space is added between the number and the unit.

The query parameter values are provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `2345674` | `2345674` |
| `add_space` | `false` | `false` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=2345674&add_space=false
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?num=2345674&add_space=false"
```

#### Response

```
{
  "data": "2MB"
}
```

Since `add_space` is set as `false`, you can observe that there is no space between the number `2` and the unit `MB`.

### Example #4: With full SI prefix

Below is an example API usage with the `num` query parameter along with `prefix` that determines when SI prefixes (kilobytes, megabytes, gigabytes, etc.) are used instead of the symbols for the units. When `prefix` is set as `true` SI prefixes like kilobytes, megabytes, gigabytes etc. are used. By default, the value of prefix is `false` i.e. symbols (KB, MB etc.) are used.

The query parameter values are provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `2345674` | `2345674` |
| `prefix` | `true` | `true` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=2345674&prefix=true
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?num=2345674&prefix=true"
```

#### Response

```
{
  "data": "2 megabytes"
}
```

In the above example, since `prefix` is set as `true`, the output returned is `megabytes` instead of `MB`.

### Example #5: With digits and trailing zeros

Below is an example API usage with the `num` query parameter along with `digits` and `trailing_zeros` query parameters. If `trailing_zeros` is specified as `false`, all trailing zeros to the right of the decimal point are removed. In case, it is `true`, any trailing zeros is not removed. By default, `trailing_zeros` is set as `false`.

The query parameter values are provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `2345674` | `2345674` |
| `digits` | `4` | `4` |
| `trailing_zeros` | `true` | `true` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=2345674&digits=4&trailing_zeros=true
```

#### cURL Request

Making the API request via cURL command line tool.

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

### Example #6: With various parameters

In this example, we will see all the parameters in action. The values of all parameters are specified in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `2345674` | `2345674` |
| `digits` | `4` | `4` |
| `prefix` | `true` | `true` |
| `add_space` | `true` | `true` |
| `trailing_zeros` | `true` | `true` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=2345674&digits=4&prefix=true&add_space=true&trailing_zeros=true
```

#### cURL Request

Making the API request via cURL command line tool.

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
