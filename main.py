from pettingzoo.mpe import simple_tag_v3

# obs_dict: A dictionary of (key=radius, value=num_of_agents_with_radius).
# If the total number of agent in obs_dict is greater than the number of good agents -
#   we ignore the last radiuses in the dict.
# If the total number of agent in obs_dict is smaller than the number of good agents -
#   we assume the remaining agents see all the map

# Note: The radiuses values are in the range [0, 2]
my_obs_dict = {10: 2, 5: 2}
factors = {"height_adversary_factor": 0}
env = simple_tag_v3.env(render_mode='human', num_good=1, num_adversaries=1, num_obstacles=1, max_cycles=1000,\
                        obs_dict=my_obs_dict, factor_dict = factors)

env.reset()
observation, reward, termination, truncation, info = env.last()
# The observation is a list of positions the first agent can observe (according to the radius).

print(observation)
for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        action = None
    else:
        action = env.action_space(agent).sample()  # this is where you would insert your policy
    print(action, observation)

    env.step(action)
env.close()

# from ray.tune.registry import register_env
# # import the pettingzoo environment
# from pettingzoo.butterfly import prison_v3
# # import rllib pettingzoo interface
# from ray.rllib.env import PettingZooEnv
# # define how to make the environment. This way takes an optional environment config, num_floors
# env_creator = lambda config: prison_v3.env(render_mode=config.get("render_mode", 'human'))
# # register that way to make the environment under an rllib name
# register_env('simple_tag', lambda config: PettingZooEnv(env_creator(config)))
# # now you can use `prison` as an environment
# # you can pass arguments to the environment creator with the env_config option in the config
# config['env_config'] = {"render_mode": 'human'}