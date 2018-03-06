from click.testing import CliRunner
from skeletor.cli import main
def test_main():
    runner = CliRunner()
    result = runner.invoke(main, ['dropdb',])
    assert 'Dropped the database' in result.output
