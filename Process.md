## Project Overview

This is an embedded computer vision project that serves as the foundation for a home cat detection system. While this project focuses on detecting a cat, the same workflow can be applied to many image classification applications, including door sensors, security cameras, and passthrough systems in virtual reality.

Edge Impulse was used to develop, train, and deploy the computer vision model, while Python and OpenCV were used to build the application running on the Raspberry Pi.

The dataset consisted of:

- **72 images** of the cat (Oliver)
- **60 background images**

The model was trained for **50 training cycles (epochs)**. This provided enough time for the model to learn while reducing the risk of overfitting, especially since the dataset contained a limited variety of background scenes.

### Model Performance

![Confusion Matrix](media/images/modelmatrix.png)

The selected MobileNetV2 model was chosen because it had the **lowest alpha value**, making it well suited for this simple classification task while conserving computational resources for an embedded system.

Overall, the model performance was satisfactory. Many innacuracies were relatated backgroundsbeing mistaken for Oliver. The model can be improved by adding more diverse backgrounds around the house while also showing the cat is places that don't have a carpet.
