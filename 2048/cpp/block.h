#ifndef __BLOCK_H__
#define __BLOCK_H__

class Block {
    private:
    int _width;
    int _x;
    int _y;
    int _value;
    public:
    Block(int width, int x, int y, int value);
    void move(int to_x, int to_y);
};

#endif