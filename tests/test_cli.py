# SPDX-FileCopyrightText: Copyright © Idiap Research Institute <contact@idiap.ch>
#
# SPDX-FileContributor: Yannick Dayer <yannick.dayer@idiap.ch>
#
# SPDX-License-Identifier: MIT

from click.testing import CliRunner

from dummy_pkg.cli import hello


def test_hello():
    """Run the main cli command."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        results = runner.invoke(hello)
        assert results.exit_code == 0
        assert results.output.startswith("Hello world")
        results = runner.invoke("hello", args=["dummy"])
        assert results.output.startswith("Hello dummy")
