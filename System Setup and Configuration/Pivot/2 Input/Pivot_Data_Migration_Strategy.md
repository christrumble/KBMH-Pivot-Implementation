Data Migration Strategy Session with Pivot - January 29
VIEW RECORDING - 31 mins (No highlights): https://fathom.video/calls/221272945

---

0:00 - Sandra Rudloff (Pivot Interiors)
  that's what 2026 will be like. So hoping by the end of this week he'll have a better idea. Does this fit into our plan, you know 2025 and if so, which quarter?  Obviously, we're really interested in doing this. Just where does it, you know, fall in with everything else too? And, you know, as we discussed the human impact.  It's something where, in fact, I'm meeting with our HRVP on Friday to talk about, you know, if we do this, who would be tapped on the shoulder and, you know, would we have to look for some temporary help to support those people because everyone already has a job.  So, you know, part of that, that's also going to get rolled into the budget and the expense. it's, it's just right now, it's a juggling game trying to figure out, okay?  Sure. No, I've got feeling, yeah, think everyone wants to do this. just what is the right timing? Gotcha. Yeah, no, I understood.

0:55 - Marcus Dallacqua (SuiteCentric)
  Yeah, it's big decision. You know, and we're still, you know, this will be a complete.

1:00 - Sandra Rudloff (Pivot Interiors)
  of the budget number, obviously. I'm also looking, I contacted Jennifer McKinney about IQ and like, okay, sun setting that.  What's the expense there? We're reaching out to Adobe Workfront to find that as well. yeah, pulling all the numbers together is interesting and some are gonna be absolute unknowns until we get there.  Like, you know, help. What's that look like? what kind of, you know, we're looking at three months of the, you know, some of our highest paid employees that we need support for, is it, you know, I did share the little graphic you did as far as, you know, the different stages and the involvement we'd have, so.  Okay, good. Yeah, just trying to work through all the numbers. Yeah, no, I understand.

1:44 - Marcus Dallacqua (SuiteCentric)
  Well, we wanted to, you know, whatever we can do to support, helping you guys make that decision in the time and things like that.  know on this call today, we wanted to focus in on data migration. Just to kind of review. You already have a data warehouse, so it sounds like we don't need to help on that front, so your historical data is in place and would stay in place, is that correct?

2:11 - Sandra Rudloff (Pivot Interiors)
  Right, not everything is in the data warehouse just because there was no need for things like, you know, AR cache posting, it's like, you know, we don't need to pull report.  It's mostly for reporting reasons, it's not necessarily a backup storage, so there are probably some areas we need to export, which is fine.  have a consultant who helped us, you know, create the exports and, you know, and also some, I don't know if we need it, they would help us build views instead of just tables.  So, depending what we talk about here, yeah, there might be the need for us to export more info into that data warehouse.  where we take it from there. Okay.

3:03 - Marcus Dallacqua (SuiteCentric)
  Yeah, in my experience, the needs are related to mostly sales historical information and documentation for audit purposes. So I guess I'm just wondering in that data warehouse, like if you need to go back and within that seven year window that you have to retain documents and pull up a PDF, do you have that available to you?  No, not PDFs.

3:31 - Sandra Rudloff (Pivot Interiors)
  Well, we have just the raw data. So, you know, we do frequently, someone says, can you tell me everything that Apple purchased over the last seven years?  And I can say yes, and dump it into, you know, an Excel file or CSV type thing. So, you know, we do have everything related to sales orders, sales, sales overhead or sales order line items.  Purchase order, header purchase order lines, you know, everything since day one. The things we don't have are related to AP and AR.  Inventory is kind of in there, we have kind of a different approach because limitations on D365 are inventory table, it has just base product numbers and a description but all item attributes are actually stored in a different table and is linked by the sales order and the item.  So let's see, there's that. And you deal with pre-sold inventory anyways, right? yeah, you're maintaining inventory.

4:32 - Marcus Dallacqua (SuiteCentric)
  Right, yeah.

4:33 - Sandra Rudloff (Pivot Interiors)
  And then GL data is not in there but that'd be easy enough to export. So I'm not sure what you would normally import to do a migration to basically be able to first to flip the switch one data the next.

