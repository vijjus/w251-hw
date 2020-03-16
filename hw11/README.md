# OpenAI Lunar Lander on TX2 #

I trained 4 different models for the Lunar Lander. From reading the OpenAI info about the lander, as well as the code that was
provided, I concluded that the model is a function approximation of the Q-function in Reinforcement Learning. 

Given some input parameters such as the current location of the lander, the location of the flags etc, the output is the 
firing strength of the three thrusters on the lander - the left & right thruster and the thruster at the bottom.

From the OpenAI page:

"Landing pad is always at coordinates (0,0). Coordinates are the first two numbers in state vector. Reward for moving from the top of the screen to landing pad and zero speed is about 100..140 points. If lander moves away from landing pad it loses reward back. Episode finishes if the lander crashes or comes to rest, receiving additional -100 or +100 points. Each leg ground contact is +10. Firing main engine is -0.3 points each frame. Solved is 200 points. Landing outside landing pad is possible. Fuel is infinite, so an agent can learn to fly and then land on its first attempt. Four discrete actions available: do nothing, fire left orientation engine, fire main engine, fire right orientation engine."

The videos of my lander are available at:
https://cloud.ibm.com/classic/storage/cloudobjectstorage/details#accountId=117794020


The inputs to the model are the previous state and the previous actions and the predicted value is the expected reward.

```
new_s, r, done, info = env.step(a)
X_train.append(list(prev_s)+list(a))
y_train.append(r)
```

## First Model ##



## LSTM Model ##

The 2nd model I tried was an LSTM. I did not expect this to do well considering the Markov process nature of the lander. Still, I wanted to try it out. LSTMs are good at memorizing time-ordered sequences, but RL problems involve an element of exploration (randomness).

```
def nnmodel(input_dim):
    model = Sequential()
    model.add(Embedding(input_dim, output_dim=256))
    model.add(LSTM(128))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['accuracy'])
    return model
```

The model kept getting large negative rewards and did not stabilize:

```
At step  39200
reward:  -19.119696257117546
total rewards  -76.58782955278734
[-0.37272105  0.05031176  0.02500752 -1.29804919 -0.2916303  -8.211586
  1.          1.        ]
At step  39300
reward:  -4.602075165013157
total rewards  -495.5043010659387
[ 0.24777851  0.16582585  0.6047049  -2.29378721 -0.26215288 -0.12728294
  0.          0.        ]
[ 0.55060596 -0.15955459  0.71787198 -0.37426138 -0.87366438  1.22325603
  0.          0.        ]
At step  39400
reward:  -12.727794084284142
total rewards  -458.4066109845098
[-0.39780068  0.41739188 -1.4026734  -1.96521695  0.55627739  0.24957081
  0.          0.        ]
[-2.71671152e-01 -3.80865033e-02 -7.52154589e-01 -6.90789488e-02
  1.37162447e-01  1.08349339e-06  1.00000000e+00  1.00000000e+00]
  ```
  
## DQN (FC) MODEL ##

Based on some research, I tried a deep FC model using __mean squared error__ as the loss function, __Adam__ as the optimizer and __accuracy__ as the evaluation metric. The learning rate was left as default for Adam (0.001).

```
def nnmodel(input_dim):
    model = Sequential()
    model.add(Dense(150,input_dim=input_dim, activation='relu'))
    model.add(Dense(120, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mean_squared_error', optimizer='Adam', metrics=['accuracy'])
    return model
 ```

  This model did much better, and completed full training (50000 steps) with a final loss value of around 84.
  
  ```
  Epoch 1/10
50001/50001 [==============================] - 53s 1ms/step - loss: 86.8118 - accuracy: 2.0000e-05
Epoch 2/10
50001/50001 [==============================] - 52s 1ms/step - loss: 85.5763 - accuracy: 1.4000e-04
Epoch 3/10
50001/50001 [==============================] - 52s 1ms/step - loss: 85.3613 - accuracy: 3.9999e-05
Epoch 4/10
50001/50001 [==============================] - 53s 1ms/step - loss: 85.8569 - accuracy: 5.9999e-05
Epoch 5/10
50001/50001 [==============================] - 50s 991us/step - loss: 85.4071 - accuracy: 0.0000e+00
Epoch 6/10
50001/50001 [==============================] - 51s 1ms/step - loss: 84.2696 - accuracy: 3.9999e-05
Epoch 7/10
50001/50001 [==============================] - 51s 1ms/step - loss: 84.6792 - accuracy: 3.9999e-05
Epoch 8/10
50001/50001 [==============================] - 49s 983us/step - loss: 85.4104 - accuracy: 7.9998e-05
Epoch 9/10
50001/50001 [==============================] - 51s 1ms/step - loss: 84.1705 - accuracy: 7.9998e-05
Epoch 10/10
50001/50001 [==============================] - 52s 1ms/step - loss: 84.3791 - accuracy: 1.2000e-04
```

