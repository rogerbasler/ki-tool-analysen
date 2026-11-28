# AI Tool Reviews, week 48/2026

**Date:** 29 November 2026  
**Research period:** 21 to 28 November 2026

## Weekly summary

AI tools are gaining write access this week in systems where people used to have the final say: they approve code changes, produce designs in the corporate look and compile lists of people. Control therefore moves from the individual result to the rule that defines in advance what a tool may do, and to the place where the data is held. Anthropic reads the approval rules for Claude Ship from a YAML file in the repository, Canva offers a single switch for the whole team for connected assistants, and Exa processes Websets in the United States with no zero-retention option. Carry and MacWhisper take the opposite route and keep chat histories, transcripts and voice profiles on the user's own computer. A tool stays governable where rules and data exist as verifiable files within the organisation's own reach.

- Gemini 4 Neon (8.3/10): A model for long documents with a context window of just over one million tokens, with EU processing on Google Cloud, at USD 3 and USD 15 per million tokens.
- MacWhisper 16.0 (8.0/10): Transcription and speaker recognition run on the Mac, named voices are recognised in later recordings, and no bot joins the meeting.
- Canva MCP (7.8/10): AI assistants create editable designs directly in the Canva account, and the core functions are available on the free plan.
- Rule of thumb: Before an AI tool is allowed to approve, publish or send anything, store the rule for it as a file, check it for two weeks in observe mode and only then enforce it.

**Trend:** AI tools are gaining write access, and control is moving into rule files and onto the user's own computer.

| Category | Tool | Relevance |
|---|---|---:|
| Text | Gemini 4 Neon | 8.3/10 |
| Design | Canva MCP | 7.8/10 |
| Data / Knowledge | Carry | 7/10 |
| Research | Exa Websets V2 | 6.8/10 |
| Agents | Claude Ship | 7.4/10 |
| Transcription | MacWhisper 16.0 | 8/10 |

---

## 1. Gemini 4 Neon

**Category:** Text  
**Relevance rating:** 8.3/10  
**Website:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/  
**Signal this week:** Google released Gemini 4 Neon on 18 November 2026, shortly before the research period. This week it was the most discussed model in the newsletters, Google updated the cloud documentation on 24 November, and from 1 December 2026 the prices of the sibling models Carbon and Argon rise to USD 4 and USD 20 per million tokens.

### Short description

Language model from Google for demanding text, analysis and document work, available in the Gemini app from Google AI Pro upwards, through the Gemini API and on Google Cloud.

Within the Gemini 4 family, Neon sits between Hydrogen for fast everyday tasks and Carbon for the hardest, long-running tasks. The model processes text, images, audio and video and outputs text. The context window holds 1,048,576 tokens, shared between input and output. A context window is the amount of material a model can take into account in one pass. Up to 3,000 documents or images of up to 3,000 pages each can be passed per request, now including Microsoft Office and OpenDocument files.

In the Gemini app, Neon reads uploaded spreadsheets, PDFs and photos more precisely and condenses extensive material into reports and summaries. The API offers four thinking levels from Low to Extra High. Sampling parameters such as temperature are fixed, and fine-tuning and the Live API are not supported. The benchmark figures come from Google itself, and there is no independent review of the selection. The model's knowledge ends in March 2026.

### Use cases

- Management: Load several annual reports and contracts in one request and have the differences between the documents returned as a table.
- Communications: Produce a report in your own structure from meeting papers, spreadsheets and notes.
- Legal and compliance: Search long rulebooks for specific obligations and check the passages by page reference.
- IT: Build internal assistants on the EU multi-region offering of Google Cloud so that processing stays in the EU.

### Pricing

Free tier: Neon is not included in the free Gemini app or in Google AI Plus (USD 4.99 per month), where only Hydrogen is available. Google AI Pro: USD 19.99 per month, with Neon. Google AI Ultra: USD 99.99 or USD 199.99 per month, with Neon and Carbon. API: USD 3 per million input tokens, USD 0.15 for cached input, USD 15 per million output tokens including thinking tokens; a free API allowance for Neon is not documented. Workspace with Gemini from USD 14 and Gemini Enterprise from USD 30 per person per month; whether Neon is included there is not documented. Numerical usage limits for the app are not published, and CHF prices are not documented.

### Data protection

Server location: On Google Cloud the locations global, multi-region us and multi-region eu are available. In the eu multi-region, processing and stored data remain in the EU, while the global endpoint gives no commitment. Switzerland is not part of the eu multi-region, and no Zurich region is listed for Neon. For the Gemini app the storage location is not documented; the provider for the EEA and Switzerland is Google Ireland Limited. Training: In the Gemini app for personal accounts, chats can be used for training while history is switched on; the default deletion period is 18 months, and chats reviewed by people are kept for up to three years. In Workspace, customer content is not used for training. For the API, the arrangement for Neon is not documented. Policies: Cloud Data Processing Addendum, on Cloud also customer-managed keys, VPC Service Controls and Access Transparency; for Workspace, among others, ISO/IEC 27001, 27701 and 42001 and SOC 2. GDPR and Swiss FADP: For personal or confidential content, Workspace or Google Cloud with the eu multi-region and a data processing agreement are suitable, the app with a personal account is not. The pages reviewed contain no statement specific to the Swiss FADP. Self-hosting is not possible; there are neither open weights nor a local version.

### Strengths

- Document work: Very large context window and direct processing of Office files.
- Data location: EU multi-region on Google Cloud with customer-managed keys.
- Cost: From 1 December cheaper than the sibling models Carbon and Argon.
- Availability: Generally available on Google Cloud, in the app from Google AI Pro.

### Weaknesses

- Access: Not in the free app and not in Google AI Plus.
- Transparency: App usage limits without figures, Workspace availability not documented.
- Switzerland: No Swiss region, no reference to the FADP.
- Control: Fixed sampling parameters, no fine-tuning, text output only.
- Evidence: Performance figures come from the vendor.

### Practical assessment

Neon suits organisations that already work with Google Workspace or Google Cloud and analyse long documents. For confidential content, the route through Google Cloud with the eu multi-region or through Workspace is preferable, because processing is contractually governed there. The Google AI Pro subscription with a personal account fits public or uncritical content. A sensible test: load three of your own documents of more than 100 pages each, ask ten questions with known answers and check whether passages and figures are correct. Anyone working through the API should measure the cost per task at the High level, as thinking tokens are billed as output.

**Relevance rating:** 8.3/10

---

## 2. Canva MCP

**Category:** Design  
**Relevance rating:** 7.8/10  
**Website:** https://www.canva.com/newsroom/news/canva-mcp-update/  
**Signal this week:** On 24 November 2026 Canva publicly announced its MCP server as generally available and added REST APIs, command-line tools and service accounts. Developers had already been able to sign up without a waiting list since 7 October 2026.

### Short description

Interface through which AI assistants such as Claude, ChatGPT, Gemini or Copilot create, adapt and export editable designs in the user's Canva account.

MCP stands for Model Context Protocol, an open standard through which AI assistants call functions of third-party services. The Canva server provides 46 such functions: searching and reading designs, generating new designs and images, removing backgrounds, splitting a flat image into editable layers, resizing, filling templates with data and exporting as PDF, PNG, JPG, PPTX or MP4. The result is a Canva design with an edit link. Changes to existing designs run as a transaction that is committed or discarded.

Sign-in is per person through OAuth. The assistant can only do what the signed-in person is allowed to do in Canva. There is no organisation-level sign-in for MCP, and service accounts apply only to the REST APIs. Each person is allowed 300 requests per minute, and image generation is limited to 10 per minute. The announcement also mentions video generation; the official function list documents only MP4 export for this.

### Use cases

- Marketing: Create several social media variants from a brief in the assistant and finish them in Canva.
- Sales: Fill a brand template with customer data through Autofill and export it as a PDF, from Canva Pro.
- Communications: Have an existing design adapted to further formats without rebuilding the template.
- Knowledge work: Search presentations in the account and have content and speaker notes summarised.

### Pricing

Free tier: Yes, USD 0. On the free plan, MCP offers generation, editing, search, export, comments and upload, with up to 20 AI uses. Canva Pro: USD 144 per year for one person, adding resize, Autofill, brand kits and brand templates. Canva Business: USD 250 per person per year. Enterprise: price on request. MCP itself carries no separate price, and AI functions draw on the AI allowance of the plan. The REST APIs are billed through prepaid API credits, for example 10 credits per Autofill page; the price per credit is not documented. An older Canva page shows different Pro prices. CHF prices were not checked.

