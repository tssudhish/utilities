# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir, "src"))

from callout import call_hello

call_hello( "Calling from another file")
