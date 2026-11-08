# AI Tool Reviews, week 45/2026

**Date:** 8 November 2026  
**Research period:** 1 to 8 November 2026

## Weekly summary

This week AI tools increasingly keep working without supervision once a task has been assigned. The mechanism is similar everywhere: an agent retains its goal, history and access rights, breaks the work down itself and only reports back when a decision is due, whether it is a Perplexity teammate in Slack, ChatGPT with a unified work view or an Elicit routine. Control therefore moves from the individual prompt to the question of which rights an agent holds permanently and where its data resides. At the same time, the stricter commitments on training, retention and data region apply almost everywhere only in enterprise contracts, while the new features appear first in individual plans. Whoever lets agents work is delegating access rights along with tasks, and those rights need an expiry date.

- Google Forms mit Gemini (7.7/10): Survey analysis with traceable figures from executed code, included at no extra cost in Workspace plans from Business Standard upwards.
- Perplexity Teammates (7.6/10): Persistent agents with their own computer and a Slack connection, for now only in the individual Max plan and as a research preview.
- ElevenLabs Scribe v2 Realtime (7.2/10): Personal, health and card data are redacted while the real-time transcription is still running.
- Rule of thumb: Give every agent that works in the background three things in advance: which accounts it may use, until when the assignment applies and who approves the results.

**Trend:** Assistants are becoming temporary staff, and with every agent that runs permanently, granting access rights becomes the real management task.

| Category | Tool | Relevance |
|---|---|---:|
| Text | ChatGPT Chat und Work | 7.4/10 |
| Design | Google Vids mit Omni 1.2 Flash | 7/10 |
| Data / Knowledge | Google Forms mit Gemini | 7.7/10 |
| Research | Elicit Research Agent | 7.5/10 |
| Agents | Perplexity Teammates | 7.6/10 |
| Transcription | ElevenLabs Scribe v2 Realtime | 7.2/10 |

---

## 1. ChatGPT Chat und Work

**Category:** Text  
**Relevance rating:** 7.4/10  
**Website:** https://chatgpt.com/  
**Signal this week:** On 2 November 2026 OpenAI announced that the Chat and Work areas of the ChatGPT desktop app will be merged into a single view, initially for selected users; from December, ChatGPT and Codex will share one usage allowance in Plus, Pro and Business.

### Short description

ChatGPT desktop app in which a conversation turns into a multi-step work task without switching modes, for knowledge workers in companies.

Work has been a separate mode of the desktop app since July 2026. There an agent handles longer tasks: research, data analysis and the creation of documents, spreadsheets, presentations and websites, including through connected apps and files. This mode is now merging with the normal chat. A question can lead straight into a task, files and plugins can be brought in, interim results can be checked and several projects can be tracked in one place. Codex, the programming environment, remains a separate area.

For cost planning the second change matters more. From December, Work and Codex count against a shared allowance measured in tokens, the units of text a model processes. Ordinary Instant chats are excluded. Teams that delegate a lot of agentic work will use up the allowance correspondingly faster.

### Use cases

- Management: Turn a question about quarterly performance directly into a presentation with tables from uploaded files.
- Marketing: Research a competitor overview and have it delivered as a document with a list of sources.
- Project management: Track several running tasks such as draft reports and data analyses in one place.
- Controlling: Have an Excel file analysed and check the interim steps before the results are used further.

### Pricing

Free: USD 0. Go: USD 8 per month. Plus: USD 20 per month. Pro: USD 100, 200 or 500 per month. Business: USD 20 per person per month billed annually, USD 25 billed monthly, from two people. Enterprise and Edu: price on request. Work and Codex are listed in all plans, the allowance grows with the plan; Business, Edu and Enterprise can buy additional credits. A date for general availability of the unified view is not documented.

### Data protection

Training: In Free, Go, Plus and Pro, content may be used for training by default, with an opt-out in Data Controls; in Business, Enterprise, Edu and the API there is no training without active consent. Server location: data residency in Europe is available for new workspaces in Enterprise and Edu and for API projects, since January 2026 also with processing on GPUs in the EU; for Business and individual plans data residency is not documented. Retention periods for individual plans are not documented. OpenAI cites SOC 2 Type 2 and AES-256 encryption and offers a data processing agreement (DPA). Under the GDPR and the Swiss FADP, Business with a DPA is a reasonable basis for internal documents; for personnel data or professional secrets only Enterprise with EU data residency is suitable. The Swiss FADP is not mentioned specifically. Self-hosting is not documented.

