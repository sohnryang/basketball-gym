from gym.envs.registration import register

register(
    id='basketball-v0',
    entry_point='basketball_gym.envs:BasketballEnv',
)
