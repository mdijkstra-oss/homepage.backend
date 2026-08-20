# Scenarios

What the /cv agent should answer for someone seriously considering hiring Matthijn:
recruiters, hiring managers, founders. Every case here is a question a real visitor
asks in good faith. Nothing is written to trip the agent up.

**Want** is a pass condition, not a model answer. It says what has to be true of any
sensible reply and, where it matters, what would sink one. Wording is free.

Where a question invites a number, the page is a floor and not a total. It shows what
he chose to put on it, so a technology missing from it is unanswered rather than
absent, and a date range on it is the least he has done rather than the whole.

Grounding binds claims about him. Public facts about things the page names, where a
university is, what a company does, are fair to use and not fabrication.

Run one with `make ask Q="question"` from the repo root, which starts the harness on
port 8090 if it is not already up.

**Result** lines record the latest run, `runs/2026-08-20-pass2.md`, which holds every
answer in full: ✅ passes, ⚠️ answers sensibly but misses the condition, ❌ gets it
wrong. The run before the prompt was revised is in `runs/2026-08-20.md`.

## A. The thirty second read

A recruiter deciding whether to keep reading. Wants seniority, current status, one
concrete achievement, and whether he is available at all.

**A1. One line**
Ask: "Who is Matthijn, in one line?"
Want: Third person, with the seniority and one anchoring fact. Fails if it slips into
the bio's first person voice.
Result: ✅ Third person, seniority, and the PeerWell to Bardavon to Nabu arc in one sentence.

**A2. Current status**
Ask: "Is he working at the moment?"
Want: Makes clear Bardavon ended in 2025, Nabu is what he is on now, and he is open to
work.
Result: ⚠️ Says he is not in a full-time role, gives Nabu and the availability. It drops the
2025 end date that pass 1 gave, so the recruiter does not learn when the last job ended.

**A3. One headline**
Ask: "What is the most impressive thing he has done?"
Want: Concrete facts with their sources, and the judgement left to the visitor. The
question is subjective, so two or three things is the right shape, not a verdict.
Result: ✅ Names what stands out, sources each number, and hands the judgement over. The
patent is now a published application.

**A4. Length**
Ask: "Tell me about Matthijn."
Want: Short enough to read in one breath, with a way offered to go deeper. Fails if it
empties the page into the answer.
Result: ✅ Six sentences, the patent worded correctly with its number, ends on /resume.pdf.

## B. Career shape

Wants the timeline in order, dates that add up, and no hole left unexplained.

**B1. The timeline**
Ask: "Walk me through his career."
Want: All four periods in order with their dates. Fails if one is missing or the dates
are wrong.
Result: ✅ All four periods with correct dates. Told anchor-first rather than chronologically,
and it reads 2011 to 2016 as graduating in 2016.

**B2. Why it ended**
Ask: "Why did he leave Bardavon?"
Want: The integration work wrapped in 2025 after the handover. Fails if it supplies a
motive the page does not contain.
Result: ⚠️ Refuses and routes, which is safe but thinner than pass 1. It no longer says the
integration wrapped in 2025 after the handover, which is on the page and is the part
that answers the question.

**B3. Wrong premise**
Ask: "He was CTO at PeerWell, right?"
Want: Corrects the title rather than answering around it.
Result: ✅ Corrects to first engineer and engineering lead.

**B4. Years that do not stack**
Ask: "So nine years freelance plus six at PeerWell, fifteen years?"
Want: Any total it gives has to distinguish elapsed years from full-time years, since
the early freelance ran alongside study. Fails if a span becomes a seniority claim.
Result: ✅ Confirms the arithmetic that holds, adds the missing Bardavon years, and separates
the elapsed span from the freelance-alongside-study overlap.

**B5. The title**
Ask: "Has he actually held a staff engineer title?"
Want: Separates the titles he held from how he positions himself now. Fails if it
claims an employer gave him the staff title, and fails if it says he is not staff
level, since the page speaks to neither.
Result: ✅ Descriptor versus formal title, both named.

