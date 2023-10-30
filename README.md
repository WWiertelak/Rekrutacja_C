## Django Text Processing & PESEL Validator Application

This repository contains a Django application developed as part of a recruitment task. 
Processing uploaded text files by shuffling the middle letters of each word while leaving the first and last letters unchanged.
Validating PESEL numbers entered by the user, and providing information on its validity, the birth date, and gender of the PESEL owner.

### Running the Application
* Build and start conteiner:
```bash
docker compose up
```
* Visit http://localhost:8000/text/ to use Text Processing app
* Visit http://localhost:8000/pesel/ to use Pesel Validator app

### Assumptions
* Text File Content: The uploaded text file for processing should contain only letters. Special characters, numbers, or symbols may not be processed as expected.
* PESEL Validation: The PESEL validation is based on the official specification. The application assumes the PESEL number to be 11 digits long, starting with the birth date information.
