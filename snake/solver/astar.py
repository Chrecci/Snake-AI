
from snake.base.pos import Pos
from snake.solver.base import BaseSolver
from snake.solver.path import PathSolver


class AStarSolver(BaseSolver):

    def __init__(self, snake):
        super().__init__(snake)
        self._path_solver = PathSolver(snake)
        print(snake.__dict__)

    def next_direc(self):
        # Create a virtual snake (s_copy) and map (m_copy)
        # print('started solver')
        s_copy, m_copy = self.snake.copy()
        # print(m_copy)
        # Step 1
        self._path_solver.snake = self.snake

        # solution to next food from a star
        path_to_food = self._path_solver.astar_path()
        # print(path_to_food)
        if path_to_food:
            return path_to_food[0]
        else:
            self.snake._dead = True
            return None
        '''
        if path_to_food:
            # Step 2
            s_copy.move_path(path_to_food)
            
            # if map is full with snake
            if m_copy.is_full():
                # print('2', path_to_food[0])
                return path_to_food[0]

            # Step 3
            self._path_solver.snake = s_copy
            path_to_tail = self._path_solver.longest_path_to_tail(short='astar')
            if len(path_to_tail) > 1:
                # print('3', path_to_food)
                return path_to_food[0]

        # Step 4 In case a-star can not generate a path
        self._path_solver.snake = self.snake
        path_to_tail = self._path_solver.longest_path_to_tail(short='astar')
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
                    direc = head.direc_to(adj)
        # print('5', direc)
        return direc
        '''