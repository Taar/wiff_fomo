import json
import sys
import os

from wiff_fomo.main import main


if '__main__' == __name__:
    path, save_path = sys.argv[1:3]
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        path
    )

    main(path, save_path)
