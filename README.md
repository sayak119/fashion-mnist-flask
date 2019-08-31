**Please star this repo if you are using it as a reference. Thanks.**
# Classification Models

This is a PoC for creating a pipeline that does the following -
* Training a model. Here it is done on **Fashion MNIST** and **MNIST** datasets.
* Load the saved weights.
* Expose an **API** using Flask.

## System Configuration Used

* **OS -** Ubuntu 18.04 LTS
* **Python Version -** 3.6
* **Conda Version -** Miniconda3-latest-Linux-x86_64
* **Shell Flavour -** ZSH (Optional)
* **Tensorflow Version -** 1.13.1
* **Keras Version -** keras-2.2.4

## How to run?

* Install Miniconda from **[here](https://docs.conda.io/en/latest/miniconda.html)**.
* Run the following command
```
conda update conda
```
* Clone the repository
* Install dependencies from `environment.yml` file
```
conda env create -f environment.yml
```

* Activate your environment
```
conda activate classification_model
```

Refer the doc **[here](https://www.anaconda.com/conda-4-6-release/)** for knowing what all flavours are supported.

* Visit `src/train` folder and run the following command
```
python3 fashion_mnist.py
```
You will get a **h5** model and a **json** file as an output in the `model` folder. **You can do the same thing for MNIST dataset.**
* Now go to `src/server` and start the server using the following command
```
python3 server.py
```
**For MNIST dataset go to** `pre-process` **folder and change json_file and load_weights accordingly**
* Open a new temrinal and visit `src/test` for images and test according to the dataset you loaded by using the following command
```
curl -X POST -F 'image=@trouser.jpg'  http://localhost:5000/predict
```
For other images, in place of `trouser.jpg` add the name of that new input image.

## Output format

Numbers are returned in both the cases. In case of **MNIST** dataset, it directly corresponds to the predicted number whereas in case of **Fashion MNIST** dataset, it corresponds to the class number. For more information refer this **[link](https://github.com/zalandoresearch/fashion-mnist#labels)**.

**NOTE :** Since `python2` is being deprecated and is going to go out of service on January 1st, 2020, hence the code was made for `python3`. Depending on the default version of `python` in your system you may or may not have to run the command as `python3 fashion_mnist.py`. It can be `python fashion_mnist.py` given that default version is `python3`.
