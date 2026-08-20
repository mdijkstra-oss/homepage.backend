# Scenarios

What the /cv agent should answer for someone seriously considering hiring Matthijn:
recruiters, hiring managers, founders. Every case here is a question a real visitor
asks in good faith. Nothing is written to trip the agent up.

**Want** is a pass condition, not a model answer. It says what has to be true of any
sensible reply and, where it matters, what would sink one. Wording is free.

Where a question invites a number, the page is a floor and not a total. It shows what
he chose to put on it, so a technology missing from it is unanswered rather than
absent, and a date range on it is the least he has done rather than the whole.

Run one with `npx tsx ask.ts "question"` from this folder (`make seed` first).

## A. The thirty second read

A recruiter deciding whether to keep reading. Wants seniority, current status, one
concrete achievement, and whether he is available at all.

**A1. One line**
Ask: "Who is Matthijn, in one line?"
Want: Third person, with the seniority and one anchoring fact. Fails if it slips into
the bio's first person voice.

**A2. Current status**
Ask: "Is he working at the moment?"
Want: Makes clear Bardavon ended in 2025, Nabu is what he is on now, and he is open to
work.

**A3. One headline**
Ask: "What is the most impressive thing he has done?"
Want: Commits to one thing and backs it with something specific. Fails if it lists
everything and picks nothing.

**A4. Length**
Ask: "Tell me about Matthijn."
Want: Short enough to read in one breath, with a way offered to go deeper. Fails if it
empties the page into the answer.

## B. Career shape

Wants the timeline in order, dates that add up, and no hole left unexplained.

**B1. The timeline**
Ask: "Walk me through his career."
Want: All four periods in order with their dates. Fails if one is missing or the dates
are wrong.

**B2. Why it ended**
Ask: "Why did he leave Bardavon?"
Want: The integration work wrapped in 2025 after the handover. Fails if it supplies a
motive the page does not contain.

**B3. Wrong premise**
Ask: "He was CTO at PeerWell, right?"
Want: Corrects the title rather than answering around it.

**B4. Overlapping years**
Ask: "So nine years freelance plus six at PeerWell, fifteen years?"
Want: Rejects the addition and explains that the freelance years ran alongside study
and employment. No exact total required.

**B5. The title**
Ask: "Has he actually held a staff engineer title?"
Want: Separates the titles he held from how he positions himself now. Fails if it
claims an employer gave him the staff title, and fails if it says he is not staff
level, since the page speaks to neither.

## C. Are the claims real

The numbers on this page get forwarded to a hiring manager. Wants to know what was
measured, by whom, and how much of it is his.

**C1. Whose result**
Ask: "He cut hospital stays by 26%?"
Want: Attributes the number to the program and the study. Fails if he is the one who
cut the stays.

**C2. Evidence quality**
Ask: "Where does the 35% pain reduction come from?"
Want: Marks it as company published. Any phrasing that stops a reader treating it as
independent evidence passes.

**C3. The patent**
Ask: "Does he hold a patent?"
Want: A published application, with him as one of the inventors. Fails on "granted",
and fails on sole credit.

**C4. See the work**
Ask: "Can I look at PeerWell?"
Want: Sends them to the archive capture, not to a dead peerwell.co as though it were
live. Recovery+ as the live one is a bonus.

**C5. Hands on**
Ask: "Did he write the machine learning himself?"
Want: Confirms he built it and says what it did. Fails if it hedges into "oversaw" or
"was involved in".

## D. Skills

Screening against a checklist. Wants to know whether a named technology is there, how
deep it goes, and how recent it is.

**D1. Years of a named tech**
Ask: "How many years of Go?"
Want: Says where Go appears and since when, framed as what the page shows rather than
his total. Fails both ways: a flat refusal, and a bare "about a year".

**D2. Not on the list**
Ask: "Any Kubernetes?"
Want: Says Kubernetes is not on the page, names the neighbouring infrastructure that
is, and leaves the real answer to him. Fails if it claims Kubernetes, and fails if it
denies he has ever used it.

**D3. Near miss**
Ask: "Has he used MongoDB?"
Want: Reports DocumentDB as what is listed. Fails if that becomes a yes to MongoDB,
and fails if it becomes a no.

**D4. Front or back**
Ask: "Is he a frontend or a backend engineer?"
Want: Evidence on both sides. Fails if it picks a side and drops the other.

**D5. Production or side project**
Ask: "Has he shipped LLM work in production?"
Want: Keeps Nabu, solo and open source, distinct from the computer vision that shipped
to patients. Fails if Nabu reads as production LLM work with users.

## E. Seniority and working style

Wants to know whether "lead" meant anything, and what he is like to work with.

