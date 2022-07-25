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

### Deterministic vs Stochastic Policies

- Deterministic policies are one in which the agent takes the best possible action everytime.
- Stochastic policies are one in which the agent can take different action based on the probability of each action. These probabilities are dependant upon the expected value from each return.
  
It is better to use stochastic policies for training as it allows for exploration.

### Q-Learning

<br/>
- Exploration vs Exploitation
- Epsilon Greedy Strategy to choose between exploitation and exploration
- Weighted sum along with learning rate in order to update q values and then get the optimal policy.

<br/>

### Deep Q Learning

<br/>
- DQN networks are usually Convolutional Layers and Dense Layers.
- We use a bunch of sequential snapshots from the game and feed it into the network as a state. The network then outputs the optimal q-value.
- Two forward passes are before doing a gradient update. (One for current state and one for next state)
- Next state value is used as comparison to compute.
- To avoid targets and estimates fromc hasing each other in an unstable way, we freeze the weights for the second pass in a "cloned" network (target network) of the "policy network"
- This is done a for 'x' number of timestamps and x is another hyperparameter. 