## Deeper QN MODEL ##

Inspired by the above, I increased the number of layers of my next model, and also experimented with __Adamax__ as the optimizer. I kept the other parameters the same for an easier comparison. I also tried the __Adam__ optimzer with this network, and emperically the Adam optimizer did slightly better.


```
def nnmodel(input_dim):
    model = Sequential()
    model.add(Dense(256,input_dim=input_dim, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mean_squared_error', optimizer='Adam', metrics=['accuracy'])
    return model
```

This model achieved a final loss on Adamax of about 77.

```
Epoch 1/10
50001/50001 [==============================] - 52s 1ms/step - loss: 77.6528 - accuracy: 5.9999e-05
Epoch 2/10
50001/50001 [==============================] - 54s 1ms/step - loss: 77.6306 - accuracy: 1.4000e-04
Epoch 3/10
50001/50001 [==============================] - 53s 1ms/step - loss: 77.8893 - accuracy: 1.2000e-04
Epoch 4/10
50001/50001 [==============================] - 55s 1ms/step - loss: 78.4142 - accuracy: 5.9999e-05
Epoch 5/10
50001/50001 [==============================] - 53s 1ms/step - loss: 77.1695 - accuracy: 1.2000e-04
Epoch 6/10
50001/50001 [==============================] - 52s 1ms/step - loss: 76.5805 - accuracy: 9.9998e-05
Epoch 7/10
50001/50001 [==============================] - 50s 1ms/step - loss: 77.9907 - accuracy: 1.6000e-04
Epoch 8/10
50001/50001 [==============================] - 52s 1ms/step - loss: 75.9157 - accuracy: 7.9998e-05
Epoch 9/10
50001/50001 [==============================] - 52s 1ms/step - loss: 76.0946 - accuracy: 5.9999e-05
Epoch 10/10
50001/50001 [==============================] - 52s 1ms/step - loss: 76.9765 - accuracy: 7.9998e-05
```

The same network reached a loss of 67 with Adam.

```
Epoch 1/10
41001/41001 [==============================] - 48s 1ms/step - loss: 68.4308 - accuracy: 0.0000e+00
Epoch 2/10
41001/41001 [==============================] - 48s 1ms/step - loss: 68.0737 - accuracy: 2.4390e-05
Epoch 3/10
41001/41001 [==============================] - 50s 1ms/step - loss: 70.4720 - accuracy: 7.3169e-05
Epoch 4/10
41001/41001 [==============================] - 48s 1ms/step - loss: 67.5865 - accuracy: 1.4634e-04
Epoch 5/10
41001/41001 [==============================] - 46s 1ms/step - loss: 68.5847 - accuracy: 2.4390e-05
Epoch 6/10
41001/41001 [==============================] - 47s 1ms/step - loss: 67.1972 - accuracy: 4.8779e-05
Epoch 7/10
41001/41001 [==============================] - 47s 1ms/step - loss: 68.0167 - accuracy: 4.8779e-05
Epoch 8/10
41001/41001 [==============================] - 48s 1ms/step - loss: 68.0358 - accuracy: 1.2195e-04
Epoch 9/10
41001/41001 [==============================] - 48s 1ms/step - loss: 70.4617 - accuracy: 4.8779e-05
Epoch 10/10
41001/41001 [==============================] - 47s 1ms/step - loss: 67.2684 - accuracy: 4.8779e-05
```


