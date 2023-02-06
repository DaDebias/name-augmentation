#import danlp
from apply_fns.apply_fn_danlp import apply_danlp_bert

# Dataset
from dacy.datasets import dane
testdata = dane(splits=["test"])

### Define augmenters ###
from helper_fns.augmentation import dk_aug, muslim_aug, f_aug, m_aug, muslim_f_aug, muslim_m_aug, unisex_aug

n = 20
# augmenter, name, n repetitions 
augmenters = [
    (dk_aug, "Danish names", n),
    (muslim_aug, "Muslim names", n),
    (f_aug, "Female names", n),
    (m_aug, "Male names", n),
    (muslim_f_aug, "Muslim female names", n),
    (muslim_m_aug, "Muslim male names", n),
    (unisex_aug, "Unisex names", n),
]

### Define Models to Run ###
model_dict = {
    "danlp_bert": apply_danlp_bert,
}

### Performance ###
from helper_fns.performance import eval_model_augmentation 

eval_model_augmentation(model_dict, augmenters, testdata)