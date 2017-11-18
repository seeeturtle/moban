from mock import patch
import moban.reporter as reporter
from StringIO import StringIO
from nose.tools import eq_


def test_partial_run():
    patcher = patch('sys.stdout', new_callable=StringIO)
    fake_stdout = patcher.start()
    reporter.report_partial_run(1, 20)
    patcher.stop()
    eq_(fake_stdout.getvalue(), 'Templated 1 out of 20 files.\n')


def test_full_run():
    patcher = patch('sys.stdout', new_callable=StringIO)
    fake_stdout = patcher.start()
    reporter.report_full_run(20)
    patcher.stop()
    eq_(fake_stdout.getvalue(), 'Templated 20 files.\n')


def test_error_message():
    patcher = patch('sys.stdout', new_callable=StringIO)
    fake_stdout = patcher.start()
    reporter.report_error_message("something wrong")
    patcher.stop()
    eq_(fake_stdout.getvalue(), 'Error: something wrong\n')


def test_report_templating():
    patcher = patch('sys.stdout', new_callable=StringIO)
    fake_stdout = patcher.start()
    reporter.report_templating('a', 'b')
    patcher.stop()
    eq_(fake_stdout.getvalue(), 'Templating a to b\n')


def test_no_action():
    patcher = patch('sys.stdout', new_callable=StringIO)
    fake_stdout = patcher.start()
    reporter.report_no_action()
    patcher.stop()
    eq_(fake_stdout.getvalue(), 'Everything is up to date!\n')
