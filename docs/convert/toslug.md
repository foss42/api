---
method: get
title: Text to Slug
desc: Slugify any text / string with ease.
path: convert/slug
---

Convert a text into human readable slug. Useful for generating SEO friendly URL slugs from the page title of your website.

## Query Parameters

| Attribute | Data Type | Required | Default Value |Description |
| ----------- | ----------- | -----------  | ----------- | ----------- |
| text | string | Yes | | The text supplied to be converted to a slug |
| sep | string | No | - | The separator to be used in the slug  |

## HTTP Response Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

## Examples

### 1. Basic Usage

Below is a basic usage of the api with just the text param. 

#### Request

```
curl "{{ site_api }}/{{ path }}?text=Winter%20is%20coming"
```

#### Response

```
{
  "data": "winter-is-coming"
}
```

In this example, the input `text` is "Winter is coming". The output i.e, the slug version "winter-is-coming" is returned. In the output, the characters of input text are converted to lowercase characters and whitespaces are replaced by the default separator '-'. 

### 2. Basic Usage with different separator

The `sep` query param can be used to specify the separator in the slug. By default it is '-'.

#### Request

```
curl "{{ site_api }}/{{ path }}?text=Winter%20is%20coming&sep=%2B"
```

#### Response

```
{
  "data": "winter+is+coming"
}
```

In this example, the input `text` is "Winter is coming". The `sep` is equal to '+', which means that the space in the output slug will be replaced by '+'. Hence, "winter+is+coming" is returned.


### Some more examples

Let us see some more examples, of inputs being converted into slug in various scenarios.

| Input Text | Output slug | 
| ----------- | ----------- | 
| " aryan #$$ " | "aryan" |
| "one kožušček" | "one-kozuscek" |
| "one TWO" | "one-two" |
| "Дrаft №2.txt" | "draft-no-2-txt" |
| "Я ♥ борщ" | "ia-borshch" |
| ""ÜBER Über " | "uber-uber" |
| "This is a test ---" | "this-is-a-test" |
| "影師嗎" | "ying-shi-ma" |
| "C'est déjà l'été." | "c-est-deja-l-ete" |
| "Nín hǎo. Wǒ shì zhōng guó rén" | "nin-hao-wo-shi-zhong-guo-ren" |
| "Компьютер" | "kompiuter" |
| "jaja---lol-méméméoo--a" | "jaja-lol-mememeoo-a" |
| "10 | 20 %" | "10-20" |
| "i love 🦄" | "i-love" |
