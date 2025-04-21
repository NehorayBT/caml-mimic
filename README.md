# caml-mimic modified for MIMIC-IV

This repo took all of its code from: https://github.com/jamesmullenbach/caml-mimic/tree/master
and modified some parts to fit for MIMIC-IV data.

Code for the paper [Explainable Prediction of Medical Codes from Clinical Text](https://arxiv.org/abs/1802.05695).

## Dependencies

- Python 3.6, though 2.7 should hopefully work as well
- pytorch 0.3.0
- tqdm
- scikit-learn 0.19.1
- numpy 1.13.3, scipy 0.19.1, pandas 0.20.3
- jupyter-notebook 5.0.0
- gensim 3.2.0
- nltk 3.2.4

Other versions may also work, but the ones listed are the ones I've used

## Data processing

To get started, first edit `constants.py` to point to this repository dir. Then, organize your data with the following structure:

```
mimicdata
|   d_icd_diagnoses.csv
|   ICD10_descriptions (already in repo)
└───mimic4/
|   |   discharge.csv
|   |   diagnoses_icd.csv
|   |   *_hadm_ids.csv (already in repo)
```

Now, make sure your python path includes the base directory of this repository. Then, in Jupyter Notebook, run all cells (in the menu, click Cell -> Run All) in `notebooks/dataproc_mimic_IV.ipynb`.

## Training a new model

To train a new model from scratch, please use the script `learn/training.py`. Execute `python training.py -h` for a full list of input arguments and flags. The `train_new_model.sh` scripts in the `predictions/` subdirectories can serve as examples (or you can run those directly to use the same hyperparameters).
