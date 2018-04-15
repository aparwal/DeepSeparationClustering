# Deep Clustering for source separation

Experimenting with [Deep Clustering Algorithm](https://arxiv.org/abs/1508.04306) for monaural source separation.

## Usage

In `configuration.py`, set `data_dir` to folder containing test files and `results_dir` to output folder and run `test.py`

### Training
run train.py for training on entire train folder in `data_dir`

### Testing and visualization
Only track wise testing as of now
run test.py followed by visualization.py


## Dependencies

* python 3.x,
* keras2.x 
* SciPy 
* pysoundfile
* scikit-learn 
* matplotlib (for visualization)


## Reference
1. [Deep clustering: Discriminative embeddings for segmentation and separation](https://arxiv.org/abs/1508.04306)
