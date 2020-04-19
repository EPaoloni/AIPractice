This project uses different approaches for building an AI to beat the game Flappy Bird.

I will be updating this document with info from my research and results from my experimentation.

The game was built taking as model the one coded by youtube user "Tech With Tim", whose series starts with the following video:
https://www.youtube.com/watch?v=MMxFDaIOHsE

It is a bit sophisticated but not extremely complex.

Then, I started learning which kind of approach you could use to build an AI for Flappy Bird.

## Neuroevolution of Augmenting topologies

First of all the concept I am going to use is NEAT (Neuroevolution of Augmenting topologies), it consists in making generations of AI. An excellent introduction to this topic can be found on youtube, from user "The Coding Train" (Daniel Shiffman), starting with: 
https://www.youtube.com/watch?v=9zfeTw-uFCw&list=PLRqwX-V7Uu6bJM3VgzjNV5YxVxUwzALHV

This concept is based on natural selection.
We need to achieve three key principles:
  * Heredity:
    There must be a process in place by which children receive the properties of their parents.
  * Variation:
    There must be a variety of traits present in the population or a means with which to introduce variation.
  * Selection:
    There must be a mechanism by which some members of a population have the opportunity to be parents and pass down their genetic information and some do not. This is typically referred to as "survival of the fittest".

The steps for building a NEAT AI approach are:
  1. Create a population of N elements
  2. Calculate fitness for N elements
  3. Reproduction / Selection
    1. Pick some parents
    2. Make a new element
      * Crossover
      * Mutation
  4. Start over with a new generation from the new element

### Fitness function

We must think about the best fitness function for our problem.
If we just use a linear function, when our parameters used for calculating the fitness gets bigger and bigger, the difference between two high developed neurons will be tiny and when we have to choose a neuron to evolve it could be the less developed.

So, for example, we could use an exponential function to make the difference between values more and more important as the fitness parameters get higher ones.

For genetic algorithms, we use fitness as a probability of the neural network of being picked to create another generation

### Pool selection based on fitness



## Neuroevolutional approach with a neural network developed by me

I've started developing my AI using as example the one built by youtube user "The Coding Train". He uploaded five videos for this, starting with:
https://www.youtube.com/watch?v=c6y21FkaUqw

As a curious fact, he loves JavaScript, so the game and AI are built in that language, but despite I know so little about python, I love it, so I'm building my AI with it.

He develops a Neuroevolutive approach, giving the neural network to the bird.
This approach consists in building random birds(in this case) and call it a generation.
We will get the best bird from the initial generation, that will be the one which gets the best score. The best score is set evaluating the fitness of every singular bird, according to their distance traveled.
Then we take the Neurons from that bird, and we start a new generation from that neuron, we build new random birds and again, we take the best and start another generation.
Whenever a bird from a generation is picked to start a new generation, we have to give that new generation a mutation rate.
That rate gives some randomness to those birds, what allows them to improve from what the previous best generation bird learnt.

We need to define the inputs, the hidden nodes and the outputs, as in any neural network.

As inputs, Daniel decided to take:
  * The Y position of the bird.
  * The Y velocity of the bird. # This one ended up being the most important input. It shows the importance of choosing the right inputs.
  * The X position of the left side of the pipes.
  * The Y position of the bottom of the upper pipe.
  * The Y position of the top of the lower pipe.

As outputs, we will have only one:
    A number from 0 to 1 that in its first half represents not jumping and in its second half represents jumping.
    (I don't like this idea too much, I would prefer to have two outputs, but for practicing I think it's ok)

As hidden nodes, we could have none of them, but we will have four of them just for having a hidden layer.


Daniel made several changes, like a slider to make game go faster, saving the best bird and adding the possibility to load a saved bird, and other improvements.

He managed to beat the game in 7 generations.

## Neuroevolution approach with tensorflow