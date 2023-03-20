from contextlib import redirect_stderr, redirect_stdout, contextmanager
import sys


class Redirect():
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush()
        self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush()
        self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr


print('Hello stdout')
stdout_file = open('stdout.txt', 'w')
stderr_file = open('stderr.txt', 'w')


with Redirect(stdout=stdout_file, stderr=stderr_file):
    print('Hello stdout.txt')
    raise Exception('Hello stderr.txt')


print('Hello stdout again')
raise Exception('Hello stderr')
