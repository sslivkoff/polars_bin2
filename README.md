# polars bin2

An enhanced `bin` namespace for polars.

The polars `str` namespace contains many functions that would also be useful to have in the `bin` namespace. The `polars_bin2` package implements these functions in the `bin2` namespace for both Series and Expr in polars.

Most of the functions in `polars_bin2` are currently implemented by 1) encoding binary data as `str`, 2) using the `str` namespace, and 3) converting the result approximately.

## Available functions in each namespace

*(as of polars 0.18.13)*

| function | `str` | `bin` | `bin2` | description |
| -------: | :---: | :---: | :----: | --- |
|        `concat`| ✅ | ❌ | - | concatenate series into single value |
|      `contains`| ✅ | ✅ | - | check if value contains subvalue |
|   `count_match`| ✅ | ❌ | - | count number of occurences |
|        `decode`| ✅ | ✅ | - | decode using provided encoding |
|        `encode`| ✅ | ✅ | - | encode using provided encoding |
|     `ends_with`| ✅ | ✅ | - | check if value ends with subvalue |
|       `explode`| ✅ | ❌ | - | return separate row for each subvalue |
|       `extract`| ✅ | ❌ | - | extract target group from provided pattern |
|   `extract_all`| ✅ | ❌ | - | extract all matches for provided pattern |
|`extract_groups`| ✅ | ❌ | - | extract all groups for provided pattern |
|       `lengths`| ✅ | ❌ | - | return byte length of each entry |
|         `ljust`| ✅ | ❌ | - | left justify according to `width` |
|        `lstrip`| ✅ | ❌ | - | remove leading subvalues |
|       `replace`| ✅ | ❌ | - | replace first subvalue occurence with new value |
|   `replace_all`| ✅ | ❌ | - | replace all subvalue occurences with new value |
|         `rjust`| ✅ | ❌ | - | right justify according to `width` |
|        `rstrip`| ✅ | ❌ | - | remove trailing subvalues |
|         `slice`| ✅ | ❌ | - | create subslices of each value |
|         `split`| ✅ | ❌ | - | split each value by a subvalue |
|   `split_exact`| ✅ | ❌ | - | split each value by a subvalue using `n` splits |
|        `splitn`| ✅ | ❌ | - | split each value by a subvalue at most `n` times |
|   `starts_with`| ✅ | ✅ | - | check if value starts with subvalue |
|         `strip`| ✅ | ❌ | - | remove leading and trailing subvalues |
|         `zfill`| ✅ | ❌ | - | fill the value with zeros |

There are also some functions in the `str` namespace that are not applicable to binary data. These are not currently implemented in `bin2`, though there might be some reason to implement them in the future:

| function | `str` | `bin` | `bin2` | description |
| -------: | :---: | :---: | :----: | :---------- |
|   `json_extract`| ✅ | ❌ | ❌ | parse values as json |
|`json_path_match`| ✅ | ❌ | ❌ | extract first match of JSON string |
|        `n_chars`| ✅ | ❌ | ❌ | return char length of each entry | 
|      `parse_int`| ✅ | ❌ | ❌ | parse integers |
|       `strptime`| ✅ | ❌ | ❌ | convert to a date/time column |
|        `to_date`| ✅ | ❌ | ❌ | convert to a date column |
|    `to_datetime`| ✅ | ❌ | ❌ | convert to a time column |
|     `to_decimal`| ✅ | ❌ | ❌ | convert to a decimal column |
|   `to_lowercase`| ✅ | ❌ | ❌ | convert to lowercase |
|        `to_time`| ✅ | ❌ | ❌ | convert to a time column |
|   `to_titlecase`| ✅ | ❌ | ❌ | convert to title case |
|   `to_uppercase`| ✅ | ❌ | ❌ | convert to upper case |
