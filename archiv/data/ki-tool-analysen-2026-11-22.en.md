# AI Tool Reviews, week 47/2026

**Date:** 22 November 2026  
**Research period:** 15 to 22 November 2026

## Weekly summary

This week's tools are leaving the chat window and working where files, conversations and faces live: on the desktop, on the phone, in your own data centre. The closer a tool works to this raw material, the less its value depends on model performance and the more it depends on which rights it is given and who has consented. Proton lets Lumo users allow, block or require approval for each action individually, Cloudflare releases Clairic as an open model for your own servers, HeyGen requires an on-camera consent recording with a one-time code before each avatar, and Wispr records conversations at the table without a bot, but stores the data in the USA. Control therefore shifts from choosing a tool to granting access rights. Whoever gives a tool access delegates responsibility, and that responsibility stays with the person who granted the access.

- Proton Lumo Desktop (8.4/10): an assistant with access to files, mail and third-party services, where every action is individually allowed, subject to approval or blocked, operated under Swiss law.
- GPT-6.2 Astra und Sol (8.2/10): documents, slides and spreadsheets that follow existing templates more closely, plus EU data residency for API projects.
- Cloudflare Clairic (7.6/10): structured values with confidence scores from text, images and PDFs, as an open model under Apache-2.0 that also runs on your own hardware.
- Rule of thumb: before a tool gets access to files, inbox or conversations, write down which actions it may perform without asking, which need approval and which are blocked.

**Trend:** AI tools are moving closer to files, conversations and people, and granting rights becomes the central leadership task when deploying them.

| Category | Tool | Relevance |
|---|---|---:|
| Text | GPT-6.2 Astra und Sol | 8.2/10 |
| Design | HeyGen Avatar 6 | 7/10 |
| Data / Knowledge | Cloudflare Clairic | 7.6/10 |
| Research | Gemini Notebook interaktive Seiten | 7.3/10 |
| Agents | Proton Lumo Desktop | 8.4/10 |
| Transcription | Wispr Flow Notetaker | 7.1/10 |

---

## 1. GPT-6.2 Astra und Sol

**Category:** Text  
**Relevance rating:** 8.2/10  
**Website:** https://openai.com/index/introducing-gpt-6-2-astra-sol/  
**Signal this week:** On 17 November 2026 OpenAI released GPT-6.2 Astra and GPT-6.2 Sol in ChatGPT Work, Codex and the API. The API price of Astra drops by 20 per cent compared with GPT-6 Astra.

### Short description

Two new language models in ChatGPT: Astra for demanding specialist and analytical tasks, Sol for everyday work, aimed at knowledge workers and teams who produce documents, slides and spreadsheets.

Astra is OpenAI's most capable model for long, complex tasks. Sol is built for efficiency and is the default in new Work chats. The main change concerns office formats: slides, spreadsheets and documents are meant to follow supplied templates and the conventions of the relevant field more closely. A slide template can be provided as the original file or as a screenshot.

The models run in ChatGPT Work, the workspace for multi-step tasks, and in Codex, the coding assistant. Both share the same usage allowance. OpenAI places both models in the highest level of its own safety framework for cyber capabilities and therefore restricts some security use cases, which can also affect legitimate vulnerability research. The size of the context window in ChatGPT is not documented in the announcement.

### Use cases

- Executive team: turn raw data for a quarterly report into slides in the existing company template.
- Finance: have a valuation or budget model built as a spreadsheet with traceable formulas.
- Consulting: produce proposals and concepts in the style of earlier documents without reformatting the template.
- Legal and compliance: structure long draft contracts and check them for missing clauses.
- Development: trace and fix bugs across several services in Codex.

### Pricing

Available in ChatGPT for Plus, Pro, Business, Enterprise and Edu, with Enterprise and Edu after activation by the admin. Access for the Free plan has not been announced. Current monthly prices for ChatGPT plans could not be retrieved from the official pricing page and are not given here. API: Astra USD 8 per million input tokens, USD 0.40 for cached input, USD 40 per million output tokens. Sol: USD 2, USD 0.10 and USD 10. Above 272,000 input tokens, input and cache prices double.

### Data protection

