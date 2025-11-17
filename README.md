Absolutely — I will **add the Run Steps section** directly into your README, properly formatted and placed after installation so the flow is perfect.

Here is the **updated README with the new “🔄 Run Steps” section included**.

---

# 📘 **README — Microsoft 365 Agents Playground Setup (Linux, Python/Node/.NET)**

This project uses the **Microsoft 365 Agents SDK**, and this guide explains how to install and use the **Microsoft 365 Agents Playground** on Linux for local testing.

It includes:

* Safe npm global setup (no sudo needed)
* Installing Agents Playground
* Allowing venv to access playground
* **Run steps (added)**
* Troubleshooting

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

# 🧩 **5. Make Agents Playground Work in Python `.venv`**

```bash
echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> .venv/bin/activate
```

---

# 🔄 **6. Run Steps (Complete Guide)** ✅ **(Added as requested)**

## **Step 1 — Activate your Python virtual environment**

```bash
source .venv/bin/activate
```

---

## **Step 2 — Run your local Python agent**

Your FastAPI/uvicorn bot must be running on port **3978**.

```bash
uvicorn app:app --reload --port 3978
```

Your bot will be available at:

```
http://localhost:3978/api/messages
```

---

## **Step 3 — Open a new terminal and launch Agents Playground**

```bash
agentsplayground
```

Playground will automatically open in browser:

```
http://localhost:3000
```

---

## **Step 4 — Connect your bot inside the Playground**

Go to:

```
http://localhost:3000/#/connect
```

Enter:

```
http://localhost:3978/api/messages
```

Click **Connect**.

---

## **Step 5 — Start chatting with your LangChain bot**

Go to:

```
http://localhost:3000/#/chat
```

Your Python LangChain agent is now working inside the Playground.

---

# 🔑 **7. Optional — Authentication Support**

```bash
agentsplayground \
  -e "http://localhost:3978/api/messages" \
  -c "emulator" \
  --client-id "YOUR_CLIENT_ID" \
  --client-secret "YOUR_CLIENT_SECRET" \
  --tenant-id "YOUR_TENANT_ID"
```

---

# 🌍 **8. Optional — Environment Variables**

```bash
export BOT_ENDPOINT="http://localhost:3978/api/messages"
export DEFAULT_CHANNEL_ID="emulator"

agentsplayground
```

---

# 🧪 **9. Troubleshooting**

| Problem                               | Solution                                  |
| ------------------------------------- | ----------------------------------------- |
| `agentsplayground: command not found` | Run `source ~/.bashrc`                    |
| npm EACCES permission error           | Re-run section 1                          |
| Agent not responding                  | Make sure uvicorn is running on port 3978 |
| AI model errors                       | Check your API keys/environment variables |

---

# 🎉 **Done!**

Now your setup is ready for:

✔ FastAPI + LangChain + Gemini
✔ Microsoft 365 Agents Playground
✔ Linux-friendly npm global install
✔ Virtual environment compatibility
✔ Local agent testing through browser

---

If you want, I can also:

📌 generate a **Teams manifest**
📌 create the **Azure deployment steps**
📌 prepare a **full PDF manual**
📌 add a **diagram** showing architecture

Just tell me!
