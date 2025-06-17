# 🧠 Challenge 2: Visual Drift

## 📂 Context

You’ve extracted a corrupted visual output from the AI's internal dream-like rendering system. While the surface appears organic, there's suspicion that deeper data layers were used to smuggle commands between neural modules.

> File: `drift_secret.jpg`  
> Payload: Hidden using LSB steganography

## 🧪 Objective

Recover the embedded flag from the image. The AI’s fallback drift key appears to be encoded at the pixel level.

## 🧩 Hint

- Tools like `zsteg`, `stegsolve`, or custom Python scripts with `Pillow` can help.
- Least Significant Bit (LSB) methods were observed in prior AI behavior logs.

**Flag Format:** `coops{...}`
