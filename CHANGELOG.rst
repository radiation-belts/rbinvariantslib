Notable changes to this project will be documented in this file.
The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`__.

Version 0.2.1 - 2025-01-22
============================
  * Workaround an issue in dependency PyGeopack that would cause segmentation faults when calling ``models.get_tsyganenko()`` with large grids (`External PyGeopack Issue #26 <https://github.com/mattkjames7/PyGeopack/issues/26>`_)

Version 0.2.0 - 2024-11-24
============================
  * Renamed package to ``rbinvariantslib`` from ``dasilva-invariants``
  * Published first pip package and overhauled unnecessary dependencies
  * Made ``get_tsyagnenko_params()``` retrieve parameters from CDAWeb API
  * Added unit test for examples and core functionality
  * Added CHANGELOG
