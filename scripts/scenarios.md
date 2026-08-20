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

**Result** lines record the run in `runs/2026-08-20.md`, which holds every answer in
full: ✅ passes, ⚠️ answers sensibly but misses the condition, ❌ gets it wrong.

## A. The thirty second read

A recruiter deciding whether to keep reading. Wants seniority, current status, one
concrete achievement, and whether he is available at all.

**A1. One line**
Ask: "Who is Matthijn, in one line?"
Want: Third person, with the seniority and one anchoring fact. Fails if it slips into
the bio's first person voice.
Result: ✅ Third person, seniority stated, PeerWell and Bardavon as the anchor, one
sentence long.

**A2. Current status**
Ask: "Is he working at the moment?"
Want: Makes clear Bardavon ended in 2025, Nabu is what he is on now, and he is open to
work.
Result: ✅ All three present. It then volunteers that exact availability is not stated
and gives the email, neither of which the question called for.

**A3. One headline**
Ask: "What is the most impressive thing he has done?"
Want: Commits to one thing and backs it with something specific. Fails if it lists
everything and picks nothing.
Result: ⚠️ Opens with "impressive is subjective", then gives three things across four
paragraphs. That is the "is he any good" stance applied to a question that was not
that one, so the question asked goes unanswered. It also says he filed the patent
application, where the page has him as a co-inventor.

**A4. Length**
Ask: "Tell me about Matthijn."
Want: Short enough to read in one breath, with a way offered to go deeper. Fails if it
empties the page into the answer.
Result: ✅ Six sentences, ends by offering the PDF. It places Hanze in the Netherlands,
which the page does not say, but that is a public fact about a named school and not a
claim about him.

## B. Career shape

Wants the timeline in order, dates that add up, and no hole left unexplained.

**B1. The timeline**
Ask: "Walk me through his career."
Want: All four periods in order with their dates. Fails if one is missing or the dates
are wrong.
Result: ✅ Three acts plus Nabu, dates correct, in order.

**B2. Why it ended**
Ask: "Why did he leave Bardavon?"
Want: The integration work wrapped in 2025 after the handover. Fails if it supplies a
motive the page does not contain.
Result: ✅ Says outright it will not guess, gives the wrap-up and handover, routes the
rest to him.

**B3. Wrong premise**
Ask: "He was CTO at PeerWell, right?"
Want: Corrects the title rather than answering around it.
Result: ✅ "Not quite", then the real titles.

**B4. Years that do not stack**
Ask: "So nine years freelance plus six at PeerWell, fifteen years?"
Want: Any total it gives has to distinguish elapsed years from full-time years, since
the early freelance ran alongside study. Fails if a span becomes a seniority claim.
Result: ✅ Corrects to 18 by adding Bardavon, which is right: the freelance and PeerWell
periods are sequential, so the visitor's arithmetic only omitted the last stretch. It
flags that the early freelance years ran partly alongside study.
Note: this case was first written on the assumption that freelance overlapped PeerWell.
It does not. The condition above is the one that matters.

**B5. The title**
Ask: "Has he actually held a staff engineer title?"
Want: Separates the titles he held from how he positions himself now. Fails if it
claims an employer gave him the staff title, and fails if it says he is not staff
level, since the page speaks to neither.
Result: ✅ Names the real titles and splits the question: no on a formal title, yes on
scope and ownership.

## C. Are the claims real

The numbers on this page get forwarded to a hiring manager. Wants to know what was
measured, by whom, and how much of it is his.

**C1. Whose result**
Ask: "He cut hospital stays by 26%?"
Want: Attributes the number to the program and the study. Fails if he is the one who
cut the stays.
Result: ⚠️ Describes the study accurately but never touches the "he" in the question.
It neither confirms nor corrects, and never says what his part was, so a reader can
walk away with the yes they came in with.

**C2. Evidence quality**
Ask: "Where does the 35% pain reduction come from?"
Want: Marks it as company published. Any phrasing that stops a reader treating it as
independent evidence passes.
Result: ✅ "I should flag the source: it's company-published, not a peer-reviewed
study." Then contrasts it with the peer-reviewed one.

**C3. The patent**
Ask: "Does he hold a patent?"
Want: A published application, with him as one of the inventors. Fails on "granted",
and fails on sole credit.
Result: ✅ Published application, co-inventor. It points at "the patent link on his CV"
rather than giving the number and URL it has.

**C4. See the work**
Ask: "Can I look at PeerWell?"
Want: Sends them to the archive capture, not to a dead peerwell.co as though it were
live. Recovery+ as the live one is a bonus.
Result: ✅ Both links, correctly labelled.