4:51 - Marcus Dallacqua (SuiteCentric)
  Well, yeah, so I'll start in the slowly but surely, Angela's gonna take over because she's the expert on this but just to kind of give you an introduction.  you typically start with entity bringing over the entity. So that would be vendors, employees, customers, contacts. If you have a list of influencers that you wanna track, that could also come over as well.  And then just so you know, from a vendor standpoint, we do have Brian Schis with I think 285 vendors in there.  there would be like a little bit of mapping, but I'm sure you have more than that in your vendor table.  So that would all come over. Those are pretty simple.

5:31 - Sandra Rudloff (Pivot Interiors)
  I was gonna say, can you share the Pantan Notes or should I make a list of this stuff? Oh yeah, yeah, I'll share that.  Yeah, I'll do the summary and everything. Yeah, and we also have this outlined.

5:43 - Angela Davis
  So we're just discussing some of it, but I can actually share some of the visuals with you as we're going as well.  And so we do that.

5:53 - Marcus Dallacqua (SuiteCentric)
  We do two years, at least two years. It should say at least two years of end of the month trial balances.

6:00 - Sandra Rudloff (Pivot Interiors)
  You import those those come in as journal entry.

6:02 - Marcus Dallacqua (SuiteCentric)
  you have your period over period reporting for at least the past two years, a lot of people opt to do more.  The only thing you want to consider and that's fine. If it was me, I would probably do more because I like my historical reporting.  You just, and there is that mapping that has to happen because you're probably going to make some changes to your chart of accounts.  And so there is with those are some things that would have to be considered, but that's all kind of that all gets figured out during discovery and that when we create that data migration strategy document.  Then on top of that, there's really the open AR AP and projects and flight considerations. And that's what I know you mentioned, you guys have about 1800 projects in flight or open owners.  think you said right.

6:48 - Sandra Rudloff (Pivot Interiors)
  Yeah, 1800 2000 that's about our app running average.

6:52 - Marcus Dallacqua (SuiteCentric)
  Yeah, so that's where some decisions will have to be made. And, and the interesting thing is really what you need to do at the beginning of  project is have a strategy and it's really towards the end of the project that you execute the strategy because you're not going to move anything that's in flight at the beginning of the project because their implementation takes number of months to do so really finding the strategy and execute it towards the end.  The way I think about it is it's going to be somewhat kind of case by case or group by group.  At this point I should turn it over to Angela because she's the expert at this and I'll stop talking and let her take it over from here but I just wanted to give you my initial thoughts.

7:35 - Angela Davis
  Sure hey you're already touching on all the fun topics there so yeah so let me just share something with you a quick visual because this is really what we end up putting together and we will have a data migration strategy session with you but I wanted to at least give you an idea of how this works.  So you'll have this collaborative approach. We'll walk through step-by-step, what to expect, what those milestones are, when we need to see some of the data from you, because we will take a subset and walk through some of the imports, and we'll prep those in advance and bring that in so that you really have accurate data for user acceptance testing and even our process walkthroughs with you.  So we'll go through that. And then you'll have a layout. We put together a complete data strategy document, and that will outline some of what I just described, and it will have a detailed list like this, how we're planning to import it.  Are there some of these things we need to write scripts for? That's a very possible and again to a large number of records that we bring in.  But as Marcus mentioned, there's all this entity data and all of these records, and you'll have an opportunity to scrub some of that if you need to clean it up.

8:54 - Marcus Dallacqua (SuiteCentric)
  We also have some utilities to do that.

8:57 - Angela Davis
  And this, I think, is the most straightforward part. of what we need to bring in. Looking at influencers and contacts, those reside like in work front or hub spot.

9:10 - Sandra Rudloff (Pivot Interiors)
  So I mean, we'll have templates, we can just cut and paste it needed, okay.

