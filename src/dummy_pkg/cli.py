#!/usr/bin/env python

# SPDX-FileCopyrightText: Copyright © Idiap Research Institute <contact@idiap.ch>
#
# SPDX-FileContributor: Yannick Dayer <yannick.dayer@idiap.ch>
#
# SPDX-License-Identifier: MIT

from pathlib import Path

import click


@click.command()
@click.argument("user", default="world")
def hello(user: str = None):
    """~Greetings!~."""
    click.echo(f"Hello {user}")
    click.echo(f"You are in '{Path().resolve()}'")
    click.echo("Have a nice day")


if __name__ == "__main__":
    hello()