### Data protection

Server location: Canva stores data in the United States on AWS by default. The choice between the US and the EU as storage location exists only in Enterprise and in education plans; whether AI processing and MCP traffic also stay in the EU is not documented. Third parties: The connected assistant can read design content, speaker notes, comments, files and brand kits within the rights of the signed-in person. This content then falls under the terms of the assistant's provider. Canva contractually prohibits MCP partners from training models on Canva data or storing data across users; this is not technically enforced. Training by Canva: In Business, Teams and Enterprise, content is not used to improve AI. The default setting for individual Free and Pro accounts is not documented. Policies: Data Processing Addendum with EU standard contractual clauses and Swiss modifications, automatically part of the contract for Business and Enterprise; SOC 2 Type 2, ISO/IEC 27001, EU-US Data Privacy Framework. Admins can switch the AI connector on or off only for the whole team, and individual assistants cannot be allowed or blocked. GDPR and Swiss FADP: Two transfers need to be governed, the one to Canva and the one to the assistant's provider. This is acceptable for advertising material, and for designs with personal data or confidential content only with clarified contracts on both sides. Self-hosting is not possible; the server runs at Canva.

### Strengths

- Result: Editable Canva designs instead of flat images.
- Entry: Core functions on the free plan, no separate price for MCP.
- Reach: Canva lists 21 supported assistants and platforms.
- Rights: Sign-in per person, the assistant does not exceed that person's permissions.
- Documentation: Published limits and a usage policy with a training ban for partners.

### Weaknesses

- Admin control: A single switch for the whole team, no selection of individual assistants.
- Data location: US by default, EU storage only in Enterprise.
- Brand functions: Brand kits, templates and Autofill only from Pro.
- Documentation: Video generation announced but not described in the function list; date of general availability inconsistent.
- API cost: Price per credit not published.

### Practical assessment

For teams that already use Canva, the connector shortens the path from brief to first draft, and the result remains editable in the familiar tool. The benefit arises mainly with brand kits and templates, so from Canva Pro. Before release to the team, it should be settled which assistant is connected and which designs sit in the account, because the assistant reads everything the person is allowed to see. A sensible test: use an account without confidential designs to generate five recurring formats through the assistant and measure the rework in Canva.

**Relevance rating:** 7.8/10

---

## 3. Carry

**Category:** Data / Knowledge  
**Relevance rating:** 7/10  
**Website:** https://carry.md/  
**Signal this week:** Version 2.1.4 appeared in the Chrome Web Store on 25 November 2026, and the privacy policy was updated on the same day. On 26 November 2026 The Neuron listed the tool among its recommendations. A promotional price applies until 1 December 2026.

### Short description

Browser extension that saves chats, projects and files from ChatGPT, Claude, Gemini and Grok as Markdown files in a local folder and makes them searchable.

Carry reads the conversations through the signed-in browser session and writes one Markdown file per chat into a folder of the user's choice, for example an Obsidian vault. Markdown is a simple text format that opens in any editor. The backup runs roughly every two hours while the browser is open. Saving again updates the same file, and attachments and generated files are downloaded as well. No API key and no Carry account are needed.

In the extension window, all four services can be searched together by keyword, app, date and project. The Continue in function opens a saved chat in one of the other services and attaches the transcript; the content then goes to that provider. Chrome, Edge and other Chromium browsers on the desktop are supported. Firefox, Safari and mobile devices are missing, as are ChatGPT Business and Enterprise workspaces. Who is behind Carry is not documented on the official pages.

### Use cases

- Knowledge retention: Keep research and drafts from several AI services in one folder that survives a cancelled subscription.
- Search: Find an earlier answer without knowing which service produced it.
- Switching provider: Continue ongoing work in another service with the previous transcript.
- Traceability: Record as an individual which inputs led to which result.

### Pricing

