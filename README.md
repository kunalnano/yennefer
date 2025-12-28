# Yennefer AI Assistant

A sharp, intelligent AI assistant inspired by Yennefer of Vengerberg. Powered by local LLMs and premium voice synthesis.

## Features

- 🧠 **Local LLM** - Runs on LM Studio (Qwen3, Llama, Mistral, etc.)
- 🎭 **Premium Voice** - ElevenLabs neural TTS with custom voice
- 💬 **Personality** - Confident, witty, doesn't suffer fools
- 📊 **Token Tracking** - Real-time context usage display
- 🖥️ **Cross-Platform** - Windows native or Mac → Windows remote

## Architecture

```
Voice Input (Win+H / Wispr Flow) → Local LLM → ElevenLabs TTS
                                      ↓
                          Sharp AI advisor responses
```

## Quick Start

### Windows (Native)

1. **Install LM Studio** and load a model (recommended: Qwen3 30B-A3B)
2. **Start LM Studio server** (Local Server tab → Start)
3. **Run setup:**
   ```powershell
   cd C:\path\to\yennefer
   .\setup.bat
   ```
4. **Add your ElevenLabs API key** to `config/jarvis.yaml`
5. **Launch:**
   ```powershell
   .\start_jarvis.bat
   ```

### Mac (Remote to Windows LM Studio)

1. **On Windows:** Enable "Serve on Local Network" in LM Studio
2. **Get Windows IP:** Run `ipconfig` on Windows
3. **On Mac:**
   ```bash
   cd ~/Projects/yennefer
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-mac.txt
   ```
4. **Edit config:** Set `api_base` to your Windows IP
5. **Launch:**
   ```bash
   python -m jarvis.main
   ```

## Configuration

### Windows (`config/jarvis.yaml`)
```yaml
voice_output:
  voice_id: YOUR_ELEVENLABS_VOICE_ID
  api_key: YOUR_ELEVENLABS_API_KEY

llm:
  backend: lmstudio
  api_base: "http://localhost:1234/v1"
  context_limit: 32000
```

### Mac (`config/jarvis.yaml`)
```yaml
voice_output:
  voice_id: YOUR_ELEVENLABS_VOICE_ID
  api_key: YOUR_ELEVENLABS_API_KEY

llm:
  backend: lmstudio
  api_base: "http://192.168.x.x:1234/v1"  # Windows IP
  context_limit: 32000
```

## Voice Options

### ElevenLabs (Recommended)
- Sign up at https://elevenlabs.io
- Create a custom voice or use stock voices
- Free tier: 10k characters/month (~$5/mo for more)

### Mac Native (Free fallback)
Set in config:
```yaml
voice_output:
  engine: macos
  macos_voice: Samantha
```

## Commands

| Command | Action |
|---------|--------|
| `status` | Show token usage |
| `clear` | Reset conversation memory |
| `quit` | Exit |

## LM Studio Setup

1. Download from https://lmstudio.ai
2. Load a model (recommended: `Qwen3 30B-A3B` for 16GB VRAM)
3. Go to **Local Server** tab
4. Click **Start Server**
5. For Mac access: Enable **Serve on Local Network**

## Project Structure

```
yennefer/
├── jarvis/
│   ├── __init__.py
│   ├── main.py          # Entry point
│   ├── orchestrator.py  # Main loop
│   ├── brain.py         # LLM integration
│   ├── voice.py         # TTS output
│   ├── ears.py          # Text input
│   └── config.py        # Config loader
├── config/
│   ├── jarvis.yaml      # Main config (gitignored)
│   ├── jarvis.windows.yaml
│   └── jarvis.mac.yaml
├── requirements.txt     # Windows deps
├── requirements-mac.txt # Mac deps
├── setup.bat           # Windows setup
├── start_jarvis.bat    # Windows launcher
└── README.md
```

## Personality

Yennefer is:
- Confident and sharp
- Tells it like it is
- Has dry wit with an edge
- Helpful but never servile
- An equal, not a servant

Example:
> **You:** I'm thinking of learning three programming languages at once.
> 
> **Yennefer:** I see. How... ambitious. You'll drown in syntax before you master any of them. Pick one. Learn it properly. Then, if you still have the will, consider the others.

## License

MIT
