import unittest

from mahjong.tests_mixin import TestMixin

from mahjong.utils import find_isolated_tile_indices, is_tile_strictly_isolated

from mahjong.tile import TilesConverter


class UtilsTestCase(unittest.TestCase, TestMixin):

    def test_find_isolated_tiles(self):
        hand_34 = TilesConverter.string_to_34_array(sou='1369', pin='15678', man='25', honors='124')
        isolated_tiles = find_isolated_tile_indices(hand_34)

        self.assertEqual(self._string_to_34_tile(sou='1') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(sou='2') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(sou='3') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(sou='4') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(sou='5') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(sou='6') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(sou='7') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(sou='8') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(sou='9') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(pin='1') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(pin='2') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(pin='3') in isolated_tiles, True)
        self.assertEqual(self._string_to_34_tile(pin='4') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(pin='5') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(pin='6') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(pin='7') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(pin='8') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(pin='9') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(man='1') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(man='2') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(man='3') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(man='4') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(man='5') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(man='6') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(man='7') in isolated_tiles, True)
        self.assertEqual(self._string_to_34_tile(man='8') in isolated_tiles, True)
        self.assertEqual(self._string_to_34_tile(man='9') in isolated_tiles, True)
        self.assertEqual(self._string_to_34_tile(honors='1') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(honors='2') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(honors='3') in isolated_tiles, True)
        self.assertEqual(self._string_to_34_tile(honors='4') in isolated_tiles, False)
        self.assertEqual(self._string_to_34_tile(honors='5') in isolated_tiles, True)
        self.assertEqual(self._string_to_34_tile(honors='6') in isolated_tiles, True)
        self.assertEqual(self._string_to_34_tile(honors='7') in isolated_tiles, True)

    def test_is_strictly_isolated_tile(self):
        hand_34 = TilesConverter.string_to_34_array(sou='1399', pin='1567', man='25', honors='1224')

        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(sou='1')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(sou='2')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(sou='3')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(sou='4')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(sou='5')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(sou='6')), True)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(sou='7')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(sou='8')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(sou='9')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(pin='1')), True)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(pin='2')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(pin='3')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(pin='4')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(pin='5')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(pin='6')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(pin='7')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(pin='8')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(pin='9')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(man='1')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(man='2')), True)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(man='3')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(man='4')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(man='5')), True)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(man='6')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(man='7')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(man='8')), True)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(man='9')), True)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(honors='1')), True)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(honors='2')), False)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(honors='3')), True)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(honors='4')), True)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(honors='5')), True)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(honors='6')), True)
        self.assertEqual(is_tile_strictly_isolated(hand_34, self._string_to_34_tile(honors='7')), True)
