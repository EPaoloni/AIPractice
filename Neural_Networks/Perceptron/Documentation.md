This project is being built to learn how to build a Perceptron, the simplest neuron we can make.

## Perceptron

A perceptron is just a neuron, it has inputs, weights for those inputs and an output.

The basic functions of a perceptron are:
1. For every input, multiply that input by its weight
2. Sum all of the weighted inputs
3. Compute the output based on that sum passed through an activation function


## Supervised Training

Once perceptron is built, we have to add the capacity to be trained.
For this, we need a known training data to feed our perceptron.

We will take a Supervised Training approach.
In order to use that approach we need to:
1. Provide the perceptron with inputs for which there is a known answer.
2. Ask the perceptron to guess an answer.
3. Compute the error. (Did it get the answer right or wrong?)
4. Adjust all the weights according to the error.
5. Return to Step 1 and repeat.


Once we initialized our perceptron with random values or with values we know should work properly,
we have to give inputs to it, then our perceptron will return an output and we will evaluate it.

For example, if we are waiting a value to be 1 or -1, we can use the following formula:
```python
error = answer - guess 
```
If our variable `error` ends up with a value of 0, so the guess will be wrong.

If the guess is right we don't need to do anything, but if the guess is wrong we have to adjust the weights of the inputs.
We will make use of a `Gradient Descent`, which consists in using the difference between the result we got from our perceptron and the right answer.
We can use the following formula:
```python
new_weight = actual_weight - delta_weight
```
Where `delta_weight` is the variable which we talked about previously.

Taking in mind that a single case is not as important to modify our trained perceptron so drastically, we add a `Learning Rate` to our `new_weight` formula,
making each particular value less important in order to prioritize the most cases.
```python
new_weight = actual_weight - delta_weight * learning_rate
```
And for example, our `Learning Rate` could be 0.1

We have to modify the perceptron's weights in order to adjust them for the following data set, and the following guess.
Finally, when our perceptron had been trained, we can use it in a real case with weights it had calculated when being trained.

