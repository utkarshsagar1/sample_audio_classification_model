# Audio Classification Model

This repository contains the example and sample files to deploy an Audio Classification Model on Katonic Platform.

## Prerequisites for Deployment:

**Note** : You need to fork the repository to deploy it on Katonic Platform

- `launch.py`: This file consists of `loadmodel`, `preprocessing` and `predict` functions.
 The first function helps to fetch the model. The second function is optional,if you are performing any kind of preprocessing on the data before prediction please add all the necessary steps into it and return the formatted input, else you can just return `False` if no processing is required. In the third function write down the code for prediction and return the results in the data structure supported by API response.   

- `schema.py`: Define your schema on how you should pass your input data in predict function.

- `requirements.txt`: Define the required packages along with specific versions this file.

## Sample Input Data for Prediction API

```python
{
  "data": [[-217.35526,70.22339,-130.38528,-53.282906,-21.19913,-22.677624,-10.85597,18.294254,6.6527047,14.324023,-12.167682,2.276836,-17.779186,10.388949,-6.582835,-0.6944583,-18.336023,1.9942513 ,-5.14333,8.3024,-12.645057,-6.529732,4.6176686,-2.179917,-6.662824,0.3597099,-3.908409,4.7756233,-6.384521,-5.379819,0.9159807,6.9704933,-0.24866624,1.6782194,-5.6111803,-2.9643471,3.1490586,-1.6930535  ,-0.6169837,0.38600525]]
}
```

## Sample Input Data for Feedback API

```python
{
  "predicted_label":[1,1,1,1,0,0,0,0,1,0,1,0],
  "true_label": [1,1,0,1,0,1,0,0,1,0,1,0]
}
```
