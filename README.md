# Yennefer AI Assistant

A sharp, intelligent AI assistant inspired by Yennefer of Vengerberg. Powered by local LLMs and premium voice synthesis.

## Features

- 🧠 **Local LLM** - Runs on LM Studio (Nemotron, Qwen3, Llama, etc.)
- 🎭 **Premium Voice** - ElevenLabs neural TTS with custom voice
- 💬 **Personality** - Confident, witty, doesn't suffer fools
- 📊 **Token Tracking** - Real-time context usage display
- 💳 **Credit Tracking** - ElevenLabs usage monitoring
- 🖥️ **Cross-Platform** - Windows native or Mac → Windows remote

## Quick Start

### 1. Prerequisites

- **LM Studio** - Download from https://lmstudio.ai
- **ElevenLabs account** - Sign up at https://elevenlabs.io (free tier available)
- **Python 3.10+**

### 2. Clone and Setup

```bash
git clone https://github.com/kunalnano/yennefer.git
cd yennefer

# Windows
.\setup.bat

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure API Keys

Copy the example environment file and add your keys:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```bash
ELEVENLABS_API_KEY=your_api_key_here
ELEVENLABS_VOICE_ID=your_voice_id_here
```

**Get your ElevenLabs API key:** https://elevenlabs.io/app/settings/api-keys

**Get your Voice ID:** Go to Voices → click your voice → copy the Voice ID from the URL or settings

### 4. Start LM Studio

1. Open LM Studio
2. Load a model (recommended: `nvidia/nemotron-3-nano-30b-a3b`)
3. Go to **Local Server** tab → **Start Server**

### 5. Launch Yennefer

```bash
# Windows
.\start_yennefer.bat

# Mac/Linux
./start_yennefer.sh
```

## Configuration

The main config file is `config/jarvis.yaml`. API keys are loaded from environment variables (`.env` file).

### Voice Settings

```yaml
voice_output:
  voice_id: ${ELEVENLABS_VOICE_ID}    # From .env
  api_key: ${ELEVENLABS_API_KEY}       # From .env
  model: eleven_turbo_v2_5             # Fast model (free tier compatible)
  
  # Voice tuning
  stability: 0.6          # 0-1: Higher = more consistent pitch
  similarity_boost: 0.75  # 0-1: Voice matching accuracy
  style: 0.0              # 0-1: Style exaggeration
  speed: 1.15             # 0.25-4.0: Speech rate
```

### LLM Settings

```yaml
llm:
  backend: lmstudio
  api_base: "http://localhost:1234/v1"  # Or remote IP for Mac
  model: auto
  max_tokens: 2048
  temperature: 0.7
  context_limit: 32000
```

## Commands

| Command | Action |
|---------|--------|
| `status` | Show LLM token usage |
| `credits` | Show ElevenLabs character usage |
| `voice` | Show voice settings |
| `clear` | Reset conversation memory |
| `quit` | Exit |

## Recommended Models

| Model | VRAM | Notes |
|-------|------|-------|
| Nemotron-3-Nano-30B-A3B | ~18GB | Best reasoning/VRAM ratio, uses `<think>` tags |
| Qwen3-30B-A3B | ~18GB | Good all-around |
| GPT-OSS-120B | ~80GB | OpenAI's open model |

**Note:** Reasoning models that use `<think>...</think>` tags are automatically filtered—thinking isn't spoken aloud.

## ElevenLabs Voice Options

| Model | Speed | Quality | Free Tier |
|-------|-------|---------|-----------|
| `eleven_turbo_v2_5` | Fastest | Good | ✅ |
| `eleven_flash_v2_5` | Fast | Good | ✅ |
| `eleven_multilingual_v2` | Slower | Best | ✅ |

Free tier includes 10,000 characters/month.

## Mac → Windows Setup

If running LM Studio on Windows and Yennefer on Mac:

1. **Windows:** In LM Studio, enable "Serve on Local Network"
2. **Windows:** Run `ipconfig` to get your IP (e.g., 192.168.1.100)
3. **Mac:** Update `config/jarvis.yaml`:
   ```yaml
   llm:
     api_base: "http://192.168.1.100:1234/v1"
   ```

## Project Structure

```
yennefer/
├── jarvis/                 # Python module
│   ├── main.py             # Entry point
│   ├── orchestrator.py     # Main conversation loop
│   ├── brain.py            # LLM integration
│   ├── voice.py            # TTS output
│   ├── ears.py             # Text input
│   └── config.py           # Config loader with env var support
├── config/
│   └── jarvis.yaml         # Main config (uses ${ENV_VARS})
├── .env.example            # Template for API keys
├── .env                    # Your API keys (gitignored)
├── requirements.txt
├── start_yennefer.bat      # Windows launcher
├── start_yennefer.sh       # Mac/Linux launcher
├── CHANGELOG.md
└── README.md
```

## Personality

Yennefer is:
- Confident and sharp
- Tells it like it is
- Has dry wit with an edge
- Helpful but never servile
- An equal, not a servant

> **You:** I'm thinking of learning three programming languages at once.
> 
> **Yennefer:** How ambitious. You'll drown in syntax before you master any of them. Pick one. Learn it properly. Then consider the others.

## Troubleshooting

**"Cannot connect to LM Studio"**
- Ensure LM Studio is running with a model loaded
- Check the server is started (Local Server → Start)
- Verify `api_base` URL matches your setup

**"ElevenLabs 401 error"**
- Check your API key in `.env`
- Verify the key at https://elevenlabs.io/app/settings/api-keys

**Voice sounds jarring/inconsistent**
- Increase `stability` to 0.7 or 0.8 in config
- Try a different ElevenLabs model

**Thinking tags being spoken**
- Update to v0.3.0+ which filters `<think>` blocks

## License

MIT

## Contributing

PRs welcome! Please read [CHANGELOG.md](CHANGELOG.md) for version history.
