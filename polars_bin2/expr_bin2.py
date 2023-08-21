from __future__ import annotations

import polars as pl


@pl.api.register_expr_namespace('bin2')
class ExprBin2:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    #
    # # functions already in the bin namespace
    #

    def contains(self, subvalue: bytes) -> bool:
        self._expr.bin.contains(subvalue)

    def decode(self, subvalue: bytes) -> bool:
        self._expr.bin.decode(subvalue)

    def encode(self, subvalue: bytes) -> bool:
        self._expr.bin.encode(subvalue)

    def ends_with(self, subvalue: bytes) -> bool:
        self._expr.bin.ends_with(subvalue)

    def starts_with(self, subvalue: bytes) -> bool:
        self._expr.bin.starts_with(subvalue)

    #
    # # functions from str namespace
    #

    def lengths(self) -> pl.Expr:
        return (self._expr.bin.encode('hex').str.lengths() / 2).cast(int)

    def slice(self, offset: int, length: int | None = None) -> pl.Expr:
        if length is not None:
            if length < 0:
                raise Exception('negative value not allowed for length')
            length = length * 2
        return (self._expr.bin.encode('hex').str.slice(offset * 2, length)).str.decode('hex')

