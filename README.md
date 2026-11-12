# AI Assignment 1 — General-Purpose Classical Reasoning Agent

**Kumar Gaurav (P26AI0006)**

Pipeline: **Natural Language Knowledge Base → Internal Representation → Classical Reasoning → True/False**

This repository contains the complete submission:

| Path | Description |
|---|---|
| `submission/reasoning_agent.ipynb` | Self-contained implementation, smoke tests, reasoning traces, public-set evaluation, and `submission.csv` generation. |
| `submission/report.pdf` | Design, algorithms, experiments, and reasoning traces. |
| `submission/submission.csv` | Demo-format predictions (`id,predicted_label`). |
| `submission/README.txt` | Submission notes and reproduction instructions. |

## Public-set results

| Dataset | Split | Accuracy | Total time | Per sample |
|---|---|---|---|---|
| RuleTaker | test (151,911) | 100.00% | 32.6 s | 0.000215 s |
| CounterBench | alpha+backdoor (1,200) | 95.00% | 0.5 s | 0.000417 s |
| FOLIO | validation, gold FOL (203) | 81.28% | 20.7 s | 0.1020 s |
| **Overall** | **3-dataset average** | **92.09%** | — | **0.0342 s** |

Overall accuracy is the unweighted mean of the three dataset accuracies. Overall inference time is the unweighted mean of the per-sample times, exactly as requested in the submission form.

## How to run

1. Install the dependencies:

   ```bash
   pip install pandas pyarrow
   ```

2. Open `submission/reasoning_agent.ipynb` in Jupyter and run all cells top to bottom.

3. The evaluation cell loads the public data from `./data` if present; otherwise it downloads RuleTaker, CounterBench, and FOLIO from Hugging Face once.

4. The final cell writes `submission.csv`. If a private test file (`private_test.csv` or `test.csv` with `id` plus context/statement columns) is present, it is used; otherwise a demo-format CSV is generated from public samples.

## Method summary

- **RuleTaker** — natural-language facts and rules are parsed into Horn clauses; forward-chaining least-fixpoint closure with negation-as-failure and contradiction retraction answers the query. Backward chaining with unification produces proof traces.
- **CounterBench** — causal mechanisms are compiled into a structural causal model; Pearl's abduction–action–prediction procedure (exhaustive root search, `do()` interventions, fixed-point propagation) answers counterfactuals.
- **FOLIO** — gold FOL (or a deterministic NL→FOL template parser) is converted to CNF; a resolution-refutation prover with unification, factoring, subsumption, and set-of-support decides entailment.

The final verdict is always produced by these hand-written classical engines. No generative model is used for inference.
