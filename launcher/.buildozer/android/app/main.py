import sys
FORCE_REMOTE = False
if '--remote' in sys.argv:
    FORCE_REMOTE = True
    sys.argv.remove('--remote')

import pypath
import kivy
kivy.require('2.0.0')
from kivy.utils import platform
from bootstrap import Bootstrap, BootstrapApp

def android_get_root():
    import android.storage
    root = pypath.local(android.storage.app_storage_path())
    print('android_get_root() ==>', root)
    return root

if platform == 'android':
    ROOT = android_get_root()
    local = False
elif FORCE_REMOTE:
    # for testing the remote deployments on the local machine
    ROOT = pypath.local('/tmp/mcont')
    local = False
else:
    # for local deployments
    ROOT = pypath.local(__file__).dirpath().dirpath()
    local = True


def get_main():
    # check and/or update the source code
    bootstrap = Bootstrap(ROOT, local)
    if bootstrap.update():
        # src updated correctly, load it
        bootstrap.load()
        from mcont.gui.app import main
        return main
    else:
        # probably we cannot connect to the sync server. Start a simple app to
        # allow the user to chance the settings
        return bootstrap_main


def bootstrap_main():
    BootstrapApp(ROOT).run()


if __name__ == '__main__':
    main = get_main()
    if platform == 'android':
        main()
    else:
        try:
            main()
        except:
            import pdb;pdb.xpm()
