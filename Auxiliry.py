from CustomAgents import *

def run_env(env, drone_policy=chaseParasiteAgent,parasite_policy=staticAgent):
    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()
        
        # Check if the episode is terminated or truncated
        if not observation[3]:
            print(agent)
            print(observation)
        if termination or truncation:
            action = None

        else:
            # If the agent is a parasite, use its given policy
            if observation[0] == False:
                action = parasite_policy(observation, env, agent)
            else:
                # else, use the drone policy
                action = drone_policy(observation, env, agent)

        # Perform the chosen action in the environment
        env.step(action)

def run_env_single(env,single_agent_policy,drone_policy=chaseParasiteAgent,parasite_policy=staticAgent):
    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()
        # Check if the episode is terminated or truncated
        if not observation[3]:
            print(agent)
            print(observation)
        if termination or truncation:
            action = None

        else:
            # If the agent is a parasite, use its given policy
            if agent=='adversary_0':
                action=single_agent_policy(observation, env, agent)
                env.step(action)
                continue

            if observation[0] == False:
                action = parasite_policy(observation, env, agent)
            else:
                # else, use the drone policy
                action = drone_policy(observation, env, agent)

        # Perform the chosen action in the environment
        env.step(action)


def run_env_multi_policy(env,policy_dict, default_drone = staticAgent, default_parasite = staticAgent):
    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()

        # Check if the episode is terminated or truncated
        if not observation[3]:
            print(agent)
            print(observation)
        if termination or truncation:
            action = None

        else:
            if agent in policy_dict:
                action=policy_dict[agent](observation,env,agent)

            # If the agent is a parasite, use its given policy
            elif observation[0] == False:
                action = default_parasite(observation, env, agent)
            else:
                # else, use the drone policy
                action = default_drone(observation, env, agent)

        # Perform the chosen action in the environment
        env.step(action)


def print_action_dict(env):
    print(("0", "stay in place"))
    print(("1", "move left"))
    print(("2", "move right"))
    print(("3", "move down"))
    print(("4", "move up"))
    for item in [(item[0], item[1][1]) for item in env.env.world.action_dict.items()]:
        print(item)

