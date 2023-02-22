---
method: get
title: Text to Sentence Case
desc: Converts the provided text into sentence case.
path: case/sentence
---

This API converts the input text into sentence case wherein the first character is capitalized and rest all characters are lowercased. It doesn't capitalize names or places.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| `text` | `string` | Yes | | The input text  |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Sample Usage

### Example #1

Below is an example API usage for the `text` query parameter provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `text` | `grass is green` | `grass%20is%20green` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?text=grass%20is%20green
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?text=grass%20is%20green"
```

#### Response

```
{
  "data": "Grass is green"
}
```

### Example #2

Below is another example API usage for the `text` query parameter provided in the table below.

| Query Parameter | Value | URL Safe Value |
| ----------- | ----------- | -----------  |
| `text` | `grass is greener in California with Tim` | `grass%20is%20greener%20in%20California%20with%20Tim` |

#### API Request

The below API request can be copied and directly executed in the browser.

```
{{ site_api }}/{{ path }}?text=grass%20is%20greener%20in%20California%20with%20Tim
```

#### cURL Request

Making the API request via cURL command line tool.

```
curl "{{ site_api }}/{{ path }}?text=grass%20is%20greener%20in%20California%20with%20Tim"
```

#### Response

```
{
  "data": "Grass is greener in california with tim"
}
```
