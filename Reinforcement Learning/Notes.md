### Markov Decision Process(MDP)

<br/>

- Environment
- Agent
- States
- Actions
- Rewards


Each next action and reward has a transition probability.

<br/>

- Return - Sum of all future rewards
- Expected return drives the agent's actions
- Discounted rate for tasks makes the agent care more about the immediate reward than the future ones

<br/>

- Policy - function that maps the probability of choosing a specific action in a specific state
- Value functions - How good is it to be in a specific state for a policy
- Action value function - How good is it for an agent to take an action while following some policy.
- Q function and Q values: Q -> quality.


<br/>

- Optimal state value function - Largest expected return achievable by any policy for a state
- Optimal action value function - Largest expected return for any policy for a state-action pair.
- Bellman optimality equations

<br/>

### Q-Learning

<br/>
- Exploration vs Exploitation
- Epsilon Greedy Strategy to choose between exploitation and exploration
- Weighted sum along with learning rate in order to update q values and then get the optimal policy.