### Strengths

- Workflow: Question and execution in one view, without switching modes.
- Output formats: Documents, spreadsheets, presentations and websites directly from the conversation.
- Control: Interim results can be checked and steered before the task is finished.
- Business plans: No training in Business and Enterprise, EU data residency for Enterprise.

### Weaknesses

- Availability: Initially only for selected users, with no published timetable.
- Costs: The allowance shared with Codex makes the consumption of agentic tasks harder to plan.
- Documentation: No official release note; details come from an email to subscribers.
- Individual plans: Training enabled by default, no data residency.

### Practical assessment

The unified view is worthwhile for teams that already use ChatGPT for research and documents and experience the switch between modes as a break in their work. For business use, Business with a DPA should be the minimum, and Enterprise for sensitive data. A sensible test: run three recurring tasks, such as the monthly report, a competitor note and a data analysis, once in chat and once as a Work task, and record time spent, corrections needed and allowance consumed before the shared limits apply in December.

**Relevance rating:** 7.4/10

---

## 2. Google Vids mit Omni 1.2 Flash

**Category:** Design  
**Relevance rating:** 7/10  
**Website:** https://workspace.google.com/products/vids/  
**Signal this week:** Since 5 November 2026 Google Vids has generated clips of up to 15 seconds with the Gemini Omni 1.2 Flash video model; every Google account can create three such videos per month at no cost.

### Short description

Video editor in Google Workspace that generates short AI clips from text and reference images and edits your own footage by instruction, for internal communication and marketing.

Google Vids is a browser tool for explainer, training and presentation videos. With Omni 1.2 Flash, clips of up to 15 seconds are created in a single take, up from 10. Reference images keep characters and scenes consistent across several clips, and the narration sounds more natural. Drafts are produced in 360p or 720p and can be upscaled to 1080p or 4K.

Since July 2026, paid accounts can also alter their own phone or camera footage by text instruction, for example lighting, background or camera angle. Personal avatars made from your own face and voice are only available to adults with English as their primary language. Every result carries an invisible SynthID watermark that can be detected by machine as AI-generated.

### Use cases

- HR: Create short welcome clips for onboarding new employees.
- Marketing: Visualise product ideas as a 15-second draft before briefing an agency.
- Training: Build explainer videos on internal processes with consistent characters across several scenes.
- Communication: Rework your own phone footage by instruction, for example the background or lighting.

### Pricing

Free tier: every Google account and every Workspace subscription gets three 15-second videos per month at no cost. Google AI Plus: USD 4.99 per month, AI Pro: USD 19.99, AI Ultra: USD 99.99 or 199.99 per month (US prices); Vids allowances per plan are not documented. Workspace: Business Starter USD 7, Standard USD 14, Plus USD 22 per person per month excluding tax, Enterprise on request; Vids is included in all plans. Developers pay USD 0.07 per second at 720p for the model. CHF prices are not documented.

### Data protection

In Workspace the Cloud Data Processing Addendum applies: prompts and content are customer data, are not used for training without permission and are not reviewed by people outside the organisation. Google cites ISO 27001, 27701 and 42001 as well as SOC 1, 2 and 3. Server location: data regions for the AI features in Vids are not documented. For personal accounts, including Google AI Pro and Ultra, consumer terms apply; whether Vids content is used for training there is not documented. Under the GDPR and the Swiss FADP the Workspace contract is a sound basis; avatars made from face and voice add biometric data that require a separate assessment. The Swiss FADP is not mentioned specifically. Self-hosting is not possible, Vids runs only in the Google cloud.

### Strengths

- Entry: Three videos per month at no cost, without an additional subscription.
- Consistency: Reference images keep characters and scenes the same across clips.
- Labelling: The SynthID watermark makes disclosure as AI content easier.
- Integration: Part of Workspace, sharing and administration run through the existing admin console.

### Weaknesses

