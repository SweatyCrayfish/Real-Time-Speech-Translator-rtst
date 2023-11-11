
# Real Time Speech Translator (rtst)

The `rtst` is a Python package for comprehensive speech processing. It integrates speech recognition, language detection, translation, and text-to-speech functionalities into a single, easy-to-use function.

## Features

- Unified function for speech recognition, language detection, translation, and speaking the translation.
- Support for multiple speech recognition services: Google, Azure, AWS, and Hugging Face.
- Automatic translation of recognized speech to English.
- Vocalization of translated text.

## Installation

Install the package using pip:

```bash
pip install rtst
```

## Quick Start

Here’s how to use `rtst` to recognize, translate, and vocalize speech:

### Single Function Usage

The package provides a `rtst` function, which takes care of the entire speech processing workflow:

```python
from rtst import process_speech

# Call the function with your preferred service and language code
process_speech(service='google', language='en-US')
```

This function will:

1. Capture speech from the microphone.
2. Recognize the speech using the specified service.
3. Detect the language of the recognized speech.
4. Translate the speech to English if it's in a different language.
5. Vocalize the translated text.

## Advanced Usage
For more advanced usage, refer to the package documentation. You can customize various aspects such as selecting different speech recognition services or handling different languages.

## License
MIT License

## Contributing

Contributions to `rtst` are welcome. Please follow the guidelines provided in the repository for contributing.