9:16 - Angela Davis
  Yep, and sometimes though it's easier for us to just get a sample of what you have and take a look at it because often it takes more work for you to fit it into a template than it does for us to just select columns and bring it in.  So we'll work with you on that. But that's actually a perfect segue to some of the things here that we outlined.  Overall, just the conversation, when I walked away from our in-person time together, my wheel started turning about all of these in-flight projects and what we would need to do to bring that in.  And I did have a few questions because I know you have some of this already in dynamics. But then you mentioned.  of spot. You know, we have things outside of that data set. When we're talking about bringing in any of those projects that are in flight, the first layer of decisions that you would have, I'm imagining we have some of these elements, you know, the opportunities or the original lead data that you've got in HubSpot right now.  So I think that's one decision point would be whether or not for anything that is in flight, do we want to go back and bring in that original CRM type data?  Okay.

10:35 - Sandra Rudloff (Pivot Interiors)
  Your thoughts on that? Yeah, I mean, it's always a question of, you know, when you're doing a data migration versus, okay, what do we want, you know, is the data so old that we'd rather not bring it in than just go from square one?  So, yeah, the opportunities would be HubSpot, design requests, waiver, that's HubSpot, or sorry, Workfront. The quotes are D365 only.  Okay, but so it's kind of a couple of this. I mean, Labor quotes actually an interesting one because I mean it starts in Workfront.  Those two a user who uses IQ to generate it. So yeah, I'm not sure what we could do with that.  That's, and like I said I'm curious what Jennifer McKinney will have to say on it, you know, the options of what how we can export data from IQ if it's even very possible or not.  Yes, some of that is difficult.

11:35 - Angela Davis
  Her and I have had some discussions on that, but it is possible to get some of that data out.  It depends again on the volume, I think, too of how manageable that is if we have to manually manipulate any of it or or do work care.  So I can chat with her in more detail on it, but I think overall then there's two basic approaches that we've discussed and seen, if we're bringing in all of the in-flight projects, is it where we really just want to bring in anything that had an accounting impact or will have an accounting impact for those open projects?  Or do we want to go back and bring in everything possible related to those open projects so that it's in that suite in one place?  So I think there's two schools of the thought.

12:29 - Sandra Rudloff (Pivot Interiors)
  I think that feeling would be anything with the accounting impact. basically when we flip our switch, everyone who works in D365, PCs, sales coordinators accounting would do everything in Orion from that point on.  And then maybe we have a six-month window where we continue to process the other peripheral data in Workfront, in IQ, with the intention  of, okay, six months later, whatever's remaining we manually create. That might, that might be, yeah, I'm thinking that's probably the easiest because otherwise, there's not just so much.  I know. I don't know how we could pop, I just think of IQ and all the documents we have and they're like all of our seeming records.  Yeah, I think that's where we got, that's exactly the sticking point there.

13:29 - Angela Davis
  Once you start to expand, then it just becomes this exponential undertaking.

13:36 - Sandra Rudloff (Pivot Interiors)
  So yeah, maybe we just stay with the, you know, the core functionality of D365. So, you know, like you said, all the elements, customers, vendors, that sort of thing.  And it really is just maybe open quotes, open orders, not filled out completely, open projects and leave it at that level.  And we run it. down the two other systems? I think that that is the most logical approach.

14:06 - Angela Davis
  And I think if I were in your shoes and I was looking to weigh the whole cost benefit, user adoption, that to me is logical, completely logical.  And that's why I highlighted some of these other aspects on the list, because I think if we carve that out and just focus on accounting impact, getting the necessary elements that you have now in the one system, then I think we should be good.  So, okay, well, I think really that was the gist of what I wanted to discuss, was just the difference in the approach.  And I think for outlining potential costs, we can get to a starting point. But like you said, there's some of it we just don't know until we get into the detail.  But with that approach, I can follow up with Jennifer McKinney, because I need to go over some of it with her anyway, and then work on getting that preliminary estimate together so that you have that for budgetary purposes.  That'd be great. Yeah, I just keep looking through this list.