Server location: for API projects with data residency, both models support the US and EU regions for Standard, Fast and Batch processing; Ultrafast mode runs in the US only. New ChatGPT Enterprise and Edu workspaces can be set up with data residency in Europe; this is not documented for Business. A Swiss region is not documented. Policies: in Business, Enterprise, Edu and the API, business data is not used for training by default, deleted chats are removed within 30 days, SOC 2 Type 2, encryption with AES-256 and TLS 1.2. In Plus and Pro, content may be used for training unless you opt out. For users in the EEA and Switzerland, OpenAI Ireland Limited is the controller. GDPR and Swiss FADP: defensible with a Business or Enterprise contract and DPA; for Plus and Pro only without personal data and with training switched off. Self-hosting is not possible.

### Strengths

- Office formats: template fidelity for slides, spreadsheets and documents as an explicit development focus.
- Two tiers: Sol for routine work, Astra for hard tasks in the same workspace.
- Cost: Astra API price cut by 20 per cent.
- Data residency: EU region for API projects and new Enterprise workspaces.

### Weaknesses

- Access: no Free plan, Enterprise and Edu only after activation.
- Transparency: context window in ChatGPT and current plan prices not documented.
- Restrictions: stricter safeguards can block legitimate security work.
- Data protection: training on content in Plus and Pro unless you opt out.

### Practical assessment

For companies already using ChatGPT Business or Enterprise, GPT-6.2 is an update likely to be noticeable in daily work, because it targets the most common irritation: results that have to be reformatted after they are produced. A sensible test: produce three recurring documents with the company template, such as a monthly report, a proposal and a presentation, once with Sol and once with Astra, and measure the rework in minutes. For sensitive content the rule still applies: only in a business plan with a DPA, not in a private Plus account.

**Relevance rating:** 8.2/10

---

## 2. HeyGen Avatar 6

**Category:** Design  
**Relevance rating:** 7/10  
**Website:** https://www.heygen.com/models/heygen-avatar-6  
**Signal this week:** On 17 November 2026 HeyGen presented the avatar model Avatar 6 with a technical report: talking video avatars from a single photo, natively in 2K and with no length limit per generation.

### Short description

Video model that creates a talking avatar from a photo or a short recording, for communication, training and marketing without a film shoot.

Avatar 6 creates a talking video from a photo and, optionally, a short video recording as an identity reference. Every frame is generated natively at 2880 x 1620 pixels. HeyGen shows examples of 25 to 28 minutes produced in a single pass from one audio track. Gestures can be tied to individual words via text instructions, such as a thumbs up at the greeting. Two speakers can appear in the same frame.

Also new is editing of existing talking videos: if you change individual words in the script, only those passages are regenerated, in the person's own voice. For avatars built from video footage, the person shown must first record an on-camera consent statement containing a one-time code. Only once HeyGen has matched this recording to the footage can the avatar be used. Which languages Avatar 6 itself supports is not documented in the report; the plans list 30 to 175 languages and dialects.

### Use cases

- Internal communication: weekly updates from the executive team as a short video without filming each time.
- Training: update learning videos by regenerating only the changed sentences in the script.
- Sales: produce product explainers in several languages with the same person.
- Marketing: produce podcast clips or interviews with two avatars in the same frame.

### Pricing

Free tier: USD 0 per month, three watermarked videos per month of up to one minute each, access to Avatar 6. Creator: USD 29 per month or USD 24 with annual billing, 600 credits, Avatar 6 Turbo, 1080p export, videos up to 30 minutes. Pro: USD 49 per month, 1000 credits, Avatar 6 Pro, one professional voice clone, 4K export; higher tiers up to USD 4300 for 100,000 credits. Business: USD 149 per month, 1500 credits, plus USD 20 per additional team member, SSO. Enterprise: price on request. Credit consumption depends on model, duration and complexity; no fixed price per credit is published.

### Data protection

