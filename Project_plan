# Doctor-Hospital Assignment Project Plan

## 1. Problem and Assumptions

We consider the problem of assigning \(N\) doctors to \(K\) hospitals. Each doctor provides a complete ranked preference list over hospitals, while hospitals do not express preferences over doctors. Each hospital \(j\) has a maximum capacity \(C_j\), and the total hospital capacity is assumed to be sufficient to assign all doctors. We assume that every doctor is eligible for every hospital and that preferences are deterministic.

We formulate the problem using binary decision variables \(x_{ij}\), where \(x_{ij}=1\) if doctor \(i\) is assigned to hospital \(j\), and 0 otherwise. Let \(r_{ij}\) denote the preference rank of hospital \(j\) for doctor \(i\).

$$
\min \sum_{i=1}^{N}\sum_{j=1}^{K} r_{ij}x_{ij}
$$

subject to

$$
\sum_{j=1}^{K}x_{ij}=1 \quad \forall i
$$

$$
\sum_{i=1}^{N}x_{ij}\leq C_j \quad \forall j
$$

$$
x_{ij}\in\{0,1\}.
$$

Thus, the objective is to minimize the total preference rank while satisfying hospital capacity constraints.

## 2. Algorithm and Baseline

We plan to implement a minimum-cost flow / transportation-based optimization algorithm. Each doctor supplies one unit of flow, each hospital has capacity \(C_j\), and the cost of assigning doctor \(i\) to hospital \(j\) is their preference rank \(r_{ij}\).

For comparison, we will implement a simple greedy baseline. Doctors are processed sequentially, and each doctor is assigned to their highest-ranked hospital that still has available capacity.

## 3. Evaluation

The primary performance measure will be average preference rank across all doctors. We will additionally report the percentage of doctors receiving their first choice, the percentage receiving a top-two choice, and the worst assigned preference rank. We will compare the optimization method and greedy baseline on synthetic preference matrices under different hospital capacity distributions.

## 4. Limitations and Extensions

The model assumes that hospitals have no preferences over doctors and that every doctor is eligible for every hospital. It does not currently account for fairness, geographic constraints, doctor specialties, hospital priorities, or uncertainty in preferences. Future extensions could incorporate hospital preferences, eligibility constraints, fairness objectives, weighted preferences, or multi-objective optimization.
