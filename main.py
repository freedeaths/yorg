# log ########################################################################
from os.path import exists, join
from panda3d.core import MultiplexStream, Notify, Filename
from yorg.yorg import Yorg
import sys
import direct.particles.ParticleManagerGlobal  # for deploy-ng


if sys.platform != 'darwin' and not exists('main.py'):
    # (on osx it shows an error window on exit)
    # is it the deployed version?
    log_path = ''
    if sys.platform == 'win32' and not exists('main.py'):
        log_path = join(str(Filename.get_user_appdata_directory()), 'Yorg')
        if not exists(log_path):
            Filename.mkdir(Filename(log_path))
    sys.stdout = open(join(log_path, 'yorg_output.txt') if log_path else 'yorg_output.txt', 'w')
    sys.stderr = open(join(log_path, 'yorg_error.txt') if log_path else 'yorg_error.txt', 'w')
    nout = MultiplexStream()
    Notify.ptr().setOstreamPtr(nout, 0)
    nout.addFile(join(log_path, 'yorg_log.txt') if log_path else 'yorg_log.txt')


# main #######################################################################
if __name__ == '__main__' or exists('main.pyo'):
    Yorg()
