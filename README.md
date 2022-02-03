# AWS-Deep-Racer
This is for the AWS Deep Racer tutorial

**Simulation video trial**

[![Deep Racer video trial](Screenshot (240).png)](https://user-images.githubusercontent.com/36229418/127618562-955e3c8d-3b3a-4d42-9123-7d5936e99501.mp4)
## Training configuration

The primary parameters that needed configuration in this excerise are the hyperparameters. The Deep Racer executes in a simulated environment where the virtual vehicle is the agent and the track is the environment. The [concepts and terminology](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-basic-concept.html) describe how each variable in the simulation affects the output. Some of the parameters configured in the simulation include:

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

This is a factor multiplied to the gradient descent that assists in training a ML model. A small learning rate can cause the ML model to take long to learn, whilst a large learning rate can exclude important learning steps. This [link](https://developers.google.com/machine-learning/crash-course/reducing-loss/learning-rate) describes how the learning rate can be chosen.

#### Experience iteration 
Also known as the number of experience episodes between each policy-updating iteration, is a set of consecutive experiences between each policy iteration that performs updates of the policy network weights. At the end of each experience iteration, the collected episodes are added to an experience replay or buffer. The size can be set in one of the hyperparameters for training. The neural network is updated by using random samples of the experiences.  For this 

#### Number of epochs

An [epoch](https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9) is defined as the complete passing of an entire dataset through a neural network both through its feedforwarf and feedback networks. A conservative choice of 10 epochs was chosen for this experiment.

### Environment simulation

The **Hotrod speedway** was chosen as the environment the agent was going to be trained in. This is important because the performance of the car is dependent on the track chosen. An algorithm can be tuned optimally but if the agent is trained in the wrong environment, its performance will degrade drastically

### Reward function

A simple reward function was chosen for this vehicle. It considered the track width as well as the distance from the centre to allocate the reward.

<p align="center">
  <img width="1000" src="https://github.com/Mufumi/Udacity-AWS-Foundations-Nanodegree/blob/main/Reward_function.png">
</p>

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
