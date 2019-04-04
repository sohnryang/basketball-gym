import gym
import numpy as np

from gym import error, spaces, utils
from gym.utils import seeding

class BasketballEnv(gym.Env):
    """
    A basketball simulation.
    """
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 50,
    }

    def __init__(self):
        self.viewer = None

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        screen_width = 250
        screen_height = 400
        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)
            rect = rendering.FilledPolygon([(0, 0), (250, 0), (0, 400)])
            self.viewer.add_geom(rect)
        return self.viewer.render(return_rgb_array=mode=='rgb_array')

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None