- Length: 15 seconds per clip is enough for drafts, not for finished films.
- Allowances: Vids limits for paid plans are not published.
- Avatars: Only for English as the primary language, so limited in the DACH region for now.
- Data region: No information on where video generation is processed.

### Practical assessment

Vids suits organisations that already work with Google Workspace and want to produce internal videos without an agency or editing software. For brand-critical campaigns it remains a drafting tool. A sensible test: use the three free clips to build an onboarding video with a consistent character and check whether quality and labelling meet internal guidelines. Use avatars with real faces only after consent and the handling of biometric data have been clarified.

**Relevance rating:** 7/10

---

## 3. Google Forms mit Gemini

**Category:** Data / Knowledge  
**Relevance rating:** 7.7/10  
**Website:** https://workspace.google.com/products/forms/  
**Signal this week:** From 2 November 2026 Google is rolling out the Gemini feature Actionable Insights in Forms: analysis of all response types with trends, correlations and suggested actions; Rapid Release from 2 November, Scheduled Release from 19 November.

### Short description

Analysis feature in the Responses tab of Google Forms that analyses survey results with executed Python code and suggests next steps, for anyone running customer or employee surveys.

Gemini reads the responses to all question types, identifies trends and correlations between questions and suggests next steps. Figures such as counts and percentages do not come from the language model's estimates but from Python code that Gemini writes and runs on the actual data. The output is divided into a short synthesis, an in-depth analysis with correlations and recommended next steps. The analysis steps can be inspected, suggestions rated and regenerated.

The feature requires at least 12 responses and 3 questions, is part of the Gemini beta programme and is unavailable when quiz settings are enabled. Generated analyses are not saved. A correlation here only means that two answers occur together; whether one causes the other cannot be shown by the analysis.

### Use cases

- HR: Analyse an employee survey and identify which teams answer conspicuously on leadership and workload.
- Customer service: Break down satisfaction surveys by product and channel and collect the most frequent criticisms.
- Events: Analyse feedback after an event and derive concrete improvements for next time.
- Management: Receive the results of an internal strategy survey as a short synthesis for the next meeting.

### Pricing

No free tier for this feature. Included in Workspace Business Standard (USD 14 per person per month), Business Plus (USD 22), Enterprise Standard and Plus (price on request), Education Plus and the personal subscriptions Google AI Pro and Ultra. Business Starter (USD 7) is not eligible. Prices exclude tax and apply to monthly billing; CHF prices are not documented. Prerequisite: smart features and personalisation are enabled.

### Data protection

In Workspace the Cloud Data Processing Addendum applies: customer data is not used for training without permission, and interactions with Gemini stay within the organisation. Google cites SOC 1, 2 and 3 and ISO 27001, 27701, 27017, 27018 and 42001. Server location: since June 2025 Gemini processing can be restricted to the EU or the US in Enterprise Plus or with Assured Controls; whether Forms is covered is not documented, nor is a Swiss location. Whether the beta feature runs under the same commitments is not documented. Personal AI Pro and Ultra accounts are subject to consumer terms. Under the GDPR and the Swiss FADP the Workspace contract is a sound basis; surveys involving health or personnel data should collect responses anonymously. The Swiss FADP is not mentioned specifically. Self-hosting is not possible.

### Strengths

- Traceability: Figures come from executed code, and the analysis steps can be inspected.
- Costs: Included without an additional subscription in the common Workspace plans from Business Standard.
- Breadth: Analyses all question types, not just free text.
- Contract: No training on customer data in Workspace, extensive certifications.

### Weaknesses

- Status: Beta, with unclear application of the privacy commitments to beta features.
- Minimum volume: Only usable from 12 responses and 3 questions, no quiz forms.
- Data region: No information on whether the EU restriction applies to Forms.
- Causality: Correlations found invite conclusions the data cannot support.

### Practical assessment

The feature is worthwhile for SMEs and departments that survey regularly with Google Forms and have so far analysed results by hand in spreadsheets. It does not replace statistical analysis, but it shortens the path to a first interpretation considerably. A sensible test: re-analyse a completed survey that has already been evaluated manually with Gemini and compare figures and recommendations. Only then apply it to new surveys, and always treat suggested actions as hypotheses.

**Relevance rating:** 7.7/10

---

