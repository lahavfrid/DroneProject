# Importing the CustomAgents module
from CustomAgents import *
from Auxiliry import *

# obs_dict: A dictionary of (key=radius, value=num_of_agents_with_radius).
# If the total number of agent in obs_dict is greater than the number of good agents -
#   we ignore the last radiuses in the dict.
# If the total number of agent in obs_dict is smaller than the number of good agents -
#   we assume the remaining agents see all the map

# Note: The radiuses values are in the range [0, 2]

# Factors dictionary that contains some factors used in the environment -

# There are 2 ways to initialize the environment:

# 1. Empty Constructor (Parameters from Setting File)
#    - Initialize the environment using an empty constructor.
#    - Read parameters from a settings file with predefined values.
#    - Allows easy configuration without modifying the code directly.
env = simple_tag_v3.env()

# 2. Parameter Constructor
#    - Initialize the environment by directly passing parameters to the constructor.
#    - Parameters include render mode, agent and adversary counts, obstacle count, maximum cycles,
#      observation and factor dictionaries, and possible agent colors.
#    - Provides flexibility and customization for specific requirements or dynamic conditions.

env = simple_tag_v3.env(
    render_mode='human',
    num_drones=2,
    num_parasites=2,
    num_obstacles=1,
    max_cycles=10000,
    num_of_possible_colors_for_agent=4,
    lamp_flag=True,
    height_flag=True,
    landmark_colide=False,
    no_dead_flag=True,
    max_hit_drone=2,
    max_hit_parasite=1,
    render_object_shrinking = False,
    out_of_bounds_reward=False


)
'''
env = simple_tag_v3.single_env(
    parasite_policy = staticAgent,
    drone_policy = staticAgent,
    render_mode='human',
    num_drones=5,
    num_parasites=5,
    num_obstacles=1,
    max_cycles=1000,
    num_of_possible_colors_for_agent=4,
    lamp_flag=True,
    height_flag=True,
    landmark_colide=False,
    no_dead_flag=False,
    max_hit_drone=1,
    max_hit_parasite=1,
    render_object_shrinking = False,
    out_of_bounds_reward=False

)
'''
# Prints the actions the agent can perform
print_action_dict(env)

# Reset the environment and get initial observation, reward, termination, truncation, and info
env.reset()
observation, reward, termination, truncation, info = env.last()

# user_input = 0
# while user_input!='Q' and user_input!="q":
#     env.step(int(user_input))
#     print(env.observe())
#     user_input = input()

policy_dic={}
policy_dic["adversary_0"]=staticAgent
policy_dic["adversary_1"]=chaseParasiteAgent
policy_dic["agent_1"]=escapeFromDronesAgent

run_env_multi_policy(env, policy_dic)

# Close the environment
env.close()

# Reset the environment and get initial observation, reward, termination, truncation, and info
env.reset()
observation, reward, termination, truncation, info = env.last()