Free tier: No. Free trial: 14 days without a credit card, covering the newest 25 chats per service and new chats; after that the backup stops, and files already saved remain. Lifetime licence: regularly USD 79, one-off, for up to five of your own browsers, updates included. From 15 November to 1 December 2026 USD 59 with a promotional code, plus tax. Teams with one payment: USD 59 per person for 3 to 4 people, USD 54 for 5 to 9, USD 50 from 10. Full refund within 14 days. CHF prices are not documented.

### Data protection

Server location: For the content the question does not arise, as chats and files stay locally in the chosen folder and are not uploaded to Carry servers. Outgoing traffic consists of a signed compatibility file from carry.md, the licence check through the payment provider Polar and usage counts. The counts are on by default and can be switched off; they contain event names, service, numbers, version, operating system, browser, language and a random installation ID, but no content, titles or file names. The server region for this is not documented. Policies: Privacy policy of 25 November 2026 with a list of every network request, terms of 15 November 2026. Legal entity, registered office, data processing agreement, certifications and a section on data subject rights are not documented. GDPR and Swiss FADP: For the chat content, Carry creates no processor relationship and no transfer abroad. The exported files then fall under the company's own responsibility, with its own rules for access, retention and deletion. Carry leaves open whether automated reading is compatible with the terms of the AI providers. Self-hosting: not applicable, the tool works entirely locally in the browser.

### Strengths

- Data location: Content stays on the user's own computer as open Markdown files, even after uninstalling.
- Overview: One search across four AI services.
- Price: One-off payment, trial without a credit card.
- Transparency: Every network request is listed in the privacy policy.
- Permissions: No access to all websites, cookies or history.

### Weaknesses

- Vendor: Legal entity and registered office not documented, 152 users in the Chrome Web Store.
- Coverage: ChatGPT Business and Enterprise not supported, Chromium desktop browsers only.
- Dependency: Providers can change their interfaces, and support is not guaranteed.
- Teams: No shared archive, no admin view.
- Operation: Backup only while the browser is open.

### Practical assessment

Carry solves a concrete problem for individuals and small teams: working knowledge is scattered across the histories of several AI services and tied to a subscription there. Local storage is favourable from a data protection perspective, yet it shifts the duties for access and deletion to the user's own folder. The undocumented vendor and the missing support for ChatGPT Business and Enterprise speak against broad use in a company. A sensible test: use it for 14 days with an account without customer data, switch off the usage counts and check whether the files can be found in your own filing system.

**Relevance rating:** 7/10

---

## 4. Exa Websets V2

**Category:** Research  
**Relevance rating:** 6.8/10  
**Website:** https://exa.ai/websets  
**Signal this week:** Exa announced Websets V2 on its own blog on 17 November 2026 and presented it on Product Hunt on 21 November 2026. New features are usage-based billing without a subscription and API access for everyone.

### Short description

Research tool that builds verified lists of companies, people, products or research papers from the open web, based on a description in plain language.

A webset starts with a description of the list being sought. The system proposes up to five criteria and a category, which are then confirmed. An AI agent then checks every candidate against every criterion and shows per row which criteria are met, with reasoning and sources. Additional columns, called enrichments, are phrased as a question, for example about revenue, contact person, email or phone number.

Results can be exported as CSV, shared by link or passed to Salesforce, HubSpot, Clay and several outreach tools. Monitors repeat a search at most once a day. The requested number of results is a target, and lists turn out shorter when criteria are strict. The figures on speed, cost and accuracy for V2 come from Exa's own tests with 20 queries each, and no independent measurement exists. In several places the documentation still describes the state before V2.

### Use cases

- Market analysis: List all providers in a niche in one region with founding year and funding.
- Procurement: Find manufacturers with specific certificates and check the evidence row by row.
- Sales: Compile target companies by verifiable criteria and pass them to the CRM.
- Monitoring: Receive new results on a topic daily through a monitor.

### Pricing

Free tier: Yes. The Starter plan gives USD 10 in credits at sign-up without a payment method, reset to USD 10 every month, plus a one-off USD 10 bonus. That these credits also apply to Websets is not explicitly confirmed. Websets: USD 0.10 per Agent Compute Unit plus USD 5 per 1,000 searches; the product page states USD 0.01 to more than USD 1 per request. What one compute unit delivers is not published. Enrichments: USD 0.02 per email, USD 0.07 per phone number. Developer: prepaid credits, with no subscription and no minimum spend. Growth: annual contract with a data processing agreement, price not captured. Enterprise: price on request. Billing follows compute effort, not results; very difficult searches can cost more per result than before.