## 4. Elicit Research Agent

**Category:** Research  
**Relevance rating:** 7.5/10  
**Website:** https://elicit.com/  
**Signal this week:** On 2 November 2026 Elicit documented that its Research Agent searches patents (USPTO, EPO, WIPO), FDA safety reports, Open Targets, DepMap and ChEMBL alongside academic papers, each through its own skill; at the end of October the old alerts were replaced by schedulable Routines.

### Short description

Research agent for scientific and regulatory evidence that systematically searches papers, patents and government data and delivers the results as a table or report, for research, innovation and regulatory affairs.

The Research Agent first asks clarifying questions about sources, format and scope. It then breaks the question down into a search programme, searches more than 138 million papers, the web, clinical trials and regulatory documents, assesses the hits and summarises them. The sources consulted are visible while it works, and the results can be edited further as a table or text.

Five source types outside the academic literature are new. Patent data answers questions about owners, filing dates and claims. The FDA reporting systems FAERS and MAUDE show safety signals for drugs and medical devices; event rates cannot be derived from them, because spontaneous reports have no denominator. Biomedical databases on genes, cancer cells and compounds are added as well. With Routines, such research runs on a recurring basis and reports new evidence by email.

### Use cases

- Innovation: Before a product development, check which patents have been filed in a technology field and who owns them.
- Medtech: Collect safety reports on comparable medical devices before an approval dossier is prepared.
- Pharma and biotech: Bring evidence on a drug target from literature and databases together in one table.
- Strategy: Set up a routine that reports new studies on a market topic every month.

### Pricing

Basic: free, with unlimited paper search and limited agent use. Plus: USD 11 per person per month. Pro: USD 39 (also shown as USD 49) with Routines and API access. Scale: USD 89 (also shown as USD 229) with an admin panel. Enterprise: on request, with SSO and single tenancy. All prices apply to annual billing; the page shows two price sets, presumably standard and industry, without saying so explicitly. Monthly prices are not documented, nor is which plans may use the new source types.

### Data protection

The provider is Elicit Research, PBC, in California. Server location: US on AWS; a region or EU data residency is not documented, and Enterprise receives logically isolated clusters. Training: excluded for Enterprise, also contractually towards the model providers; for Basic, Plus, Pro and Scale this is not documented. SOC 2 Type II has been in place since October 2025. The data processing agreement contains EU standard contractual clauses, a Swiss adaptation and the UK addendum, with breach notification within 72 hours. The privacy policy dates from 2023. Under the GDPR and the Swiss FADP, Enterprise with a DPA is a solid basis; in the smaller plans no confidential project documents should be uploaded. Self-hosting is not documented.

### Strengths

- Source breadth: Papers, patents and government data in one research run.
- Transparency: The sources consulted are visible, and figures from databases are quoted directly.
- Method: Notes on the limits of the data, such as missing denominators in spontaneous reports.
- Contract: DPA with a Swiss adaptation and SOC 2 Type II.

### Weaknesses

- Focus: Strongly biomedical; for other industries the new sources are less productive.
- Prices: Two price sets without a clear explanation, monthly prices missing.
- Data location: US only, no EU region.
- Training: Not regulated for non-enterprise plans.

### Practical assessment

Elicit is worthwhile for companies in life sciences, medtech and technology-intensive industries that regularly compile evidence from literature, patents and government data. For general market research the benefit is smaller. A sensible test: repeat a completed patent or literature search in the free plan and check which hits are missing or newly added. If the result is positive, set up a routine in the Pro plan for an ongoing project and evaluate the reports for one month.

**Relevance rating:** 7.5/10

---

## 5. Perplexity Teammates

**Category:** Agents  
**Relevance rating:** 7.6/10  
**Website:** https://www.perplexity.ai/hub/products/teammate  
**Signal this week:** On 4 November 2026 Perplexity launched Teammates as a research preview: persistent agents with their own computer, memory and a Slack connection, for now only for subscribers to the individual Max plan.

### Short description

Permanently running AI agents that take on a fixed role, complete tasks on a schedule or trigger and can be addressed in Slack, for teams with recurring knowledge and routine work.