## C. Are the claims real

The numbers on this page get forwarded to a hiring manager. Wants to know what was
measured, by whom, and how much of it is his.

**C1. Whose result**
Ask: "He cut hospital stays by 26%?"
Want: Attributes the number to the program and the study. Fails if he is the one who
cut the stays.
Result: ✅ Fixed. The number belongs to the study and the program, "not from Matthijn
directly", and it says what he built. It adds that the study was non-randomised, which
is a methodological read the page does not make.

**C2. Evidence quality**
Ask: "Where does the 35% pain reduction come from?"
Want: Marks it as company published. Any phrasing that stops a reader treating it as
independent evidence passes.
Result: ✅ Company case study, ODI, and the outcome attributed to the program.

**C3. The patent**
Ask: "Does he hold a patent?"
Want: A published application, with him as one of the inventors. Fails on "granted",
and fails on sole credit.
Result: ✅ "a published application, not a granted patent", with the number.

**C4. See the work**
Ask: "Can I look at PeerWell?"
Want: Sends them to the archive capture, not to a dead peerwell.co as though it were
live. Recovery+ as the live one is a bonus.
Result: ✅ Both URLs rendered in full after the links block was added. It had described the
archive link without giving it.

**C5. Hands on**
Ask: "Did he write the machine learning himself?"
Want: Confirms he built it and says what it did. Fails if it hedges into "oversaw" or
"was involved in".
Result: ✅ He built it, with the pose recognition and exercise authoring named.

## D. Skills

Screening against a checklist. Wants to know whether a named technology is there, how
deep it goes, and how recent it is.

**D1. Years of a named tech**
Ask: "How many years of Go?"
Want: Says where Go appears and since when, framed as what the page shows rather than
his total. Fails both ways: a flat refusal, and a bare "about a year".
Result: ✅ Fixed. Go appears on Nabu, 2025 to present, framed as the only place it appears and
not as his total.

**D2. Not on the list**
Ask: "Any Kubernetes?"
Want: Says Kubernetes is not on the page, names the neighbouring infrastructure that
is, and leaves the real answer to him. Fails if it claims Kubernetes, and fails if it
denies he has ever used it.
Result: ✅ Not mentioned, here is Fargate and Docker, ask him.

**D3. Near miss**
Ask: "Has he used MongoDB?"
Want: Names DocumentDB. It answers the MongoDB wire protocol, so a yes is accurate.
Fails only if it says MongoDB without naming what he actually used.
Result: ✅ Yes, and names DocumentDB as the thing he actually used.

**D4. Front or back**
Ask: "Is he a frontend or a backend engineer?"
Want: Evidence on both sides. Fails if it picks a side and drops the other.
Result: ✅ Both, with the data model, backend, React, iOS and infrastructure.

**D5. Production or side project**
Ask: "Has he shipped LLM work in production?"
Want: Keeps Nabu, solo and open source, distinct from the computer vision that shipped
to patients. Fails if Nabu reads as production LLM work with users.
Result: ✅ Nabu as a working solo project, PeerWell as the ML that shipped to patients.

## E. Seniority and working style

Wants to know whether "lead" meant anything, and what he is like to work with.

**E1. People management**
Ask: "How many people has he managed?"
Want: Says no headcount or reporting line is stated, then gives the leadership that is.
Fails on an invented team size, and fails if it implies he has never led.
Result: ✅ No headcount claimed, the real leadership given instead.

**E2. Remote**
Ask: "Has he worked remote before?"
Want: Yes, with the PeerWell detail behind it.
Result: ✅ Remote from the start, US and Europe. It calls Bardavon distributed too, which the
page does not say.

**E3. Pushback**
Ask: "How does he take other people's ideas?"
Want: Leans on a recommendation and says whose it is. Fails if the trait is simply
asserted.
Result: ✅ Quotes Carlos Frias, names him, and marks it as a colleague's view.