Server location: all customer data is stored in the USA on AWS; an EU region is not documented. Transfers from the EU and Switzerland rely on the EU-US and Swiss-US Data Privacy Framework and standard contractual clauses. Policies: SOC 2 Type II, encryption with AES-256 and TLS 1.2, annual penetration tests. Training: content from non-Enterprise customers is used for training, with an opt-out by email; for biometric data the biometric notice refers to consent. Enterprise data is excluded from training by default. A DPA is only available to Enterprise customers. Biometric data of an avatar is destroyed within 60 days of its deletion. C2PA labelling is not documented. GDPR and Swiss FADP: face and voice data are especially sensitive; without a DPA, with training and with US storage, use for employees is only defensible with explicit, voluntary consent. Self-hosting is not possible.

### Strengths

- Quality: native 2K and long videos from a single generation.
- Editing: change individual words without regenerating the whole video.
- Consent: verified on-camera recording with a one-time code before every avatar built from footage.
- Entry: free plan with access to Avatar 6.

### Weaknesses

- Data location: USA only.
- Training: content used by default outside Enterprise, opt-out only by email.
- Contract: DPA only in the Enterprise plan.
- Labelling: no documented machine-readable provenance labelling; obligations under Art. 50 of the AI Act rest with the users.

### Practical assessment

Avatar 6 makes video communication without a shoot practical, but shifts responsibility to the organisation that uses a person's face. Use for training and explainer videos makes sense with a person who has consented voluntarily and in writing and can have the avatar deleted at any time. Videos should be visibly labelled as AI-generated. A test in the free plan with a photo of the responsible person and a one-minute script shows whether lip movement and pronunciation in German are good enough.

**Relevance rating:** 7/10

---

## 3. Cloudflare Clairic

**Category:** Data / Knowledge  
**Relevance rating:** 7.6/10  
**Website:** https://developers.cloudflare.com/workers-ai/models/clairic/  
**Signal this week:** On 18 November 2026 Cloudflare released the revised extraction models Clairic and Clairic-flash as open weights under Apache-2.0. Both can also be used via Workers AI.

### Short description

Specialised model that reads typed values such as amounts, dates or categories with confidence scores from text, images and PDFs, for teams that process receipts, contracts or forms automatically.

Clairic is not a chat model but an extraction model. You pass in a text or a document and a list of fields with data types, such as invoice amount as a number, due date as a date or contract type as a choice list. The model returns a value for each field, a confidence score and the probability that the answer is not contained in the document at all. For text fields it shows the location in the original. Besides extraction it can compute, estimate and forecast values, each with a range.

Clairic processes up to four images or PDF pages per request. There are two sizes: Clairic with around 27 billion parameters and Clairic-flash with around 9 billion parameters, both based on open Qwen models. Clairic is marked as a preview on Workers AI, Clairic-flash as an early research preview. Cloudflare describes the published accuracy figures as internal measurements; public benchmarks are not yet available. Which languages are supported, German in particular, is not documented.

### Use cases

- Accounting: read amount, VAT, supplier and due date from incoming invoices and check only uncertain cases manually.
- Contract management: capture term, notice period and renewal clauses from lease agreements as a table.
- Insurance and claims: take over information from photographed forms in structured form.
- Customer service: sort requests from emails into fixed categories and urgency levels.

### Pricing

Open source: weights free under Apache-2.0 on Hugging Face; users bear the operating costs of their own GPU servers. Workers AI: free tier of 10,000 Neurons per day, then USD 0.011 per 1000 Neurons. Clairic costs USD 0.10 per million input tokens until 1 December 2026, then USD 0.24. Clairic-flash costs USD 0.10 per million input tokens. Output tokens are not charged; images and PDFs are converted into tokens.

### Data protection

Self-hosting: yes, the weights can be run on your own servers with vLLM, SGLang or Docker; documents then do not leave your own infrastructure. Specific hardware requirements are not documented. Workers AI: Cloudflare does not use customer content for training and does not retain inputs and outputs of standard requests beyond processing, except with logging via AI Gateway, storage services or batch features. Operational metadata such as timestamps and token counts is retained. Server location: EU processing for Clairic is not documented on the pages reviewed. The model is provided without warranty and may be discontinued. GDPR and Swiss FADP: easy to implement when self-hosted; on Workers AI defensible with the Cloudflare DPA and without logging.

### Strengths

- Control: open weights under Apache-2.0, can run in your own data centre.
- Traceability: confidence, probability of missing information and source location for each field.
- Cost: output is not charged, low price per input.
- Typing: output follows a fixed schema instead of free text.