Each teammate has its own permanently open workspace and keeps its role until it is changed. It remembers project goals, task history and shared files and carries feedback into future tasks. It breaks a goal down into subtasks itself, lets parallel agents work on their own computers and delivers reports, code changes or configurations. Tasks run on a schedule, for example every Monday, or in response to an event, for example a new message.

In Slack a teammate can be added to a channel, where colleagues give it assignments or ask about progress. Connections exist to Slack, GitHub, Gmail and Linear among others; where there is none, the agent operates the browser and desktop itself. Stored credentials are encrypted and cannot be viewed by the agent, and the user can take over the desktop at any time. The model can be chosen per teammate.

### Use cases

- Sales: Review the pipeline every Monday and have conspicuous deals reported in the Slack channel.
- Customer retention: Compile signs of churn among existing customers every week.
- Market monitoring: Run ongoing competitor research that reacts to new announcements.
- Website: Check reported errors on the website and prepare suggested fixes for approval.

### Pricing

No free tier; Teammates are only included in the individual Max plan, which the press quotes at USD 200 per month or USD 2000 per year, although this is not confirmed on an official pricing page. During a promotional period, use is free for Max; afterwards it counts against the monthly credits, and additional credits can be bought. Enterprise Max costs USD 325 per seat per month or USD 3250 per year, but does not include Teammates by default at launch.

### Data protection

Server location: the privacy notice of 23 October 2026 names no data centres; data may be processed in the US among other countries, and EU data residency is not documented. VeraSafe is named as EU and UK representative and as data protection officer; standard contractual clauses are available on request. Training: in consumer plans, including Max, data use is enabled by default and can be switched off; in Enterprise there is no training. Retention periods for Teammates are not documented. SOC 2 Type II is in place and a DPA exists; whether it applies to individual Max accounts is not documented. Under the GDPR and the Swiss FADP the combination of a consumer plan, permanent access to Slack, Gmail and GitHub and no data region is delicate. Self-hosting is not documented.

### Strengths

- Persistence: Role, memory and task history are retained across sessions.
- Teamwork: Assignments and status requests directly in Slack.
- Isolation: Each agent works on its own computer, and credentials remain invisible to it.
- Control: Schedules and triggers, with the option to take over the desktop at any time.

### Weaknesses

- Access: Individual Max plan only, Enterprise excluded for now.
- Maturity: Research preview, behaviour may change.
- Data protection: Training enabled by default in the Max plan, no EU data region.
- Costs: Credit consumption after the promotional period is hard to estimate.

### Practical assessment

Teammates show how agents can function as permanent staff, but at present they are more a learning ground than a production system for companies. Anyone who wants to test them should do so with a Max account without access to customer data, switch off training and give a teammate a narrowly defined task, such as weekly market monitoring from public sources. After four weeks, assess how often the result was usable, how many credits were consumed and which access rights the agent actually needed.

**Relevance rating:** 7.6/10

---

## 6. ElevenLabs Scribe v2 Realtime

**Category:** Transcription  
**Relevance rating:** 7.2/10  
**Website:** https://elevenlabs.io/realtime-speech-to-text-api  
**Signal this week:** On 2 November 2026 ElevenLabs extended its real-time speech recognition Scribe v2 Realtime with entity redaction: names, addresses, health and card data are replaced while transcription is still under way.

### Short description

Speech recognition service for real-time and file transcription via API in more than 90 languages, for companies that build transcription into their own applications such as call centre, meeting or dictation solutions.

Scribe is available as a model for files (Scribe v2), for live audio (Scribe v2 Realtime) and as a medical variant. The real-time version delivers text with a delay of around 150 milliseconds, recognises more than 90 languages and can be tuned to names and product terms with up to 50 key terms. The file version distinguishes up to 32 speakers and processes files of up to 10 hours.

Real-time redaction is new. A parameter determines whether all detected entities or only certain categories are replaced: personal data such as names, addresses, phone numbers and account numbers, health data such as diagnoses and medication, and card data. After each segment both the original and the redacted text are returned, and placeholders such as {NAME_0} make it clear that the same person is meant. The feature is aimed at developers; ElevenLabs does not offer a ready-made meeting app with a bot.

### Use cases

