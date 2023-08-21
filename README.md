# polars bin2

An enhanced `bin` namespace for polars.

The polars `str` namespace contains many functions that would also be useful to have in the `bin` namespace. The `polars_bin2` package implements these functions in the `bin2` namespace for both Series and Expr in polars.

Most of the functions in `polars_bin2` are currently implemented by 1) encoding binary data as `str`, 2) using the `str` namespace, and 3) converting the result approximately.

## Installation

`pip install polars_bin2`

## Example Usage

Importing `polars_bin2` registers the namespace.

```python
import polars_bin2

addresses = [
    b'\xda\xc1\x7f\x95\x8d.\xe5#\xa2 b\x06\x99E\x97\xc1=\x83\x1e\xc7',
    b'\xa0\xb8i\x91\xc6!\x8b6\xc1\xd1\x9dJ.\x9e\xb0\xce6\x06\xebH',
    b'_\x98\x80ZN\x8b\xe2U\xa3(\x80\xfd\xec\x7fg(\xc6V\x8b\xa0'
]

series = pl.Series('address', addresses)
print(series.bin2.lengths())
```

## Available functions in each namespace

*(as of polars 0.18.13)*

| function | `str` | `bin` | `bin2` | description |
| -------: | :---: | :---: | :----: | --- |
|        `concat`| ✅ | ❌ | ✅ | concatenate series into single value |
|      `contains`| ✅ | ✅ | ✅ | check if value contains subvalue |
|   `count_match`| ✅ | ❌ | ✅ | count number of occurences |
|        `decode`| ✅ | ✅ | ✅ | decode using provided encoding |
|        `encode`| ✅ | ✅ | ✅ | encode using provided encoding |
|     `ends_with`| ✅ | ✅ | ✅ | check if value ends with subvalue |
|       `lengths`| ✅ | ❌ | ✅ | return byte length of each entry |
|         `ljust`| ✅ | ❌ | ✅ | left justify according to `width` |
|       `replace`| ✅ | ❌ | ✅ | replace first subvalue occurence with new value |
|   `replace_all`| ✅ | ❌ | ✅ | replace all subvalue occurences with new value |
|         `rjust`| ✅ | ❌ | ✅ | right justify according to `width` |
|         `slice`| ✅ | ❌ | ✅ | create subslices of each value |
|         `split`| ✅ | ❌ | ✅ | split each value by a subvalue |
|   `starts_with`| ✅ | ✅ | ✅ | check if value starts with subvalue |
|         `zfill`| ✅ | ❌ | ✅ | fill the value with zeros |

Strip functions cannot be implemented because strip works on single chars and `bin`-`str` encodings do not have a 1:1 mapping of bytes to chars. For example, using a hex encoding could remove an extra zero, making the encoding invalid, whereas base64 encoding does not have a 1:1 mapping of chars to bytes.

| function | `str` | `bin` | `bin2` | description |
| -------: | :---: | :---: | :----: | :---------- |
|        `lstrip`| ✅ | ❌ | ❌ | remove leading subvalues |
|        `rstrip`| ✅ | ❌ | ❌ | remove trailing subvalues |
|         `strip`| ✅ | ❌ | ❌ | remove leading and trailing subvalues |

There are some other functions in the `str` namespace that are not applicable to binary data. These are not currently implemented in `bin2`, though there might be some reason to implement them in the future:

| function | `str` | `bin` | `bin2` | description |
| -------: | :---: | :---: | :----: | :---------- |
|        `explode`| ✅ | ❌ | ❌ | return separate row for each subvalue |
|        `extract`| ✅ | ❌ | ❌ | extract target group from provided pattern |
|    `extract_all`| ✅ | ❌ | ❌ | extract all matches for provided pattern |
| `extract_groups`| ✅ | ❌ | ❌ | extract all groups for provided pattern |
|   `json_extract`| ✅ | ❌ | ❌ | parse values as json |
|`json_path_match`| ✅ | ❌ | ❌ | extract first match of JSON string |
|        `n_chars`| ✅ | ❌ | ❌ | return char length of each entry | 
|      `parse_int`| ✅ | ❌ | ❌ | parse integers |
|    `split_exact`| ✅ | ❌ | ❌ | split each value by a subvalue using `n` splits |
|         `splitn`| ✅ | ❌ | ❌ | split each value by a subvalue at most `n` times |
|       `strptime`| ✅ | ❌ | ❌ | convert to a date/time column |
|        `to_date`| ✅ | ❌ | ❌ | convert to a date column |
|    `to_datetime`| ✅ | ❌ | ❌ | convert to a time column |
|     `to_decimal`| ✅ | ❌ | ❌ | convert to a decimal column |
|   `to_lowercase`| ✅ | ❌ | ❌ | convert to lowercase |
|        `to_time`| ✅ | ❌ | ❌ | convert to a time column |
|   `to_titlecase`| ✅ | ❌ | ❌ | convert to title case |
|   `to_uppercase`| ✅ | ❌ | ❌ | convert to upper case |

