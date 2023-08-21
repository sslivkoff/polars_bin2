
# polars bin2

An enhanced `bin` namespace for polars.

The polars `str` namespace contains many functions that would also be useful to have in the `bin` namespace. The `polars_bin2` package implements these functions in the `bin2` namespace for both Series and Expr in polars.

The functions in `polars_bin2` are currently implemented by 1) encoding binary data as `str`, 2) using the `str` namespace, and 3) converting the result.

## Available functions

| function | `str` namespace | `bin` namespace | `bin2` namespace |
| --- | --- | --- | --- |
|           concat  │  ✅  │  ❌ | - |
|         contains  │  ✅  │  ✅ | - |
|      count_match  │  ✅  │  ❌ | - |
|           decode  │  ✅  │  ✅ | - |
|           encode  │  ✅  │  ✅ | - |
|        ends_with  │  ✅  │  ✅ | - |
|          explode  │  ✅  │  ❌ | - |
|          extract  │  ✅  │  ❌ | - |
|      extract_all  │  ✅  │  ❌ | - |
|   extract_groups  │  ✅  │  ❌ | - |
|     json_extract  │  ✅  │  ❌ | - |
|  json_path_match  │  ✅  │  ❌ | - |
|          lengths  │  ✅  │  ❌ | - |
|            ljust  │  ✅  │  ❌ | - |
|           lstrip  │  ✅  │  ❌ | - |
|          n_chars  │  ✅  │  ❌ | - |
|        parse_int  │  ✅  │  ❌ | - |
|          replace  │  ✅  │  ❌ | - |
|      replace_all  │  ✅  │  ❌ | - |
|            rjust  │  ✅  │  ❌ | - |
|           rstrip  │  ✅  │  ❌ | - |
|            slice  │  ✅  │  ❌ | - |
|            split  │  ✅  │  ❌ | - |
|      split_exact  │  ✅  │  ❌ | - |
|           splitn  │  ✅  │  ❌ | - |
|      starts_with  │  ✅  │  ✅ | - |
|            strip  │  ✅  │  ❌ | - |
|         strptime  │  ✅  │  ❌ | - |
|          to_date  │  ✅  │  ❌ | - |
|      to_datetime  │  ✅  │  ❌ | - |
|       to_decimal  │  ✅  │  ❌ | - |
|     to_lowercase  │  ✅  │  ❌ | - |
|          to_time  │  ✅  │  ❌ | - |
|     to_titlecase  │  ✅  │  ❌ | - |
|     to_uppercase  │  ✅  │  ❌ | - |
|            zfill  │  ✅  │  ❌ | - |

There are also some functions in the `str` namespace that are not applicable to binary data. These are not implemented in `bin2`:



