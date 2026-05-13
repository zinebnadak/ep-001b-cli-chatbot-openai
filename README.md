# Episode 001b — CLI Chatbot with Memory (OpenAI)

> Same mechanic as my [ep-001 — Original build with Anthropic](https://github.com/zinebnadak/ep-001-cli-chatbot-memory) but this time with OpenAI´s API. 

## The Problem / The Question
ep-001 built this with Anthropic. This rebuild uses the OpenAI API to expose
the differences in how each SDK structures the same conversation loop.

## What I Built
The same CLI chatbot from ep-001, full conversation history preserved across
turns, but rebuilt with the OpenAI Python SDK and gpt-4o-mini.

## What I Learned
› The memory mechanic is identical. A list of dicts with `"role"` and `"content"`, sent with every request. The model is stateless on both APIs.
› OpenAI´s old API for chat was widely known the "Chat Completions API": `client.chat.completions.create()`
› Anthropic: `client.messages.create()` OpenAI (new): `client.responses.create()` and uses input=, instead of messages= like Anthropic and the old API does. 
› The parameter names are different but the logic is the same. `messages=` becomes `input=`, `system=` becomes `instructions=`.
› Anthropic requires no `api_key=` argument if the key is set in the environment, the client picks it up automatically `Anthropic()`. OpenAI requires you to pass it explicitly with `OpenAI(api_key=...)`
›`RateLimitError` and `APIError` for error handling exist in both SDKs.
› I noticed the OpenAI API response structure is slightly different when drilling into it to extract the text and append it to history. Anthropic response object: `message.content[0].text`. OpenAI response object: `response.output[0].content[0].text`


## How to Run

1. Clone the repo

```bash
$ git clone https://github.com/zinebnadak/ep-001b-cli-chatbot-openai
$ cd ep-001b-cli-chatbot-openai
```

2. Create and activate a virtual environment

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Install dependencies

```bash
$ pip install -r requirements.txt
```

4. Add your API key

```bash
$ cp .env.example .env
```

Open `.env` and replace with your actual OpenAI API key

5. Run

```bash
$ python src/main.py
```

## Tech Used
- `openai` — Python SDK for the OpenAI API (model: gpt-4o-mini)
- `python-dotenv` — loads the API key from `.env`

## References
- [OpenAI Developers API Docs](https://developers.openai.com/api/docs)
- [OpenAI — Chat Completions API](https://platform.openai.com/docs/guides/chat-completions)
- [Create a model response, accepted parameters](https://developers.openai.com/api/reference/python/resources/responses/methods/create)
- [ep-001 — Original build with Anthropic](https://github.com/zinebnadak/ep-001-cli-chatbot-memory)

by [Zineb Nadak](https://github.com/zinebnadak) · [X](https://x.com/zinebnadak) · [LinkedIn](https://www.linkedin.com/in/zinebnadak)