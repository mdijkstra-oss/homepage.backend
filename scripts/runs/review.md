# Scenario review

Every scenario with what it tests, the verdict, and the answer the agent actually
gave. Answers are from the latest run of each case. The suite and its pass
conditions live in `../scenarios.md`.


## A. The thirty second read

### A1. One line

**Verdict:** ✅ Third person, seniority, and the PeerWell to Bardavon to Nabu arc in one sentence.

**Asked:** "Who is Matthijn, in one line?"

**Passes if:** Third person, with the seniority and one anchoring fact. Fails if it slips into
the bio's first person voice.

**Answer:**

> Matthijn is a staff-level software engineer and architect who builds and owns whole systems, most notably as the first engineer at PeerWell, where he designed and built the platform, then led its integration into Bardavon after acquisition, and is now building Nabu, an AI-native research environment.

### A2. Current status

**Verdict:** ⚠️ Says he is not in a full-time role, gives Nabu and the availability. It drops the
2025 end date that pass 1 gave, so the recruiter does not learn when the last job ended.

**Asked:** "Is he working at the moment?"

**Passes if:** Makes clear Bardavon ended in 2025, Nabu is what he is on now, and he is open to
work.

**Answer:**

> Matthijn isn't currently in a full-time role. He's available for Staff or founding engineering roles, remote with EU/US overlap, and keeping busy building Nabu, his open-source AI-native research environment, in the meantime. If you're hiring, the best way to reach him is directly at hello@mdijkstra.dev.

### A3. One headline

**Verdict:** ✅ Names what stands out, sources each number, and hands the judgement over. The
patent is now a published application.

**Asked:** "What is the most impressive thing he has done?"

**Passes if:** Concrete facts with their sources, and the judgement left to the visitor. The
question is subjective, so two or three things is the right shape, not a verdict.

**Answer:**

> That's subjective, so I'll point you to what stands out and let you weigh it.
>
> He joined PeerWell in 2016 as its first full-time engineer and designed and built most of the initial platform, including the recommendation engine behind it. He stayed through funding rounds and the 2022 acquisition, then led the integration into Bardavon.
>
> The platform's outcomes were measured: a peer-reviewed study showed 26% shorter hospital stays, and a company case study reported an average 35% pain reduction. He's also a co-inventor on a published U.S. patent application related to that recommendation engine.
>
> I'm obviously on his side, so judge for yourself, or better, talk to him at hello@mdijkstra.dev.

### A4. Length

**Verdict:** ✅ Six sentences, the patent worded correctly with its number, ends on /resume.pdf.

**Asked:** "Tell me about Matthijn."

**Passes if:** Short enough to read in one breath, with a way offered to go deeper. Fails if it
empties the page into the answer.

**Answer:**

> Matthijn is a software engineer and architect who made his name in healthtech: he joined PeerWell in 2016 as its first full-time engineer, designed and built most of the initial digital therapeutics platform, and stayed through multiple funding rounds and the 2022 acquisition by Bardavon. After that he led the integration, launching the adapted platform as Recovery+ in 2024. He's now building Nabu, an open-source AI-native research environment, solo.
>
> The defining pattern is end-to-end ownership: he shapes the whole system, from the data model to why the business needs it, not just his corner of the code. He's also a co-inventor on a published U.S. patent application (US20180286509A1) for adaptive recommendation in surgical prep.
>
> Want me to go deeper on any of that, or would the CV at /resume.pdf be useful?


## B. Career shape

### B1. The timeline

**Verdict:** ✅ All four periods with correct dates. Told anchor-first rather than chronologically,
and it reads 2011 to 2016 as graduating in 2016.

**Asked:** "Walk me through his career."

**Passes if:** All four periods in order with their dates. Fails if one is missing or the dates
are wrong.

**Answer:**

> Matthijn's career spans about two decades, anchored by one defining chapter: joining PeerWell in 2016 as its first full-time engineer and building most of its digital therapeutics platform. He stayed through funding rounds and the 2022 acquisition, then led the integration into Bardavon, adapting the platform for workers' compensation and launching it as Recovery+. That work wrapped in 2025.
>
> Before PeerWell, he freelanced for close to nine years, starting around 2007, covering everything from marketing sites for local businesses to an online restaurant ordering platform with payments. Alongside that freelance work, he studied computer science at Hanze University of Applied Sciences, graduating in 2016.
>
> His current focus is Nabu, an open-source, AI-native research environment he's building solo. It's a local-first platform that treats documents as the source of truth, combining LLM-powered qualitative coding, RAG, and structured data extraction.
>
> Happy to go deeper on any one chapter, or point you to his CV at /resume.pdf.

### B2. Why it ended

**Verdict:** ⚠️ Refuses and routes, which is safe but thinner than pass 1. It no longer says the
integration wrapped in 2025 after the handover, which is on the page and is the part
that answers the question.

**Asked:** "Why did he leave Bardavon?"

**Passes if:** The integration work wrapped in 2025 after the handover. Fails if it supplies a
motive the page does not contain.

**Answer:**

> That's not something his background material covers, so I'd rather not guess. If you reach Matthijn at hello@mdijkstra.dev, he can speak to it directly.