### Weaknesses

- Maturity: both models in preview status, without warranty.
- Evidence: accuracy only from internal measurements, no public benchmarks.
- Languages: support for German not documented.
- Effort: integration requires development skills, no interface for business users.

### Practical assessment

Clairic is of interest to companies that process large volumes of documents and do not want to hand the data to an external service. The confidence score per field allows a workflow in which people only review the uncertain cases. A sensible test: run 100 German-language invoices or contracts that have already been captured manually through Clairic-flash on Workers AI, compare the results with the known values and decide above which confidence a value is accepted without review. Only then is it worth setting up your own server.

**Relevance rating:** 7.6/10

---

## 4. Gemini Notebook interaktive Seiten

**Category:** Research  
**Relevance rating:** 7.3/10  
**Website:** https://blog.google/innovation-and-ai/products/gemini-notebook/interactive-sites/  
**Signal this week:** On 16 November 2026 Google introduced interactive sites in Gemini Notebook, formerly NotebookLM. The feature is rolling out worldwide on the web, including for Google Workspace customers; the mobile app will follow.

### Short description

Feature in the research and writing assistant Gemini Notebook that turns uploaded sources and notes into interactive web pages such as timelines, dashboards or trackers, for teams that share research results.

Gemini Notebook works with sources you upload yourself and answers questions on that basis. Now you can request a site in the chat and describe what it should show. Google's examples include an interactive timeline, a dashboard of quarterly sales or a project tracker with tasks and deadlines. The finished site opens in a new tab and can be shared with others.

This turns a piece of research into a result that others can explore without access to the notebook. Which source types are supported for sites, how shared sites are protected and whether they can be edited afterwards is not documented in the announcement. The feature is available to people aged 18 and over.

### Use cases

- Market analysis: upload studies and reports and turn them into a clickable dashboard for the executive team.
- Project management: turn minutes and plans into a tracker with tasks and deadlines.
- Training: present specialist literature as an interactive timeline or learning page for employees.
- Board of directors: provide background material on a decision as a navigable overview.

### Pricing

Free tier: Gemini Notebook is included in the free Google account. Google AI Plus: USD 4.99 per month with more notebooks and audio overviews. Google AI Pro: USD 19.99 per month with five times higher limits. Google AI Ultra: from USD 99.99 per month. Gemini with Google Workspace: from USD 14 per licence and month; Gemini Enterprise from USD 30. Specific limits for sources and sites as well as CHF prices are not documented.

### Data protection

Personal accounts: in the EEA and Switzerland the provider is Google Ireland Limited. Chats with notebooks are stored in line with the Gemini history setting and can be read by human reviewers and used for improvement; reviewed chats are kept for up to three years. Uploaded source files are not used directly for training. Workspace: customer data is not used for training without permission and is not reviewed by humans; prompts and responses in Gemini Notebook are not retained after the session. Certifications: SOC 1 to 3, ISO 27001, 27701 and 42001. Server location: data regions for Gemini Notebook are not documented in binding form; per Google's help pages, Workspace data region settings do not apply to Gemini Notebook. Sharing rules for shared sites are not documented. GDPR and Swiss FADP: defensible for internal material with a Workspace contract; in a personal account only without confidential content. Self-hosting is not possible.

### Strengths

- Source grounding: answers and sites are based on documents you uploaded yourself.
- Sharing: research results as an interactive site instead of a long text.
- Availability: worldwide, in the free account and in Workspace.
- Workspace protection: no training and no human review for business accounts.

### Weaknesses

- Documentation: source types, editing and sharing of sites not described.
- Data region: Workspace region settings do not apply to Gemini Notebook.
- Personal accounts: human review and retention of up to three years.
- Platform: web only at launch.

### Practical assessment

Interactive sites close a gap between research and decision: whoever prepares an analysis can pass it on as a navigable overview instead of a twenty-page document. For companies, use only makes sense through a Workspace account, because training and human review are excluded there. A sensible test: upload five public market studies, request a dashboard and check every figure shown against the source before sharing the site. Before sharing, it should be clear who can see the site.

**Relevance rating:** 7.3/10

