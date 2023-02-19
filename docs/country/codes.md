---
method: get
title: Country Code Dictionary
desc: Fetch the country code dictionary where country names are keys and the Alpha-2 (two-lettered) country codes are the values corresponding to the keys.
path: country/codes
---

This API fetches the country code dictionary where country names are keys and the Alpha-2 (two-lettered) country codes are the values corresponding to the keys.

## Example

Below is an example of the api usage. 

#### Request

```
curl -X 'GET' \
  '{{ site_api }}/{{ path }}' \
  -H 'accept: application/json'
```

#### Response

```
{
  "data": {
    "Afghanistan": "AF",
    "Albania": "AL",
    "Algeria": "DZ",
    "American Samoa": "AS",
    "Andorra": "AD",
    "Angola": "AO",
    ...
  }
}
```
