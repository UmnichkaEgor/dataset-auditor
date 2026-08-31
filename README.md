# Dataset Auditor CLI

A small Python program for checking dataset files.

## What it does

* Checks `.json` files for errors.
* Reads `.log` files and calculates the mean loss.
* Scans all supported files in a folder.
* Creates an `audit_report.json` with the results.
* Can be used from the command line with `argparse`.

## Requirements

* Python 3.x
* No additional libraries are needed.

## Usage

```bash
python3 dataset_auditor.py --dir path/to/dataset
```

The program scans the selected folder and saves the results in `audit_report.json`.

## School Practice

This project was made for my school internship to practice Python, working with files, JSON, error handling and command-line arguments.