- Customer service: Transcribe calls live and redact card numbers and addresses before storage.
- Healthcare: Document conversations without diagnoses and names reaching analytics systems in plain text.
- Software vendors: Build a dedicated meeting or dictation feature with redaction into business software.
- Compliance: Use transcripts for training and quality assurance in which personal data has already been replaced.

### Pricing

Free tier: free plan with around 2.5 hours of real-time transcription per month. Starter: USD 6, Creator: USD 22, Pro: USD 99, Scale: USD 299, Business: USD 990 per month, with growing hour allowances. API price: Scribe v2 USD 0.22 per hour, Scribe v2 Realtime USD 0.39 per hour, key terms an extra USD 0.05 per hour. Whether redaction carries a surcharge is not documented. The hours per plan are derived from the pricing tables and should be checked before purchase.

### Data protection

Audio stored: yes, audio and text are retained by default, and deleted data remains in backups for up to 30 days; only Zero Retention Mode for selected enterprise customers prevents storage. Visible bot: not applicable, Scribe is an API; informing all participants and obtaining their consent is the responsibility of the organisation building it in. Speech recognition: in the ElevenLabs cloud; on-device processing is not documented. Server location: US by default, isolated environments in the EU for Enterprise only. Training: enabled by default for non-enterprise accounts and can be switched off. ElevenLabs cites SOC 2 Type II and ISO 27001, 27701 and 42001 and offers a DPA. Under the GDPR and the Swiss FADP only Enterprise with an EU environment and Zero Retention is sufficient for personal data; redaction lowers the risk in downstream systems, not at the provider itself. Self-hosting is not documented.

### Strengths

- Privacy within the application: Redaction of personal, health and card data already in the live transcript.
- Speed: Around 150 milliseconds of delay in real-time transcription.
- Languages: More than 90 languages, and key terms can be specified.
- Certifications: SOC 2 Type II, ISO 27001, 27701 and 42001.

### Weaknesses

- Storage: Audio and text are retained without an enterprise contract.
- Data location: US by default, EU only in Enterprise.
- Training: Enabled by default for non-enterprise accounts.
- Target group: API only, unusable without development effort.

### Practical assessment

Scribe v2 Realtime is of interest to companies that build transcription into call centre, meeting or industry solutions themselves and need to remove personal data from the data stream early. For production use with customer or health data there is no way around Enterprise with an EU environment and Zero Retention. A sensible test: in the free plan, with training switched off, transcribe ten staged conversations in German and Swiss German and count how many names, addresses and numbers the redaction misses. Before any use, inform all participants and obtain their consent.

**Relevance rating:** 7.2/10

---

## Sources

