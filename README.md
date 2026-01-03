# LUCIDITY Beat Map

> **Visual degradation analysis for AI outputs - See WHERE quality drops, not just how much**

![Beat Map Demo](https://img.shields.io/badge/Status-Live%20Demo-brightgreen) ![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![License](https://img.shields.io/badge/License-Proprietary-red)

---

## 🎯 The Problem

AI outputs look great at first glance. But they degrade in **6 predictable ways**:

- **Repetition** - Same ideas, over and over
- **Vagueness** - Generic replacing specific  
- **Intent Decay** - Drifting from your prompt
- **Confidence Inflation** - False certainty
- **Voice Degradation** - Inconsistent tone
- **Entropy Collapse** - Loss of complexity

Manual review takes hours and misses subtle patterns.

---

## 💡 The Solution: Beat Map

**LUCIDITY Beat Map** is a visual timeline showing exactly where AI quality degrades across your content.

```
╔════════════════════════════════════════════════════════════╗
║              LUCIDITY BEAT MAP ANALYSIS                    ║
╠════════════════════════════════════════════════════════════╣
║ Document Flow: [████████████████████████████████████]     ║
║ Degradation:   [░░░░▓▓▓▓░░░░░░░░▓▓▓▓░░░░]                ║
║                     ↑ Spike    ↑ Spike                    ║
║                   @ 25%      @ 60%                         ║
╚════════════════════════════════════════════════════════════╝
```

🟢 Green = Good  
🟡 Yellow = Caution  
🟠 Orange = Warning  
🔴 Red = Critical

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/yourusername/lucidity-beatmap.git
cd lucidity-beatmap

# Run the demo (zero dependencies)
python3 lucidity_beatmap.py

# Analyze your own content
python3 lucidity_beatmap.py your_file.txt

# Open interactive HTML demo
open beatmap_demo.html
```

**No installation needed** - works with Python 3.7+

---

## ✨ Key Features

### 📊 Visual Timeline
See degradation patterns across your entire document at a glance

### 🎯 Pinpoint Accuracy  
Not "your document has issues" but "Intent Decay spikes at paragraph 12"

### 🔍 6-Category Analysis
Detects all degradation types simultaneously:
- REP: Repetition score
- VAG: Vagueness level
- INT: Intent Decay detection
- CNF: Confidence Inflation check
- VOI: Voice Degradation analysis
- ENT: Entropy Collapse measurement

### ⚡ Lightning Fast
Analyze documents in seconds, not hours

### 🎨 Dual Output
- **ASCII Terminal**: Color-coded timeline in your terminal
- **Interactive HTML**: Clickable, hoverable web visualization

---

## 📖 How It Works

LUCIDITY uses **ACTS** (Automated Convergence Triangulation System):

1. **14-vector analysis** measures content quality across multiple dimensions
2. **Segments your content** into 20 timeline blocks  
3. **Calculates degradation** for each segment
4. **Visualizes patterns** showing WHERE issues occur
5. **Generates recommendations** for specific fixes

---

## 🎬 See It In Action

### Terminal Output
Run `python3 lucidity_beatmap.py` to see:
- Color-coded Beat Map timeline
- Category-by-category breakdown
- Executive summary with key findings
- Actionable recommendations

### Interactive Demo
Open `beatmap_demo.html` in your browser for:
- Hoverable segments with details
- Click-to-zoom visualization
- Professional report layout
- Shareable insights

---

## 📝 Example Usage

```python
from lucidity_beatmap import LucidityBeatMap

# Load your content
with open('ai_output.txt', 'r') as f:
    content = f.read()

# Create Beat Map
beatmap = LucidityBeatMap(segments=20, use_color=True)
beatmap.analyze_content(content, degradation_data)

# Generate visualizations
print(beatmap.render_ascii(width=70))
html = beatmap.render_html()

# Get executive summary
summary = beatmap.generate_meeting_summary()
print(f"Key Finding: {summary['finding']}")
print(f"Action: {summary['action']}")
```

---

## 🎯 Use Cases

✅ **Content Teams** - Blog post and article quality verification  
✅ **Developers** - AI-generated code review  
✅ **Enterprise** - Documentation quality assurance  
✅ **Education** - Academic writing assessment  
✅ **Compliance** - Regulated content validation  

---

## 📊 Sample Analyses

We've included 3 pre-analyzed examples in `/demo_samples/`:

- `sample_good.txt` - Low degradation (technical guide)
- `sample_medium.txt` - Medium degradation (mixed quality)
- `sample_bad.txt` - High degradation (repetitive content)

Run analysis on each to see the differences!

---

## 🔬 The Technology

### ACTS Engine
Proprietary 14-vector convergence system measuring:
- Semantic coherence
- Lexical diversity  
- Information density
- Logical flow
- Voice consistency
- Confidence markers
- And 8 more dimensions

### Beat Map Visualization (Patent Pending)
Transforms abstract quality scores into intuitive visual timelines

### The ROT (6 Degradation Categories)
Comprehensive taxonomy of AI output quality issues

---

## 🌟 What Makes LUCIDITY Different

| Feature | LUCIDITY | Traditional Tools |
|---------|----------|-------------------|
| Shows WHERE degradation occurs | ✅ Visual timeline | ❌ Overall score only |
| Multiple degradation types | ✅ 6 categories | ❌ Single metric |
| Actionable recommendations | ✅ Specific sections | ❌ Vague advice |
| Speed | ✅ Seconds | ❌ Manual hours |
| Visual output | ✅ Beat Map | ❌ Text reports |

---

## 🛠️ Requirements

- Python 3.7 or higher
- No external dependencies for core functionality

**That's it!** Zero configuration needed.

---

## 📄 License

Proprietary technology. Patent applications on file.

**LUCIDITY Framework:** Michael Edwin Robinson  
**ACTS Execution:** Terrance Robinson

For licensing inquiries, demo requests, or enterprise deployment:
- 📧 Email: [your-email]
- 🌐 Web: [your-website]
- 💼 LinkedIn: [your-linkedin]

---

## 🎯 Try LUCIDITY

1. **⭐ Star this repo** to get updates
2. **📥 Clone and run** the demo
3. **🔗 Try the interactive version** → [Open beatmap_demo.html](./beatmap_demo.html)
4. **📝 Request a demo** of your content → [Demo Request Form](#)

---

## 🚀 What's Next

- [ ] Web service deployment
- [ ] API endpoints for integration  
- [ ] Batch processing capabilities
- [ ] Custom baseline support
- [ ] Team collaboration features

---

## 📚 Documentation

- [Integration Guide](./BEATMAP_INTEGRATION.md) - Add Beat Map to existing systems
- [Presentation Materials](./LUCIDITY_ONE_PAGE_SUMMARY.txt) - Overview and use cases
- [Demo Script](./LUCIDITY_DEMO_SCRIPT.txt) - Present LUCIDITY effectively

---

## 💬 Community

Questions? Issues? Ideas?

- **GitHub Issues** - Bug reports and feature requests
- **Discussions** - Share your use cases
- **Twitter/X** - [@YourHandle] - Follow for updates

---

## 🙏 Acknowledgments

Built for the AI community struggling with quality control.

Special thanks to early testers and everyone who provided feedback during development.

---

**Remember:** AI outputs degrade. LUCIDITY shows you WHERE.

---

<div align="center">

**[⭐ Star this repo]** • **[🔗 Try the demo]** • **[📧 Request access]**

Made with 💚 by Robinson & Robinson

</div>
