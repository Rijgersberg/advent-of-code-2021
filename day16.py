from math import prod

from more_itertools import chunked

from aoc import get_input


class Packet:
    def __init__(self, bin_str, in_hex=False):
        if in_hex:
             bin_str = self.hex_to_bits(bin_str)

        self.pos = 0

        self.version = int(bin_str[:3], 2)
        self.pos += 3
        self.id = int(bin_str[3:6], 2)
        self.pos += 3

        if self.id == 4:
            self.value, skip = self.parse_literal(bin_str[self.pos:])
            self.pos += skip
            self.packets = []
        else:
            self.value = None
            self.length_type_id = bin_str[6]

            self.pos = 7
            if self.length_type_id == '0':
                subpacket_str_len_max = int(bin_str[self.pos: self.pos+15], 2)
                subpacket_str_len = 0

                self.pos += 15

                self.packets = []
                while subpacket_str_len < subpacket_str_len_max:
                    p = Packet(bin_str[self.pos:])
                    self.packets.append(p)
                    self.pos += p.pos
                    subpacket_str_len += p.pos

            elif self.length_type_id == '1':
                n_sub_packets_max = int(bin_str[self.pos: self.pos+11], 2)
                n_sub_packets = 0

                self.pos += 11

                self.packets = []
                while n_sub_packets < n_sub_packets_max:
                    p = Packet(bin_str[self.pos:])
                    self.packets.append(p)
                    self.pos += p.pos

                    n_sub_packets += 1
            else:
                raise ValueError

    def __repr__(self):
        return f'Packet(version={self.version}, id={self.id}, value={self.value},' \
               f'n_subpackets={len(self.packets)})'

    def evaluate(self):
        match self.id:
            case 0:
                return sum(p.evaluate() for p in self.packets)
            case 1:
                return prod(p.evaluate() for p in self.packets)
            case 2:
                return min(p.evaluate() for p in self.packets)
            case 3:
                return max(p.evaluate() for p in self.packets)
            case 4:
                return self.value
            case 5:
                a, b = self.packets
                return int(a.evaluate() > b.evaluate())
            case 6:
                a, b = self.packets
                return int(a.evaluate() < b.evaluate())
            case 7:
                a, b = self.packets
                return int(a.evaluate() == b.evaluate())

    @property
    def score(self):
        return self.version + sum(p.score for p in self.packets)

    @staticmethod
    def hex_to_bits(hex):
        return  ( bin(int(hex, 16))[2:] ).zfill(4 * len(hex))

    @staticmethod
    def parse_literal(bin_str):
        values = []
        for i, s in enumerate(chunked(bin_str, 5), start=1):
            cont, *val = s
            values.append(''.join(val))
            if cont == '0':
                return int(''.join(values), 2), 5 * i


p = Packet(get_input(day=16, as_list=False), in_hex=True)
print(p.score)
print(p.evaluate())
