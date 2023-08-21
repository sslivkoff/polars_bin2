from __future__ import annotations

import typing

import polars as pl


@pl.api.register_series_namespace('bin2')
class ExprBin2:
    def __init__(self, series: pl.Series):
        self._series = series

    #
    # # functions already in the bin namespace
    #

    def contains(self, subvalue: bytes) -> pl.Series:
        return self._series.bin.contains(subvalue)

    def decode(self, encoding: typing.Literal['hex', 'base64']) -> pl.Series:
        return self._series.bin.decode(encoding)

    def encode(self, encoding: typing.Literal['hex', 'base64']) -> pl.Series:
        return self._series.bin.encode(encoding)

    def ends_with(self, subvalue: bytes) -> pl.Series:
        return self._series.bin.ends_with(subvalue)

    def starts_with(self, subvalue: bytes) -> pl.Series:
        return self._series.bin.starts_with(subvalue)

    #
    # # functions from str namespace
    #

    def concat(self, delimiter: bytes = b'') -> pl.Series:
        return (
            self._series.bin.encode('hex')
            .str.concat(delimiter.hex())
            .str.decode('hex')
        )

    def count_match(self, pattern: bytes) -> pl.Series:
        return self._series.bin.encode('hex').str.count_match(pattern.hex())

    def lengths(self) -> pl.Series:
        return (self._series.bin.encode('hex').str.lengths() / 2).cast(int)

    def ljust(self, width: int, fill_char: bytes = b'\x00') -> pl.Series:
        fill_char_hex = fill_char.hex()
        if len(set(fill_char)) != 1:
            raise Exception('must use fill value with a single char in hex')
        return (
            self._series.bin.encode('hex')
            .str.ljust(width=width * 2, fill_char=fill_char_hex[0])
            .str.decode('hex')
        )

    def replace(
        self, pattern: bytes, value: bytes, *, literal: bool = False, n: int = 1
    ) -> pl.Series:
        return (
            self._series.bin.encode('hex')
            .str.replace(pattern.hex(), value.hex(), literal=literal, n=n)
            .str.decode('hex')
        )

    def replace_all(
        self, pattern: bytes, value: bytes, literal: bool = False
    ) -> pl.Series:
        return (
            self._series.bin.encode('hex')
            .str.replace_all(pattern.hex(), value.hex(), literal=literal)
            .str.decode('hex')
        )

    def rjust(self, width: int, fill_char: bytes = b'\x00') -> pl.Series:
        fill_char_hex = fill_char.hex()
        if len(set(fill_char)) != 1:
            raise Exception('must use fill value with a single char in hex')
        return (
            self._series.bin.encode('hex')
            .str.rjust(width=width * 2, fill_char=fill_char_hex[0])
            .str.decode('hex')
        )

    def slice(self, offset: int, length: int | None = None) -> pl.Series:
        if length is not None:
            if length < 0:
                raise Exception('negative value not allowed for length')
            length = length * 2
        return (
            self._series.bin.encode('hex').str.slice(offset * 2, length)
        ).str.decode('hex')

    def split(self, by: bytes, *, inclusive: bool = False) -> pl.Series:
        return (
            self._series.bin.encode('hex')
            .str.split(by.hex(), inclusive=inclusive)
            .list.eval(pl.element().str.decode('hex'))
        )

    def zfill(self, alignment: int) -> pl.Series:
        return (
            self._series.bin.encode('hex')
            .str.zfill(alignment * 2)
            .str.decode('hex')
        )

