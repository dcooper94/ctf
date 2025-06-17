# 🧠 Challenge 3: Bootstrapped

## 📂 Context

You've extracted a binary used during the AI's core boot process. It's small, deliberately obfuscated, and used for verifying logic integrity during startup. The flag is checked in memory against a hardcoded obfuscated value.

> File: `ai_boot.c`  
> Category: Reverse Engineering / Binary Analysis  
> Format: XOR-obfuscated flag

## 🧪 Objective

Recover the flag embedded within the logic validation routine.

## 🧩 Hint

- XOR obfuscation is commonly used to hide static strings
- Tools like `strings`, Ghidra, or a Python one-liner can help
- You’re looking for something compared against user input

**Flag Format:** `coops{...}`
