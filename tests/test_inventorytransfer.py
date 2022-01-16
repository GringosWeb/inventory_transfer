
from pytest import raises
from inventorytransfer.main import InventoryTransferTest

def test_inventorytransfer():
    # test inventorytransfer without any subcommands or arguments
    with InventoryTransferTest() as app:
        app.run()
        assert app.exit_code == 0


def test_inventorytransfer_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with InventoryTransferTest(argv=argv) as app:
        app.run()
        assert app.debug is True


def test_command1():
    # test command1 without arguments
    argv = ['command1']
    with InventoryTransferTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'bar'
        assert output.find('Foo => bar')


    # test command1 with arguments
    argv = ['command1', '--foo', 'not-bar']
    with InventoryTransferTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'not-bar'
        assert output.find('Foo => not-bar')
