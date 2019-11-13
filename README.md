# Football Player Predictor

This project loads, cleans, and models data from EA Sports FIFA 19. Further data frames are created for future analysis and development including custom labels generated on players through the process and my expertice in the field:

* Python (3.7.4)

### System

This project was created on a Macbook Pro running MacOS Mojave.

#### Python

This project used Python 3.7.4 and Anaconda 4.7.12. All Python packages can be found in the [`environment.yml`] file.

#### `fifa-env` environment
To create a new [`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) environment to use this repo, run:

```bash
# generate the fifa-env environment from the environment.yml file
conda create --name fifa-env --file environment.yml
# active (go into) the fifa-env environment
conda activate fifa-env
```

Within `fifa-env`, you can run `conda install <package-name>` to install additional packages. To ensure your additions to the repository remain reproducible, generate your own [`environment.yml`](environment.yml) with the following code:

```bash
conda list --export > environment.yml
```

## Acknowledgements

### Data

Thank you to [Aishwarya Sharma](https://www.kaggle.com/aishwarya1992) for publishing his [FIFA 19 Player Database on Kaggle](https://www.kaggle.com/aishwarya1992/fifa-19-player-database/):

> [This] Data set consists of all the player data from EA Sports FIFA 19. It contains all the attributes and ratings for all players in the data set. 

