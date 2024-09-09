# Exercise 03: Convolutional Neural Networks & Hyperoptimisation

<!---
ITU KSADMAL1KU-NLP - Advanced Machine Learning for NLP in KCS 2024

by Stefan Heinrich, Bertram Højer, Christian H. Rasmussen, & material by Kevin Murphy.

All info and static material: https://learnit.itu.dk/course/view.php?id=3024579
--->


## Optional revision task 1: Understanding filters for CNNs

Go through the notebook *E03_filters.ipynb* (in [Colab](https://colab.research.google.com/drive/1Kk0jiuwVGAtmLC0iwHUX9FLrnM5U9UwT)) and refresh your basic understanding of how filters work. 


## Task 2: Practising applying a CNN to image data and visualising basic results

The goal of this exercise is to expand your understanding of implementing neural network architectures and training methods in the tensorflow or pytorch frameworks, and on the way, get to know interesting tasks and datasets as well as practising visualisation options. In particular, we look into CIFAR10 in order to get a better insight into building up a filter hierarchy with CNNs.

For this exercise, you can use the prepared stub *E03_cnn_mnist_pytorch.ipynb* (or in [Colab](https://colab.research.google.com/drive/1n8CDZTrTkwfhJuJRFwxxljb7FfcLoafI)). Alternatively, reuse and reimplement the data loading in a tensorflow implementation if you prefer this framework - this is highly recommended.

1. Have a brief read-up on the CIFAR10 dataset: https://www.cs.toronto.edu/~kriz/cifar.html

2. Plot some data characteristics (samples, class distributions, or anything that you find useful to understand the data better). What is your most peculiar observation?

3. Reimplement a CNN for classification as you have seen in task 2.4 with the MLP (feel free to copy+paste from there or online sources, as long as you understand what you are doing). Is the CNN better than the previously trained MLP? What differences in results have you found?

4. Plot some training progress (loss and accuracy). Plot some model analyses (confusion matrix and accuracy on the test dataset). Are there classes that are difficult to classify correctly?

5. Optional expert sub-task: if you chosen the PyTorch path, then redo the exercise by implementing a CNN in tensorflow, otherwise redo the exercise in Pytorch.


## Optional task 3: Exploring monitoring tools and ML Ops

Now we expand our tool set for monitoring training and analysing trained models. For this, let's look into available monitoring tools and MLops.
- Join our live coding session (will be done on *AML4KCS2024-NLP-E03-Intro-logging-WnB.ipynb* (or see in [Colab](https://colab.research.google.com/drive/176gesf_IcQsyH4nqD9-bzfS2FkfCrOQ7)) )
- Read into the introductions and APIs of Tensorflow (https://www.tensorflow.org/tensorboard), Weights & Biases (https://docs.wandb.ai), Neptuni.ai, and guild.ai. What advantages and disadvantages can you find? Can you recognise different use cases for the different tools?
- Have a brief search of additional monitoring tools and MLops frameworks and share and discuss them in your group.


## Task 4: Performing a hyperparameter search on the CNN for image data

Now take your solution from task 3.2 and investigate it with the help of tensorboard OR weights&biases

1. Add Weights&Biases or Tensorboard solution for task 3.2. You might want to check a tutorial for your use case:
   - https://docs.wandb.ai/guides/integrations/pytorch
   - https://docs.wandb.ai/guides/integrations/tensorflow
   - https://www.tensorflow.org/tensorboard/get_started
   - https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html 

2. Optional expert sub-task: integrate both Weights&Biases or Tensorboard into your solution and compare both in the following task.

3. Conduct an experiment with different settings for the hyperparameters: batch_size, learning_rate, number & size of CNN layers, and filters (e.g. kernel_size). What is the best setup according to the best accuracy that you could find? What hyperparameters are particularly sensitive to different settings for this task?

4. For your experiment, analyse the impact of the training and the internal representation on your solution, particularly check:
   - Do specific hyperparameters and their setting lead to getting stuck in a local optima and what could be the reasons?
   - Can you identify dependencies of the hyperparameters, either in general or for specific hyperparameter settings?
   - What is the impact of the weight norm, meaning the shape and width of the distributions of weights within the layers?
 