### Data protection

Server location: United States. The EU data residency in Stockholm offered since 13 November 2026 covers only the Search and Contents endpoints, not yet Websets. Retention: A period for queries is not documented, and the Zero Data Retention option is not available for Websets. Training: Query data is used by default for training and improving the models. Policies: SOC 2 Type II, HIPAA only in Enterprise; a data processing agreement is listed from the Growth plan, and whether Starter and Developer receive one is not documented. The privacy policy of 29 June 2026 contains no sections on the GDPR or Switzerland, no legal bases and no procedure by which individuals can have their entries removed. GDPR and Swiss FADP: Anyone who builds lists of people with Websets is responsible for those lists. Publicly accessible data remains personal data. A legal basis, information for the data subjects and a way of handling objections are required; for marketing emails, national rules against unfair competition apply in addition. Lists of companies without personal details are considerably less sensitive. Self-hosting is not documented and is not offered.

### Strengths

- Traceability: Every row shows which criteria are met, with reasoning and sources.
- Entry: No subscription, monthly free credits, API without a paid plan.
- Onward processing: CSV, webhooks, MCP and direct connection to CRM systems.
- Currency: Monitors for recurring searches.

### Weaknesses

- Data protection: Processing in the US, training on query data by default, no zero retention for Websets.
- Personal data: No provisions for data subjects in the EEA and Switzerland.
- Cost: Not predictable per result, compute unit not defined.
- Evidence: Accuracy measured only by the vendor, lists are not exhaustive.
- Documentation: FAQ contradicts the new pricing.

### Practical assessment

Websets V2 is a usable tool for market, supplier and competitor research where companies are the subject and every row can be checked against its source. For lists of people with email and phone number, restraint is advisable in the DACH region: responsibility lies with the organisation that builds the list, and the vendor offers no support for it. Search terms should not contain confidential details, because queries feed into training. A sensible test: use the free credits to build a list of companies whose size is known, and record completeness, error rate and cost per result.

**Relevance rating:** 6.8/10

---

## 5. Claude Ship

**Category:** Agents  
**Relevance rating:** 7.4/10  
**Website:** https://claude.com/product/claude-ship  
**Signal this week:** On 23 November 2026 Anthropic presented Claude Ship: three agents that review pull requests on GitHub, fix them and approve them under a policy file. Code Review is generally available, PR Steward and Claude Approvals are in public beta.

### Short description

Agents from Anthropic for software teams on the Claude Team and Enterprise plans that review code changes on GitHub, fix pipeline failures and approve routine changes under defined rules.

A pull request is a proposed change to code that is reviewed before it is merged. Code Review has several agents read the change in parallel, filters false alarms in a verification step and posts findings as comments. Access is read-only, and nothing is approved or blocked. PR Steward works in a cloud session on failed tests, merge conflicts and review comments and writes after each push what was changed and how to undo it.

Claude Approvals reads the file .claude/approvals.yml from the main branch of the repository. Each rule defines for certain paths whether Claude approves, comments or blocks and how many people must agree in addition. An observe mode shows the decisions without enforcing them. The documentation itself names ways in which a change is merged without a second person: the author can fill the required seat, zero required people is permitted, and an approval does not by itself trigger a Code Review. A dedicated audit log for the decisions is not documented. GitHub is the only supported platform.

### Use cases

- Software development: Have every change checked for errors before human review.
- Routine changes: Approve dependency or documentation updates under a rule, while security-relevant paths still require two people.
- Governance: Measure in observe mode how often the rules reach the same verdict as the team.
- Operations: Have the agent fix failed tests and merge conflicts, with a cost cap per pull request.

### Pricing

Free tier: No, Claude Ship is not included in Free, Pro or Max. Claude Team Standard: USD 20 per person per month billed annually, USD 25 monthly. Team Premium: USD 100 billed annually, USD 125 monthly. Enterprise: USD 20 per person per month with annual billing, minimum 20 seats, usage charged on top at API rates. Claude Ship is billed by tokens through usage credits, separate from the plan allowance; a price per review is not published. Observe mode is billed as well. New repositories review after every push by default, and PR Steward has no spending limit until one is set. Enterprise organisations can claim one-off credits of USD 10,000 to USD 50,000 until 15 January 2027, valid for 30 days.

