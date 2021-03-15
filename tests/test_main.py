from unittest import TestCase
from click.testing import CliRunner
from md_click.main import cli
import pathlib
import shutil

DOCS_DIR = './docs/commands'


class TestCLI(TestCase):
    """
    Test CLI commands
    """

    def setUp(self) -> None:
        """ Create new CLI Runner"""
        self.runner = CliRunner(echo_stdin=False)

    def test_dumps(self):
        """ Test the CLI dumps command"""
        resp = self.runner.invoke(
            cli,
            args=['dumps','--baseModule=examples.app.cli', '--baseCommand=main', f'--docsPath={DOCS_DIR}']
        )
        assert resp.exit_code == 0, f'CLI failed. Response: {resp.stdout}'

    def tearDown(self) -> None:
        """ Delete DOCS DIR """
        docs_dir = pathlib.Path(DOCS_DIR)
        for dir in docs_dir.parents:
            if dir == pathlib.Path('.'):
                continue
            shutil.rmtree(dir, ignore_errors=True)