15:17 - Sandra Rudloff (Pivot Interiors)
  Yeah, I think if we removed, oh boy, do you think about that? Yeah, if we removed, let's see, I agree.  Opportunities and trending. I think we probably want to start fresh with that design because they would quote, yeah, I think we can streamline this down.  Obviously, one other groups to weigh in on it, but I think like time entry, which we have in two different systems, I would skip those.  It's going to be a different set up going forward. Actually, this is an interesting question. So everything we have obviously already has numbers.  associated with a project, you know, sales order PO. And we'll have a different sequence once we start doing things live in Orion, right?  So it'd be very easy for us to identify, you know, hey, if this project starts with a four, we know it won't have any time entry consent and say starting press, you know, projects that start with a one, which are Orion generated will, I think that we can make that happen.

16:26 - Angela Davis
  Yes. And so that we bring in the old numbers, the way that you had them and then start with a new numbering sequence.  That's really common to identify the newly created projects. And it can be alphanumeric if you wanted it to, but it doesn't have to be.  But I'm thinking, yeah, anything here that's project related, bringing the sales order, the detail there. Was it acknowledged based on the PO data that's linked?  The one of the. Picking points there, and we'll work through it. It has to do with some of the acknowledgments.  But I think we can come up with a plan for that. We might, again, have to do some scripting there.  And get down to anything that you had an order processed for that you've received a deposit on already. So that's fine.  But those are things that we can import. All of the things that I think are to me, the no-brainer type imports that we would be doing are those that are not highlighted.  These were the questionable transactions, and I think it's not really worth it. So I can update this to just note that we'd be keeping that in the other systems.  And then in-flight data, we'll clearly need samples and we'll to see. But yeah, I think that's really the just event.  Kind of a side question.

17:59 - Sandra Rudloff (Pivot Interiors)
  Does I know there's the whole SharePoint integration potential, which will definitely want to be taken advantage of, but are documents actually stored within Orion NetSuite anywhere, is it like for us with the AP automations and invoice capture, we actually have the system attached a vendor invoice to the purchase order.  does NetSuite or Orion do that, or is it all external? No, you can do that.

18:31 - Angela Davis
  You can attach documents within that suite because we have our own file cabinet there, but then in addition to that, we have that SharePoint integration, so you can share the files between SharePoint and that suite.

18:44 - Marcus Dallacqua (SuiteCentric)
  Yeah, and importantly, too, is the SharePoint integration works inside of NetSuite. So when you go to that purchase order, or the vendor bill, you'll see the PDF for that particular vendor bill in the SharePoint tab.

18:59 - Angela Davis
  So even though

19:00 - Marcus Dallacqua (SuiteCentric)
  It's reference inside Orion, even though it's stored in SharePoint.

19:04 - Sandra Rudloff (Pivot Interiors)
  Yeah, because one of the things we're facing, which we have to put on hold until we, you know, make a decision this way is document storage and curaging.  We get emails from our clients saying, hey, it's been three years since this project. Can you verify you deleted all documents relating to this?  And it's, well, how many systems do I go through to hunt for this one project data? So, you know, ideally nothing is stored within, you know, net suite unless there's a very easy way to purge by date.  So, no, I think that we would want to streamline that.

19:39 - Angela Davis
  So again, that's process related configuration related, and I would say let's point that in one direction so that you don't have to manage both or worry about storage costs either.

19:52 - Sandra Rudloff (Pivot Interiors)
  And we were talking, okay, you know, we'll have to figure out, you know, some kind of way to download all these documents.

21:00 - Angela Davis
  to bring in all of the GL history, and then we reconfound validated all with you.

21:05 - Sandra Rudloff (Pivot Interiors)
  Yeah, probably since to bring more just because you never know when you need it, and they'll just make it easier.  mean, like sales tax audits every four years. yeah, we don't want to have to look into systems to pull in a GL data or trial balance if we needed it.  yeah, I think I'd like to go back on the trial balance, the full seven years. And then we can make this, you know, sales orders.  So we've got it all already in our data warehouse. I mean, we don't need to go terribly far back with any of these documents, so.  OK.

21:42 - Angela Davis
  Are the chart of accounts, is the chart of account structured the same over the seven years? already have that?  Chart of accounts, yes.

