#ifndef __SCENE_H__
#define __SCENE_H__

#include "block.h"
#include <vector>

class Scene {
    private:
        int _height;
        int _weight;

        std::vector<Block> _blocks;

    public:
        Scene();

        void move_left();
        void move_right();
        void move_up();
        void move_down();
};

#endif __SCENE_H__