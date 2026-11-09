# 🎧 DTMF Audio Survey – Gender-Sensitive Applications

This repository demonstrates how to use **Dual-Tone Multi-Frequency (DTMF)** tones for collecting survey responses through phone calls.  
It adapts the original decoder from [ribt/dtmf-decoder](https://github.com/ribt/dtmf-decoder) and applies it to survey contexts—particularly useful when verbal answers may not be safe or comfortable to share.

---

## 🧠 Why DTMF?

In **sensitive surveys**, such as those related to **gender, safety, or well-being**, participants may prefer not to speak directly.  
Instead, they can **press a key on their phone** (e.g., “Press 1 for Yes, 2 for No”), generating tones that are decoded later.  
This preserves confidentiality while enabling structured data collection.

> ⚠️ **Limitations:**  
> This method may not work on older phones or those without a physical or touch keypad interface.

---

## 📂 Repository Structure

```
.
├── 00_Form.xlsx          # Example of a SurveyCTO form design
├── audio_test.wav        # Sample audio with recorded DTMF tones
├── 01_DTMF.py            # Main decoder script
├── 02_Commands.py        # Commands for terminal in CMD or Visual Studio Code
├── DTMF_Guide.pdf        # Visual guide (6 steps to process audios)
└── README.md
```
## ⚙️ Installation

Requires Python 3.8+.

```bash
git clone https://github.com/USUARIO/NOMBRE-REPO.git
cd NOMBRE-REPO
pip install numpy scipy matplotlib
```

## ▶️ Quick Start

1. Record or export the call audio as `.wav`.
2. Run the decoder on the sample file:

```bash
python 01_DTMF.py audio_test.wav
```

3. The script prints the detected keys (e.g., `1 2 1 3`), which map to the answer options defined in `00_Form.xlsx`.

See `DTMF_Guide.pdf` for the full 6-step process.

## 💬 Ethical Note

DTMF-based surveys can support ethical, anonymous, and secure data collection when dealing with gender-based violence, harassment, or sensitive behavior studies.
They allow respondents to participate without verbal disclosure, protecting their identity and comfort.
However, these tools should complement, not replace, broader ethical safeguards such as informed consent, data protection, and contextual risk assessment.

## 🙏 Acknowledgments

Special thanks to the original authors of ribt/dtmf-decoder.
This repository serves as a tutorial on how DTMF can be applied in phone-based surveys, especially in gender-sensitive research contexts.
