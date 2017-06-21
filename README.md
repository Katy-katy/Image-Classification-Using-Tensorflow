# Image-Classification-Using-Tensorflow
I am working on this project for a Kaggle competition:

https://www.kaggle.com/c/intel-mobileodt-cervical-cancer-screening

My goal is accurately identify a woman’s cervix type (type 1, type 2 or type 3) based on the image. As a training set I am using about 1500 images.

I started with very low resolution (50 by 50), the gray scale, and one hidden layer. I got test accuracy: 47.6%.

Then I increased the picture size up to 100 by 100 and got test accuracy: 45.2% - 
the better resolution did not give me the better result. 

Then I decided to try color photos since it looks like pictures of Type 1 have more red area than of Type 2 and 3. I got test accuracy: 49.2% using 50 by 50 resolution and full color photos. 

Using the full color pictures works better than grayscale. The next step could be increasing the size of the photos and increasing the number of training examples, but, unfortunately, the memory limitation of my machine does not permit me to try that.
