import yaml
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import matthews_corrcoef, confusion_matrix, precision_recall_fscore_support

class Params():
    """Class that loads hyperparameters from a yaml file."""
    def __init__(self, yaml_path):
        with open(yaml_path) as f:
            params = yaml.load(f, Loader=yaml.FullLoader)
            self.__dict__.update(params)

    def save(self, yaml_path):
        with open(yaml_path, 'w') as f:
            yaml.dump(self.__dict__, f, indent=4)

    def update(self, yaml_path):
        """Loads parameters from yaml file"""
        with open(yaml_path) as f:
            params = yaml.load(f)
            self.__dict__.update(params)

    @property
    def dict(self):
        """Gives dict-like access to Params instance by `params.dict['learning_rate']"""
        return self.__dict__




'''metrics for evaluating classifications tasks'''
def binary_classification_metrics(labels, preds):
    assert len(labels) == len(preds)

    accuracy =  (labels == preds).mean()
    mcc = matthews_corrcoef(labels, preds)
    cm = confusion_matrix(labels, preds)
    precision, recall, fscore, support = precision_recall_fscore_support(labels, preds)
    pearson_corr = pearsonr(preds, labels)[0]
    spearman_corr = spearmanr(preds, labels)[0]


    return {
            "accuracy": accuracy,
            "mcc": mcc,
            "precision": precision,
            "recall": recall,
            "fscore": fscore,
            "support": support,
            "cm": cm,
            "pearson_corr": pearson_corr,
            "spearman_corr": spearman_corr,
            }
