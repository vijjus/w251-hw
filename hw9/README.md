* How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)
* Do you think your model is fully trained? How can you tell?
* Were you overfitting?
* Were your GPUs fully utilized?
* Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck?
* Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?
* How big was your training set (mb)? How many training lines did it contain?
* What are the files that a TF checkpoint is comprised of?
* How big is your resulting model checkpoint (mb)?
* Remember the definition of a "step". How long did an average step take?
* How does that correlate with the observed network utilization between nodes?
