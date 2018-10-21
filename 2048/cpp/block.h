#ifndef __BLOCK_H__
#define __BLOCK_H__

class Block {
    private:
        int _width;
        int _x;
        int _y;
        int _value;
        int _speed;
    public:
        Block(int width, int x, int y, int value, int speed);
        void move(int delta_x, int delta_y);

        int get_x();
        int get_y();
        int get_width();
};

#endif