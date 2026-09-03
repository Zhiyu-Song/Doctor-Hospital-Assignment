# Doctor-Hospital Assignment

## Project Goal

Develop software to assign N doctors to K hospitals based on doctor preference rankings while respecting hospital capacity constraints.

The goal is to find an assignment that maximizes overall doctor satisfaction while ensuring that:

Each doctor is assigned to exactly one hospital.
Each hospital does not exceed its capacity.
The assignment is feasible under all specified constraints.

## Team

- Yuchen Ai
- Xinhao Jin
- Zhiyu Song

## Proposed Method

Hungarian Algorithm (Kuhn–Munkres Algorithm) with modifications to handle hospital capacity constraints.

Because the standard Hungarian algorithm is designed for a one-to-one assignment problem, we will adapt the problem by representing hospital capacity appropriately, such as by creating multiple hospital slots corresponding to available positions.

## Baseline

Greedy assignment based on doctor preferences.

Doctors are processed sequentially. For each doctor, assign them to their highest-ranked hospital that still has available capacity.

This provides a simple and interpretable baseline for comparison with the optimization-based method.

## Objective

Minimize the total preference cost across all doctors:

## Evaluation

Compare the proposed optimization method against the greedy baseline using:

### Total preference cost
Lower is better.
### Average preference rank
Average rank of the hospital assigned to each doctor.
Lower is better.
### First-choice assignment rate
Percentage of doctors assigned to their first-choice hospital.
Higher is better.
### Top-2 / Top-3 assignment rate
Percentage of doctors assigned to one of their top 2 or top 3 choices.
Higher is better.
### Worst assigned rank
Highest preference rank received by any doctor.
Lower is better.
### Runtime
Compare computational efficiency as the number of doctors and hospitals increases.

## Status

Project planning stage.
