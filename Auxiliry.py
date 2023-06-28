from CustomAgents import *

def run_env(env, drone_policy=greedyAgent,parasite_policy=staticAgent):
    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()
        # Check if the episode is terminated or truncated
        print(observation)
        if termination or truncation:
            action = None

        else:
            # If the agent is a parasite, use its given policy
            if observation[1] == False:
                action = parasite_policy(observation, env, agent)
            else:
                # else, use the drone policy
                action = drone_policy(observation, env, agent)

        # Perform the chosen action in the environment
        env.step(action)
