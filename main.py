from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2


class DontCrushDuckieTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        # getting the initial picture
        obs, _, _, _ = env.step([0, 0])
        # convect in for work with cv
        img = cv2.cvtColor(np.ascontiguousarray(obs), cv2.COLOR_BGR2RGB)

        # add here some image processing
        print(img)

        condition = True
        while condition:
            condition = True

            obs, reward, done, info = env.step([1, 0])
            print(reward)
            img = cv2.cvtColor(np.ascontiguousarray(obs), cv2.COLOR_BGR2RGB)

            if reward < 65:
                condition = False
                obs, reward, done, info = env.step([0, 0])

            # add here some image processing
            env.render()