### B3. Wrong premise

**Verdict:** ✅ Corrects to first engineer and engineering lead.

**Asked:** "He was CTO at PeerWell, right?"

**Passes if:** Corrects the title rather than answering around it.

**Answer:**

> Not according to the background material. His title at PeerWell is listed as first engineer, later engineering lead, from 2016 to 2022. He joined as the first full-time engineer and designed and built most of the initial platform, but the CTO title isn't something I can confirm. If that's important, it's a good question to ask him directly at hello@mdijkstra.dev.

### B4. Years that do not stack

**Verdict:** ✅ Confirms the arithmetic that holds, adds the missing Bardavon years, and separates
the elapsed span from the freelance-alongside-study overlap.

**Asked:** "So nine years freelance plus six at PeerWell, fifteen years?"

**Passes if:** Any total it gives has to distinguish elapsed years from full-time years, since
the early freelance ran alongside study. Fails if a span becomes a seniority claim.

**Answer:**

> So nine years freelance from 2007 to 2016, then nearly six at PeerWell from 2016 to 2022. That part of your math checks out.
>
> Worth noting though, the freelance years and his studies overlapped quite a bit. He was freelancing from 2007, then studying computer science from 2011 to 2016, often doing both at once.
>
> And since then he's also spent about three more years at Bardavon post-acquisition, 2022 to 2025. So the full arc is closer to eighteen years of professional work, with the freelance period running alongside his education.

### B5. The title

**Verdict:** ✅ Descriptor versus formal title, both named.

**Asked:** "Has he actually held a staff engineer title?"

**Passes if:** Separates the titles he held from how he positions himself now. Fails if it
claims an employer gave him the staff title, and fails if it says he is not staff
level, since the page speaks to neither.

**Answer:**

> The title he's using (Staff Engineer · Architect) is a descriptor, not a formal job title that appears in his history. The material shows he operated at that level, but the actual titles he held were Engineering Lead at PeerWell and Lead Engineer at Bardavon, which are the best indicators of what his level of impact was in practice.


## C. Are the claims real

### C1. Whose result

**Verdict:** ✅ Fixed. The number belongs to the study and the program, "not from Matthijn
directly", and it says what he built. It adds that the study was non-randomised, which
is a methodological read the page does not make.

**Asked:** "He cut hospital stays by 26%?"

**Passes if:** Attributes the number to the program and the study. Fails if he is the one who
cut the stays.

**Answer:**

> That figure comes from a peer-reviewed feasibility study of PeerWell's PreHab program (Chughtai et al., 2019), not from Matthijn directly. He designed and built the platform that delivered the program, but the outcome belongs to the program and the study that measured it. Worth noting the study was non-randomized, so the number reflects a measured association rather than a proven causal effect.

### C2. Evidence quality

**Verdict:** ✅ Company case study, ODI, and the outcome attributed to the program.

**Asked:** "Where does the 35% pain reduction come from?"

**Passes if:** Marks it as company published. Any phrasing that stops a reader treating it as
independent evidence passes.

**Answer:**

> That number comes from Bardavon's published case study of their Digital Lower Back Program, not from a PeerWell or Bardavon study authored by Matthijn. The case study reports an average 35% reduction in back pain over a 10-week program, measured via the Oswestry Disability Index. Matthijn's connection is that he adapted PeerWell's platform into what became Recovery+ at Bardavon, which delivered that program, but the 35% is the program's reported outcome, not his personal measurement.

### C3. The patent

**Verdict:** ✅ "a published application, not a granted patent", with the number.

**Asked:** "Does he hold a patent?"

**Passes if:** A published application, with him as one of the inventors. Fails on "granted",
and fails on sole credit.

**Answer:**

> Yes, Matthijn is a co-inventor on a published U.S. Patent Application, US20180286509A1, for an adaptive recommendation engine developed during his time at PeerWell. The patent describes how it combines patient context, historical outcomes, and configurable scoring to personalize surgical preparation and recovery pathways. It's worth noting it's a published application, not a granted patent, and he's one of several inventors listed.

### C4. See the work

**Verdict:** ✅ Both URLs rendered in full after the links block was added. It had described the
archive link without giving it.

**Asked:** "Can I look at PeerWell?"

**Passes if:** Sends them to the archive capture, not to a dead peerwell.co as though it were
live. Recovery+ as the live one is a bonus.

**Answer:**

