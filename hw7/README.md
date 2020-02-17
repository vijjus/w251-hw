Question: Describe your solution in detail. What neural network did you use? What dataset was it trained on? 
What accuracy does it achieve?

I used a pre-trained model from TensorFlow called the Single Shot multibox Detector (SSD) model that has been trained on the 
WIDERFace dataset. The model is built from this work:

"Speed/accuracy trade-offs for modern convolutional object detectors."
Huang J, Rathod V, Sun C, Zhu M, Korattikara A, Fathi A, Fischer I, Wojna Z,
Song Y, Guadarrama S, Murphy K, CVPR 2017

The latest version of the TensorFlow object detection pre-trained models are based on the MobileNetV3 CNN architecture.

Question: Does it achieve reasonable accuracy in your empirical tests? Would you use this solution to develop a robust, 
production-grade system?

I tried a number of experiments with 1 person and 2 people in the frame, with each person looking in arbitrary directions. The
SSD model was able to capture the faces in most of these experiments (~90%). In some cases, especially with 2 people in the
frame, if a face was only partially in the frame, the model was sometimes not able to detect it. Looking at the TensorFlow
object detection GitHub page (https://github.com/tensorflow/models/tree/master/research/object_detection) it seems that the
models are state of the art MobileNetV3 based, and are also available to run on low-power devices such as the Google Pixel
phone. Based on this, I think this model can be used in building robust, production grade applications.

Question: What framerate does this method achieve on the Jetson? Where is the bottleneck?

For a single image, the average inference time was *0.088 seconds*. This comes out to about 12.5 fps on the TX2. I think the
bottleneck would be in calculations as the resized image is sent through the model in the forward pass.

Question: Which is a better quality detector: the OpenCV or yours?

I think OpenCV was doing a slightly better job, but the SSD model isn't that far behind.
