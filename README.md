# ⚡ Yennefer

<div align="center">

**A local AI assistant with attitude, premium voice, and zero cloud dependency.**

*"Magic is chaos, art, and science. It is a curse, a blessing, and progress."*

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LM Studio](https://img.shields.io/badge/LM%20Studio-Local%20LLM-00D084?style=for-the-badge&logo=ai&logoColor=white)](https://lmstudio.ai)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-Voice-8B5CF6?style=for-the-badge&logo=audio&logoColor=white)](https://elevenlabs.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-F97316?style=for-the-badge)](LICENSE)

<br>

[Features](#-features) • [Quick Start](#-quick-start) • [Configuration](#-configuration) • [Models](#-recommended-models) • [Roadmap](#-roadmap)

</div>

---

## 🎭 What Is This?

Yennefer is a conversational AI that runs **entirely on your machine** using [LM Studio](https://lmstudio.ai). She's not another sycophantic assistant—she has opinions, standards, and won't coddle you.

The only cloud touch is [ElevenLabs](https://elevenlabs.io) for premium neural TTS (optional—free tier gives you 10K chars/month).

<table>
<tr>
<td width="50%">

**Why local?**
- 🔒 Your conversations never leave your hardware
- 💰 No API rate limits or surprise bills  
- 🔄 Swap models anytime—Nemotron, Qwen, Llama, whatever
- ✈️ Works offline (except voice synthesis)

</td>
<td width="50%">

**Why Yennefer?**
- 🎯 Direct feedback, not corporate pleasantries
- 🧠 Actually helpful, not just agreeable
- 🎙️ Premium voice that doesn't sound like a robot
- ⚡ Fast—runs on your GPU, not a queue

</td>
</tr>
</table>

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                              YOUR MACHINE                                │
│  ┌──────────┐      ┌─────────────────┐      ┌─────────────────────┐    │
│  │   You    │─────▶│    Yennefer     │─────▶│     LM Studio       │    │
│  │ keyboard │      │  (orchestrator) │      │  (local LLM engine) │    │
│  └──────────┘      └────────┬────────┘      └─────────────────────┘    │
│                             │                                           │
└─────────────────────────────┼───────────────────────────────────────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │   ElevenLabs    │  ← Only external call
                     │   (voice API)   │
                     └─────────────────┘
```

---

## ✨ Features

| | Feature | Description |
|:--:|---------|-------------|
| 🧠 | **Local LLM** | Any GGUF model via LM Studio—Nemotron, Qwen, Llama, Mistral, DeepSeek, you name it |
| 🎙️ | **Premium Voice** | ElevenLabs neural TTS with custom voice cloning support |
| 🎭 | **Real Personality** | Sharp, confident, witty—inspired by Yennefer of Vengerberg |
| 📊 | **Token Tracking** | Visual context window with auto-trim at 85% capacity |
| 💳 | **Credits Monitor** | Real-time ElevenLabs character usage tracking |
| 🧹 | **Thinking Stripper** | Auto-removes `<think>` tags so reasoning isn't spoken aloud |
| 🖥️ | **Cross-Platform** | Windows native or Mac → Windows remote via LAN |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Why |
|-------------|-----|
| **Python 3.10+** | Runtime |
| **[LM Studio](https://lmstudio.ai)** | Local LLM backend |
| **[ElevenLabs account](https://elevenlabs.io)** | Voice synthesis (free tier works) |
| **NVIDIA GPU** | Recommended for decent speed |

### Installation

```bash
# Clone the repo
git clone https://github.com/kunalnano/yennefer.git
cd yennefer

# Windows
.\setup.bat

# Mac/Linux
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Configuration

```bash
# Create your environment file
cp .env.example .env
```

Edit `.env` with your keys:
```bash
ELEVENLABS_API_KEY=your_key_here      # From elevenlabs.io/settings/api-keys
ELEVENLABS_VOICE_ID=your_voice_id     # From your Voice Library
```

### Launch

1. **Start LM Studio** → Load a model → Local Server → Start
2. **Run Yennefer:**

```bash
# Windows
.\start_yennefer.bat

# Mac/Linux
./start_yennefer.sh
```

That's it. She's waiting.

---

## 🎮 Commands

| Command | What It Does |
|:--------|:-------------|
| `status` | Show token usage and context window health |
| `credits` | Display ElevenLabs character usage |
| `voice` | Show voice settings and session stats |
| `clear` | Wipe conversation memory |
| `quit` | Exit gracefully |

> 💡 **Pro tip:** On Windows, press `Win+H` for system-level voice dictation.

---

## 🤖 Recommended Models

Tested configurations that work well:

| Model | VRAM | Speed | Notes |
|-------|:----:|:-----:|-------|
| **NVIDIA Nemotron-Mini-4B** | ~4GB | ⚡⚡⚡ | Great for quick interactions |
| **Nemotron-3-Nano-30B-A3B** | ~18GB | ⚡⚡ | Best reasoning-to-VRAM ratio. Uses `<think>` tags. |
| **Qwen3-30B-A3B** | ~18GB | ⚡⚡ | Excellent all-around performer |
| **Llama-3.1-8B-Instruct** | ~6GB | ⚡⚡⚡ | Good for lighter hardware |
| **DeepSeek-R1-Distill-Qwen-14B** | ~10GB | ⚡⚡ | Strong reasoning model |

> 🧠 **Reasoning models** that use `<think>...</think>` tags are automatically filtered. Yennefer thinks before speaking, but keeps her thoughts to herself.

---

## 🎙️ Voice Configuration

ElevenLabs model options:

| Model | Latency | Quality | Best For |
|-------|:-------:|:-------:|----------|
| `eleven_turbo_v2_5` | ⚡ Fastest | Good | Daily use |
| `eleven_flash_v2_5` | Fast | Good | Balance |
| `eleven_multilingual_v2` | Slower | Best | Quality priority |

Fine-tune the voice in `config/jarvis.yaml`:

```yaml
voice_output:
  stability: 0.6          # 0-1: Higher = more consistent pitch
  similarity_boost: 0.75  # 0-1: Voice matching accuracy
  style: 0.0              # 0-1: Style exaggeration (keep low)
  speed: 1.15             # 0.25-4.0: Speech rate
```

---

## 🌐 Remote Setup (Mac → Windows)

Running LM Studio on a beefy Windows rig but want to talk from your Mac?

1. **Windows (LM Studio):** Enable "Serve on Local Network" in Local Server settings
2. **Windows:** Run `ipconfig` → note your LAN IP (e.g., `192.168.1.100`)
3. **Mac:** Update `config/jarvis.yaml`:
   ```yaml
   llm:
     api_base: "http://192.168.1.100:1234/v1"
   ```

Your Mac becomes a thin client to your GPU server.

---

## 🎭 Personality

Yennefer doesn't do corporate AI pleasantries. She's helpful, but she'll call out bad ideas.

<table>
<tr>
<td>

> **You:** I'm thinking of learning three programming languages at once.
>
> **Yennefer:** How ambitious. You'll drown in syntax before you master any of them. Pick one. Learn it properly. Then consider the others.

</td>
</tr>
<tr>
<td>

> **You:** Can you help me with my code?
>
> **Yennefer:** Show me what you've got. I'll tell you what's wrong with it.

</td>
</tr>
<tr>
<td>

> **You:** I want to build a startup but I have no idea what problem to solve.
>
> **Yennefer:** Then you don't want to build a startup—you want the *idea* of building one. Find a problem that genuinely irritates you first. The business comes after.

</td>
</tr>
</table>

She's an equal, not a servant. Inspired by Yennefer of Vengerberg—confident, sharp, doesn't suffer fools gladly.

---

## 🗂️ Project Structure

```
yennefer/
├── jarvis/                 # Core Python package
│   ├── main.py             # Entry point + ASCII banner
│   ├── orchestrator.py     # Conversation loop controller
│   ├── brain.py            # LLM integration (OpenAI-compatible API)
│   ├── voice.py            # ElevenLabs TTS + thinking tag stripper
│   ├── ears.py             # Input handler
│   └── config.py           # YAML loader with ${ENV_VAR} expansion
├── config/
│   └── jarvis.yaml         # Main configuration file
├── .env.example            # API key template
├── requirements.txt        # Python dependencies
├── start_yennefer.bat      # Windows launcher
├── start_yennefer.sh       # Mac/Linux launcher
├── CHANGELOG.md            # Version history
└── README.md               # You are here
```

---

## 🐛 Troubleshooting

<details>
<summary><strong>"Cannot connect to LM Studio"</strong></summary>

- Is LM Studio running with a model loaded?
- Check Local Server tab shows "Running"
- Verify `api_base` in config matches your setup (default: `http://localhost:1234/v1`)
</details>

<details>
<summary><strong>"ElevenLabs 401 error"</strong></summary>

- Verify API key in `.env` file
- Check key validity at https://elevenlabs.io/app/settings/api-keys
- Ensure you haven't exceeded your character limit
</details>

<details>
<summary><strong>Voice sounds robotic or jarring</strong></summary>

- Increase `stability` to 0.7-0.8 in config
- Try `eleven_multilingual_v2` model for smoother output
- Reduce `speed` if words are clipping
</details>

<details>
<summary><strong>Thinking tags being spoken aloud</strong></summary>

- Update to v0.3.0+ (automatic stripping included)
- The stripper handles `<think>`, `<thinking>`, unclosed tags, and edge cases
</details>

---

## 📋 Roadmap

### Coming Soon
- [ ] **Wake word detection** — "Hey Yennefer"
- [ ] **Streaming TTS** — Start speaking before generation completes
- [ ] **Interrupt handling** — Stop mid-sentence when you speak

### Future
- [ ] **Memory persistence** — Remember across sessions
- [ ] **Multi-voice support** — Switch characters on the fly
- [ ] **Tool plugins** — Let her actually *do* things (file ops, web search, etc.)

---

## 📜 License

MIT — Do whatever you want. Credit appreciated but not required.

---

## 🤝 Contributing

PRs welcome. See [CHANGELOG.md](CHANGELOG.md) for what's been done.

**Good first contributions:**
- Wake word detection integration (Porcupine, Snowboy, etc.)
- Alternative TTS backends (Coqui, Bark, local options)
- Voice activity detection for natural turn-taking
- Tiktoken integration for accurate token counting

---

<div align="center">

<br>

**Built with spite and good taste.**

<br>

*If you find this useful, star the repo. Yennefer doesn't ask for validation, but the algorithm appreciates it.*

</div>
