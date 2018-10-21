#include "scene.h"

Scene::Scene(int height, int width) {
    _width = width;
    _height = height;
}

void Scene::move_down(int distance) {
    for (Block block : _blocks) {
        if (can_move(DOWN, block)) {
            block.move(0, distance);
        }
    }
}

void Scene::move_left(int distance) {
    for (Block block : _blocks) {
        if (can_move(LEFT, block)) {
            block.move(-distance, 0);
        }
    }
}

void Scene::move_right(int distance) {
    for (Block block : _blocks) {
        if (can_move(RIGHT, block)) {
            block.move(distance, 0);
        }
    }
}

void Scene::move_up(int distance) {
    for (Block block : _blocks) {
        if (can_move(UP, block)) {
            block.move(0, -distance);
        }
    }
}

bool Scene::can_move(Direction direction, Block block) {
    
    switch (direction)
    {
        case UP: return block.get_y() <= 0 ? true : false; break;
        case RIGHT: return block.get_x() >= _width - block.get_width() ? true : false; break;
        case DOWN: return block.get_y() >= _height - block.get_width() ? true : false; break;
        case LEFT: return block.get_x() <= 0 ? true : false; break;
        default: break;
    }
}