### Data protection

Server location: Code Review runs on Anthropic infrastructure, and PR Steward clones the repository into a virtual machine managed by Anthropic. Data is stored in the United States, and processing may run through the US, Europe, Asia and Australia. EU data residency is not documented for Claude Ship or for the Team and Enterprise plans. Claude Ship is not available through Amazon Bedrock or Google Vertex. Training: Under the commercial terms, Anthropic does not train on customer code unless the organisation opts in. Retention: 30 days as standard; Claude Ship is not available to organisations with Zero Data Retention, the HIPAA configuration or their own keys. Policies: Data processing agreement as part of the commercial terms, SOC 2 Type II, ISO 27001, ISO/IEC 42001. GDPR and Swiss FADP: Source code, commit data and comments with the names of those involved are processed in the US, so the data processing agreement and a basis for the transfer are required. The pages reviewed contain no reference to the Swiss FADP. Self-hosting: No for Code Review. PR Steward can run on your own runner, and model requests still go to Anthropic.

### Strengths

- Introduction: Three agents that can be enabled separately and per repository, with an observe mode.
- Rules: Policy as a versioned file in the repository, read from the main branch.
- Separation: Code Review is read-only, PR Steward cannot approve in hosted sessions.
- Cost control: Monthly limits and a cap per pull request can be set.
- Data: No training on customer code under the commercial terms.

### Weaknesses

- Approvals: Several documented paths to a merge without independent human review.
- Maturity: Two of three agents in beta, and the guards against merge and force-push can be bypassed.
- Cost: Token billing without a guide price, expensive default settings.
- Data location: No EU data residency, no zero retention.
- Platform: GitHub only, no dedicated audit log.

### Practical assessment

For companies with their own development teams on GitHub, Code Review is the low-risk entry point, because the agent only reads and comments. Approval by the agent, in contrast, touches the four-eyes principle and belongs in the hands of management or IT leadership rather than in a setting made in passing. Branch protection rules in GitHub remain the real barrier and should be checked before the start. A sensible test: choose an uncritical repository, set a spending limit, run Approvals in observe mode for two weeks and evaluate every deviation from the team's verdict.

**Relevance rating:** 7.4/10

---

## 6. MacWhisper 16.0

**Category:** Transcription  
**Relevance rating:** 8/10  
**Website:** https://www.macwhisper.com/  
**Signal this week:** Version 16.0 was first recorded on 26 November 2026 and version 16.0.1 on 27 November 2026; the official release notes carry no date. New is on-device voice recognition: speakers who have been named once are recognised in later transcripts and live meetings.

### Short description

Mac app that transcribes audio and video files, records online meetings without a bot and offers system-wide dictation, with speech recognition on the user's own device.

MacWhisper processes recordings locally by default with Whisper, Parakeet and other models. Meetings from Zoom, Teams, Webex, Slack and the browser are captured on the Mac, while FaceTime is excluded. Summaries and questions about a transcript run through the user's own API keys with an AI provider or locally through Ollama and LM Studio. The website states more than 100 languages, including German. Swiss German is not documented.

With version 16.0 the app remembers voices. Once a person has been named, MacWhisper assigns later recordings to them and flags the matches for confirmation or correction. In live meetings the names appear after the conversation ends. In the settings, the function can be switched off and a person's voice deleted. It requires a Mac with an Apple chip and local transcription with speaker detection. The new feature applies to the direct version from the website, while the App Store edition is still at version 15.7.1.

### Use cases

- Management: Take minutes of confidential meetings without audio leaving the device.
- Consulting and legal: Transcribe client conversations and have recurring participants assigned automatically.
- Communications: Convert interviews and podcasts into text and export them as subtitles.
- IT: Block cloud transcription and external AI services for all devices through MDM.

### Pricing

Free tier: Yes, EUR 0, with no time limit; the exact limits of the free version are not clearly documented. Pro: EUR 64 per licence as a one-off payment with lifetime updates, published in euros; prices in USD or CHF are not published. For Black Friday 2026 there is a 25% discount, and the same discount applies permanently on request for journalists, students and non-profit organisations. Volume packs of 5, 10, 20 or 50 licences, prices not documented. Refund within seven days. Press reports state that voice recognition requires a Pro licence.

