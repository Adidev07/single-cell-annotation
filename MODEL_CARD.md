# Model / system card

## Intended use

Classify fictional cell populations from gene-count profiles while keeping held-out donors out of training. Educational local experiment; no production deployment is implied.

## Data

Synthetic arrays, manually written documents or replayed JSON. No real user records. Seeds and sample inputs are recorded in app.py and sample_input.json.

## Method

Simulate count data with three marker programs and donor-specific variation. Normalize each cell by library size, apply log1p, fit scaling on training donors and learn a multiclass softmax classifier.

## Evaluation protocol

Hold out donors 6 and 7 entirely. Report accuracy and macro F1 against a training-majority baseline; save donor identities and predictions to audit the split.

## Known limits

Cell labels, genes and counts are synthetic. This is not UCE or a biological foundation model; real donor and platform shifts can be much larger.

## Verification status

Local tests and default experiment are executed during packaging. Live model generation is not exercised in the build. A successful validation result is limited to the checks implemented in code.

## Further work

Use a licensed annotated single-cell dataset, preserve donor-level splitting, add unknown-cell rejection and compare a pretrained cell representation.
