
# 📘 **README — Microsoft 365 Agents Playground Setup (Linux, Python/Node/.NET)**

This project uses the **Microsoft 365 Agents SDK** and a **Python LangChain Agent (Gemini LLM)**.
This guide explains setup, environment variables, installing the Playground, and running everything locally.

---

# 🔐 **0. Create `.env` File (API Keys Required)** ✅ *(New Section Added)*

Before running the bot, you must create an `.env` file in your project root:

```
/my-project/microsoft-bot/.env
```

Create it:

```bash
nano .env
```

Add the following variables:

```ini
# Google Gemini API Key (LLM)
API_KEY=YOUR_GOOGLE_GEMINI_API_KEY

# Optional: Bot settings
PORT=3978
ENV=development
```

### ✔ Which API key do you need?

You need a **Google Gemini API Key** from:

🔗 [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

Add it as:

```
API_KEY=AIzaSyXXXXXXXXXXXX
```

### ✔ Why `.env`?

Your Python code loads this key:

```python
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
```

This keeps your key **private** and **not hard-coded**.

---

# 🚀 **1. Fix npm Global Permission Issues (Linux)**

```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
```

---

# 🛠️ **2. Add npm Global Bin to Your Shell PATH**

```bash
echo 'export PATH=$HOME/.npm-global/bin:$PATH' >> ~/.bashrc
echo 'export PATH=$HOME/.npm-global/bin:$PATH' >> ~/.profile
source ~/.bashrc
```

---

# 📦 **3. Install Microsoft 365 Agents Playground**

```bash
npm install -g @microsoft/m365agentsplayground
```

---

# 🔍 **4. Verify Installation**

```bash
which agentsplayground
ls -l ~/.npm-global/bin/agentsplayground
```

---

# 🧩 **5. Allow Playground Inside Python venv**

```bash
echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> .venv/bin/activate
```

---

# 🔄 **6. Run Steps**

## **Step 1 — Activate your venv**

```bash
source .venv/bin/activate
```

## **Step 2 — Run your local Python Agent**

```bash
uvicorn app:app --reload --port 3978
```

Bot available at:

```
http://localhost:3978/api/messages
```

## **Step 3 — Open Agents Playground**

```bash
agentsplayground
```

It opens:

```
http://localhost:3000
```

## **Step 4 — Connect your bot**

Go to:

```
http://localhost:3000/#/connect
```

Enter endpoint:

```
http://localhost:3978/api/messages
```

Connect → Chat.

---

# 🔑 **7. Optional — Auth Mode**

```bash
agentsplayground \
  -e "http://localhost:3978/api/messages" \
  -c "emulator" \
  --client-id "YOUR_CLIENT_ID" \
  --tenant-id "YOUR_TENANT_ID"
```

---

# 🌍 **8. Optional — Environment Variables for Playground**

```bash
export BOT_ENDPOINT="http://localhost:3978/api/messages"
export DEFAULT_CHANNEL_ID="emulator"

agentsplayground
```

---

# 🧪 **9. Troubleshooting**

| Problem            | Fix                                 |
| ------------------ | ----------------------------------- |
| command not found  | run `source ~/.bashrc`              |
| missing API key    | Check `.env` and `printenv API_KEY` |
| bot not responding | Ensure uvicorn is running           |
| Gemini errors      | Ensure API_KEY is valid             |

---

# 🎉 **Done!**

Your repo now includes:

✔ `.env` API key instructions
✔ Local Gemini + LangChain agent
✔ Microsoft 365 Playground integration
✔ Linux/npm-safe installation