21:53 - Sandra Rudloff (Pivot Interiors)
  We did make some changes to, like, we have three, we have a department and a division, so, like. And Francisco office for health care, that sort of thing.  And I think we made a change midway through, but it's been pretty static for the last two or four years.  So, yeah, turn that counts minimal change. And we might have added the couple, but that's not much. OK.

22:18 - Angela Davis
  Because otherwise, it's a mapping exercise so that we would align the seven years so that it would be logical.  But if that makes sense, and it's something that you want, and it is aligned with the chart of accounts structure, no problem, once you've run the imports for the one year instead of data, then again.

22:37 - Sandra Rudloff (Pivot Interiors)
  sometimes people choose to do that even after go live.

22:41 - Angela Davis
  know, we focus on so many other things, and your users, and then you can always go back and bring in historical data as well and get people up and running.

22:51 - Sandra Rudloff (Pivot Interiors)
  So that's kind of a common approach.

22:53 - Angela Davis
  Questions, though? Yeah, I think that just strategy, again, for just pass here. I have enough based on what I already know, just in general, having worked with other dealers and then what you just answered to be able to do a prelim estimate and prelim plan.  So, Marcus, anything else you can think of? No, I'm good.

23:18 - Marcus Dallacqua (SuiteCentric)
  I think we're in good spot. Okay.

23:22 - Sandra Rudloff (Pivot Interiors)
  I think with all of these, you know, components for the, for an implementation, and like I said, getting the numbers from IQ and work front, we know they're ballpark, things change, things happen.  So, at least it'll give us a better understanding of just some of the, know, the costs that aren't, you know, on paper, just trying to pull it all together.

23:49 - Angela Davis
  Yep, that's understandable. there are little nuances, like one of the things that I've thought about and we've discussed would be you have customer invoices that have been processed.  But you have some that are related, obviously, to projects that are closed, we won't be bringing those in. So I think there will be a mix and match of some things, and it's all the detail, right?  It's always in the detailed planning, but we'll go through all of those, and we have a good starting point.  Okay. That'd be great, yeah.

24:21 - Sandra Rudloff (Pivot Interiors)
  Yep.

24:22 - Angela Davis
  And if you think of anything else, let me know, but we'll take the approach of just focusing on what's in dynamics now.  I like that. Okay. Yeah.

24:31 - Sandra Rudloff (Pivot Interiors)
  All right.

24:32 - Angela Davis
  So that's all I've got. Marcus, I'll turn him back over to you. I think I'm good.

24:36 - Marcus Dallacqua (SuiteCentric)
  As far as next steps. Angela will be delivering that to you. Is there anything else you need from us, Sandy?  Um, I know the quote you presented had an expiration.

24:49 - Sandra Rudloff (Pivot Interiors)
  I think of was it today or yesterday? It's pretty. it's the end of January.

24:54 - Marcus Dallacqua (SuiteCentric)
  Yeah.

24:54 - Sandra Rudloff (Pivot Interiors)
  So we'll have to get a new quote. And there was some changes with next week's editions.

24:59 - Marcus Dallacqua (SuiteCentric)
  So. We will be, I have a meeting with our NetSuite rep tomorrow morning, actually, very, very. So we'll be reviewing the new additions.

25:08 - Sandra Rudloff (Pivot Interiors)
  And so, yeah, we'll have to start from scratch there.

25:10 - Marcus Dallacqua (SuiteCentric)
  I don't think I'll ask for another quote from them, though, until there's some indication from your guys' side that you're looking to move forward.

25:19 - Sandra Rudloff (Pivot Interiors)
  Yeah, I get it. I know you had mentioned LEAF as a potential funding resource. I guess what was, is there any flexibility to what's due upon signing?  So, mean, could we, because I could see, we'll sign it, but we don't want to start any implementation until, say, August, that sort of thing.  If that's a potential that would be amount due at signing. So that might be something that will help convince someone where they are, or just  help him finding the timeline.

