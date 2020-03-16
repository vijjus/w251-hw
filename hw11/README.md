# Lunar Lander on TX #

I trained 4 different models for the Lunar Lander. From reading the OpenAI info about the lander, as well as the code that was
provided, I concluded that the model is a function approximation of the Q-function in Reinforcement Learning. 

Given some input parameters such as the current location of the lander, the location of the flags etc, the output is the 
firing strength of the three thrusters on the lander - the left & right thruster and the thruster at the bottom.

From the OpenAI page:

"Landing pad is always at coordinates (0,0). Coordinates are the first two numbers in state vector. Reward for moving from the top of the screen to landing pad and zero speed is about 100..140 points. If lander moves away from landing pad it loses reward back. Episode finishes if the lander crashes or comes to rest, receiving additional -100 or +100 points. Each leg ground contact is +10. Firing main engine is -0.3 points each frame. Solved is 200 points. Landing outside landing pad is possible. Fuel is infinite, so an agent can learn to fly and then land on its first attempt. Four discrete actions available: do nothing, fire left orientation engine, fire main engine, fire right orientation engine."