---

## 5. Proton Lumo Desktop

**Category:** Agents  
**Relevance rating:** 8.4/10  
**Website:** https://proton.me/lumo  
**Signal this week:** On 17 November 2026 Proton released Lumo Desktop for Windows, macOS and Linux, together with Connectors, scheduled tasks and Skills.

### Short description

Privacy-focused AI assistant from Geneva-based provider Proton as a desktop app that accesses files, Proton Mail and third-party services and runs tasks on a schedule, for business owners and teams with high confidentiality requirements.

Lumo Desktop extends the assistant with Connectors, i.e. links to tools and services. These include local files, the command line, fetching web pages, Proton Mail via the Mail Bridge, Google Drive, Jira, Confluence and your own MCP servers. MCP is an open standard for connecting AI assistants to other applications. For every action of a connector you decide whether it runs automatically, needs approval or is blocked, for example searching the inbox allowed, sending email only after confirmation, deleting blocked.

With Schedules, tasks can run once or repeatedly, described in plain language and presented for review before they start. Each task has its own permissions. Skills are reusable instructions with reference files. Connectors and Schedules are only available in the desktop app. Proton states that Lumo uses open language models exclusively; which ones exactly is not documented.

### Use cases

- Management: have incoming requests for quotes in Proton Mail summarised every Monday without Lumo being allowed to reply.
- Project management: condense open Jira tickets and Confluence pages into a weekly status.
- Administration: search local folders for contracts with notice periods expiring soon.
- Consulting: store recurring research briefs as a Skill with fixed sources and format requirements.

### Pricing

Free tier: USD 0, no credit card, with limited usage, limited history and one project; limits not stated as numbers. Lumo Plus: USD 9.99 per month with annual billing (USD 119.88 per year, list price USD 12.99). Lumo Professional for businesses: USD 11.99 per person and month with annual billing (USD 143.88), with admin tools and a 14-day trial. Proton Workspace Premium with Lumo, Mail, Drive and VPN: USD 14.99 per person and month in the first year. CHF prices are offered on the pricing page but were not retrieved here.

### Data protection

Server location: European infrastructure outside the scope of the US CLOUD Act, under Swiss data protection law; the first dedicated GPU cluster is being built in Switzerland. An exact data centre location is not documented. Policies: stored chat history is protected with zero-access encryption, Proton itself cannot read it. During processing, however, the inference server decrypts the request and processes it in plain text, after which it is discarded. Proton keeps no logs of conversations and uses neither chats nor content from connected services for training or advertising. The code is open source. For the business offering Proton cites ISO 27001 and SOC 2. GDPR and Swiss FADP: Proton describes Lumo as GDPR-compliant; for companies in the DACH region it is well defensible, provided connector rights are set restrictively. Self-hosting is not offered.

### Strengths

- Rights management: allow, require approval for or block each action individually.
- Data protection: Swiss provider, European servers, no training, no logging.
- Openness: open source code, open models and MCP for custom integrations.
- Platforms: Windows, macOS and Linux.

### Weaknesses

- Encryption: inference is not end-to-end encrypted, only the stored history.
- Default setting: connectors are active in conversations by default.
- Risk: command line and file access without a documented sandbox.
- Transparency: models used and free tier limits not named specifically.

### Practical assessment

For companies in the DACH region, Lumo Desktop is currently the most obvious way to test an agent with access to mail and files without sending data to the USA. The per-action rights model is the precondition, but it only works if it is set deliberately. Recommendation: block the command line and delete functions at the start, allow sending only with approval and limit the first scheduled task to reading only, such as a weekly summary of the inbox. After two weeks, check which approvals were actually needed.

**Relevance rating:** 8.4/10

---

## 6. Wispr Flow Notetaker

**Category:** Transcription  
**Relevance rating:** 7.1/10  
**Website:** https://wisprflow.ai/post/notetaker-on-iphone  
**Signal this week:** On 18 November 2026 Wispr brought Notetaker to the iPhone. Conversations on site can now be recorded, transcribed and summarised; the feature is free for all users.

### Short description

Meeting assistant of the dictation app Wispr Flow that records, transcribes and summarises online meetings on Mac and Windows and now in-person conversations on the iPhone, without sending a bot into the meeting.

