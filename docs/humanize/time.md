---
method: get
title: Time Difference to Human
desc: Convert time difference into a human readable form (for social media, chat apps).
path: humanize/time
---

This API returns a time difference in human readable version as typically displayed in social media apps like `2 minutes ago`, `3 days ago`, etc.

The input date can be of [ISO 8601 format](https://www.w3.org/TR/NOTE-datetime) or a custom format. The valid forms of ISO 8601 date-time formats are provided in the table below:

| Format | Description | Example |
| ----------- | ----------- | --------- |
| `YYYY` | Year | `1997` |
| `YYYY-MM` | Year and month | `1997-07` |
| `YYYY-MM-DD` | Complete date | `1997-07-16` |
| `YYYY-MM-DDThh:mm` | Complete date plus hours and minutes (UTC) | `1997-07-16T19:20` |
| `YYYY-MM-DDThh:mm:ss` | Complete date plus hours, minutes and seconds (UTC) | `1997-07-16T19:20:30` |
| `YYYY-MM-DDThh:mm:ss.s` | Complete date plus hours, minutes, seconds and a decimal fraction of a second (UTC) | `1997-07-16T19:20:30.45` |
| `YYYY-MM-DDThh:mmTZD` | Complete date plus hours and minutes (with Time-zone) | `1997-07-16T19:20+01:00` |
| `YYYY-MM-DDThh:mm:ssTZD` | Complete date plus hours, minutes and seconds (with Time-zone) | `1997-07-16T19:20:30+01:00` |
| `YYYY-MM-DDThh:mm:ss.sTZD` | Complete date plus hours, minutes, seconds and a decimal fraction of a second (with Time-zone) | `1997-07-16T19:20:30.45+01:00` |

where:

| Symbol | Description |
| ----------- | ----------- |
| `YYYY` | Four-digit year |
| `MM` | Two-digit month (`01` = January, etc.) |
| `DD` | Two-digit day of month (`01` through `31`) |
| `hh` | Two digits of hour (`00` through `23`) (am/pm NOT allowed) |
| `mm` | Two digits of minute (`00` through `59`) |
| `ss` | Two digits of second (`00` through `59`) |
| `s` | One or more digits representing a decimal fraction of a second |
| `TZD` | Time zone designator (`Z` for UTC or `+hh:mm` or `-hh:mm`). If TZD is missing it is considered UTC timezone. |

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| `dt` | `string` | Yes | | The input date-time string. It should be a valid ISO 8601 format as shown above. If it is a custom date-time format, then `fmt` parameter is required. |
| `dt_ref` | `string` | No | | Used to supply a reference timestamp from which the difference is calculated. If not provided, the current system timestamp is used. |
| `fmt` | `string` | No | | Used to provide the format of the timestamp if `dt` is not provided in a valid ISO 8601 format. (See example for more details) |
| `units` | `string` | No | `FULL` | Used to specify whether the units of the output time difference is full (like minutes) or short (like m). Can be `SHORT` or `FULL`. (See example for more details) |
| `cutoff_now` | `integer` | No | `1` | Is the number of seconds of time difference for which `"now"` is returned instead of the actual time difference. Default is set as `1` which means that any time difference less than a second is returned as `"now"` instead of the time difference in milliseconds |
| `add_adverb` | `boolean` | No | `false` | Adds `"ago"` or `"from now"` based on the time difference. (See example for more details) |
| `use_article` | `boolean` | No | `false` | Specifies when to use articles `"a"` and `"an"` instead of `"1"`. (See example for more details) |
| `round_down` | `boolean` | No | `true` | Rounds the time difference to the largest unit quantity that is less than or equal to it. |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

### Example #1

Below is an example API usage with just the `dt` query parameter whose value is as provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `2023-02-09T21:27:15` | `2023-02-09T21:27:15` |

As `dt_ref` is not provided the current system timestamp is used for calculating the difference which is `2023-02-23T06:51:46` (in UTC)

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=2023-02-09T21:27:15
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-09T21:27:15"
```

#### Response

```
{
  "data": "1 week"
}
```

In this example, the actual difference between `dt` and the current system timestamp is 13 days, 9 hours, 24 minutes, and 31 seconds. By default, the time difference is rounded down to the largest unit quantity that is less than or equal to it, i.e., 1 week as the difference is less than 2 weeks. This behaviour can be changed by providing the `round_down` query parameter (Example #10).

### Example #2: With dt_ref same as dt

Below is an example API usage with the `dt` query parameter along with `dt_ref`, the reference timestamp from which the difference is calculated.
The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `2023-02-08T21:27:15` | `2023-02-08T21:27:15` |
| `dt_ref` | `2023-02-08T21:27:15` | `2023-02-08T21:27:15` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T21:27:15
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T21:27:15"
```

#### Response

```
{
  "data": "now"
}
```

As `dt` is equal to `dt_ref`, `"now"` is returned.

### Example #3: With dt_ref different from dt

Below is an example API usage with the `dt` query parameter along with `dt_ref`, the reference timestamp from which the difference is calculated.
The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `2023-02-08T21:27:15` | `2023-02-08T21:27:15` |
| `dt_ref` | `2023-02-08T21:22:15` | `2023-02-08T21:22:15` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T21:22:15
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T21:22:15"
```

#### Response

```
{
  "data": "5 minutes"
}
```

Here, the time difference between `dt` and `dt_ref` is returned.

### Example #4: With past or future indicators (adverbs)

`add_adverb` adds `ago` or `from now` to the time difference between `dt` and `dt_ref`. If `dt` is ahead in time compared to `dt_ref`, `from now` is added, else `ago` is used. 

The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `2023-02-08T21:27:15` | `2023-02-08T21:27:15` |
| `dt_ref` | `2023-02-08T21:22:15` | `2023-02-08T21:22:15` |
| `add_adverb` | `true` | `true` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T21:22:15&add_adverb=true
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T21:22:15&add_adverb=true"
```

#### Response

```
{
  "data": "5 minutes from now"
}
```

In the above example, since `dt` is 5 minutes ahead of `dt_ref`, the result returned is `5 minutes from now`.

### Example #5: With past or future indicators (adverbs)

The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `2023-02-08T21:27:15` | `2023-02-08T21:27:15` |
| `dt_ref` | `2023-02-08T23:22:15` | `2023-02-08T23:22:15` |
| `add_adverb` | `true` | `true` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T23:22:15&add_adverb=true
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T23:22:15&add_adverb=true"
```

#### Response

```
{
  "data": "1 hour ago"
}
```

In the above example, since `dt` is 1 hour behind `dt_ref`, the result returned is `1 hour ago`.

### Example #6: Using articles

`use_article`, if set as `true` adds an article (`a`, `an`) to the time difference instead of `1`. 

For example, `1 minute ago` will become `a minute ago`. 

Note, `use_article` will only work when the unit of time difference is `1` i.e, `1 second`, `1 minute` or `1 hour` only.

The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `2023-02-08T21:27:15` | `2023-02-08T21:27:15` |
| `dt_ref` | `2023-02-08T23:22:15` | `2023-02-08T23:22:15` |
| `use_article` | `true` | `true` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T23:22:15&use_article=true
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T23:22:15&use_article=true"
```

#### Response

```
{
  "data": "an hour"
}
```

Here, `dt` is 1 hour behind `dt_ref` and `use_article` is set as `true`. Hence, the result returned is `an hour` instead of `1 hour`.

### Example #7: Using articles + past/present indicators

The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `2023-02-08T21:27:15` | `2023-02-08T21:27:15` |
| `dt_ref` | `2023-02-08T23:22:15` | `2023-02-08T23:22:15` |
| `use_article` | `true` | `true` |
| `add_adverb` | `true` | `true` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T23:22:15&use_article=true&add_adverb=true
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T23:22:15&use_article=true&add_adverb=true"
```

#### Response

```
{
  "data": "an hour ago"
}
```

Here, `dt` is 1 hour behind `dt_ref` and `add_adverb` & `use_article` are set as `true`. Hence, the result returned is `an hour ago` instead of `1 hour ago`.

### Example #8: With short or full units

`units` refer to the time units. They can either be `FULL` or `SHORT`. The default value for `units` is `FULL` i.e., `second`, `minute` and `hour` are used. When units is set to `SHORT`, `s`, `m` and `hr` are used respectively.

The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `2023-02-08T21:27:15` | `2023-02-08T21:27:15` |
| `dt_ref` | `2023-02-08T21:22:15` | `2023-02-08T21:22:15` |
| `units` | `SHORT` | `SHORT` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T21:22:15&units=SHORT
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T21:22:15&units=SHORT"
```

#### Response

```
{
  "data": "5 m"
}
```

Since, `units` is set to `SHORT` here, `m` is used instead of `minutes`.

### Example #9: Using cutoff_now

`cutoff_now` is the number of seconds of time difference for which "now" is returned instead of the actual time difference. By default, `cutoff_now` is set as `1`, which means that any time difference less than 1 second is returned as "now" instead of the time difference in milliseconds.

The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `2023-02-08T21:27:15` | `2023-02-08T21:27:15` |
| `dt_ref` | `2023-02-08T21:22:15` | `2023-02-08T21:22:15` |
| `cutoff_now` | `301` | `301` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T21:22:15&cutoff_now=301
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21:27:15&dt_ref=2023-02-08T21:22:15&cutoff_now=301"
```

#### Response

```
{
  "data": "now"
}
```

In this example, time difference between `dt` and `dt_ref` is 5 minutes or 300 seconds. But, as `cutoff_now` is set as `301` seconds, it returns `now`.

### Example #10: Using round_down

`round_down` rounds the time difference to the largest unit quantity that is less than or equal to it. For example, "1 week, 2 days" becomes "1 week". This is the default behaviour (`true`).

If `round_down` is turned `false`, this value is rounded to the nearest largest unit quantity. For example, "1 week, 2 days" still returns "1 week", but "1 week, 5 days" returns "2 weeks".

The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `2023-02-09T21:27:15` | `2023-02-09T21:27:15` |
| `dt_ref` | `2023-02-23T06:51:46` | `2023-02-23T06:51:46` |
| `round_down` | `false` | `false` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=2023-02-09T21:27:15&dt_ref=2023-02-23T06:51:46&round_down=false
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-09T21:27:15&dt_ref=2023-02-23T06:51:46&round_down=false"
```

#### Response

```
{
  "data": "2 weeks"
}
```

Here, in this example, difference between `dt` and `dt_ref` is 1 week, 6 days, 9 hours, 24 minutes, and 31 seconds. Since `round_down` is set as `false`, the value is rounded to `2 weeks` and returned.

### Example #11: Custom timestamp formatting

`fmt` is used to provide the format of the timestamp if it is not in a valid ISO 8601 format. [Click here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) to learn more about formatting date strings.

The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `21 January 2014` | `21%20January%202014` |
| `dt_ref` | `22 January 2014` | `22%20January%202014` |
| `fmt` | `%d %B %Y` | `%25d%20%25B%20%25Y` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=21%20January%202014&dt_ref=22%20January%202014&fmt=%25d%20%25B%20%25Y
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=21%20January%202014&dt_ref=22%20January%202014&fmt=%25d%20%25B%20%25Y"
```

#### Response

```
{
  "data": "1 day"
}
```

### Example #12: Custom timestamp formatting

`fmt` is used to provide the format of the timestamp if it is not in a valid ISO 8601 format. [Click here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) to learn more about formatting date strings.

The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `22 January 2014 19 12 22` | `22%20January%202014%2019%2012%2022` |
| `dt_ref` | `22 January 2014 20 12 22` | `22%20January%202014%2020%2012%2022` |
| `fmt` | `%d %B %Y %H %M %S` | `%25d%20%25B%20%25Y%20%25H%20%25M%20%25S` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=22%20January%202014%2019%2012%2022&dt_ref=22%20January%202014%2020%2012%2022&fmt=%25d%20%25B%20%25Y%20%25H%20%25M%20%25S
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=22%20January%202014%2019%2012%2022&dt_ref=22%20January%202014%2020%2012%2022&fmt=%25d%20%25B%20%25Y%20%25H%20%25M%20%25S"
```

#### Response

```
{
  "data": "1 hour"
}
```

### Example #13: Using all parameters

In this example, we will see all the parameters in action.

The value of query parameters are provided in the table below:

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `dt` | `08-Feb-2023 21:27:15` | `08-Feb-2023%2021:27:15` |
| `dt_ref` | `08-Feb-2023 21:22:40` | `08-Feb-2023%2021:22:40` |
| `fmt` | `%d-%b-%Y %H:%M:%S` | `%25d-%25b-%25Y%20%25H:%25M:%25S` |
| `units` | `SHORT` | `SHORT` |
| `cutoff_now` | `200` | `200` |
| `add_adverb` | `true` | `true` |
| `use_article` | `true` | `true` |
| `round_down` | `false` | `false` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?dt=08-Feb-2023%2021:27:15&dt_ref=08-Feb-2023%2021:22:40&fmt=%25d-%25b-%25Y%20%25H:%25M:%25S&units=SHORT&cutoff_now=200&add_adverb=true&use_article=true&round_down=false
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?dt=08-Feb-2023%2021:27:15&dt_ref=08-Feb-2023%2021:22:40&fmt=%25d-%25b-%25Y%20%25H:%25M:%25S&units=SHORT&cutoff_now=200&add_adverb=true&use_article=true&round_down=false"
```

#### Response

```
{
  "data": "5 m from now"
}
```

In this example, 
- the format of the timestamp `fmt` is set as `"%d-%b-%Y %H:%M:%S"` and `dt` is 4 minutes 35 seconds ahead of `dt_ref`. 
- As `units` is equal to `SHORT`, `minutes` become `m`. 
- `cutoff_now` is `200`, hence will have no impact on the result as the time difference is 4 minutes 35 seconds or 275 seconds. 
- `add_adverb` is `true`, hence `from now` will be added to the result. 
- `use_article` is `true`, but will have no impact as time difference is greater than 1 unit of time difference (minute). 
- As `round_down` is set as `false`, 4 minutes 35 seconds will become 5 minutes. 

Thus, the result returned is `"5 m from now"`.
