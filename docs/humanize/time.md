---
method: get
title: Time Difference to Human
desc: Convert time difference into a human readable form (for social media, chat apps).
path: humanize/time
---

This API returns a time difference in human readable version as typically displayed in social media apps like `2 minutes ago`, `3 days ago`, etc. </h4>

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| `dt` | string | Yes | | Date-time string. It should be a valid [ISO 8601 format](https://www.w3.org/TR/NOTE-datetime). If it is a custom date-time format, then `fmt` parameter is required. |
| `dt_ref` | string | No | | Used to supply a reference timestamp from which the difference is calculated. If not provided, the current system timestamp is used. |
| `fmt` | string | No | | Used to provide the format of the timestamp if it is not in a valid ISO 8601 format. (See example for more details) |
| `units` | string | No | `FULL` | Can be `SHORT` or `FULL`. (See example for more details) |
| `cutoff_now` | integer | No | `1` | Is the number of seconds of time difference for which `"now"` is returned instead of the actual time difference. Default is set as `1` which means that any time difference less than a second is returned as `"now"` instead of the time difference in milliseconds |
| `add_adverb` | boolean | No | `false` | Adds `"ago"` or `"from now"` based on the time difference. (See example for more details) |
| `use_article` | boolean | No | `false` | Specifies when to use articles `"a"` and `"an"` instead of `"1"`. (See example for more details) |
| `round_down` | boolean | No | `true` | Rounds the time difference to the largest unit quantity that is less than or equal to it. |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

### 1. Basic Usage

Below is a basic usage of the api with just the `dt` param. 

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21%3A27%3A15"
```

#### Response

```
{
  "data": "3 minutes"
}
```

In this example, the difference between `dt` and the current system timestamp i.e., `"3 minutes"` is returned.

### 2. Basic usage with dt_ref

`dt_ref` signifies the base time. If it is not supplied or set as `None`, the current system timestamp is used for the analysis of time difference.

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21%3A27%3A15&dt_ref=2023-02-08T21%3A27%3A15"
```

#### Response

```
{
  "data": "now"
}
```

Since, `dt` is equal to `dt_ref`, `"now"` is returned.

### 3. Basic with dt_ref

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21%3A27%3A15&dt_ref=2023-02-08T21%3A22%3A15"
```

#### Response

```
{
  "data": "5 minutes"
}
```

Here, the time difference between `dt` and `dt_ref` is returned.

### 4. Basic with add_adverb

`add_adverb` adds ago or from now to the time difference between `dt` and `dt_ref`. If `dt` is ahead in time compared to `dt_ref`, from now is added, else ago is used. 

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21%3A27%3A15&dt_ref=2023-02-08T21%3A22%3A15&add_adverb=true"
```

#### Response

```
{
  "data": "5 minutes from now"
}
```

In the above example, since `dt` is 5 minutes ahead of `dt_ref` the result returned is 5 minutes from now.


### 5. Basic with add_adverb

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21%3A27%3A15&dt_ref=2023-02-08T23%3A22%3A15&add_adverb=true"
```

#### Response

```
{
  "data": "1 hour ago"
}
```

In the above example, since `dt` is 1 hour behind `dt_ref`, the result returned is 1 hour ago.

### 6. Basic with use_article

`use_article`, if set as `True` adds an article (`a`, `an`) to the time difference instead of `1`. 

For example, `1 minute ago` will become `a minute ago`. The default value of `use_article` is `false`. 

Note, `use_article` will only work when the unit of time difference is `1` i.e, `1 second`, `1 minute` or `1 hour` only.

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21%3A27%3A15&dt_ref=2023-02-08T23%3A22%3A15&use_article=true"
```

#### Response

```
{
  "data": "an hour"
}
```

Here, `dt` is 1 hour behind `dt_ref` and `use_article` is set as `true`. Hence, the result returned is an hour.

### 7. Basic with units

`units` refer to the time units. They can either be `FULL` or `SHORT`. The default value for `units` is `FULL` i.e., second, minute and hour will be used. When units is set to `SHORT`, s,m and hr are simultaneously used.

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21%3A27%3A15&dt_ref=2023-02-08T21%3A22%3A15&units=SHORT"
```

#### Response

```
{
  "data": "5 m"
}
```

Since, `units` is set to `SHORT` here, m is used instead of minutes.

### 8. Basic with cutoff_now

`cutoff_now` is the number of seconds of time difference for which "now" is returned instead of the actual time difference. By default, `cutoff_now` is set as `1`, which means that any time difference less than 1 second is returned as "now" instead of the time difference in milliseconds.

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21%3A27%3A15&dt_ref=2023-02-08T21%3A22%3A15&cutoff_now=301"
```

#### Response

```
{
  "data": "now"
}
```

Here, in this example, time difference between `dt` and `dt_ref` is 5 minutes or 300 seconds. Since `cutoff_now` is equal to 301 seconds, it returns now.

### 9. Basic with round_down

`round_down` if True (default), rounds the time difference to the largest unit quantity that is less than or equal to it. For example, "1 week, 2 days" becomes "1 week". If turned `False`, "1 week, 2 days" still returns "1 week", but "1 week, 5 days" returns "2 weeks".

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=2023-02-08T21%3A27%3A15&dt_ref=2023-02-08T21%3A22%3A40&round_down=false"
```

#### Response

```
{
  "data": "5 minutes"
}
```

Here, in this example, difference between `dt` and `dt_ref` is 4 minutes 35 seconds. Since `round_down` is set as `false`, 5 minutes is returned instead of 4 minutes.

### 10. Basic with fmt

`fmt` is used to provide the format of the timestamp if it is not in a valid ISO 8601 format. [Click here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) to learn more about formatting date strings.

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=21-January%202014&dt_ref=22-January%202014&fmt=%25d-%25B%20%25Y"
```

#### Response

```
{
  "data": "1 day"
}
```

Here `fmt` is equal to `%d-%B %Y`, with `dt` being equal to "21-January 2014" and `dt_ref` being equal to "22-January 2014" and the result is then returned as 1 day. The separators for the format of the timestamp can be chosen by the user.

### 11. Basic with fmt

`fmt` is used to provide the format of the timestamp if it is not in a valid ISO 8601 format. [Click here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) to learn more about formatting date strings.

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=22%20January%202014%2019%2012%2022&dt_ref=22%20January%202014%2020%2012%2022&fmt=%25d%20%25B%20%25Y%20%25H%20%25M%20%25S"
```

#### Response

```
{
  "data": "1 hour"
}
```

### 12. Complete request

In this example, we will see all the parameters in action

#### Request

```
curl "{{ site_api }}/{{ path }}?dt=08-Feb-2023%2021%3A27%3A15&dt_ref=08-Feb-2023%2021%3A22%3A40&fmt=%25d-%25b-%25Y%20%25H%3A%25M%3A%25S&units=SHORT&cutoff_now=200&add_adverb=true&use_article=true&round_down=false"
```

#### Response

```
{
  "data": "5 m from now"
}
```

In this example, the format of the timestamp `fmt` is set as `"%d-%b-%Y %H:%M:%S"` and `dt` is 4 minutes 35 seconds ahead of `dt_ref`. Since `units` is equal to `SHORT`, minutes become m. `cutoff_now` is 200, hence will have no impact on the result as the time difference is 4 minutes 35 seconds or 275 seconds. `add_adverb` is `true`, hence "from now" will be added to the result. `use_article` is true, but will have no impact as time difference is greater than 1 unit of time difference, here it is 4 minutes. Now, since `round_down` is set as false, 4 minutes 35 seconds will become 5 minutes. Thus, the result returned is "5 m from now".
