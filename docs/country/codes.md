---
method: get
title: Country Code Dictionary
desc: Fetch the country code dictionary where country names are keys and the Alpha-2 (two-lettered) country codes are the values corresponding to the keys.
path: country/codes
---

This API fetches the country code dictionary where country names are keys and the Alpha-2 (two-lettered) country codes are the values corresponding to the keys.

## Sample Usage

This API has no query parameters.

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}
```

#### cURL Request

Making the API request via cURL command line tool.

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
