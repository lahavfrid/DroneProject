
#The envelope with parameters (env(......)) takes precedence over the settings, allowing for specific customization.
#However, if you prefer to create an environment using the default parameters from the settings, you can simply initiate it as env();

# obs_dict: A dictionary of (key=radius, value=num_of_agents_with_radius).
# This dictionary helps set the observation radius for each agent.
# If the total number of agent in obs_dict is greater than the number of good agents -
#   we ignore the last radiuses in the dict.
# If the total number of agent in obs_dict is smaller than the number of good agents -
#   we assume the remaining agents see in a radius of 2.
obs_dict = {0: 10, 0.00001: 1}

render_mode='human' #Run without rendering using "rgb_array" insted of "human".
num_good=0          #Number of green agents
num_adversaries=1   #Number of red agents
num_obstacles=1     #Number of shadowed fields
max_cycles=1000     #Number of cycles for the simulation
num_of_possible_colors_for_agent = 3
render_object_shrinking = True  #Allow rendering to shrink when agents are out of bounds.

factor_dict_default = {} #  The default factor for each parameter is 1
                         #  The factors are multiplied by the observation radius, so it's recommended
                         #  to give values that are lower than 1 for interference factors,
                         #  and values that are higher than 1 for improvement factors.

# landmark_interference_factor - Used when an agent is inside a landmark (shadow).
factor_dict_default["landmark_interference_factor"] = 1.0

# lamp_improvement_factor - Used when an agent is lighting a lamp (not necessarily inside a shadow).
factor_dict_default["lamp_improvement_factor"] = 1.0

# shadow_interference_factor - Used when an agent is lighting a lamp (not necessarily inside a shadow).
factor_dict_default["shadow_interference_factor"] = 1.0

# height_adversary_factor - Used when an agent is in high height, and he's seeing an adversary.
factor_dict_default["height_adversary_factor"] = 1.0

# height_non_adversary_factor - Used when an agent is in high height, and he's seeing a non-adversary.
factor_dict_default["height_non_adversary_factor"] = 1.0

# height_other_factor - Used when an agent is in low height, and he's seeing an adversary in high height.
factor_dict_default["height_other_factor"] = 1.0
