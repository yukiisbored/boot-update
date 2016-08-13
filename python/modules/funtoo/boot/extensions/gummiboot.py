# -*- coding: ascii -*-

import os
import shlex

from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT

from funtoo.boot.extension import Extension
from funtoo.boot.extension import ExtensionError

def getExtension(config):
	""" Gets the extension based on the configuration """
	return GummibootExtension(config)

class GummibootExtension(Extension):
        """ Implements an extension for the gummiboot bootloader """

        def __init__(self, config, testing = False):
                Extension.__init__(self.config)

        def isAvailable(self):
                if not os.path.exists("/sys/firmware/efi"):
                        allmsgs.append(["fatal", "EFI doesn't exist / not enabled on this system"])
                        return [False, []]
                elif not os.path.exists("/boot/loader"):
                        allmsgs.append(["fatal", "/boot/loader does not exist; Assuming gummiboot is not installed / /boot is not ESP"])
                        return [False, []]
                return [True, []]
