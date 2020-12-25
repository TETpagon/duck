from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2


class DontCrushDuckieTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        condition = True
        while condition:
            obs, reward, done, info = env.step([1, 0])
            img = np.ascontiguousarray(obs)

            # Выделяем пиксели желтых и оранжевых оттенков
            yellow_pixels = cv2.inRange(img, (150, 150, 0), (255, 255, 150))

            # Считаем количество пикселей с желтыми и оранжевым оттенками
            amount = cv2.countNonZero(yellow_pixels)

            # Если на картинке больше 20000 пикселей желтого и оранжевого оттенков, то перестаем ехать
            condition = amount < 20000

            env.render()
