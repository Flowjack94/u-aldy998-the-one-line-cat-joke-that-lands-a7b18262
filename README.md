# The One-Line Cat Joke That Lands

[![Competition](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/Flowjack94/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/Flowjack94/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262

A single one-line cat joke, under 200 characters, written by a deterministic
program for the make.fun competition "The One-Line Cat Joke That Lands".

## The joke

> My cat sat on the keyboard at 3:12 a.m., deleted 4,096 lines of code, and git blame says the intern did it — Ticket #4821: closed, won't fix.

## How it works

`main.py` writes the joke exactly as-is to `/output/entry.txt` and prints
its character count and SHA-256 hash. It validates the entry first: it must
be non-empty, a single line, at most 200 characters, and free of control
characters.

Run it with:

```sh
python3 main.py
```