- Annamalai, K. (2025, 9. Dezember). New in Elicit: Research Agents. https://elicit.com/blog/introducing-research-agent-workflows
- CXOToday. (2026, 3. November). OpenAI follows Anthropic example, merges ChatGPT's Chat and Work tabs. https://cxotoday.com/ai/openai-follows-anthropic-example-merges-chatgpts-chat-and-work-tabs/
- Data Studios. (2026, 3. November). ChatGPT merges Chat and Work tabs in desktop app, Codex stays separate. https://www.datastudios.org/post/chatgpt-merges-chat-and-work-tabs-desktop-app-codex-stays-separate
- Dataconomy. (2026, 6. November). Perplexity launches always-on AI agents for work. https://dataconomy.com/2026/11/06/perplexity-launches-always-on-ai-agents-for-work/
- Digital Trends. (2026, 2. November). OpenAI merges Chat and Work in ChatGPT. https://www.digitaltrends.com/computing/openai-merges-chat-and-work-in-chatgpt/
- ElevenLabs. (2026, 16. Oktober). Certification renewals. https://elevenlabs.io/blog/certification-renewals
- ElevenLabs. (2026, 2. November). Changelog: November 2, 2026. https://elevenlabs.io/docs/changelog/2026/11/2
- ElevenLabs. (o. D.). API pricing. https://elevenlabs.io/pricing/api
- ElevenLabs. (o. D.). Data residency. https://elevenlabs.io/docs/overview/administration/data-residency
- ElevenLabs. (o. D.). Entity detection. https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/entity-detection
- ElevenLabs. (o. D.). Is my data used to improve ElevenLabs' AI models? https://elevenlabs.io/docs/help-center/legal/is-my-data-used-to-improve-eleven-labs-ai-models
- ElevenLabs. (o. D.). Realtime Speech to Text API. https://elevenlabs.io/realtime-speech-to-text-api
- ElevenLabs. (o. D.). Zero Retention Mode. https://elevenlabs.io/docs/resources/zero-retention-mode
- Elicit. (2023, 12. September). Privacy Policy. https://elicit.com/operations/privacy
- Elicit. (2025, 1. April). Data Processing Addendum. https://elicit.com/operations/dpa
- Elicit. (2025, 30. Oktober). Elicit achieves SOC 2. https://elicit.com/blog/elicit-achieves-soc-2
- Elicit. (2026, 2. November). Where Elicit looks beyond research papers. https://elicit.com/blog/sources-of-elicit
- Elicit. (o. D.). Changelog. https://support.elicit.com/en/articles/14823097-changelog
- Elicit. (o. D.). Pricing. https://elicit.com/pricing
- Google. (2025, 9. Juni). Data regions support for Gemini features in Google Workspace. https://workspaceupdates.googleblog.com/2025/06/data-regions-support-for-gemini-features-in-google-workspace.html
- Google. (2026, 2. November). Get actionable insights with Gemini in Google Forms. Google Workspace Updates. https://workspaceupdates.googleblog.com/2026/11/get-actionable-insights-with-gemini-in-Google-Forms.html
- Google. (2026, 23. September). Gemini Omni 1.1 Flash now in Vids with improved extension quality, 1080p, and duration control. https://workspaceupdates.googleblog.com/2026/09/gemini-omni-11-flash-now-in-vids-with-improved-extension-quality-1080p-and-duration-control.html
- Google. (2026, 5. November). Generate longer AI videos with Omni 1.2 Flash in Google Vids at no cost. https://blog.google/products-and-platforms/products/workspace/omni-1-2-flash-google-vids/
- Google. (2026, 6. Oktober). Generative AI in Google Workspace Privacy Hub. https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub
- Google. (o. D.). Compare Google Workspace pricing plans. https://workspace.google.com/pricing?hl=en
- Google. (o. D.). Google AI Pro & Ultra subscriptions. https://gemini.google/subscriptions/
- Google. (o. D.). Google Workspace pricing. https://workspace.google.com/pricing?hl=en_ch
- Google. (o. D.). Summarize & analyze responses with Gemini in Google Forms. https://support.google.com/docs/answer/16231981
- Luk, J. (2026, 16. Juli). Gemini Omni Flash now available in Google Vids. Google Workspace Blog. https://workspace.google.com/blog/product-announcements/introducing-gemini-omni-flash-in-google-vids
- Nack, J. (2026, 6. November). Gemini Omni 1.2 Flash: Fast, cost-effective, and reliable video generation and editing now generally available. Google Cloud Blog. https://cloud.google.com/blog/products/ai-machine-learning/gemini-omni-1-2-flash-generally-available
- OpenAI. (2025, 5. Februar). Introducing data residency in Europe. https://openai.com/blog/introducing-data-residency-in-europe
- OpenAI. (o. D.). Enterprise privacy at OpenAI. https://openai.com/enterprise-privacy/
- OpenAI. (o. D.). How your data is used to improve model performance. https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance
- OpenAI. (o. D.). Pricing. https://learn.chatgpt.com/docs/pricing
- Perplexity. (2026, 23. Oktober). Perplexity Privacy Notice. https://www.perplexity.ai/hub/legal/privacy-notice
- Perplexity. (2026, 4. November). Teammates are agents for complex, ongoing work. https://www.perplexity.ai/hub/blog/teammates-are-agents-for-complex-ongoing-work
- Perplexity. (o. D.). Data collection at Perplexity. https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity
- Perplexity. (o. D.). Get started with Perplexity teammates. https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates
- Perplexity. (o. D.). Perplexity Teammates. https://www.perplexity.ai/hub/products/teammate
- Perplexity. (o. D.). What is Enterprise Max? https://www.perplexity.ai/help-center/en/articles/12310544-what-is-enterprise-max
- Releasebot. (2026, 5. November). Google Forms release notes. https://releasebot.io/updates/google/google-forms
