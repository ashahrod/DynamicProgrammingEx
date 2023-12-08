# Sequence Alignment: Dynamic Programming

## Overview
This project revolves around the application of dynamic programming to solve the sequence alignment problem. The primary focus is on efficiently determining the likelihood of one string being a misspelling of another. The README details a greedy approach, its limitations, and the development of a dynamic programming algorithm to overcome these challenges.

## Part 1: Sequence Alignment
The problem is framed as aligning two strings and determining the maximum score based on a scoring function. A Greedy Approach, GreedyAlignment, is introduced, and its shortcomings are highlighted through lemmas. These lemmas underscore scenarios where the greedy approach produces suboptimal alignments.

## Part 2: A Greedy Approach
Greedy algorithms, like GreedyAlignment, are demonstrated to be unsound through the proof of lemmas. These lemmas illustrate situations where the greedy approach yields lower-scoring alignments than the optimal ones, emphasizing the need for a more robust solution.

## Part 3: A Dynamic Programming Approach
A dynamic programming algorithm is designed and implemented to align strings. This example shows insights into problem reduction and the three possibilities for aligning pairs of characters. Input formats and expected output for the program are defined.

### Example Usage
```bash
$ ./compile.sh
$ ./run.sh input_data.txt
Alignment with score 15:
p r o f e s s o r
p r o f - s s i r