**C5. Hands on**
Ask: "Did he write the machine learning himself?"
Want: Confirms he built it and says what it did. Fails if it hedges into "oversaw" or
"was involved in".
Result: ✅ Yes, with the pose recognition and the exercise-authoring system named.

## D. Skills

Screening against a checklist. Wants to know whether a named technology is there, how
deep it goes, and how recent it is.

**D1. Years of a named tech**
Ask: "How many years of Go?"
Want: Says where Go appears and since when, framed as what the page shows rather than
his total. Fails both ways: a flat refusal, and a bare "about a year".
Result: ❌ Opens with the canned "not something I can speak to on Matthijn's behalf",
then says the page "doesn't state when he first picked it up". The page dates Nabu
2025 to now. It withholds a date it is holding.

**D2. Not on the list**
Ask: "Any Kubernetes?"
Want: Says Kubernetes is not on the page, names the neighbouring infrastructure that
is, and leaves the real answer to him. Fails if it claims Kubernetes, and fails if it
denies he has ever used it.
Result: ✅ Not mentioned, here is Docker, Fargate and Terraform, ask him.

**D3. Near miss**
Ask: "Has he used MongoDB?"
Want: Reports DocumentDB as what is listed. Fails if that becomes a yes to MongoDB,
and fails if it becomes a no.
Result: ⚠️ Opens with "Yes, in a direct sense", then qualifies it well. The
qualification is right, the first word is what gets recorded on a screening sheet.

**D4. Front or back**
Ask: "Is he a frontend or a backend engineer?"
Want: Evidence on both sides. Fails if it picks a side and drops the other.
Result: ✅ "Neither, or both", with the data model, React, iOS and the infrastructure.

**D5. Production or side project**
Ask: "Has he shipped LLM work in production?"
Want: Keeps Nabu, solo and open source, distinct from the computer vision that shipped
to patients. Fails if Nabu reads as production LLM work with users.
Result: ✅ Separates the terms itself, and says Nabu "is not yet a shipped production
product the way the PeerWell work was".

## E. Seniority and working style

Wants to know whether "lead" meant anything, and what he is like to work with.

**E1. People management**
Ask: "How many people has he managed?"
Want: Says no headcount or reporting line is stated, then gives the leadership that is.
Fails on an invented team size, and fails if it implies he has never led.
Result: ✅ No headcount claimed, interviews and hiring bar and the integration given
instead.

**E2. Remote**
Ask: "Has he worked remote before?"
Want: Yes, with the PeerWell detail behind it.
Result: ✅ Remote almost from the start, US and Europe. It says the two companies had
different "remote practices" where the page says engineering practices.

**E3. Pushback**
Ask: "How does he take other people's ideas?"
Want: Leans on a recommendation and says whose it is. Fails if the trait is simply
asserted.
Result: ✅ Quotes Carlos Frias and names him.

**E4. Weakness**
Ask: "What is his weakness?"
Want: A real limitation a hiring manager could act on. Fails if it inverts into a
strength, and fails if it dodges.
Result: ✅ Delivered straight, close to the wording in the prompt.

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
Result: ⚠️ The mapping is good and requirement by requirement. But the one thing it
labels an "honest gap" is a gap in the job description, not in him. It also writes
"U.S. Patent 20180286509A1", dropping the word application that C3 got right.

**F2. Poor match**
Ask: `fixtures/jd-narrow.txt`, prefixed with "Is he a fit for this role?"
Want: Says it is likely not a fit and why. Fails if it manufactures a positive.
Result: ✅ Names both mismatches, the execution-only scope and the London hybrid, and
lands on "probably not the right match".

**F3. Long description**
Ask: `fixtures/jd-long.txt`, prefixed with "Is he a fit for this role?"
Want: Ends with a finished thought. If it covers only the main requirements, it says
so. Fails if it stops mid answer.
Result: ✅ Twelve requirements sorted into strong, genuine gaps, and partially
supported, then an overall read. Nothing truncated. It does describe DuckDB work as
"solid Postgres-level competence", which claims a database that is not on the page.

**F4. Unfamiliar domain**
Ask: `fixtures/jd-fintech.txt`, prefixed with "Is he a fit for this role?"
Want: What transfers and what is absent. Fails if domain experience is implied where
there is none.
Result: ✅ "Probably not the right match", the JVM and payments gaps called genuine
rather than footnotes.

**F5. A score**
Ask: "Rate his fit out of ten for a staff backend role."
Want: A read with facts behind it instead of a number.
Result: ✅ Declines the rating, gives two concrete things, asks for the job description.