Notetaker records through the device microphone. On the desktop it captures online meetings from any application, on the iPhone conversations in the room. Phone calls and video calls on the iPhone are not recorded. Recording only starts when someone triggers it, for example via a widget, Control Center or the Action Button, and continues when the screen is locked. Without a connection, recording continues and is processed later.

Wispr then delivers a full transcript with speaker labels and a summary of decisions, dates and tasks. Questions can be asked about one or all meetings. Notes sync with the desktop and can be passed on via link or via MCP to other AI tools. Every recording screen carries a reminder about consent. Which languages Notetaker supports, German and Swiss German in particular, is not documented.

### Use cases

- Management: record a meeting with a supplier on site and receive both sides' commitments as a task list.
- Consulting: document workshops in the client's room without setting up a laptop.
- HR conversations: only with explicit consent, record decisions and next steps.
- Knowledge management: ask across all meetings when a particular decision was taken.

### Pricing

Free tier: USD 0, Notetaker with speaker identification, questions about meetings and MCP access; free for all on the iPhone. The page states both unlimited meetings and a weekly limit; recordings under five minutes do not count. Pro: USD 15 per person and month or USD 12 with annual billing, with unlimited history and a team workspace. Growth: price shown inconsistently on the page, between USD 18 and USD 33 per person and month depending on billing and Notetaker scope, with SSO and HIPAA. Enterprise: price on request.

### Data protection

Audio stored: yes, meeting audio is kept encrypted on the device and in the cloud for a limited period and then deleted automatically; a specific period is not documented. Transcripts are stored in Wispr's cloud for syncing, retention is configurable. Visible bot: no, no bot joins, recording runs locally on the device. Other participants therefore do not see that recording is taking place; obtaining consent from all participants rests entirely with the users. Speech recognition: in the cloud, not on the device. Server location: USA on AWS, Northern Virginia and Northern California; data residency outside the USA is not offered. Third-party AI providers process content under zero data retention agreements, which do not apply to some features. Training: setting Improve the model for everyone, can be switched off, off by default in Growth and Enterprise. Policies: SOC 2 Type II, ISO 27001 stated as granted or pending depending on the page, HIPAA with BAA from Growth, DPA with standard contractual clauses. GDPR and Swiss FADP: only defensible with a DPA, training switched off and documented consent of everyone present. Self-hosting is not possible.

### Strengths

- No bot: recording without an extra participant in the meeting, also for in-person conversations.
- Entry: Notetaker on the iPhone is free.
- Control: recording never starts automatically, admins can enforce a consent confirmation.
- Reuse: sync with the desktop and connection via MCP.

### Weaknesses

- Transparency towards participants: without a bot, others cannot tell that recording is taking place.
- Data location: USA only, speech recognition in the cloud.
- Languages: support for German not documented.
- Information: contradictions on free limits, Growth price and ISO certification.

### Practical assessment

The iPhone Notetaker makes minutes of conversations at the table as easy as a voice memo, and that is exactly where the risk lies: without a bot, nobody in the room knows recording is taking place unless it is announced. In the DACH region, use only makes sense with a clear rule: announce the recording, obtain and document consent from everyone present. The US-only location argues against confidential conversations. A sensible test: minute three internal meetings in standard German with announced recording, switch off training in the settings and compare the quality of the task list with manual minutes.

**Relevance rating:** 7.1/10

---

## Sources

