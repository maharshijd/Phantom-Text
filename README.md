# PHANTOMTEXT

> beyond what meets the eye.

PhantomText is a lightweight text utility for encoding and recovering messages using an access key.

The project provides a simple interface while keeping the underlying implementation separate from the user-facing application.

**Live Demo:** [phantomtext.streamlit.app](https://phantomtext.streamlit.app)

**Medium Blog:** [Making of PhantomText](https://maharshijd.medium.com/what-you-can-hide-inside-ordinary-text-building-phantomtext-6b3325f5631d)

## Version

**v1.3**

## Features

- Encode messages using an access key
- Decode messages using the original access key
- Randomly generated cover text
- Access-key verification
- Invalid-key handling
- Separate encoding and decoding modules
- Streamlit-based interface
- Message length validation
- Dark-themed interface

## Project Structure

```text
Phantom-Text/
│
├── tool.py
├── encode.py
├── decode.py
├── README.md
└── LICENSE
