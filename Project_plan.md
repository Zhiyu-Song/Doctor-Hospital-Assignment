# Doctor-Hospital Assignment Project Plan

## 1. Problem and Assumptions

We consider the problem of assigning (N) doctors to (K) hospitals. Each doctor provides a complete ranked preference list over all hospitals, while hospitals do not express preferences over doctors.

Each hospital (j) has a maximum capacity (C_j), and the total hospital capacity is assumed to be sufficient to assign all doctors:

[
\sum_{j=1}^{K} C_j \geq N.
]

We assume that:

Each doctor must be assigned to exactly one hospital.
Each hospital can accept at most (C_j) doctors.
Every doctor is eligible for every hospital.
Doctor preferences are complete and deterministic.
Hospitals do not have preferences or priorities over doctors.
There are no additional constraints such as geographic location, specialty, or fairness requirements.

We formulate the problem using binary decision variables (x_{ij}), where (x_{ij}=1) if doctor (i) is assigned to hospital (j), and (0) otherwise. Let (r_{ij}) denote the preference rank of hospital (j) for doctor (i), where a smaller rank indicates a stronger preference.

## 2. Algorithm and Baseline

Proposed Method: Kuhn–Munkres (KM) Algorithm

We plan to implement the Kuhn–Munkres (KM) algorithm for the doctor-hospital assignment problem.

The standard KM algorithm solves a one-to-one assignment problem. Since each hospital in our problem can accept multiple doctors, we will modify the assignment formulation to incorporate hospital capacity constraints.

A hospital with capacity (C_j) can be represented by (C_j) assignment positions. Each position corresponds to the same hospital and has the same preference cost for each doctor. This allows the capacitated doctor-hospital assignment problem to be represented as a matching problem that can be solved using the KM algorithm.

For example, if hospital (j) has capacity (C_j=3), we create three equivalent positions:

[
H_{j,1}, H_{j,2}, H_{j,3}.
]

For doctor (i), the assignment cost to each of these positions is:

[
c_{i,j,k}=r_{ij}.
]

We will then apply the KM algorithm to the resulting cost matrix and map the assigned positions back to their corresponding hospitals.

Baseline: Greedy Assignment

We will implement a simple greedy algorithm as the baseline.

Doctors are processed sequentially. For each doctor, the algorithm assigns them to their highest-ranked hospital that still has available capacity.

The greedy baseline does not reconsider previous assignments, allowing us to compare its performance with the globally optimized assignment produced by KM.

## 3. Evaluation

We will compare the improved KM algorithm with the greedy baseline using synthetic preference matrices under different hospital capacity distributions.

Primary Metric

Average Preference Rank

\frac{1}{N}
\sum_{i=1}^{N}r_{i,a_i}
]

where (a_i) is the hospital assigned to doctor (i).

A lower average preference rank indicates greater overall doctor satisfaction.

Secondary Metrics

1. First-Choice Assignment Rate

The percentage of doctors assigned to their first-choice hospital.

[
\frac{#{\text{doctors assigned to first choice}}}{N}
]

Higher is better.

2. Top-2 Assignment Rate

The percentage of doctors assigned to one of their top-two choices.

Higher is better.

3. Worst Assigned Preference Rank

The highest preference rank received by any doctor.

Lower is better.

4. Total Preference Cost

[
\sum_{i=1}^{N}r_{i,a_i}
]

This directly corresponds to the optimization objective.

5. Runtime

We will measure the computational runtime of both algorithms as the number of doctors and hospitals increases.

This will allow us to evaluate not only assignment quality but also computational scalability.

Experimental Settings

We will generate synthetic preference matrices under different scenarios, including:

Different numbers of doctors and hospitals.
Balanced versus uneven hospital capacities.
Different levels of competition for popular hospitals.
Different ratios between total hospital capacity and the number of doctors.

For each setting, we will compare the greedy baseline and improved KM algorithm using the evaluation metrics above.

## 4. Limitations and Extensions

The current model assumes that hospitals have no preferences over doctors and that every doctor is eligible for every hospital.
Future extensions could incorporate hospital preferences, eligibility constraints, fairness objectives, weighted preference functions, or multi-objective optimization.

##5. Status

Project planning stage.