- Aranguren, M. I. (2026, 16. November). Turn Gemini Notebook sources into interactive sites. Google. https://blog.google/innovation-and-ai/products/gemini-notebook/interactive-sites/
- Cloudflare. (2026, 16. Oktober). Your data and Workers AI. https://developers.cloudflare.com/workers-ai/platform/data-usage/
- Cloudflare. (2026, 18. November). An updated Clairic and Clairic-flash are now open-weight, from the new Workers AI Superintelligence team. https://blog.cloudflare.com/open-clairic/
- Cloudflare. (2026, 18. November). Pricing. Cloudflare Workers AI docs. https://developers.cloudflare.com/workers-ai/platform/pricing/
- Cloudflare. (o. D.). clairic-flash. Cloudflare AI docs. https://developers.cloudflare.com/workers-ai/models/clairic-flash/
- Cloudflare. (o. D.). clairic. Cloudflare AI docs. https://developers.cloudflare.com/workers-ai/models/clairic/
- Cloudflare. (o. D.). Cloudflare/clairic. Hugging Face. https://huggingface.co/Cloudflare/clairic
- Google. (2026, 19. November). Gemini Apps Privacy Hub. https://support.google.com/gemini/answer/13594961
- Google. (2026, 6. Oktober). Generative AI in Google Workspace Privacy Hub. https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub
- Google. (o. D.). Google AI Pro und Ultra: Abonnements. https://gemini.google/subscriptions/
- HeyGen Research. (2026, 17. November). HeyGen Avatar 6 technical report. https://www.heygen.com/research/avatar-6-model
- HeyGen. (2026, 15. Oktober). Privacy policy. https://www.heygen.com/privacy
- HeyGen. (2026, 5. Mai). Biometric information privacy notice. https://www.heygen.com/biometric-privacy-notice
- HeyGen. (o. D.). HeyGen Avatar 6: AI avatar model that looks like you. https://www.heygen.com/models/heygen-avatar-6
- HeyGen. (o. D.). Pricing plans for creators and marketers. https://www.heygen.com/pricing
- HeyGen. (o. D.). Security practices. https://www.heygen.com/security
- Maguire, E. (2026, 17. November). Proton launches Lumo Desktop, bringing connectivity and automation to privacy-first AI. Proton. https://proton.me/blog/lumo-desktop-features
- OpenAI. (2025, 5. Februar). Introducing data residency in Europe. https://openai.com/index/introducing-data-residency-in-europe/
- OpenAI. (2026, 17. November). GPT-6.2 Astra and Sol. https://learn.chatgpt.com/docs/whats-new/gpt-62-astra-sol.md
- OpenAI. (2026, 17. November). Introducing GPT-6.2 Astra and Sol. https://openai.com/index/introducing-gpt-6-2-astra-sol/
- OpenAI. (2026, 24. August). Europe privacy policy. https://openai.com/policies/eu-privacy-policy/
- OpenAI. (2026, 8. Januar). Enterprise privacy at OpenAI. https://openai.com/enterprise-privacy/
- Perez, S. (2026, 17. November). Proton's Lumo, a privacy-focused alternative to ChatGPT and Claude, arrives on desktop. TechCrunch. https://techcrunch.com/2026/11/17/protons-lumo-a-privacy-focused-alternative-to-chatgpt-and-claude-arrives-on-desktop/
- PricingSaaS. (2026, 19. November). Wispr Flow brought Notetaker meeting notes to iPhone. https://pricingsaas.com/news/article/wisprflow-brought-notetaker-meeting-notes-to-iphone
- Proton. (2025, 4. August). Lumo security model: How Proton makes AI private. https://proton.me/blog/lumo-security-model
- Proton. (o. D.). About Lumo, the privacy-first AI assistant. https://proton.me/lumo
- Proton. (o. D.). Lumo pricing and plans. https://proton.me/lumo/pricing
- Proton. (o. D.). Private AI for business plans and pricing. https://proton.me/business/lumo/pricing
- TestingCatalog. (2026, 17. November). OpenAI launches GPT-6.2 Astra and Sol on ChatGPT and APIs. https://www.testingcatalog.com/openai-launches-gpt-6-2-astra-and-sol-on-chatgpt-and-apis.md
- Unite.AI. (2026, 18. November). Wispr Flow brings AI meeting notes to iPhone. https://www.unite.ai/wispr-flow-notetaker-iphone-meeting-notes/
- Wispr. (2026, 18. August). Data controls. https://wisprflow.ai/data-controls
- Wispr. (2026, 18. November). Wispr Flow Notetaker now goes with you. https://wisprflow.ai/post/notetaker-on-iphone
- Wispr. (2026, 19. August). Privacy policy. https://wisprflow.ai/privacy-policy
- Wispr. (o. D.). Enterprise privacy and security. https://wisprflow.ai/enterprise-privacy
- Wispr. (o. D.). Pricing. https://wisprflow.ai/pricing
