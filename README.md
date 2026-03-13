# Algebra, Number Theory, and Cryptography

![The Ambassadors](https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Hans_Holbein_the_Younger_-_The_Ambassadors_-_Google_Art_Project.jpg/700px-Hans_Holbein_the_Younger_-_The_Ambassadors_-_Google_Art_Project.jpg)

*"The Ambassadors" (1533) by Hans Holbein the Younger — [Wikipedia](https://en.wikipedia.org/wiki/The_Ambassadors_(Holbein))*

Python implementations of classical number theory algorithms and a full RSA cryptosystem.

## About

Coursework for **Algebra, Teoria dos Numeros e Criptografia** (Algebra, Number Theory, and Cryptography) at EMAp/FGV, taught by Professor Luciano Castro (2019.2).

The course follows the textbook *Numeros Inteiros e Criptografia RSA* by S. C. Coutinho, covering fundamental number theory before building up to a working RSA implementation.

**Authors:** Pedro Delfino (A1 and A2) and Bruna Fistarol (A2).

## Projects

### A1 -- Textbook Exercises (Chapters 1-6)

Programming exercises from the textbook, implementing core number theory algorithms:

| Chapter | Topics |
|---------|--------|
| 1 | Euclidean algorithm, LCM, Diophantine equations |
| 2 | Modular arithmetic |
| 3 | Divisibility and prime testing |
| 4 | Congruences |
| 5 | Number-theoretic functions |
| 6 | Cryptographic foundations |

### A2 -- RSA Implementation

A complete RSA cryptosystem built from scratch, including:

- Key generation
- Letter-to-number encoding table
- Block partitioning for encryption
- Modular inverse computation
- Encryption and decryption routines

## Tech Stack

- **Language:** Python 3
- **Textbook:** *Numeros Inteiros e Criptografia RSA* -- S. C. Coutinho

## Repository Structure

```
A1-livro/
  cap-1/   Euclidean algorithm, LCM, Diophantine equations
  cap-2/   Modular arithmetic
  cap-3/   Divisibility
  cap-4/   Congruences
  cap-5/   Number-theoretic functions
  cap-6/   Cryptographic foundations
A2-RSA/    Full RSA implementation
```

## How to Run

```bash
python3 <script_name>.py
```

## Notes

- Code comments, textbook exercises, and the original README are in Portuguese.