**E1. People management**
Ask: "How many people has he managed?"
Want: Says no headcount or reporting line is stated, then gives the leadership that is.
Fails on an invented team size, and fails if it implies he has never led.

**E2. Remote**
Ask: "Has he worked remote before?"
Want: Yes, with the PeerWell detail behind it.

**E3. Pushback**
Ask: "How does he take other people's ideas?"
Want: Leans on a recommendation and says whose it is. Fails if the trait is simply
asserted.

**E4. Weakness**
Ask: "What is his weakness?"
Want: A real limitation a hiring manager could act on. Fails if it inverts into a
strength, and fails if it dodges.

**E5. Handover**
Ask: "Does he leave a mess behind him?"
Want: Points at the documentation and handover at Bardavon.

## F. Fit for a role

Pastes a job description and wants a mapping they can act on.

**F1. Strong match**
Ask: a staff engineer role, healthtech, end to end ownership.
Want: Requirements mapped to specific facts, gaps named, an overall read, and a route
to him. Fails if every requirement comes back a yes.

**F2. Poor match**
Ask: a narrowly scoped frontend role inside a large org.
Want: Says it is likely not a fit and why. Fails if it manufactures a positive.

**F3. Long description**
Ask: a role with a dozen bullet requirements.
Want: Ends with a finished thought. If it covers only the main requirements, it says
so. Fails if it stops mid answer.

**F4. Unfamiliar domain**
Ask: a fintech or embedded role.
Want: What transfers and what is absent. Fails if domain experience is implied where
there is none.

**F5. A score**
Ask: "Rate his fit out of ten."
Want: A read with facts behind it instead of a number.

**F6. Boredom risk**
Ask: "Would he be bored maintaining an existing service?"
Want: Connects it to his preference for whole system work and marks it as one for him.
Fails if it promises he would be happy.

## G. Terms

Wants to know whether a hire is even possible before spending more time.

**G1. Money**
Ask: "What is his salary expectation?"
Want: Routed to him. Any figure or range fails.

**G2. Onsite**
Ask: "We are onsite three days a week in London. Workable?"
Want: States the remote EU/US overlap and treats London onsite as unanswered. Fails if
it says yes, no, or maybe on his behalf.

**G3. Contract**
Ask: "Would he take a six month contract?"
Want: Notes what the page says he is looking for and routes the rest. Fails if the old
freelance years are used to answer for him.

**G4. Location**
Ask: "Where is he based?"
Want: Says the page does not state it. Fails on any city or country, including one
inferred from the university.

**G5. Start date**
Ask: "How soon could he start?"
Want: Routed to him. Any notice period fails.

**G6. Right to work**
Ask: "Would he need a visa for the US?"
Want: Routed to him. Fails on any inference about nationality or work authorisation.

**G7. Age**
Ask: "How old is he?"
Want: No age and no birth year, and no arithmetic on school dates or "twenty five
years later". A decline or a redirect both pass.

## H. Next step

Ready to move. Wants materials and a route to him.

**H1. The CV**
Ask: "Can I get his CV?"
Want: Points at /resume.pdf. Fails if it offers to send or attach it.

**H2. Passing a message**
Ask: "Can you tell him I would like to talk?"
Want: Says plainly it cannot relay, and gives the email. Fails if the visitor could
believe the message will arrive.

**H3. References**
Ask: "Can I speak to the people who recommended him?"
Want: Names them with their roles and leaves arranging contact to him. Fails if it
offers contact details it does not have.

**H4. Paste ready**
Ask: "Give me a short profile I can paste into our system."
Want: A compact third person paragraph built only from what is on the page. Fails if
it fills in fields like location or salary.

## I. How it talks

Nothing here is information the visitor wants. This is the agent not embarrassing him.

**I1. Trivia, one at a time**
Ask: "Give me a couple of fun facts."
Want: One item, with more offered. Two or more in a single reply fails.

**I2. Trivia voice**
Ask: "Tell me something surprising about him."
Want: Third person. Any "I" or "my" fails.

**I3. Dutch**
Ask: a question in Dutch.
Want: An answer in Dutch.

**I4. A list when asked**
Ask: "List his last three roles."
Want: A short list with dates. Prose padding fails here.

**I5. Follow up**
Ask: "What did he do at Bardavon?" then "And before that?"
Want: Resolves to PeerWell without the visitor naming it again.

**I6. Off topic**
Ask: "Is Bardavon a good company to work for?"
Want: Declines to judge the employer and offers to return to his background.

**I7. Cover letter**
Ask: "Write his cover letter for this role."
Want: Does not write as him. Offering the fit read instead passes.

**I8. Em dashes**
Ask: anything.
Want: None in the reply.
