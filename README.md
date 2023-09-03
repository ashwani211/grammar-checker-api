
# Grammar Checker API

An API for grammar correction using a ML model trained on a small dataset.


## Features

- Takes string intput in URL
- Processes string using Gramformer ML model
- Returns grammar corrected string in JSON format
## Tech Used

- Python
- Flask
- Torch
- Gramformer


## Working

The API takes input string in URL, processes string and corrects grammar with the help of Gramformer, a machine learning model trained on a small dataset to correct grammatical errors in the String. Then model is hosted on a server which returns the corrected value in JSON format.

Input
--|

- If a String **str** is input, write value of URL as follows:

    ```bash
    var URL = [API_URL] + "/api/" + str;
    ```

Output
--|

- Parse the URL using http get method to get the desired JSON output.

## Installation

After cloning the repository to server machine, proceed with the following steps:


- Install [Python](https://www.python.org/downloads/)
- Check Pip version
    ```bash
    pip --version
    ```
- Install [Pip](https://pypi.org/project/pip/), **if not installed**

    ```bash
    python get-pip.py
    ```
- **If using Windows**, Add Pip To Windows Environment Variables

Installing required packages:
---|

- Run the following commands and you're good to go

```bash
  pip install torch
  pip install spacy
  pip install Flask
  pip install Flask-CORS
  pip install -U git+https://github.com/PrithivirajDamodaran/Gramformer.git
```


Hosting the API:
--|
- Run the API on machine:

```bash
  python main.py
```
    
## Troubleshooting

- **CORS issue**: Cross-origin resource sharing is a mechanism that allows restricted resources on a web page to be accessed from another domain outside the domain from which the first resource was served.

- **Bluestacks issue**: If we've hosted our server locally and we are trying to access localhost i.e. http://127.0.0.1:[PORT] from Bluestacks, then there might be a issue in communcation. Try using http://10.0.2.2:[PORT]


## FAQ

#### Does the API work offline?

*Yes, refer **Installation** section, do the installation on your local machine and you're good to go. If facing difficulty, refer troubleshooting section.*

#### Why I am not able to host the API?

*We need to download the required libraries to be able to host the API. Refer **Installation** section.*

#### Why the API is throwing error?

*The application that is trying to call to the API needs to have access to it. Refer **Troubleshooting** section.*

#### Is the API ready for production?

*No. Gramformer is trained on a small dataset and currently is not production ready.*

## Author

- [Ashwani Kumar Singh](https://github.com/ashwani211)
## Acknowledgement

 - [Prithviraj Damodaran](https://github.com/PrithivirajDamodaran/Gramformer)


## Feedback

If you have any feedback, please reach out to us at ashwanikumarsingh.varanasi@gmail.com

