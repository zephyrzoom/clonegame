#include "block.h"

Block::Block(int width, int x, int y, int value, int speed) {
    _width = width;
    _x = x;
    _y = y;
    _value = value;
    _speed = speed;
}

void Block::move(int delta_x, int delta_y) {
    _x += delta_x;
    _y += delta_y;
}

int Block::get_x() {
    return _x;
}

int Block::get_y() {
    return _y;
}

int Block::get_width() {
    return _width;
}