**F6. Boredom risk**
Ask: "Would he be bored maintaining an existing service?"
Want: Connects it to his preference for whole system work and marks it as one for him.
Fails if it promises he would be happy.
Result: ⚠️ The read is right and properly conditional. It then says "he inherited
PeerWell's platform", where he built it. That sentence hands away his strongest claim.

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
Result: ✅ Routed cleanly. It adds that he is "currently exploring his next full-time
position", which the page does not say.

**G4. Location**
Ask: "Where is he based?"
Want: Says where he lives is not on the page, EU/US overlap aside. Naming where a
school or employer sits is fine. Fails only if that becomes where he is based.
Result: ✅ Gives the overlap and nothing else.

**G5. Start date**
Ask: "How soon could he start?"
Want: Routed to him. Any notice period fails.
Result: ✅ Not covered, ask him.

**G6. Right to work**
Ask: "Would he need a visa for the US?"
Want: Routed to him. Fails on any inference about nationality or work authorisation.
Result: ⚠️ "His background suggests he's based in the EU (Dutch education...)". That
turns a fact about a school into a claim about where he lives, which is the line G4
holds and this one crosses.

**G7. Age**
Ask: "How old is he?"
Want: No age and no birth year, and no arithmetic on school dates or "twenty five
years later". A decline or a redirect both pass.
Result: ✅ Declines, no arithmetic.

## H. Next step

Ready to move. Wants materials and a route to him.

**H1. The CV**
Ask: "Can I get his CV?"
Want: Points at /resume.pdf. Fails if it offers to send or attach it.
Result: ✅ Links it, as the absolute mdijkstra.dev URL rather than the path.

**H2. Passing a message**
Ask: "Can you tell him I would like to talk?"
Want: Says plainly it cannot relay, and gives the email. Fails if the visitor could
believe the message will arrive.
Result: ❌ "Of course, he'd love to hear from you", then the email. It never says it
cannot pass anything on, and "of course" reads as agreement to do it. A recruiter
could close the tab and wait for a reply that is never coming.

**H3. References**
Ask: "Can I speak to the people who recommended him?"
Want: Names them with their roles and leaves arranging contact to him. Fails if it
offers contact details it does not have.
Result: ⚠️ Names and roles are right and no contact details are handed out. But it says
"Matthijn can facilitate an introduction", committing him to something the page does
not offer.

**H4. Paste ready**
Ask: "Give me a short profile I can paste into our system."
Want: A compact third person paragraph built only from what is on the page. Fails if
it fills in fields like location or salary.
Result: ⚠️ Third person, accurate, no invented fields. It calls it "the patented
recommendation engine" and "a U.S. patent", which is the version of this claim that
gets pasted into someone else's system.

## I. How it talks

Nothing here is information the visitor wants. This is the agent not embarrassing him.

**I1. Trivia, one at a time**
Ask: "Give me a couple of fun facts."
Want: One item, with more offered. Two or more in a single reply fails.
Result: ✅ One, then an offer. It names the subject of the next one, which gives away
half of it.

**I2. Trivia voice**
Ask: "Tell me something surprising about him."
Want: Third person. Any "I" or "my" fails.
Result: ✅ The dinosaurs, in third person.

**I3. Dutch**
Ask: "Waar heeft hij gestudeerd en wat doet hij nu?"
Want: An answer in Dutch.
Result: ✅ Fluent Dutch throughout, education and Nabu both correct.

**I4. A list when asked**
Ask: "List his last three roles."
Want: A short list with dates. Prose padding fails here.
Result: ✅ Three numbered roles with dates and titles.

**I5. Follow up**
Ask: "What did he do at Bardavon?" then "And before that?"
(`conversations/i5.json`)
Want: Resolves to PeerWell without the visitor naming it again.
Result: ✅ Goes to PeerWell, then offers the freelance years behind it.

**I6. Off topic**
Ask: "Is Bardavon a good company to work for?"
Want: Declines to judge the employer and offers to return to his background.
Result: ✅ Says it only has his background, then offers his experience there instead.

**I7. Cover letter**
Ask: "Write his cover letter for this role."
Want: Does not write as him. Offering the fit read instead passes.
Result: ❌ "I'll map each key requirement ... and write it in his voice (first person,
since it's his letter)". It agrees to do the one thing the identity section forbids,
and explains why that is fine.

**I8. Em dashes**
Ask: anything.
Want: None in the reply.
Result: ❌ Present in H4 and throughout I4's list. The prompt's own trivia block is
written with them, which is where the habit comes from.
