#include "block.h"

Block::Block(int width, int x, int y, int value) {
    _width = width;
    _x = x;
    _y = y;
    _value = value;
}

void Block::move(int to_x, int to_y) {
    _x = to_x;
    _y = to_y;
}