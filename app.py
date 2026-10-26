"""Classify fictional cell populations from gene-count profiles while keeping held-out donors out of training."""
from kit import *
TITLE='Donor-Held-Out Single-Cell Annotation'
LIVE=False

def generate(seed=42):
    rng=np.random.default_rng(seed);donors=np.repeat(np.arange(8),80);y=rng.integers(0,3,len(donors));rates=np.ones((3,30))*.5
    for label in range(3):rates[label,label*6:label*6+6]+=3
    offsets=rng.lognormal(0,.12,(8,30));library=rng.lognormal(0,.3,(len(y),1));counts=rng.poisson(rates[y]*offsets[donors]*library)
    return counts,y,donors
def run(d,a):
    counts,y,donors=generate(a.seed);tr,te=group_split(donors,[6,7]);x=log_normalize(counts);mean,scale=standardize_fit(x[tr]);z=(x-mean)/scale;w=fit_softmax(z[tr],y[tr],3);p=softmax(np.column_stack([np.ones(len(te)),z[te]])@w).argmax(axis=1)
    return dict(test_accuracy=float(np.mean(p==y[te])),test_macro_f1=macro_f1(y[te],p,3),majority_accuracy=float(np.mean(y[te]==np.bincount(y[tr]).argmax())),train_donors=np.unique(donors[tr]).tolist(),test_donors=[6,7],genes='GENE_00 through GENE_29; fictional marker programs'),dict(weights=w,mean=mean,scale=scale,counts=counts,labels=y,donors=donors)

if __name__=="__main__":main(run)
