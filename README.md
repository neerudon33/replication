
# Self-Consistent Quasiparticle Model for the Quark-Gluon Plasma

### Numerical Replication of Published Research

## Overview

This repository contains a computational replication of the numerical results presented in the research paper on the **self-consistent quasiparticle model (SCQPM)** for a pure gluon Quark-Gluon Plasma (QGP).

Rather than treating quarks and gluons as free, massless particles, the quasiparticle model describes them as effective particles whose masses emerge dynamically from their interactions with the surrounding hot medium. These effective masses depend on the plasma properties themselves, making the problem intrinsically **self-consistent**.

The objective of this project is to reproduce the thermodynamic behaviour reported in the original publication through numerical computation, validate the published results, and gain insight into the computational techniques used in finite-temperature Quantum Chromodynamics (QCD).

---

# Physics Background

## What is the Quark-Gluon Plasma?

Under ordinary conditions, quarks and gluons are permanently confined inside hadrons due to the strong interaction described by Quantum Chromodynamics (QCD).

However, at extremely high temperatures (approximately

[
T \gtrsim 170 \ \text{MeV}
]

or

[
\sim 2 \times 10^{12}\ \text{K}
]

), matter undergoes a phase transition into a new state known as the **Quark-Gluon Plasma (QGP)**.

In this phase,

* quarks become deconfined,
* gluons propagate freely over nuclear length scales,
* the medium behaves as a strongly interacting many-body system.

Understanding this state is essential for describing

* the early Universe microseconds after the Big Bang,
* heavy-ion collisions at RHIC and CERN-LHC,
* finite-temperature QCD.

---

## Why a Quasiparticle Model?

Direct QCD calculations at finite temperature are highly non-linear and difficult to solve analytically.

The quasiparticle approach simplifies the many-body problem by replacing strongly interacting particles with **effective quasiparticles** possessing temperature-dependent masses.

Unlike phenomenological models with arbitrary fitting parameters, the self-consistent quasiparticle model determines these masses through plasma physics itself.

The effective mass depends on the plasma frequency,

which depends on the particle density,

which again depends on the effective mass.

This circular dependence produces a nonlinear self-consistent problem that must be solved numerically.

---

# Computational Methodology

The entire project revolves around solving a coupled nonlinear numerical problem.

Instead of directly evaluating thermodynamic quantities, the computation proceeds through several sequential stages.

## Step 1 — Running Coupling Constant

The QCD coupling constant is evaluated as a function of temperature.

Unlike ordinary constants, the strong coupling decreases at higher temperatures due to asymptotic freedom.

This quantity determines the interaction strength inside the plasma and influences every subsequent calculation.

---

## Step 2 — Plasma Frequency

Using the running coupling, the plasma frequency is calculated.

The plasma frequency represents collective oscillations of gluons inside the medium and determines the quasiparticle effective mass.

Since it depends on the gluon density, it cannot be computed directly.

---

## Step 3 — Self-Consistent Gluon Density

The central computational challenge of this work is solving for the normalized gluon density.

The density appears inside its own defining equation through the effective mass, producing a transcendental nonlinear equation.

No analytical solution exists.

Instead, numerical root-finding is employed until convergence is achieved.

This iterative procedure forms the core of the entire project.

---

## Step 4 — Effective Thermal Mass

After obtaining the self-consistent density, the quasiparticle thermal mass is evaluated.

This mass changes continuously with temperature and represents the interaction effects experienced by gluons inside the plasma.

---

## Step 5 — Thermodynamic Integrals

The computed quasiparticle mass is substituted into Bose-Einstein distribution integrals.

These integrals are evaluated numerically to obtain

* Energy density
* Pressure
* Entropy density

Numerical quadrature techniques are required because closed-form solutions generally do not exist.

---

## Step 6 — Thermodynamic Consistency

The pressure is obtained from the energy density using thermodynamic relations rather than assuming an ideal gas equation.

This guarantees consistency between all thermodynamic observables throughout the temperature range.

---

# Numerical Techniques

The implementation relies entirely on scientific computing methods.

Major numerical techniques include

* Numerical integration
* Root-finding algorithms
* Iterative fixed-point convergence
* Temperature-dependent parameter evaluation
* Numerical differentiation where required
* High-resolution sampling over the temperature domain

The calculations are performed entirely in Python using optimized scientific libraries.

---

# Software Stack

* Python 3
* NumPy
* SciPy
* Matplotlib

These libraries provide efficient numerical computation, integration routines, nonlinear solvers, and scientific visualization.

---

# Repository Structure

```
.
├── src/                 # Numerical implementation
├── figures/             # Generated plots
├── report/              # Internship report and documentation
├── presentation/        # Seminar slides
├── README.md
└── requirements.txt
```

---

# Computational Workflow

```
Temperature Grid
        │
        ▼
Evaluate Running Coupling
        │
        ▼
Compute Plasma Frequency
        │
        ▼
Solve Self-Consistent Density Equation
        │
        ▼
Determine Effective Gluon Mass
        │
        ▼
Evaluate Bose-Einstein Integrals
        │
        ▼
Calculate Thermodynamic Quantities
        │
        ▼
Generate Figures
        │
        ▼
Compare with Published Results
```

---

# Results

The numerical implementation successfully reproduces the thermodynamic behaviour reported in the reference paper.

Generated quantities include

* Effective gluon mass
* Normalized gluon density
* Energy density
* Pressure
* Entropy density

The reproduced plots demonstrate good agreement with the published numerical results, validating both the computational implementation and the underlying physical model.

---

# Learning Outcomes

This project provided practical experience in

* Scientific programming
* Numerical methods in computational physics
* Finite-temperature Quantum Chromodynamics
* Nonlinear equation solving
* Numerical integration
* Data visualization
* Reproducible computational research
* Verification of published scientific results

---

# Future Work

Possible extensions include

* Full quark-gluon plasma (including quark flavours)
* Finite chemical potential
* Comparison with modern lattice QCD datasets
* GPU-accelerated numerical computation
* Higher-order running coupling corrections
* Parallel parameter sweeps
* Improved convergence algorithms

---

# Reference

This work is a computational replication performed for academic purposes during the SRIBS Summer Internship.

The implementation follows the methodology presented in the original research paper while being independently programmed in Python to reproduce the published numerical results.
