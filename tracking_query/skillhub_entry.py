#!/usr/bin/env python3
from __future__ import annotations

import sys


SLUG = "tracking-query"


def main() -> None:
    sys.argv[0] = SLUG

    from .cli import cli

    cli(prog_name=SLUG, obj={})


if __name__ == "__main__":
    main()
