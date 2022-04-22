#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from snake.base.pos import Pos
from snake.solver.base import BaseSolver
from snake.solver.path import PathSolver


class GreedySolver(BaseSolver):

    def __init__(self, snake):
        super().__init__(snake)
        self._path_solver = PathSolver(snake)
        print(snake.__dict__)

    def next_direc(self):
        # Create a virtual snake (s_copy) and map (m_copy)
        s_copy, m_copy = self.snake.copy()
        # print(m_copy)
        # Step 1
        self._path_solver.snake = self.snake
        path_to_food = self._path_solver.shortest_path_to_food()
        # return path_to_food[0] # uncomment if you want to use only shortest path. Can trap itself
        #print(path_to_food)
        if path_to_food:
            return path_to_food[0]
        else:
            self.snake._dead = True
            return None
        # send virtual snake to eat food. After virtual snake eats, if there's a long route from head to tail stail, keep moving original path (Step 3)
        # otherwise, follow hamiltonian path (Step 4)
        '''
        if path_to_food:
            # Step 2
            s_copy.move_path(path_to_food)
            
            # if map is full with snake
            if m_copy.is_full():
                # print('2', path_to_food[0])
                return path_to_food[0]

            # Step 3 (after eating food, if longest path to tail > 1)
            self._path_solver.snake = s_copy
            path_to_tail = self._path_solver.longest_path_to_tail(short='greedy')
            if len(path_to_tail) > 1:
                # print('3', path_to_food)
                return path_to_food[0]

        # Step 4 (if currently longest path to tail > 1)
        self._path_solver.snake = self.snake
        path_to_tail = self._path_solver.longest_path_to_tail(short = 'greedy')
        if len(path_to_tail) > 1:
            # print('4', path_to_tail)
            return path_to_tail[0]

        # Step 5 (all else fails, run away from food until short path can be reached, or not in danger)
        head = self.snake.head()
        direc, max_dist = self.snake.direc, -1
        for adj in head.all_adj():
            if self.map.is_safe(adj):
                dist = Pos.manhattan_dist(adj, self.map.food)
                if dist > max_dist:
                    max_dist = dist
                    # go in direction that is furthest from food
                    direc = head.direc_to(adj)
        # print('5', direc)
        return direc
        '''