# lambdata
Python package for useful data science functions, produced for Unit3 material.

## Main Features

There are a few things contained within the lambdata packet.
* Within example_module, we have a toy class set for different Animals.
* Also within example_module, we have the split_it function- this is designed to import dependencies, and train/validate/test split an existing dataframe. It will return train, val, test at appropriate ratios.
* Within example_module, there are datascience function to create a Logistic Regression pipeline via the pipe_it command.
* Within example_module, there is a datascience function to take a dataframe and break it into a train, validate and test set via the split_it command.
* Within example_module, there is a datascience function that takes a validate dataframe, and produces a confusion matrix via the confuse_me command.
* The classes module contains an object constructor for Gamers and different types of Gamers that inherit from one another. They will accept hobbies and phrases, and 

## Where to get it.

The source code for this package an be found on GitHub at: https://github.com/RobDBennett/lambdata

This is also available to have installed on your python terminal via the command:
```sh 
pip install -i https://test.pypi.org/simple/ lambdata-robdbennett 
```

## Dependencies

* [Pandas](https://pandas.pydata.org/)
* [NumPy](https://www.numpy.org)
* [Scikit-Learn](https://scikit-learn.org/stable/)
* [Random](https://docs.python.org/3/library/random.html)
* [CategoryEncoders](https://pypi.org/project/category-encoders/)

## License

[BSD 3](LICENSE)