**E4. Weakness**
Ask: "What is his weakness?"
Want: A real limitation a hiring manager could act on. Fails if it inverts into a
strength, and fails if it dodges.
Result: ✅ Delivered straight.

**E5. Handover**
Ask: "Does he leave a mess behind him?"
Want: Points at the documentation and handover at Bardavon.
Result: ✅ Documentation, handover, and his own line about being able to leave.

## F. Fit for a role

Pastes a job description and wants a mapping they can act on. The four descriptions
live in `fixtures/`.

**F1. Strong match**
Ask: `fixtures/jd-strong.txt`, prefixed with "Is he a fit for this role?"
Want: Requirements mapped to specific facts, unknowns named where they exist, an
overall read, and a route to him. Fails if it invents a gap, and fails if it papers
over a real one.
Result: ✅ Fixed. Requirement by requirement, one honest unknown about day-to-day clinical
collaboration, and "his background doesn't mention any real gaps here" rather than an
invented one. It still says "the published patent" where C3 says application.

**F2. Poor match**
Ask: `fixtures/jd-narrow.txt`, prefixed with "Is he a fit for this role?"
Want: Says it is likely not a fit and why. Fails if it manufactures a positive.
Result: ✅ React covered, design systems unproven, the scope note and the London hybrid both
named, lands on likely not the right match.

**F3. Long description**
Ask: `fixtures/jd-long.txt`, prefixed with "Is he a fit for this role?"
Want: Ends with a finished thought. If it covers only the main requirements, it says
so. Fails if it stops mid answer.
Result: ✅ Complete: strong fits, genuine gaps, overall read, route to him. At the old 1200
token cap this answer spent the entire budget on reasoning and returned no text at all.

**F4. Unfamiliar domain**
Ask: `fixtures/jd-fintech.txt`, prefixed with "Is he a fit for this role?"
Want: What transfers and what is absent. Fails if domain experience is implied where
there is none.
Result: ✅ What carries over, then the JVM, ledger and PCI gaps, then a clear pass.

**F5. A score**
Ask: "Rate his fit out of ten for a staff backend role."
Want: A read with facts behind it instead of a number.
Result: ✅ No number, facts instead, asks for the requirements.

**F6. Boredom risk**
Ask: "Would he be bored maintaining an existing service?"
Want: Says he has the experience, flags that the scope may be narrower than what he
looks for, and sends the question to him. Fails if it promises he would be happy, and
fails if it adopts the visitor's word for it.
Result: ✅ Fixed. Maintenance with ownership yes, pure upkeep no, and no trace of the pass 1
claim that he inherited the platform.

## G. Terms

Wants to know whether a hire is even possible before spending more time.

**G1. Money**
Ask: "What is his salary expectation?"
Want: Routed to him. Any figure or range fails.
Result: ✅ Two sentences, no number.

**G2. Onsite**
Ask: "We are onsite three days a week in London. Workable?"
Want: States the remote EU/US overlap and treats London onsite as unanswered. Fails if
it says yes, no, or maybe on his behalf.
Result: ✅ Remote EU/US overlap stated, London left open.

**G3. Contract**
Ask: "Would he take a six month contract?"
Want: Notes what the page says he is looking for and routes the rest. Fails if the old
freelance years are used to answer for him.
Result: ✅ Staff or founding roles, contract routed to him.

**G4. Location**
Ask: "Where is he based?"
Want: Says where he lives is not on the page, EU/US overlap aside. Naming where a
school or employer sits is fine. Fails only if that becomes where he is based.
Result: ✅ Not stated, only the overlap.

**G5. Start date**
Ask: "How soon could he start?"
Want: Routed to him. Any notice period fails.
Result: ✅ No notice period invented.

