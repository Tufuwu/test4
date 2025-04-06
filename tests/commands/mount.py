#
# Copyright (C) 2017  Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
# Red Hat Author(s): Vratislav Podzimek <vpodzime@redhat.com>
#

import unittest
from tests.baseclass import CommandTest

from pykickstart.errors import KickstartParseError

class F27_TestCase(CommandTest):
    command = "mount"

    def runTest(self):
        self.assert_parse("mount /dev/sda1 /boot", "mount /dev/sda1 /boot\n")
        self.assert_parse("mount /dev/sda1 /boot --reformat", "mount /dev/sda1 /boot --reformat\n")
        self.assert_parse("mount /dev/sda1 /boot --reformat=xfs", "mount /dev/sda1 /boot --reformat=xfs\n")
        self.assert_parse("mount /dev/sda1 /boot --reformat=xfs --mkfsoptions=\"-L BOOT\"",
                          "mount /dev/sda1 /boot --reformat=xfs --mkfsoptions=\"-L BOOT\"\n")
        self.assert_parse("mount /dev/sda1 /boot --reformat=xfs --mountoptions=user",
                          "mount /dev/sda1 /boot --reformat=xfs --mountoptions=\"user\"\n")
        self.assert_parse("mount /dev/sda3 none  --reformat=swap", "mount /dev/sda3 none --reformat=swap\n")

        self.assert_parse_error("mount /dev/sda1", KickstartParseError)
        self.assert_parse_error("mount /boot", KickstartParseError)
        self.assert_parse_error("mount /dev/sda1 /boot --mkfsoptions=\"-L BOOT\"", KickstartParseError)

if __name__ == "__main__":
    unittest.main()
