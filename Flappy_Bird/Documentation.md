This project uses different approaches for building an AI to beat the game Flappy Bird.

The game was built taking as model the one coded by youtube user "Tech With Tim", whose series starts with the following video:
https://www.youtube.com/watch?v=MMxFDaIOHsE

It is a bit sophisticated but not extremely complex.

Then, I started learning which kind of approach you could use to build an AI for Flappy Bird.

I've started developing my AI using as example the one built by youtube user "The Coding Train" (Daniel Shiffman). He uploaded five videos for this, starting with:
https://www.youtube.com/watch?v=c6y21FkaUqw

As a curious fact, he loves JavaScript, so the game and AI are built in that language, but despite I know so little about python, I love it, so I'm building my AI with it.

He develops a Neuroevolutive approach, giving the neural network to the bird.
This approach consists in building random birds(in this case) and call it a generation.
We will get the best bird from the initial generation, that will be the one which gets the best score.
Then we take the Neurons from that bird, and we start a new generation from that neuron, we build new random birds and again, we take the best and start another generation.


We need to define the inputs, the hidden nodes and the outputs, as in any neural network.

As inputs, Daniel decided to take:
    The Y position of the bird.
    The Y velocity of the bird. # This one ended up being the most important input. It shows the importance of choosing the right inputs.
    The X position of the left side of the pipes.
    The Y position of the bottom of the upper pipe.
    The Y position of the top of the lower pipe.

As outputs, we will have only one:
    A number from 0 to 1 that in its first half represents not jumping and in its second half represents jumping.
    (I don't like this idea too much, I would prefer to have two outputs, but for practicing I think it's ok)

As hidden nodes, we could have none of them, but we will have four of them just for having a hidden layer.
