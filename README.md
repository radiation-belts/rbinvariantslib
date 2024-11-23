# Radiation Belts InvariantsLibrary (rbinvariantslib)

## Overview

`rbinvariantslib` is an open-source Python library for calculating the adiabatic invariants for radiation belt research.

This library supports gridded model output and the T96 and TS05 magnetic field models. 

> [!IMPORTANT]
> **This library is currently in active development.** 
> 
> Some functions are placeholders and may not yet have full implementations. Expect ongoing updates and new features as the library evolves.

<!--
[![Documentation Status](https://readthedocs.org/projects/rbamlib/badge/?version=latest)](https://rbamlib.readthedocs.io/latest/?badge=latest)
-->

## Key Features

- **Invariants**: Calculation of K and L*
- **Modeling Support**: Key empirical models including TS05 and T96, Arbitrary Gridded Modeling output, and direct support for SWMF output from the CCMC and LFM.

## Architecture
The library is architected into a `models` package for loading instances of `MagneticFieldModel`, and an `invariants` package which provides functions to calculate K and L*.

## Development and Contribution

The library is being developed in compliance with the Heliophysics Community (PyHC) Standards and HP Data Policy. It
will be documented, tested with a planned release on Python Package Index (PyPI).

### How to Contribute

The contributions from the community as welcomed!
If you're interested in contributing, please see CONTRIBUTING.md.

## Installation and Usage

You can install the package from PyPI using the following command:
```bash
pip install rbinvariantslib
```

## Documentation
For more information, please see our documentation at: 

https://rbinvariantslib.readthedocs.io/

## License

`rbinvariantslib` is released under the BSD-License (3-clause version). See the LICENSE.rst file for details.
