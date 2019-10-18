import unittest
from ring_buffer import RingBuffer

class RingBufferTests(unittest.TestCase):
    def setUp(self):
        self.buffer = RingBuffer(5)

    def test_ring_buffer(self):
        self.assertEqual(len(self.buffer.storage), 5)

        self.buffer.append('a')
        self.buffer.append('b')
        self.buffer.append('c')
        self.buffer.append('d')
        print(self.buffer.storage);
        self.assertEqual(len(self.buffer.storage), 5)
        self.assertEqual(self.buffer.get(), ['a', 'b', 'c', 'd'])
        print(self.buffer.storage);
        self.buffer.append('e')
        self.assertEqual(len(self.buffer.storage), 5)
        self.assertEqual(self.buffer.get(), ['a', 'b', 'c', 'd', 'e'])
        print(self.buffer.storage);
        self.buffer.append('f')
        self.assertEqual(len(self.buffer.storage), 5)
        print(self.buffer.storage);
        self.assertEqual(self.buffer.get(), ['f', 'b', 'c', 'd', 'e'])
        self.buffer.append('g')
        print(self.buffer.storage);
        self.buffer.append('h')
        print(self.buffer.storage);
        self.buffer.append('i')
        print(self.buffer.storage);
        self.assertEqual(len(self.buffer.storage), 5)
        self.assertEqual(self.buffer.get(), ['f', 'g', 'h', 'i', 'e'])


if __name__ == '__main__':
    unittest.main()
