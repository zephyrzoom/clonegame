#ifndef __SCENE_H__
#define __SCENE_H__

#include "block.h"
#include <vector>


enum Direction {UP, RIGHT, DOWN, LEFT};

class Scene {
    private:
        int _height;
        int _width;

        std::vector<Block> _blocks;

    public:
        Scene(int height, int width);

        void move_left(int distance);
        void move_right(int distance);
        void move_up(int distance);
        void move_down(int distance);

        bool can_move(Direction direction, Block block);
};

#endif __SCENE_H__