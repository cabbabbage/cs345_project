
# Python Feature Extraction and Implementation

This toolkit provides a set of Python classes for extracting various linguistic and structural features from text data. It's designed to be used with CSV files containing text entries, allowing users to enrich their datasets with additional features for further analysis or machine learning tasks.

## Installation

Before using the toolkit, ensure you have Python 3 installed on your system. Additionally, you'll need to install the following dependencies:

```bash
pip install nltk language_tool_python tqdm
```

Ensure you also have the necessary NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```

## Components

The toolkit comprises several Python files, each responsible for a distinct aspect of feature extraction or the toolkit's operation:

### `add_feature.py`

This script is designed to integrate with CSV files, adding new columns that represent extracted features from the text data.

- **Description**: Adds a new feature column to a specified CSV file. If the `reanalyze` option is set to `True`, it will replace existing columns with the same title; otherwise, it keeps the existing column.
- **Functionality**: Extends CSV files with new data columns based on text analysis.

### `main.py`

The main driver script preforms feature extraction process. This verion is for Linux, manual csv path entry.

- **Description**: Coordinates the feature extraction process, allowing users to select a CSV file and automatically applying all available feature extractions.

### `main_win.py`

The main driver script preforms feature extraction process. This verion is for Windows, UI csv selection.

- **Description**: Coordinates the feature extraction process, allowing users to select a CSV file and automatically applying all available feature extractions.

### Feature Extractors

Each of the following files defines a class responsible for extracting a specific feature from text. They implement a `get` method that accepts a text string and returns the feature value.

#### `Sentences.py`

- **Feature**: Sentence Count
- **Return Type**: Integer (number of sentences)

#### `Length.py`

- **Feature**: Word Count
- **Return Type**: Integer (number of words)

#### `Paragraphs.py`

- **Feature**: Paragraph Count
- **Return Type**: Integer (number of paragraphs)
- **Description**: Counts the number of paragraphs in the provided text, considering any non-empty sequence of text separated by newline characters as a paragraph.

#### `Correctness.py`

- **Feature**: Text Correctness
- **Return Type**: Float (1.0 for perfectly correct text, 0.0 for entirely incorrect text)
- **Description**: Analyzes the text for spelling and grammatical errors, returning a correctness score based on the proportion of errors.

#### `Quotations.py`

- **Feature**: Quotation Coverage
- **Return Type**: Float (percentage of text within quotations)
- **Description**: Calculates what percentage of the text is enclosed in single or double quotes.

#### `Confidence.py`

- **Feature**: Confidence Level
- **Return Type**: Float (percentage of sentences deemed confident)
- **Description**: Assesses the confidence level of the text by identifying the presence of insecure words and calculating the percentage of sentences without them.

#### `POS.py`

- **Feature**: Part of Speech Count
- **Return Type**: Float (count of the specified part of speech divided by the text length)
- **Description**: Counts occurrences of a specified part of speech in the text.
- **Note**: Note multiple instances of this class are used for different parts of speech see "get_features" method in main.

#### `PassiveVoice.py`

- **Feature**: Passive Voice Usage
- **Return Type**: Float (percentage of sentences in passive voice)
- **Description**: Identifies and calculates the percentage of sentences written in passive voice.

## Usage

1. Run `main.py`.
2. Select a CSV file through the file dialog.
3. The script will automatically add new columns to the CSV file for each feature extracted by the included classes.