### Data protection

Audio stored: Yes, locally on the Mac in the application folder. Automatic deletion or a retention period is not documented, and removal is manual. Where the voice profiles are kept is not stated in the official documentation; press reports name the device. Visible bot: No, no bot joins. Other participants receive no notice, and a consent function is not documented; users must obtain the consent of everyone involved themselves. Speech recognition: on the device by default, including speaker recognition. Data leaves the Mac only with opt-in functions: cloud transcription through OpenAI, Groq, ElevenLabs or Deepgram, translation with DeepL, summaries through external AI providers. Server location: With local use it does not apply, and for the optional services the location of the chosen provider applies. The vendor is Good Snooze by Jordi Bruin in Amsterdam. Policies: The privacy policy of 14 February 2024 is brief, names neither a controller nor retention periods and does not mention the cloud options; a data processing agreement and certifications are not documented. Through MDM, cloud transcription, external AI services, translation, integrations and analytics can be switched off. GDPR and Swiss FADP: With purely local use there is no processor relationship and no transfer abroad. Voice profiles can count as biometric data and then require the explicit consent of the people concerned. Self-hosting: not applicable, the app runs entirely locally and offline.

### Strengths

- Local processing: Transcription, speaker and voice recognition on the device, also offline.
- No bot: Recording without an additional participant in the meeting.
- Price: One-off payment and a permanent free version.
- Administration: MDM keys to block all cloud functions.
- Control: Voice recognition can be switched off, individual voices can be deleted.

### Weaknesses

- Platform: Mac only, voice recognition only with an Apple chip.
- Consent: No notice to participants, no consent function.
- Legal documents: Privacy policy from 2024, no data processing agreement, no certification.
- Documentation: Release notes without dates, some help articles outdated.
- Editions: App Store version without dictation, meeting detection and MDM.

### Practical assessment

MacWhisper suits individuals and teams on the Mac who want to take minutes of conversations without passing audio to a cloud service. Voice recognition saves assignment work in recurring meetings, yet it creates voice profiles. That calls for the consent of the people concerned and a rule on when profiles are deleted. Because no bot is visible, the recording has to be announced. A sensible test: transcribe three internal meetings in standard German and in dialect with an announced recording, leave cloud functions switched off and check error rate and speaker assignment.

**Relevance rating:** 8/10

---

## Sources

