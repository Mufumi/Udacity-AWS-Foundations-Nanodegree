# AWS-Deep-Racer
This is for the AWS Deep Racer tutorial

**Simulation video trial**

[![Deep Racer video trial](Screenshot (240).png)](https://user-images.githubusercontent.com/36229418/127618562-955e3c8d-3b3a-4d42-9123-7d5936e99501.mp4)
## Training configuration

The primary parameters that needed configuration in this excerise are the hyperparameters. The Deep Racer executes in a simulated environment where the virtual vehicle is the agent and the track is the environment.

### Hyperparameter Parameters

#### Gradient descent batch size

Gradient descent is an optimization algorithm often used for finding the weights or coefficients of machine learning algorithms, such as artificial neural networks and logistic regression. This [link](https://machinelearningmastery.com/gentle-introduction-mini-batch-gradient-descent-configure-batch-size/) gives a brief definition.

#### Entropy

Entropy is defined as randomness in the information being processed in your machine learning project from this [source](https://addepto.com/what-is-entropy-in-machine-learning/#:~:text=Simply%20put%2C%20entropy%20in%20machine%20learning%20is%20related,it%20means%20to%20you%20and%20your%20ML%20projects.)

#### Discount factor
 
The discount factor is a real value from 0 to 1 that cares for the rewards agent achieved in the past, present, and future-In different words, it relates the rewards to the time domain. This [article](https://towardsdatascience.com/penalizing-the-discount-factor-in-reinforcement-learning-d672e3a38ffe) describes how to optimize this parameter.

#### Loss type

For this experiment, I chose the Huber loss function. This [link](https://towardsdatascience.com/understanding-the-3-most-common-loss-functions-for-machine-learning-regression-23e0ef3e14d3) provides an overview on the three most common loss functions for Machine Learning Regression

#### Learning rate

This is a factor multiplied to the gradient descent that assists in training a ML model. A small learning rate can cause the ML model to take long to learn, whilst a large learning rate can exclude important learning steps. This [link](https://developers.google.com/machine-learning/crash-course/reducing-loss/learning-rate) describes how the learning rate can be chosen

#### Discount factor

##### Number of experience episodes between each policy-updating iteration

#### Number of epochs

### Environment simulation

**Hotrod speedway**

Performance of car is dependent on the track chose

### Reward function



### Sensors

**Lidar, Stereo camera**

### Action space

**Speed and Steering angle**

### Action space type

Choose between **continuous** and **discrete**

### Framework

**Tensorflow**

### Reinforcment Learning Algorithm

**PPO**

### 
