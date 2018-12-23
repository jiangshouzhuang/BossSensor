# BossSensor
Hide your screen when your boss is approaching.

## Demo
The boss stands up. He is approaching.

![standup](https://github.com/Hironsan/BossSensor/blob/master/resource_for_readme/standup.jpg)

When he is approaching, the program fetches face images and classifies the image.
 
![approaching](https://github.com/Hironsan/BossSensor/blob/master/resource_for_readme/approach.jpg)

If the image is classified as the Boss, it will monitor changes.

![editor](https://github.com/Hironsan/BossSensor/blob/master/resource_for_readme/editor.jpg)

## Requirements

* WebCamera
* Python3.5
* OSX
* Anaconda
* Lots of images of your boss and other person image
* For Mac's user, install PyQt5:
conda install --channel https://conda.anaconda.org/conda-forge pyqt

Put images into [data/boss](https://github.com/Hironsan/BossSensor/tree/master/data/boss) and [data/other](https://github.com/Hironsan/BossSensor/tree/master/data/other).

## Usage
Before the formal implementation, there are several points to note:
* Modify the batch_size size of the train in boss_train.py according to the data size of the picture below
* Modify the value of cascade_path, the parameter of camera_reader.py, according to the actual Python environment variable
* For pyqt versions, select image_show_pyqt4.py or image_show_pyqt5.py
* Create a **store** directory to store model data 

Now let's officially run the test:

First, Train boss image.

```
$ python boss_train.py
```


Second, start BossSensor. 

```
$ python camera_reader.py
```

## Install
Install OpenCV, PyQt5, Anaconda.

```
conda install --channel https://conda.anaconda.org/conda-forge pyqt
conda create -n python35 python=3.5
source activate python35
conda install -c https://conda.anaconda.org/menpo opencv3
conda install -c conda-forge tensorflow
pip install -r requirements.txt
```

Change Keras backend from Theano to TensorFlow. 

## Licence

[MIT](https://github.com/Hironsan/BossSensor/blob/master/LICENSE)

## Author

[Hironsan](https://github.com/Hironsan)
