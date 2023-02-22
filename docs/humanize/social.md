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
| `num` | `integer` | Yes | | Refers to the number of social media numbers which will be turned into a human readable version. Hence should always be >= 0 |
| `digits` | `integer` | No | `1` | Specifies the maximum number of digits after the decimal |
| `system` | `string` | No | `NA` | Determines when to switch between `NA` (US) abbreviation ("K", "M", "B", "T"), `UK` abbreviation ("k", "m", "bn", "tn") or Short Scale , `SS` system ("thousand", "million", "billion", "trillion). See examples for more details. |
| `add_space` | `boolean` | No | `false` | Specifies whether space should be added between the number and the unit. See examples for more details |
| `trailing_zeros` | `boolean` | No | `false` | Indicates whether all trailing zeros to the right of the decimal point should be removed or not. See examples for more details |

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
| `num` | `5567` | `5567` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=5567
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?num=5567"
```

#### Response

```
{
  "data": "5.6K"
}
```

In the example, `num` is equal to `5567` and the output returned is `5.6K`.

### Example #2: Specifying max. no. of digits after decimal

Below is an example API usage for the `num` query parameter along with the `digits` parameter that specifies the max. number of digits after the decimal. The default value of digits is `1`. If the digit parameter is set to `2`, 2 significant digits after the decimal point is displayed. Let us see that via an example.

All parameter values are provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `5567` | `5567` |
| `digits` | `2` | `2` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=5567&digits=2
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?num=5567&digits=2"
```

#### Response

```
{
  "data": "5.57K"
}
```

Here, as you can see since `digits` is set as `2`, we can see 2 significant digits after the decimal point. Hence, the result returned is `5.57K`.

### Example #3: Adding space between the value and unit

Below is an example API usage for the `num` query parameter along with the `add_space` parameter that specifies whether a space should be added between the number and the unit (1 K or 1K). The default value for `add_space` is set as `false` which means by default no space is added between the number and the unit. Let us see an example to understand it better.

All parameter values are provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `5567` | `5567` |
| `add_space` | `true` | `true` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=5567&add_space=true
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?num=5567&add_space=true"
```

#### Response

```
{
  "data": "5.6 K"
}
```

Since `add_space` is set as `true`, you can observe a space between the number `5.6` and the unit `K`.

### Example #4: Using a different unit abbreviation system

Below is an example API usage for the `num` query parameter along with the `system` parameter that determines when to switch between the different system as shown in the table below.

| Permitted Value of `system` | System | Returns Unit|
| ----------- | ----------- | -----------  |
| `NA` | North American or US (Default) | `K`, `M`, `B`, `T` |
| `UK` | United Kingdom or British | `k`, `k`, `bn`, `tn` |
| `SS` | Short Scale | `thousand`, `million`, `billion`, `trillion` |

Let us see an example to understand it better. All parameter values are provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `5567` | `5567` |
| `system` | `UK` | `UK` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=5567&system=UK
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?num=5567&system=UK"
```

#### Response

```
{
  "data": "5.6k"
}
```

In the above example, since `system` is set as `UK`, the output returned is `5.6k` which is as per the UK abbreviation system.

### Example #5: Trailing zeros

Below is an example API usage for the `num` query parameter along with `digits` and `trailing_zeros` parameters. If `trailing_zeros` is set as `true`, the trailing zeros to the right of the decimal point are retained. By default, `trailing_zeros` is set as `false`.

Let us see an example to understand it better. All parameter values are provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `5567` | `5567` |
| `digits` | `4` | `4` |
| `trailing_zeros` | `true` | `true` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=5567&digits=4&trailing_zeros=true
```

#### cURL Request

Making the API request via cURL command line tool.

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

### Example #6: Various Parameters

In this example, we will see all the parameters in action.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `8700000` | `8700000` |
| `digits` | `3` | `3` |
| `system` | `SS` | `SS` |
| `add_space` | `true` | `true` |
| `trailing_zeros` | `true` | `true` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=8700000&digits=3&system=SS&add_space=true&trailing_zeros=true
```

#### cURL Request

Making the API request via cURL command line tool.

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

### Example #7: num is greater than trillion 

If `num` is greater than trillion, the result will be specified in trillions no matter how large the amount. Let us see an example.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `num` | `2900000000000000000` | `2900000000000000000` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?num=2900000000000000000
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?num=2900000000000000000"
```

#### Response

```
{
  "data": "2900000T"
}
```
