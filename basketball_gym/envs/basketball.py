import gym
import numpy as np

from gym import error, spaces, utils
from gym.utils import seeding

class BasketballEnv(gym.Env):
    """
    This class implements single play mode of basketball gym.

    Observations
    ------------
    Type: Box(6)

    === ================
    Num Observation
    --- ----------------
    0   Ball position
    1   Player X coord
    2   Player Y coord
    3   Opponent X coord
    4   Opponent Y coord
    5   Penalty
    === ================

    Actions
    -------
    Type: Discrete(5)

    === ====================
    Num Action
    --- --------------------
    0   Move player forward
    1   Move player backward
    2   Move player left
    3   Move player right
    4   Shoot the ball
    === ====================

    Reward
    ------
    Reward is 10 when the player scores, and -10 if the opponent scores.
    Also, player gets 1 when it gets the ball, and -1 if it loses it.

    Starting State
    --------------
    === =====
    Num Value
    --- -----
    0       0
    1     125
    2      80
    3     125
    4     320
    5       0
    === =====

    Episode Termination
    -------------------
    Penalty is bigger than 1000
    If opponent scores, penalty increases by 10.
    If opponent steals the ball, penalty increases by 1.
    """

    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 50,
    }

    def __init__(self):
        self.viewer = None
        self.state = None
        self.PLAYER_SIZE = 16

    def rect_coords(self, pos):
        return [
            (pos[0] - self.PLAYER_SIZE / 2, pos[1] - self.PLAYER_SIZE / 2),
            (pos[0] + self.PLAYER_SIZE / 2, pos[1] - self.PLAYER_SIZE / 2),
            (pos[0] + self.PLAYER_SIZE / 2, pos[1] + self.PLAYER_SIZE / 2),
            (pos[0] - self.PLAYER_SIZE / 2, pos[1] + self.PLAYER_SIZE / 2),
        ]

    def player_coords(self):
        return self.rect_coords((self.state[1], self.state[2]))

    def opponent_coords(self):
        return self.rect_coords((self.state[3], self.state[4]))

    def step(self, action):
        pass

    def reset(self):
        self.state = np.array([0, 125, 80, 125, 320, 0])

    def render(self, mode='human'):
        screen_width = 250
        screen_height = 400
        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)
            upper_goal = rendering.FilledPolygon([
                (110, 0),
                (140, 0),
                (140, 30),
                (110, 30),
            ])
            upper_goal.set_color(0.5, 0.5, 0.5)
            lower_goal = rendering.FilledPolygon([
                (110, 400),
                (140, 400),
                (140, 370),
                (110, 370),
            ])
            lower_goal.set_color(0.5, 0.5, 0.5)
            self.viewer.add_geom(upper_goal)
            self.viewer.add_geom(lower_goal)
            player = rendering.FilledPolygon(self.player_coords())
            self.player_trans = rendering.Transform()
            player.add_attr(self.player_trans)
            player.set_color(0, 0.5, 0)
            self.viewer.add_geom(player)
            opponent = rendering.FilledPolygon(self.opponent_coords())
            self.opponent_trans = rendering.Transform()
            opponent.add_attr(self.opponent_trans)
            opponent.set_color(1, 0, 0)
            self.viewer.add_geom(opponent)
            half_line = rendering.Line(start=(0, 200), end=(250, 200))
            half_line.set_color(0, 0, 0)
            self.viewer.add_geom(half_line)
        return self.viewer.render(return_rgb_array=mode=='rgb_array')

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None
