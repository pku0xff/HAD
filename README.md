# HAD: Hallucination Annotation and Detection

This is the official repository for the paper **HAD: HAllucination Detection Language Models Based on a Comprehensive Hallucination Taxonomy**. We currently release the training and test data used in this work.

## Download Data

The training data files are not included in this repository. Please download the data archive from the following link and extract it to the project root directory:

- [Download data.zip](https://drive.google.com/file/d/1MIG81gHtOjarUGv_RC_In8lNUw_aS5ju/view?usp=drive_link)

After downloading, extract the archive so that the `data/` directory is placed at the project root:

```bash
unzip data.zip
```

## Data Description

### Training Data

To train a fully functional HAD model with hallucination type classification, you can directly use the data in the `data/prompts/` directory. Each entry is a JSON object with the following format:

```json
{
  "prompt_id": "nq_6910392503958514724",
  "prompt": "### Instruction ###\nGiven a pair of task input and task output, your goal is to detect whether the task output contains any hallucination.\nIf a hallucination is present, specify the type of hallucination, identify the hallucination span, and provide the correct version of the output.\n\n### Example ###\n**Task Input:**\nWho did ed sheeran tour with in 2010?\n\n**Task Output:**\nExample\n\n### Your Detection ###",
  "response": "**Hallucination Type:**\nNone\n\n**Hallucination Span:**\nNone\n\n**Correction:**\nNone"
}
```

To train a binary classification HAD model (hallucination vs. no hallucination), use the data in `data/binary_prompts/`. The data source is the same as `prompts/`, but the response format uses a **Hallucination Label** field instead of **Hallucination Type**. Each entry follows this format:

```json
{
  "prompt_id": "nq_6910392503958514724",
  "prompt": "### Instruction ###\nGiven a pair of task input and task output, your goal is to detect whether the task output contains any hallucination.\nIf a hallucination is present, identify the hallucination span and provide the correct version of the output.\n\n### Example ###\n**Task Input:**\nWho did ed sheeran tour with in 2010?\n\n**Task Output:**\nExample\n\n### Your Detection ###",
  "response": "**Hallucination Label:**\nNo hallucination\n\n**Hallucination Span:**\nNone\n\n**Correction:**\nNone"
}
```

### Source Training Data

The source training data before prompt formatting is available in the `data/split/` directory. Each entry is a JSON object with the following format:

```json
{
  "source": "nq",
  "id": "nq_6910392503958514724",
  "task": "short-form QA",
  "task_input": "Who did ed sheeran tour with in 2010?",
  "task_output": "Example",
  "hallucination_type": "None",
  "hallucination_span": "None",
  "correction": "None"
}
```

### Test Data

The test data is provided in `data/hadtest.json`. Each entry contains the source information, task input/output, hallucination annotation, and a formatted prompt for evaluation.

### Hallucination Data

- `data/checked_hallu_data.json`: Hallucination data that has been filtered through automated screening, without additional sampling or splitting.
- `data/raw_hallu_data.json`: The raw, unfiltered hallucination data before any screening.

## Utilities

`utils.py` contains utility functions for constructing prompts and parsing model outputs.

## Project Structure

```
HAD/
├── data/
│   ├── prompts/              # Formatted training data (full classification)
│   │   ├── train.json
│   │   └── dev.json
│   ├── binary_prompts/       # Formatted training data (binary classification)
│   │   ├── train.json
│   │   └── dev.json
│   ├── split/                # Source training data before prompt formatting
│   │   ├── train.json
│   │   └── dev.json
│   ├── hadtest.json          # Test data
│   ├── checked_hallu_data.json   # Auto-filtered hallucination data (no sampling/splitting)
│   └── raw_hallu_data.json       # Raw unfiltered hallucination data
└── utils.py                  # Utility functions for prompt construction and output parsing
```