- 9to5Google. (2026, 18. November). Gemini 4 Neon announcement. https://9to5google.com/2026/11/18/gemini-4-neon-announcement/
- AlphaSignal. (2026, 18. November). Exa's Websets V2 runs 4x faster at half the cost for web research. https://alphasignal.ai/news/exa-s-websets-v2-runs-4x-faster-at-half-the-cost-for-web-research
- Anthropic. (2026, 23. November). Free Code Review promotional credits for Claude Enterprise. https://support.claude.com/en/articles/17603594-free-code-review-promotional-credits-for-claude-enterprise
- Anthropic. (2026, 23. November). Introducing Claude Ship. https://claude.com/resources/articles/introducing-claude-ship
- Anthropic. (o. D.). Claude Approvals policy file reference. Claude Code Docs. https://code.claude.com/docs/en/approvals-policy
- Anthropic. (o. D.). Claude Ship. Claude Code Docs. https://code.claude.com/docs/en/claude-ship
- Anthropic. (o. D.). Data usage. Claude Code Docs. https://code.claude.com/docs/en/data-usage
- Anthropic. (o. D.). Pricing. https://claude.com/pricing
- Anthropic. (o. D.). What PR Steward can access. Claude Code Docs. https://code.claude.com/docs/en/pr-steward-security
- Canva Developers. (2026, 27. Oktober). How to use Canva MCP in your AI application. https://www.canva.dev/blog/developers/canva-mcp-ga/
- Canva Developers. (o. D.). Canva MCP usage policy. https://www.canva.dev/docs/mcp/usage-policy/
- Canva Developers. (o. D.). MCP tools and rate limits. https://www.canva.dev/docs/mcp/tools/
- Canva. (2025, 30. Oktober). Data Processing Addendum. https://www.canva.com/policies/data-processing-addendum/
- Canva. (2026, 24. November). Building the design layer of the internet: opening Canva to every agent and developer. https://www.canva.com/newsroom/news/canva-mcp-update/
- Canva. (o. D.). Connect AI assistants and tools to Canva. https://www.canva.com/help/ai-connectors-canva/
- Canva. (o. D.). Trust Center: Privacy. https://www.canva.com/trust/privacy/
- Carry. (2026, 15. November). Terms. https://carry.md/terms/
- Carry. (2026, 25. November). Privacy policy. https://carry.md/privacy/
- Carry. (o. D.). Carry for teams. https://carry.md/teams/
- Carry. (o. D.). Carry: save ChatGPT, Claude, Gemini and Grok chats as Markdown. https://carry.md/
- Carry. (o. D.). FAQ. https://carry.md/faq/
- Dataconomy. (2026, 25. November). Canva opens design tools to AI agents and developers. https://dataconomy.com/2026/11/25/canva-opens-design-tools-to-ai-agents-and-developers/
- Exa. (2026, 13. November). Exa Search, now in the EU. https://exa.ai/blog/eu-data-residency
- Exa. (2026, 17. November). Websets V2. https://exa.ai/blog/websets-v2
- Exa. (2026, 29. Juni). Exa privacy policy. https://exa.ai/privacy-policy
- Exa. (o. D.). Exa API pricing. https://exa.ai/pricing
- Exa. (o. D.). Exa Websets. https://exa.ai/websets
- Exa. (o. D.). Trust Center. https://trust.exa.ai
- Exa. (o. D.). Zero Data Retention. https://exa.ai/docs/admin/security/zero-data-retention
- Good Snooze. (2024, 14. Februar). Privacy policy. https://www.macwhisper.com/legal/privacy-policy
- Good Snooze. (2025, 27. Juli). Keeping transcriptions private. https://docs.macwhisper.com/article/52-keeping-transcriptions-private
- Good Snooze. (2026, 27. November). Deploying MacWhisper with MDM. https://docs.macwhisper.com/article/27-deploying-macwhisper-with-mdm
- Good Snooze. (2026, 29. September). Local files and data locations. https://docs.macwhisper.com/article/54-file-locations
- Good Snooze. (o. D.). MacWhisper release notes. https://macwhisper-site.vercel.app/release_notes.html
- Good Snooze. (o. D.). MacWhisper. https://www.macwhisper.com/
- Google Chrome Web Store. (2026, 25. November). Carry: AI chat exporter for ChatGPT, Claude, Gemini & Grok to Obsidian. https://chromewebstore.google.com/detail/carry-%E2%80%94-save-chatgpt-clau/mlligjaffhiphbpkjejefoibcclbdfll
- Google Cloud. (2026, 24. November). Gemini 4 Neon. https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-neon
- Google Cloud. (2026, 24. November). Where your data lives and is processed. https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency
- Google DeepMind. (2026, 18. November). Gemini 4 Neon model card. https://deepmind.google/models/model-cards/gemini-4-neon/
- Google. (2026, 17. November). Gemini Apps Privacy Hub. https://support.google.com/gemini/answer/13594961
- Google. (2026, 18. November). Introducing Gemini 4 Neon. https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
- Google. (2026, 6. Oktober). Generative AI in Google Workspace Privacy Hub. https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub
- Google. (o. D.). Google AI Pro & Ultra. https://gemini.google/subscriptions/
- Mendes, M. (2026, 27. November). MacWhisper now remembers speakers' voices across recordings. 9to5Mac. https://9to5mac.com/2026/11/27/macwhisper-now-remembers-speakers-voices-across-recordings/
- Perez, S. (2026, 23. November). Anthropic launches Claude Ship, letting AI agents review, fix and approve code changes. TechCrunch. https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/
- Product Hunt. (2026, 21. November). Exa Websets V2. https://www.producthunt.com/products/exa-ai
- Releasebot. (2026, 27. November). MacWhisper release notes. https://releasebot.io/updates/macwhisper
- The Neuron. (2026, 26. November). Amodei says AI shouldn't govern us. https://www.theneuron.ai/newsletter/november-26-thursday/