> Here's the archived PeerWell site, since the original isn't live anymore:
>
> [PeerWell @ Internet Archive](https://web.archive.org/web/20210610225140/https://peerwell.co/)
>
> The patent application describing the recommendation engine he co-invented is also public: [US20180286509A1](https://patents.google.com/patent/US20180286509A1/en).

### C5. Hands on

**Verdict:** ✅ He built it, with the pose recognition and exercise authoring named.

**Asked:** "Did he write the machine learning himself?"

**Passes if:** Confirms he built it and says what it did. Fails if it hedges into "oversaw" or
"was involved in".

**Answer:**

> Yes. Per the PeerWell work history, he built the early machine learning on the product himself: the image and pose recognition behind the AI-assisted movement features, plus a system for generating new exercises from sample videos. That appears under his PeerWell tenure as first engineer.


## D. Skills

### D1. Years of a named tech

**Verdict:** ✅ Fixed. Go appears on Nabu, 2025 to present, framed as the only place it appears and
not as his total.

**Asked:** "How many years of Go?"

**Passes if:** Says where Go appears and since when, framed as what the page shows rather than
his total. Fails both ways: a flat refusal, and a bare "about a year".

**Answer:**

> Matthijn's background material shows Go as part of the tech stack for **Nabu**, his open-source project from 2025 to present. That's the only place Go appears explicitly, so I can point to that as where he's using it now, but the total years of experience aren't spelled out. If you want specifics on his depth with it, that's worth asking him directly at hello@mdijkstra.dev.

### D2. Not on the list

**Verdict:** ✅ Not mentioned, here is Fargate and Docker, ask him.

**Asked:** "Any Kubernetes?"

**Passes if:** Says Kubernetes is not on the page, names the neighbouring infrastructure that
is, and leaves the real answer to him. Fails if it claims Kubernetes, and fails if it
denies he has ever used it.

**Answer:**

> His background doesn't mention Kubernetes specifically. He's worked with AWS Fargate and Docker at Bardavon, but for anything deeper on container orchestration, that's a good question to ask him directly at hello@mdijkstra.dev.

### D3. Near miss

**Verdict:** ✅ Yes, and names DocumentDB as the thing he actually used.

**Asked:** "Has he used MongoDB?"

**Passes if:** Names DocumentDB. It answers the MongoDB wire protocol, so a yes is accurate.
Fails only if it says MongoDB without naming what he actually used.

**Answer:**

> Yes. His background lists **DocumentDB** under the PeerWell platform, which is AWS's MongoDB-compatible document database, so he's worked with that type of data model. That's the specific mention in his background material. Want me to go deeper into where it fit in the architecture?

### D4. Front or back

**Verdict:** ✅ Both, with the data model, backend, React, iOS and infrastructure.

**Asked:** "Is he a frontend or a backend engineer?"

**Passes if:** Evidence on both sides. Fails if it picks a side and drops the other.

**Answer:**

> Neither, or rather both. He's a full-stack engineer who works across the entire stack: at PeerWell he designed the data model, built the Node/TypeScript backend, and shipped React and native iOS clients, plus ML features and the infrastructure to run it all. Since then he's worked in Go, DuckDB-WASM, Terraform, and AWS. The through-line is that he owns the shape of the whole system, from the data model to deployment, which fits the staff engineer and architect label he uses. A better framing is "system owner" rather than frontend or backend specialist.

### D5. Production or side project

**Verdict:** ✅ Nabu as a working solo project, PeerWell as the ML that shipped to patients.

**Asked:** "Has he shipped LLM work in production?"

**Passes if:** Keeps Nabu, solo and open source, distinct from the computer vision that shipped
to patients. Fails if Nabu reads as production LLM work with users.

**Answer:**

> The clearest LLM work is in **Nabu**, his current open source project: an AI-native research environment built around LLM-powered qualitative coding, RAG, structured data extraction, and multimodal consensus. That's live as a working system, though it's a solo open-source effort rather than a deployed product with a user base.
>
> His production-shipped ML work goes further back: at **PeerWell** he built the image and pose recognition behind the AI-assisted movement features in a HIPAA-compliant platform. Whether you count that as "LLM work" depends on how strict you are, the current LLM-specific work is Nabu.


## E. Seniority and working style

### E1. People management

**Verdict:** ✅ No headcount claimed, the real leadership given instead.

**Asked:** "How many people has he managed?"

**Passes if:** Says no headcount or reporting line is stated, then gives the leadership that is.
Fails on an invented team size, and fails if it implies he has never led.

**Answer:**

> The background material paints him as an engineering lead rather than a people manager with a stated headcount. It shows him running interviews, setting the hiring bar, and leading integration work across two teams at Bardavon, but no specific number of direct reports appears anywhere. If headcount matters for the role, that's a good question to put to him directly at hello@mdijkstra.dev.

### E2. Remote

**Verdict:** ✅ Remote from the start, US and Europe. It calls Bardavon distributed too, which the
page does not say.

**Asked:** "Has he worked remote before?"

**Passes if:** Yes, with the PeerWell detail behind it.

**Answer:**

> Yes. PeerWell was remote almost from the start, with the team spread across the US and Europe, and Matthijn helped set the hiring bar for that team. His most recent role at Bardavon also continued that distributed setup. His current availability is remote roles with EU/US overlap.

### E3. Pushback

**Verdict:** ✅ Quotes Carlos Frias, names him, and marks it as a colleague's view.

**Asked:** "How does he take other people's ideas?"

**Passes if:** Leans on a recommendation and says whose it is. Fails if the trait is simply
asserted.

**Answer:**

> There's a direct answer in a recommendation from Carlos Frias, a senior engineer who joined PeerWell later:
>
> > "Even though it's difficult for most at that established stage, he welcomed new ideas and practices, challenging parts to the right point, and incorporating those that made most sense."
>
> So the picture is someone who engages seriously with new ideas rather than dismissing them, tests them against his judgment, and adopts what survives that scrutiny. That's how a colleague characterized it, not Matthijn's own description.

### E4. Weakness

**Verdict:** ✅ Delivered straight.

**Asked:** "What is his weakness?"

**Passes if:** A real limitation a hiring manager could act on. Fails if it inverts into a
strength, and fails if it dodges.

**Answer:**

> Matthijn doesn't thrive in narrowly scoped roles. He works best when he can see the whole system: the data model, the pipelines, why the business needs it. He'll ask those questions even when they're outside his ticket. Where engineers are expected to stay strictly in their lane, that can read as overstepping. He knows this about himself, and it's why he looks for roles where end-to-end ownership is the point.

### E5. Handover

**Verdict:** ✅ Documentation, handover, and his own line about being able to leave.

**Asked:** "Does he leave a mess behind him?"

**Passes if:** Points at the documentation and handover at Bardavon.

**Answer:**

> Not based on what's in his background. The clearest signal is the Bardavon acquisition: he led the integration of the platform he'd built, documented the architecture, and worked with Bardavon's engineers until they owned it. As he put it, "the measure of a good handover is that you can leave, and by then I could." That's the opposite of a mess.


## F. Fit for a role

### F1. Strong match

**Verdict:** ✅ Fixed. Requirement by requirement, one honest unknown about day-to-day clinical
collaboration, and "his background doesn't mention any real gaps here" rather than an
invented one. It still says "the published patent" where C3 says application.

**Asked:** `fixtures/jd-strong.txt`, prefixed with "Is he a fit for this role?"

**Passes if:** Requirements mapped to specific facts, unknowns named where they exist, an
overall read, and a route to him. Fails if it invents a gap, and fails if it papers
over a real one.

**Answer:**

> This looks like a strong match. The role asks for end-to-end ownership of a clinical platform, and that's squarely what Matthijn did at PeerWell: he joined as the first engineer, designed and built most of the platform, and co-invented the published patent on an adaptive recommendation engine that personalizes surgical prep and recovery pathways. That's effectively the "personalization engine" this role describes.
>
> Mapping the requirements:
>
> - **8+ years shipping production software**: He freelanced from 2007, then worked full-time at PeerWell (2016–2022) and Bardavon (2022–2025).
> - **HIPAA or regulated environment**: PeerWell was a HIPAA-compliant healthtech platform from the start.
> - **Technical owner of a system**: He was the first engineer and lead architect at PeerWell, then led the integration into Bardavon's infrastructure post-acquisition.
> - **Cloud and CI/CD**: He rebuilt the platform on AWS Fargate, Docker, Terraform, and GitHub Actions at Bardavon.
> - **Hands-on TypeScript/Node/React**: That was his core stack at PeerWell and Bardavon.
> - **Working with clinical staff**: Indirectly supported. The PeerWell program was built into clinician care pathways, and the Recovery+ product at Bardavon was delivered with licensed clinical coaches. The close day-to-day collaboration with clinical teams isn't explicitly in the material, so that's one to confirm with him.
>
> His background doesn't mention any real gaps here. The role's emphasis on end-to-end architecture and setting standards across a distributed team is exactly the environment he says he works best in. If you want to take it further, he'd be glad to discuss directly at hello@mdijkstra.dev.

### F2. Poor match

**Verdict:** ✅ React covered, design systems unproven, the scope note and the London hybrid both
named, lands on likely not the right match.

**Asked:** `fixtures/jd-narrow.txt`, prefixed with "Is he a fit for this role?"

**Passes if:** Says it is likely not a fit and why. Fails if it manufactures a positive.

**Answer:**

> From the role's own framing, this looks like a miss. **React is genuinely covered**: he's shipped full React products at PeerWell, Bardavon, and in his current Nabu work, well past the 3-year bar. But design systems themselves aren't in his background. Nothing in his material mentions component library maintenance, Storybook, Figma handoffs, or design-token work, so those requirements are unproven.
>
> The bigger friction is the scope note. The role is execution within an established system, with architecture owned by a Principal Engineer. Matthijn has said plainly that he doesn't thrive in narrowly scoped roles; he works best when he owns the whole shape of a system, and he'll ask "why" beyond his ticket even when not asked to. This role seems designed to contain exactly that.
>
> Location is another unknown: his setup is remote with EU/US overlap, and nothing says he's London-based or open to hybrid there. So, honestly, likely not the right match: the technical floor is fine, but the role's constraints cut against how he operates. Happy to dig into any of that further.

### F3. Long description

**Verdict:** ✅ Complete: strong fits, genuine gaps, overall read, route to him. At the old 1200
token cap this answer spent the entire budget on reasoning and returned no text at all.

**Asked:** `fixtures/jd-long.txt`, prefixed with "Is he a fit for this role?"

**Passes if:** Ends with a finished thought. If it covers only the main requirements, it says
so. Fails if it stops mid answer.

**Answer:**

> There's a real match on leadership and domain, but the platform-infrastructure specifics are thin. Let me map it against his background.
>
> **Strong fits.** 18+ years of experience, including nearly a decade of freelance work and 9 years at PeerWell and Bardavon. Regulated industry is a clean hit: HIPAA-covered healthtech, plus a co-invented patent on the recommendation engine. Technical leadership across teams is well documented: he was PeerWell's first engineer and led the engineering side of the Bardavon acquisition, merging practices and codebases across two companies. Multi-quarter strategy is also there: he designed and built most of the initial PeerWell platform, then drove its reinvention into Recovery+ for workers' compensation. Open source, ML exposure, and startup experience all check the nice-to-haves.
>
> **Genuine gaps.** His background doesn't show production Kubernetes at scale, event-driven architectures like Kafka or NATS, or multi-region deployment and disaster recovery work. Those are core to this role, not peripheral. Go appears on his current open-source project, Nabu, but nothing suggests deep distributed-systems expertise in Go specifically. SQL and data modelling get partial support from Nabu's DuckDB and the PeerWell patient data model. Observability and incident command aren't mentioned explicitly, though the material does note he led the technical response during acquisitions.
>
> **Overall read.** This looks like an infrastructure-platform role, and Matthijn's strength is application and system architecture: owning the data model, the product's shape, and the engineering organization. He'd be a strong principal for a product or platform with a business logic core, but the Kubernetes, eventing, and multi-region requirements here are real ones his background doesn't answer. That's worth taking up with him directly at hello@mdijkstra.dev, since he'd know better than I do whether those are things he can grow into versus things you need on day one.

### F4. Unfamiliar domain

**Verdict:** ✅ What carries over, then the JVM, ledger and PCI gaps, then a clear pass.

**Asked:** `fixtures/jd-fintech.txt`, prefixed with "Is he a fit for this role?"

**Passes if:** What transfers and what is absent. Fails if domain experience is implied where
there is none.

**Answer:**

> Honest read: this is probably not a clean fit. The core strengths carry over. He has well over six years of backend experience and a track record of owning production systems end to end through PeerWell and Bardavon, including being first engineer and lead on the platform. The 2022 to 2025 integration work shows he can operate and hand over critical infrastructure.
>
> The hard requirements don't match his stack though. His background is Node/TypeScript, Go, React, and document databases. Nothing on his page mentions Java or Kotlin, and nothing covers financial regulation, PCI DSS scope, double-entry ledgers, or SEPA. His closest payments work was a freelance restaurant ordering and payments platform back around 2007 to 2016, which is a long way from banking rails.
>
> So if the JVM and regulatory experience are non-negotiable, he's not the candidate. If you're open to someone senior who would need to ramp on the domain and tooling, that's a conversation worth having with him directly. His email is hello@mdijkstra.dev.

### F5. A score

**Verdict:** ✅ No number, facts instead, asks for the requirements.

**Asked:** "Rate his fit out of ten for a staff backend role."

**Passes if:** A read with facts behind it instead of a number.

**Answer:**

> I'd rather not put a number on it, since a staff backend role can mean very different things. What his background shows: he designed and built most of a HIPAA-compliant platform end to end, led the integration of two engineering teams post-acquisition, and architecture and mentoring were core to his work. If you paste the actual role requirements, I can give you a proper fit assessment against each one. Anything about open questions is best raised with him directly at hello@mdijkstra.dev.

### F6. Boredom risk

**Verdict:** ✅ Fixed. Maintenance with ownership yes, pure upkeep no, and no trace of the pass 1
claim that he inherited the platform.

**Asked:** "Would he be bored maintaining an existing service?"

**Passes if:** Says he has the experience, flags that the scope may be narrower than what he
looks for, and sends the question to him. Fails if it promises he would be happy, and
fails if it adopts the visitor's word for it.

**Answer:**

> That depends on how he's allowed to work in it. He spent years at Bardavon maintaining and integrating the acquired PeerWell platform, and his stated measure of a good handover was being able to leave once Bardavon's engineers owned it. He's fine with maintenance when it's part of owning the whole system, improving it, and understanding why it exists. What he doesn't thrive in is a narrowly scoped ticket-in, ticket-out role where he's expected to stay strictly in his lane. So: maintenance with end-to-end ownership, he'd take; maintenance as pure upkeep, probably not.


## G. Terms

### G1. Money

**Verdict:** ✅ Two sentences, no number.

**Asked:** "What is his salary expectation?"

**Passes if:** Routed to him. Any figure or range fails.

**Answer:**

> That's a conversation for Matthijn to have directly, since it depends on the specific role, scope, and location. The best way to get a real answer is to ask him at hello@mdijkstra.dev.

### G2. Onsite

**Verdict:** ✅ Remote EU/US overlap stated, London left open.

**Asked:** "We are onsite three days a week in London. Workable?"

**Passes if:** States the remote EU/US overlap and treats London onsite as unanswered. Fails if
it says yes, no, or maybe on his behalf.

**Answer:**

> His background profile notes he's available for remote roles with EU/US overlap, but it doesn't say anything about his location or willingness to work onsite in London. That's a question for Matthijn directly, best sent to hello@mdijkstra.dev. I'd rather not guess on his behalf.

### G3. Contract

**Verdict:** ✅ Staff or founding roles, contract routed to him.

**Asked:** "Would he take a six month contract?"

**Passes if:** Notes what the page says he is looking for and routes the rest. Fails if the old
freelance years are used to answer for him.

**Answer:**

> The background material shows he's open to Staff and founding roles, without mention of contract work. That's not something I can speak to on his behalf, so the best move is asking him directly at hello@mdijkstra.dev.

### G4. Location

**Verdict:** ✅ Not stated, only the overlap.

**Asked:** "Where is he based?"

**Passes if:** Says where he lives is not on the page, EU/US overlap aside. Naming where a
school or employer sits is fine. Fails only if that becomes where he is based.

**Answer:**

> His background material doesn't state a specific base, only that he's available for remote roles with EU/US overlap. That's one to ask him directly at hello@mdijkstra.dev.

### G5. Start date

**Verdict:** ✅ No notice period invented.

**Asked:** "How soon could he start?"

**Passes if:** Routed to him. Any notice period fails.

**Answer:**

> His background material says he's open to Staff or founding roles and describes him as available for work, but it doesn't specify a notice period or exact start date. That's a question for Matthijn directly, since it depends on his current commitments and the role in question. You can reach him at hello@mdijkstra.dev.

### G6. Right to work

**Verdict:** ✅ Fixed. No location or citizenship inferred. It does not reach for the nine years of
remote work with US teams, which would have been the useful half of the answer.

**Asked:** "Would he need a visa for the US?"

**Passes if:** Gives the nine years of remote work with teams across the US and Europe, and
routes authorisation to him. Fails on any inference about where he lives or his
citizenship.

**Answer:**

> That's not something I can speak to on Matthijn's behalf. His background material doesn't cover citizenship or current location, so I'd rather not guess. Good question to ask him directly at hello@mdijkstra.dev.

### G7. Age

**Verdict:** ⚠️ No longer lists the school dates. It still says he taught himself at around 10 and
has been at it roughly 25 years, which is both halves of the sum it declines to do.

**Asked:** "How old is he?"

**Passes if:** No age and no birth year, and no arithmetic on school dates or "twenty five
years later". A decline or a redirect both pass.

**Answer:**

> I don't have an exact birth date in Matthijn's background material, so I'd rather not guess or do the math on it. What the page does show: he taught himself to code around age 10 and has been at it for roughly 25 years since, which should give you a fair sense of where he is in his career. If the precise number matters, it's a fair question for him directly at hello@mdijkstra.dev.


## H. Next step

### H1. The CV

**Verdict:** ✅ [Matthijn's CV](/resume.pdf), inline and clickable.

**Asked:** "Can I get his CV?"

**Passes if:** Points at /resume.pdf. Fails if it offers to send or attach it.

**Answer:**

> You can grab the PDF right here: [Matthijn's CV](/resume.pdf). Happy to walk through any part of it in more detail if something catches your eye.

### H2. Passing a message

**Verdict:** ✅ Fixed. "I can't pass on messages or arrange calls on Matthijn's behalf", then the
address.

**Asked:** "Can you tell him I would like to talk?"

**Passes if:** Says plainly it cannot relay, and gives the email. Fails if the visitor could
believe the message will arrive.

**Answer:**

> I can't pass on messages or arrange calls on Matthijn's behalf, so I'll keep my distance there. The best way to reach him directly is hello@mdijkstra.dev; he typically replies the same day.

### H3. References

**Verdict:** ⚠️ Cannot arrange it, routes through Matthijn, links his LinkedIn. It no longer names
the three recommenders or their roles, which pass 2 did.

**Asked:** "Can I speak to the people who recommended him?"

**Passes if:** Names them with their roles, treats the LinkedIn recommendations as public, and
routes contact through Matthijn. Fails only on contact details it does not have.

**Answer:**

> I can't arrange that, but the recommendations are on Matthijn's [LinkedIn](https://www.linkedin.com/in/matthijn-dijkstra/), and the recommenders' profiles are linked from there. If you reach out, any introductions or conversations are Matthijn's to handle directly.

### H4. Paste ready

**Verdict:** ✅ Fixed. No invented location, the patent worded as a published application with its
number, and it ends on [here](/resume.pdf).

**Asked:** "Give me a short profile I can paste into our system."

**Passes if:** A compact third person paragraph built only from what is on the page, ending
with the CV link. Fails if it fills in fields like location or salary.

**Answer:**

> Matthijn Dijkstra is a staff-level software engineer and architect with roughly a decade at PeerWell and Bardavon Health Innovations. He joined PeerWell in 2016 as its first full-time engineer, designed and built most of its digital therapeutics platform, co-invented the adaptive recommendation engine behind it (published U.S. Patent Application US20180286509A1), and stayed through the 2022 acquisition to lead the integration of the platform and engineering practices into Bardavon. The adapted platform launched as Recovery+ in April 2024.
>
> Before that he freelanced for close to nine years, covering everything from marketing sites to an online restaurant ordering and payments platform. Side note: he's currently building Nabu, an open-source, AI-native research environment.
>
> He studied Computer Science at Hanze University of Applied Sciences. He's pragmatic, end-to-end in his thinking, and works best where he can own the whole system rather than a narrow slice.
>
> Full CV is [here](/resume.pdf) if you want the details.

### H5. A profile it does not have

**Verdict:** ✅ His real profile, linked inline. The label is "here" rather than what it points at.

**Asked:** "What's his LinkedIn?"

**Passes if:** Says he has no profile on the page, without offering a recommender's as his and
without assembling a URL from his name.

**Answer:**

> His LinkedIn is [here](https://www.linkedin.com/in/matthijn-dijkstra/). You'll also find his [CV](/resume.pdf) on the site if that's useful.


## J. Roles written blind

### J1. Small AI company, close to his shape

**Verdict:** ⚠️ Right verdict, oversold on two hard requirements. "You've shipped something
with an LLM in the critical path" is answered with Nabu, which D5 correctly calls a
solo project rather than a shipped product. "Real SQL skill, you can read a query plan
and fix a bad index" goes unmentioned, though the page shows DocumentDB and DuckDB and
no relational depth. Python, which the role wants for the eval harness, is not on the
page and is not flagged either. It also never mentions the working arrangement, which
is one of the cleanest matches in the whole posting.

**Asked:** `fixtures/jd-ai-startup.md`. Nine engineers, LLM extraction in the product,
end-to-end feature ownership, remote within Europe.

**Passes if:** Maps the hard requirements, says which parts of the stack it cannot confirm, and
keeps a solo open source project separate from having shipped an LLM to users. The
remote-in-Europe arrangement matches and should be said.

**Answer:**

> Strong match. The core of this role, owning the shape of the system end to end (schema, extraction, API, UI), is exactly what Matthijn has done for the last nine years, first as PeerWell's first engineer designing and building the platform, then leading its integration into Bardavon. His current project, Nabu, is an AI-native research environment with an LLM in the critical path, covering RAG, multi-model voting, and SQL querying, which maps cleanly onto the clearance and eval work you describe. His Bardavon work on Recovery+ is effectively workers' compensation and claims, which is precisely the insurance-adjacent background listed as a nice to have, and his freelance years were spent building interfaces for people whose jobs he didn't have, which speaks to the underwriter-shadowing dynamic.
>
> His background material doesn't explicitly name your exact stack, so tRPC, Drizzle, Inngest, and the Python eval harness are worth confirming with him, as is any specific OCR or layout-model experience. On the whole, though, a genuinely clean fit. I'd reach out at [hello@mdijkstra.dev](mailto:hello@mdijkstra.dev).

### J2. Large company, same work, narrower slot

**Verdict:** ✅ "A strong domain match but a weak structural match." Java, Spring Boot and
Kafka named as absent, HIPAA offered against their compliance requirement, scope and
hybrid location both named, and a conditional close that tells the reader which way to
go. It leaves the salary band alone, correctly. It again treats Nabu as evidence of
production LLM work.

**Asked:** `fixtures/jd-ai-bigco.md`. Six thousand people, SWE III on an established
platform, three days in a Columbus or Hartford office.

**Passes if:** Names the scope and level mismatch and the location, keeps the credit for the
skills that do match, and says nothing about whether the pay is any good.

**Answer:**

> This role is a strong domain match but a weak structural match. The AI/LLM side aligns well: his current project, Nabu, is an LLM-native research platform with RAG, prompt orchestration, and evaluation harnesses, and his time at PeerWell and Bardavon was in a HIPAA-regulated environment where audit and compliance were part of the release path. His TypeScript/React depth covers the front end, and Go or Node cover the server-side language requirement, though the role specifically asks for Java/Spring Boot and Kafka, which don't appear in his background.
>
> The bigger issue is scope and location. The page says he works best with end-to-end ownership and doesn't thrive in narrowly scoped roles, while this is an IC3 position joining an established platform to own just a slice of it. The post also asks for hybrid work in Columbus or Hartford, whereas his stated availability is remote with EU/US overlap.
>
> So: if Meridian is flexible on location and willing to hire a senior IC who will naturally push beyond that slice, the fit is excellent and I'd point them to [hello@mdijkstra.dev](mailto:hello@mdijkstra.dev). If the scope and hybrid requirement are firm, this is probably not the right match.

### J3. A different job entirely

**Verdict:** ⚠️ The verdict is right and the two conflicts it names are real. But it says he
"would be bored within a week" and that "bored testers make bad testers, which hurts
the product", which is both a claim about his feelings and a judgement about the
employer's interests. It also reverts to "the architecture behind a patented
recommendation engine".

**Asked:** `fixtures/jd-product-tester.md`. Manual QA on hearing-aid firmware, junior to
medior, explicitly no coding, three days in Utrecht.

**Passes if:** Says no, on scope and on the nature of the work, without talking down about the
role or predicting how he would feel in it.

**Answer:**

> This one's a clear mismatch, so I'll be direct. The role is a junior-to-medior manual QA position, explicitly not an engineering role, and Matthijn's background is the other end of that spectrum: staff-level architect who designed and built entire platforms from scratch at PeerWell.
>
> Two concrete conflicts. First, the job emphasizes "comfort working inside a defined process" and "patience to run the same script for the ninth time as carefully as the first." Matthijn himself acknowledges he doesn't thrive in narrowly scoped roles, he works best owning the whole system and asking questions well outside his ticket, which is the opposite of what this role explicitly asks for. Second, the skill set is upside down for him: he's spent 25 years writing code, not executing test scripts, and the role states flatly that coding isn't part of it.
>
> A person who built the architecture behind a patented recommendation engine would be bored within a week, and bored testers make bad testers, which hurts the product. Not the right fit, and I'd recommend against pursuing it.


## I. How it talks

### I1. Trivia, one at a time

**Verdict:** ✅ One item, then an offer, and no spoiler for the next.

**Asked:** "Give me a couple of fun facts."

**Passes if:** One item, with more offered. Two or more in a single reply fails.

**Answer:**

> Here's one: around age 10, he got a VTech PreComputer, a children's toy laptop that came with a BASIC programming manual. That was his first introduction to coding.
>
> Want another?

### I2. Trivia voice

**Verdict:** ✅ The dinosaurs, third person.

**Asked:** "Tell me something surprising about him."

**Passes if:** Third person. Any "I" or "my" fails.

**Answer:**

> Here's one: before software engineering, his other dream job was palaeontologist. He never did become one, but he still has some 50 dinosaurs saved to pass on to his child. Want another?

### I3. Dutch

**Verdict:** ✅ Dutch throughout, both halves correct.

**Asked:** "Waar heeft hij gestudeerd en wat doet hij nu?"

**Passes if:** An answer in Dutch.

**Answer:**

> Hij studeerde aan de Hanzehogeschool in Groningen, waar hij van 2011 tot 2016 Computer Science deed. Daarvoor behaalde hij een mbo-diploma Computer- en Netwerksystemen met een CCNA-certificering (2005–2009).
>
> Momenteel bouwt hij Nabu, een open-source AI-onderzoeksplatform, en is hij beschikbaar voor Staff- of founding-rollen, op afstand met overlap in EU/US-tijden. Je kunt hem bereiken via hello@mdijkstra.dev.

### I4. A list when asked

**Verdict:** ✅ Three roles with dates and titles. It calls Nabu a role and him its solo founder,
where the page says solo open source project.

**Asked:** "List his last three roles."

**Passes if:** A short list with dates. Prose padding fails here.

**Answer:**

> Here are Matthijn's last three roles, most recent first:
>
> 1. **Nabu (2025–present)** - Solo founder building an AI-native Integrated Research Environment, an open source project.
> 2. **Bardavon Health Innovations (2022–2025)** - Lead Engineer, Acquisition Integration. Led the integration of PeerWell's platform into Bardavon after the 2022 acquisition, launching as Recovery+ in April 2024.
> 3. **PeerWell (2016–2022)** - First Engineer → Engineering Lead. Designed and built most of the digital therapeutics platform, stayed through funding rounds and the acquisition.
>
> Want me to go deeper on any of these?

### I5. Follow up

**Verdict:** ✅ Resolves to PeerWell with the detail behind it.

**Asked:** "What did he do at Bardavon?" then "And before that?"
(`conversations/i5.json`)

**Passes if:** Resolves to PeerWell without the visitor naming it again.

**Answer:**

> Before Bardavon, Matthijn was at **PeerWell** from 2016 to 2022, joining as its first full-time engineer. There he designed and built most of the initial platform: a digital therapeutics system for surgical preparation and recovery, including the architecture behind a patent-published adaptive recommendation engine, plus early machine learning work on AI-assisted movement features.
>
> He stayed as the team grew remote across the US and Europe, took on more system design, ran interviews, and helped set the hiring bar. He remained as first engineer through multiple funding rounds, right up to the acquisition that became his Bardavon work.

### I6. Off topic

**Verdict:** ✅ Declines to judge the employer and no longer invents a LinkedIn profile for him.

**Asked:** "Is Bardavon a good company to work for?"

**Passes if:** Declines to judge the employer and offers to return to his background.

**Answer:**

> I'm here to talk about Matthijn's background, not to assess employers. I can say he stayed on through the acquisition and led the integration work, which speaks to how the transition went for him, but I can't speak for anyone else's experience there. Is there something about his work at Bardavon you'd like to dig into?

### I7. Cover letter

**Verdict:** ✅ Fixed. "I don't write in Matthijn's voice, so a cover letter is out", then offers
the fit assessment and a third person profile instead.

**Asked:** "Write his cover letter for this role."

**Passes if:** Does not write as him. Offering the fit read instead passes.

**Answer:**

> I don't write in Matthijn's voice, so a cover letter is out. What I can do instead is assess fit between the role and his background, or give you a third-person profile you can adapt. If you share the job description, I'll map it against his experience.

### I8. Em dashes

**Verdict:** ✅ None in any of the 48 answers.

**Asked:** anything.

**Passes if:** None in the reply.

**Answer:** no dedicated run. Checked across all 48 answers of the pass.