26:02 - Marcus Dallacqua (SuiteCentric)
  Yeah, there are some things that we can do to get creative and yeah, okay, so if you wanted to if you wanted to like lock in before the end of January, but you wanted to delay the beginning of the implementation there and Adam jumped on here, I'm glad because there are things that we have worked out with.  That's before in the past to do that. So Adam, you want to, I've seen that happen before where we get the signature, but we delay the accounting provision to later.  What are your thoughts on that? Yeah, they only extend that to a month. So yeah, think CLR did that.

26:38 - Adam Baruh
  like, I think if you made commitment, now they would extend it to probably, I guess, March 1st, they wouldn't activate your net somebody count to March 1st.  just for clarity around that. But I think there's probably more flexibility on the um, certainly the professional services side of things, the deposit that that we asked.  for there and potentially the Orion side of things, but that's more on this call. Yeah, and let me talk about LEAF for a second, because LEAF is a great option.

27:08 - Marcus Dallacqua (SuiteCentric)
  So LEAF will finance all three things. So here's the three costs you have. You have your net speed costs, your Orion costs, so they're both software, then you have the implementation costs.  It's pretty unique for a finance company to finance all three, but they will finance all three. well. So what they do is they finance all of that for all five years.  We recommend a five-year contract versus a three-year contract, because you hold on to your discount longer. And you start with a monthly payment.  It's a monthly payment starting in the first month. So it does make it quite a bit more manageable and a lot better for budgeting standpoint.  Heather is your LEAF representative. I don't know if you've met Heather before. a lot with leaf because for whatever reason, yeah, out here, no one wants to lease.

28:04 - Sandra Rudloff (Pivot Interiors)
  It's all out right out. So it's like, that's great. But yeah, we used to try to push it and we had, you know, relationships with the league people, but just it's not much in demand here.  So it's another option.

28:19 - Marcus Dallacqua (SuiteCentric)
  It's another option. The interest rate was pretty reasonable with the one that we just did. I thought was really reasonable and it was lower than what they give to their clients.  So like they definitely, they definitely treated the dealer well. And almost all miller and old dealers are pre-approved. So they didn't even look at, I think I can say this.  Maybe I won't say it.

28:40 - Angela Davis
  just say, it went very fast and they were pre-approved. From an implementation perspective, the one thing that would be to your advantage of getting that NetSuite instance, even going a couple of months early, user adoption, talking about change management.  have to. coming to people involved. If you flip the switch to get your instance provisioned and then just hit the ground running, you don't have as much time to allow your users to do some of the learning, right?  The online learning, get them acclimated. Our team can go in and do the bundle installs with Orion. There's a lot of prep work that can be done behind the scenes if you do consider that path.  So there's some benefit to it.

29:29 - Sandra Rudloff (Pivot Interiors)
  So if you redo the quote, know, new numbers and then, you know, give some options as far as either, you know, delay to start implementation, delay deposits, and of course, leave financing that I think would be, you know, some information Kim would really appreciate.

29:46 - Marcus Dallacqua (SuiteCentric)
  Okay, so with your permission, can I switch out the leaf to loop them in the conversation? That'd be great.  Yeah. Yeah, I'll do that right away.

29:55 - Sandra Rudloff (Pivot Interiors)
  And then, yeah, I'm meeting with the NetSuite Rep tomorrow.

29:58 - Marcus Dallacqua (SuiteCentric)
  So we'll get the update.

30:01 - Sandra Rudloff (Pivot Interiors)
  Okay, and then y'all, you know, try and ping him in the next couple days when he's not in a meeting and see what his schedule looks like and just kind of know what we've discussed and, you know, may see some new numbers next week.  All right, very good.

30:16 - Marcus Dallacqua (SuiteCentric)
  I'll get to work on that.

30:18 - Sandra Rudloff (Pivot Interiors)
  right.

30:19 - Marcus Dallacqua (SuiteCentric)
  Thanks, everyone.

30:20 - Angela Davis
  Thanks, and appreciate it.

30:21 - Sandra Rudloff (Pivot Interiors)
  Thanks, Andy. Bye.

30:22 - Adam Baruh
  Bye. Bye.

30:23 - Sandra Rudloff (Pivot Interiors)
  Bye.

30:24 - Adam Baruh
  Bye. Bye.