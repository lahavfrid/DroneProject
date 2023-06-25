
#The envelope with parameters (env(......)) takes precedence over the settings, allowing for specific customization.
#However, if you prefer to create an environment using the default parameters from the settings, you can simply initiate it as env();

# obs_dict: A dictionary of (key=radius, value=num_of_agents_with_radius).
# If the total number of agent in obs_dict is greater than the number of good agents -
#   we ignore the last radiuses in the dict.
# If the total number of agent in obs_dict is smaller than the number of good agents -
#   we assume the remaining agents see all the map


obs_dict = {0: 10, 0.00001: 1}
render_mode='human' #Run without rendering using "rgb_array" insted of "human".
num_good=0          #Number of green agents
num_adversaries=1   #Number of red agents
num_obstacles=1     #Number of shadowed fields
max_cycles=1000     #Number of cycles for the simulation
num_of_possible_colors_for_agent = 3
render_object_shrinking = True  #Allow rendering to shrink when agents are out of bounds.

factor_dict = {} #The default factor for each key is 1
factor_dict["landmark_interference_factor"] = 1.0
factor_dict["lamp_improvement_factor"] = 1.0
factor_dict["shadow_interference_factor"] = 1.0
factor_dict["height_adversary_factor"] = 1.0
factor_dict["height_non_adversary_factor"] = 1.0
factor_dict["height_other_factor"] = 1.0
