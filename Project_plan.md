# Doctor-Hospital Assignment Project Plan

## 1. Problem and Assumptions

We consider the problem of assigning \(N\) doctors to \(K\) hospitals. Each doctor provides a complete ranked preference list over hospitals, while each hospital has a maximum capacity $$\(C_j\)$$. We assume

$$
\sum_{j=1}^{K} C_j \geq N.
$$

Each doctor must be assigned to exactly one hospital, and each hospital cannot exceed its capacity. All doctors are eligible for all hospitals, and preferences are deterministic.

Let $$x_{ij}\in{0,1}$$ indicate whether doctor $$\(i\)$$ is assigned to hospital $$\(j\)$$, and let $$\(r_{ij}\)$$ be doctor $$\(i\)$$'s preference rank for hospital $$\(j\)$$. We aim to minimize total preference cost:

$$
\min \sum_{i=1}^{N}\sum_{j=1}^{K} r_{ij}x_{ij}
$$

subject to

$$
\sum_{j=1}^{K}x_{ij}=1,\quad \forall i,
$$

$$
\sum_{i=1}^{N}x_{ij}\leq C_j,\quad \forall j.
$$

## 2. Algorithm and Baseline

### Proposed Method: Kuhn–Munkres (KM) Algorithm

We will use the **Kuhn–Munkres (KM) algorithm** and adapt it to handle hospital capacity constraints.

Since standard KM solves a one-to-one assignment problem, each hospital $$\(j\)$$ will be expanded into $$\(C_j\)$$ equivalent assignment slots. For example, a hospital with capacity 3 is represented by three slots with identical assignment costs. The resulting problem can then be formulated as a one-to-one matching problem and solved using KM. If necessary, dummy doctors or hospital slots will be added to obtain a square cost matrix.

### Baseline: Greedy Assignment

As a baseline, doctors are processed sequentially and each doctor is assigned to their highest-ranked hospital that still has available capacity. The greedy algorithm does not reconsider previous assignments.

## 3. Evaluation

We will compare KM with the greedy baseline using synthetic preference matrices under different hospital capacity distributions.

We will evaluate:

* **Average preference rank** — primary metric; lower is better.
* **First-choice assignment rate** — percentage receiving their top choice; higher is better.
* **Top-2 assignment rate** — percentage receiving a top-two choice; higher is better.
* **Worst assigned rank** — highest rank assigned to any doctor; lower is better.
* **Runtime** — computational cost as problem size increases.

We will test different numbers of doctors and hospitals, balanced and uneven hospital capacities, and different levels of competition for popular hospitals.

## 4. Limitations and Extensions

The current model does not consider hospital preferences, doctor specialties, geographic constraints, fairness, or incomplete/uncertain preferences. Future extensions could incorporate eligibility constraints, hospital priorities, fairness objectives, or weighted preference functions.

## 5. Status

**Project planning stage.**

Next steps are to finalize the KM-based formulation, implement the greedy baseline and capacity-aware KM algorithm, generate test cases, and compare the two methods using the evaluation metrics above.