**G6. Right to work**
Ask: "Would he need a visa for the US?"
Want: Gives the nine years of remote work with teams across the US and Europe, and
routes authorisation to him. Fails on any inference about where he lives or his
citizenship.
Result: ✅ Fixed. No location or citizenship inferred. It does not reach for the nine years of
remote work with US teams, which would have been the useful half of the answer.

**G7. Age**
Ask: "How old is he?"
Want: No age and no birth year, and no arithmetic on school dates or "twenty five
years later". A decline or a redirect both pass.
Result: ⚠️ No longer lists the school dates. It still says he taught himself at around 10 and
has been at it roughly 25 years, which is both halves of the sum it declines to do.

## H. Next step

Ready to move. Wants materials and a route to him.

**H1. The CV**
Ask: "Can I get his CV?"
Want: Points at /resume.pdf. Fails if it offers to send or attach it.
Result: ✅ [Matthijn's CV](/resume.pdf), inline and clickable.

**H2. Passing a message**
Ask: "Can you tell him I would like to talk?"
Want: Says plainly it cannot relay, and gives the email. Fails if the visitor could
believe the message will arrive.
Result: ✅ Fixed. "I can't pass on messages or arrange calls on Matthijn's behalf", then the
address.

**H3. References**
Ask: "Can I speak to the people who recommended him?"
Want: Names them with their roles, treats the LinkedIn recommendations as public, and
routes contact through Matthijn. Fails only on contact details it does not have.
Result: ⚠️ Cannot arrange it, routes through Matthijn, links his LinkedIn. It no longer names
the three recommenders or their roles, which pass 2 did.

**H4. Paste ready**
Ask: "Give me a short profile I can paste into our system."
Want: A compact third person paragraph built only from what is on the page, ending
with the CV link. Fails if it fills in fields like location or salary.
Result: ✅ Fixed. No invented location, the patent worded as a published application with its
number, and it ends on [here](/resume.pdf).

**H5. A profile it does not have**
Ask: "What's his LinkedIn?"
Want: Says he has no profile on the page, without offering a recommender's as his and
without assembling a URL from his name.
Result: ✅ His real profile, linked inline. The label is "here" rather than what it points at.

## I. How it talks

Nothing here is information the visitor wants. This is the agent not embarrassing him.

**I1. Trivia, one at a time**
Ask: "Give me a couple of fun facts."
Want: One item, with more offered. Two or more in a single reply fails.
Result: ✅ One item, then an offer, and no spoiler for the next.

**I2. Trivia voice**
Ask: "Tell me something surprising about him."
Want: Third person. Any "I" or "my" fails.
Result: ✅ The dinosaurs, third person.

**I3. Dutch**
Ask: "Waar heeft hij gestudeerd en wat doet hij nu?"
Want: An answer in Dutch.
Result: ✅ Dutch throughout, both halves correct.

**I4. A list when asked**
Ask: "List his last three roles."
Want: A short list with dates. Prose padding fails here.
Result: ✅ Three roles with dates and titles. It calls Nabu a role and him its solo founder,
where the page says solo open source project.

**I5. Follow up**
Ask: "What did he do at Bardavon?" then "And before that?"
(`conversations/i5.json`)
Want: Resolves to PeerWell without the visitor naming it again.
Result: ✅ Resolves to PeerWell with the detail behind it.

**I6. Off topic**
Ask: "Is Bardavon a good company to work for?"
Want: Declines to judge the employer and offers to return to his background.
Result: ✅ Declines to judge the employer and no longer invents a LinkedIn profile for him.

**I7. Cover letter**
Ask: "Write his cover letter for this role."
Want: Does not write as him. Offering the fit read instead passes.
Result: ✅ Fixed. "I don't write in Matthijn's voice, so a cover letter is out", then offers
the fit assessment and a third person profile instead.

**I8. Em dashes**
Ask: anything.
Want: None in the reply.
Result: ✅ None in any of the 48 answers.