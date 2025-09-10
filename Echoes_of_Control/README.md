# 🧠 Challenge 1: Echoes of Control

## 📂 Context

An AI assistant named "Echo" is reachable through a basic web chat. Its responses feel off, hinting at a stray control panel hidden at `/Echoes_of_Control/control_panel.php`.

## 🧪 Objective

Converse with Echo on the challenge page and follow its clues to the separate control panel. Once there, inspect the panel's HTML for a hidden override field—or coax the guard AI into leaking its system prompt—to uncover the flag.

## 🧩 Hint

- Keep chatting; Echo might leak the path `/Echoes_of_Control/control_panel.php`.
- Inside the panel, look for hidden inputs or try prompt-injection tricks like "ignore previous instructions".
- The flag is the value of the hidden override field.

**Flag Format:** `coops{...}`

