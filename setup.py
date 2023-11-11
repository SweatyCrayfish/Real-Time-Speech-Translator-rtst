from setuptools import setup, find_packages

setup(
    name="speech_recog_pkg",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "speechrecognition",
        "langdetect",
        "googletrans==3.1.0a0",
        "pyttsx3",
        "azure-cognitiveservices-speech",
        "boto3",
        "transformers",
        "numpy",
        "tensorflow",
        "soundfile",
        "librosa",
        # Add any other necessary packages here
    ],
    entry_points={"console_scripts": ["speech-recog=speech_recog_pkg.main:main"]},
)
