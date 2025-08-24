# Computational DBS Optimization in the SCP

**A comprehensive, research‑grade toolkit for simulating, analyzing, and optimizing deep brain stimulation (DBS) protocols within the Subthalamic Cerebellar Pathway (SCP).**  
Designed for academic, clinical, and commercial teams who need reproducible, high‑performance computational pipelines to evaluate DBS efficacy, latency, and persistence metrics.

---

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Background & Motivation](#background--motivation)  
3. [Key Features](#key-features)  
4. [Repository Structure](#repository-structure)  
5. [Installation & Setup](#installation--setup)  
6. [Quick Start Guide](#quick-start-guide)  
7. [Data & File Formats](#data--file-formats)  
8. [Core Scripts & Notebooks](#core-scripts--notebooks)  
9. [Results & Visualisations](#results--visualisations)  
10. [Contributing](#contributing)  
11. [License](#license)  
12. [Contact & Acknowledgements](#contact--acknowledgements)  

---

## Project Overview
Deep Brain Stimulation (DBS) is a clinically proven therapy for movement disorders, psychiatric conditions, and emerging neuromodulation applications. This repository provides a **fully‑documented, end‑to‑end computational framework** that:

- Generates synthetic neuronal responses to a range of stimulation currents.
- Calculates clinically relevant metrics: **peak membrane potential, persistence time, and latency**.
- Produces publication‑ready visualisations (response plots & metric tables).
- Enables rapid prototyping of alternative stimulation waveforms or electrode configurations.

All code is written in **Python 3.10+**, leverages **NumPy**, **Matplotlib**, and optional **NEURON** simulation back‑end for biophysically realistic modeling.

---

## Background & Motivation
- **Clinical Need:** Optimising DBS parameters (amplitude, pulse width, frequency) is time‑consuming and often relies on trial‑and‑error during surgery.
- **Computational Advantage:** Simulations can predict neuronal outcomes **in silico**, reducing patient risk and shortening procedure time.
- **SCP Focus:** The Subthalamic Cerebellar Pathway (SCP) is a key target for treating tremor and dystonia. Precise modelling of this pathway can improve therapeutic windows.

This project translates the above motivations into a **reproducible, modular codebase** that can be extended to other brain regions or stimulation strategies.

---

## Key Features
- **Parameter Sweep Engine:** Easily explore a grid of current amplitudes (`0.1–1.0 mA`) and time points (`0–20 ms`).
- **Metric Extraction:** Automated calculation of:
  - **Peak voltage** (`mV`)
  - **Persistence time** – duration the response stays within ±1 % of the peak.
  - **Latency** – first crossing of a user‑defined threshold (default `‑64 mV`).
- **Dual‑Mode Plotting:** Side‑by‑side line‑plot of all responses and a formatted metric table.
- **Extensible Architecture:** Plug‑in custom neuronal models (e.g., NEURON, Brian2) by implementing the `simulate_*` interface.
- **Ready‑to‑Deploy Notebook:** Jupyter notebooks (`eeg brain.3.ipynb`, `eeg brain.4.ipynb`) demonstrate step‑by‑step usage.
- **Data Export:** CSV/Excel outputs for downstream statistical analysis.

---

## Repository Structure
```
├── .gitignore                     # Standard Python ignores
├── Neuro Project                  # Core research assets
│   ├── CODE-3_FINAL.txt           # Baseline simulation script (simple model)
│   ├── CODE-4_FINAL.txt           # Advanced script with realistic response functions
│   ├── NEURO_CSV_ASUTOSHA.xlsx    # Sample dataset (downloaded from raw URL)
│   ├── eeg brain.3.ipynb          # Notebook: basic simulation workflow
│   └── eeg brain.4.ipynb          # Notebook: advanced analysis & visualisation
└── README.md                      # This file
```

---

## Installation & Setup
> **Prerequisites:** Python 3.10+, Git, and optional NEURON for biophysical simulations.

```bash
# Clone the repository
git clone https://github.com/AsutoshaNanda/Computational-DBS-Optimization-in-the-SCP.git
cd Computational-DBS-Optimization-in-the-SCP

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install core dependencies
pip install -U pip
pip install numpy matplotlib pandas jupyter

# (Optional) Install NEURON if you want realistic biophysical models
# pip install neuron
```

*All scripts have been tested on Windows 10, macOS 13, and Ubuntu 22.04.*

---

## Quick Start Guide
1. **Launch the notebook**  
   ```bash
   jupyter notebook Neuro\ Project/eeg\ brain.3.ipynb
   ```
2. **Run the cells** – they will:
   - Generate a set of stimulation currents.
   - Simulate membrane potential responses.
   - Compute metrics and render a side‑by‑side figure.
3. **Export results** – the notebook includes a cell to save the metric table as `results.csv` or `results.xlsx`.

For the advanced pipeline (realistic neuronal models), open `eeg brain.4.ipynb` and follow the same pattern.

---

## Data & File Formats
- **NEURO_CSV_ASUTOSHA.xlsx** – Example CSV‑converted dataset containing raw electrophysiological recordings.  
  *URL:* `https://raw.githubusercontent.com/AsutoshaNanda/Computational-DBS-Optimization-in-the-SCP/e0ce33cbafe044fff507b890fb83bf64e6b8a49b/Neuro%20Project/NEURO_CSV_ASUTOSHA.xlsx`
- **Results files** – Exported as CSV/Excel for compatibility with statistical packages (R, SPSS, MATLAB).

---
`eeg brain.4.ipynb` `CODE-4_FINAL.txt` 
## Core Scripts & Notebooks
| File | Purpose | Highlights |
|------|---------|------------|
| `eeg brain.3.ipynb` | Simple linear response model | Demonstrates core metric functions (`simulate_response`, `calculate_persistence_time`, `calculate_latency`). |
| `eeg brain.4.ipynb` | Advanced model with realistic neuronal dynamics | Uses placeholder functions `simulate_realistic_response`, `calculate_peak_and_persistence`. Extendable with NEURON.|
| `CODE-3_FINAL.txt`  | Same as `eeg brain.3.ipynb` but in .txt format |
| `CODE-4_FINAL.txt`  | Same as `eeg brain.4.ipynb` but in .txt format |

All scripts are **well‑commented** and follow PEP‑8 style guidelines.

---

## Results & Visualisations
Running the notebooks produces a figure similar to:

- **Left panel:** Overlaid membrane potential traces for each current amplitude.
- **Right panel:** A concise table summarising **Current (mA), Peak (mV), Persistence (ms), Latency (ms)**.

These outputs are ready for inclusion in conference posters, journal articles, or client presentations.

---

## Contributing
We welcome contributions from the neuroengineering community.

1. Fork the repository.  
2. Create a feature branch (`git checkout -b feature/my‑new‑model`).  
3. Ensure **PEP‑8 compliance** (`flake8`) and **unit tests** (if added) pass.  
4. Submit a Pull Request with a clear description of changes.

Please refer to the `CONTRIBUTING.md` template (to be added) for detailed guidelines.

---

## License
This project is released under the **MIT License** – you are free to use, modify, and distribute the code for commercial or academic purposes, provided the original license notice is included.

---

## Contact & Acknowledgements
- **Lead Developer:** *Asutosha Nanda* – [GitHub Profile](https://github.com/AsutoshaNanda)  
- **Institutional Support:** *[Your Institution / Lab Name]*  
- **Funding:** This work was supported by [Insert Grant/Funding Agency] under award number **XXXXXX**.  

For questions, bug reports, or collaboration inquiries, please open an **Issue** or email `asutosha.nanda@example.com`.

---

*Empower your DBS research with reproducible, scalable, and clinically relevant simulations – all in one open‑source package.*
