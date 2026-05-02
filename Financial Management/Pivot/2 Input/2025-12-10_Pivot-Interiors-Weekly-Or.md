# Pivot Interiors - Weekly Orion Check-In/Financial Mgmt BRD Review

**Meeting Date:** 10th Dec, 2025 - 11:00 AM

---

**Chris Trumble** *[00:04]*: Good morning, Sandra. 
**Debbie Herbert** *[00:06]*: Good morning. 
**Chris Trumble** *[00:08]*: Morning, Sandy. 
**Chris Trumble** *[00:16]*: Oh, you're on mute, Sandy. 
**Sandra Rudloff** *[00:20]*: But you wish you could do that all the time. Mutely. I was gonna say Kevin and his team, who are all on now, they're the important people, and Brian's gonna miss the first part, so we can get started whenever you want. 
**Chris Trumble** *[00:33]*: All right, sounds good. 
**Debbie Herbert** *[00:35]*: Okay. I wanted to just give a quick project update and then use the rest of the time to go through the comments on the Financial management BRD. The quick update is we did deliver the project management workfront BRD last week. The other two, which are setup and commissions, are both under PM review. Solution architect review on our side. We talked about that yesterday. We really want to try to get through those by the end of the week, so you should be getting those soon. The question I had for you all is, were you able to meet between last week and now and make any of those decisions that you guys were contemplating? 
**Sandra Rudloff** *[01:30]*: Kind of. We got a couple decisions. I think the big important. Yeah, actually, I think we made some decisions, so. Relating to finance. Right? Is that what you're. Yeah, yeah, we can go over them. We did come up with some decisions. 
**Debbie Herbert** *[01:44]*: Okay. Do you want to just go through them as we go through the document? 
**Sandra Rudloff** *[01:48]*: I can tell you off the top, we do want to go with sweet tax. 
**Debbie Herbert** *[01:52]*: Okay. 
**Sandra Rudloff** *[01:53]*: And that's a big one. Fixed assets, we wouldn't want to do. If we want to do it until 2027, just let it. Keep our current process for 2026. 
**Debbie Herbert** *[02:10]*: Let everything bake a little bit before you take on something else. 
**Sandra Rudloff** *[02:14]*: Pretty much let us, you know, take a hard look at it and see if it's something we want to do. 
**Debbie Herbert** *[02:19]*: Okay. 
**Sandra Rudloff** *[02:20]*: The. 
**Chris Trumble** *[02:22]*: I think. 
**Sandra Rudloff** *[02:23]*: What was the other one, Kevin? Oh, AP Automation. 
**Chris Trumble** *[02:27]*: Yeah. 
**Sandra Rudloff** *[02:29]*: That'S another one that I think we still need more info. In fact, there's a comment on there, like, I know Avanto is a potential solution, but we don't know all what they do and how much is it, because the one demo we had scheduled, they canceled and they never rescheduled. 
**Chris Trumble** *[02:46]*: Oh. 
**Sandra Rudloff** *[02:46]*: So. That'S kind of still up in the air. But I. I think whether it's Avanto or the. I'm trying to think. The Netsuite app for that I thought was kind of pricey, like 4,000 or 4,500amonth. 
**Chris Trumble** *[03:05]*: No. Was it a month or was it a year? 
**Sandra Rudloff** *[03:09]*: I was shocked at the dollar amount. I thought it was pretty high. But I also need clarification on that, too, so. And then we had other questions about, like, well, if there's already like expense. I'm getting too deep into the BRD. I know, but if expense processing is already kind of factored in with routing and approvals, then it's like, you know, I guess we just have a lot of questions about the AP side so we can cover it on the BRD. Was there any other decisions we. 
**Kevin Baugh** *[03:37]*: Yeah, yeah. Another one is Expensify. Right. So internally we are not committed to Expensify. I mean, we're essentially using it as a data aggregator and approval flow software. We're not even doing direct deposit through it or anything like that. So I would imagine that Native netsuite has an expense management tool. We've. I've looked it up on YouTube that seems adequate for our needs. It would be fantastic if we could implement direct deposit through that tool. I'm not sure if that's a possibility, but I mean, Sandy, what we're spending a month for expensifying what we're getting out of it just doesn't make a lot of sense for us long term if we have something in Oracle. 
**Sandra Massey** *[04:20]*: And so I want to say a couple of things. 
**Chris Trumble** *[04:24]*: Yep. 
**Sandra Massey** *[04:25]*: Sandy, I will put on my task to send you some information around AP automation from the NetSuite side of teams. Now, pricing and all that stuff you might have to discuss with your account manager. And as far as Kevin, as far as expense, you can submit expenses from NetSuite no problem and establish approval process as well. But direct deposit does not work with expense reports. And so that be the caveat to it. I'm not sure if that makes any impact on your decision. 
**Kevin Baugh** *[05:04]*: Is there a way, I would imagine the system is smart enough where if we aggregate like say an employee is entitled to $50 reimbursement for a month, could that not route to like the payroll piece of Oracle? 
**Sandra Rudloff** *[05:20]*: Yeah. 
**Sandra Massey** *[05:21]*: So there's a way that you can say, okay, this expense is reimbursable or it's not. And so what we'll do is we create due to the employee. And if you have some sort of like ach process, you can order a nacha file that you submit to your bank. You can do that way. 
**Kevin Baugh** *[05:43]*: Okay, so not technically a direct deposit, but a way to process the electronic payment. 
**Sandra Massey** *[05:49]*: Correct. 
**Kevin Baugh** *[05:51]*: Okay, I mean, I think that would be much better than our current process. Correct, Helen? So, all right, I think that's. Yeah. So I guess, Sorry, I don't mean to detract from the conversation, but as far as like expensify, that was one other item in there where, you know, I don't know that we need to go down the expensified connector path for this yet. I would prefer to just see what we can do with the native expense management tool before committing to that. 
**Sandra Rudloff** *[06:17]*: And there was a whole section on just bank automation and reconciliation, so maybe exploring that, you know, and talking about it like Kevin says, you know. 
**Chris Trumble** *[06:26]*: Right. 
**Sandra Rudloff** *[06:27]*: Not having to cut a check in mail is probably the ultimate goal, let's put it that way. 
**Chris Trumble** *[06:32]*: Yeah. 
**Kevin Baugh** *[06:33]*: And another question on that is I'm assuming that Oracle is pretty much bank agnostic, given how many customers Oracle has. You know, we are currently with Comerica bank, but I'm just curious how flexible the system is. If we ever had to switch down the road. I'm sure that's. That's fairly easy and doable. 
**Chris Trumble** *[06:51]*: There's like. There's a few. 
**Sandra Massey** *[06:53]*: Sorry, I was gonna say there's a. 
**Chris Trumble** *[06:54]*: Few hundred banks that they integrate with. 
**Chris Trumble** *[06:57]*: Yep. 
**Chris Trumble** *[06:57]*: Like their. Their bank reconciliation app. The list is very long. It's. Unless it's like some very specific regional bank that's pretty small. 
**Chris Trumble** *[07:06]*: They. 
**Chris Trumble** *[07:07]*: So far what I've seen is they do integrate. 
**Chris Trumble** *[07:09]*: Okay. Yeah. Yep. 
**Debbie Herbert** *[07:15]*: Okay. Okay. Well, I jotted that stuff down and I will send out the status report. So you guys have that. Let me share my screen. What I'd like to do next. Well, any other, like, overall status we should talk about before I switch? 
**Sandra Rudloff** *[07:36]*: I don't think so. When do you want the project management one done by, like into this week? 
**Debbie Herbert** *[07:41]*: That would be. Yeah, that would be great if you guys can do it. 
**Sandra Rudloff** *[07:46]*: We. 
**Debbie Herbert** *[07:46]*: We still have a couple things to go through on our side, so another day or two wouldn't make a whole lot of difference, but collectively, if we can try to get everything. Out there scrubbed, updated and finished by the end of the month, I think we would be doing. We'd be doing okay. 
**Sandra Rudloff** *[08:06]*: Okay. 
**Debbie Herbert** *[08:07]*: Okay. Okay. Thank you for those updates. Let me share my screen. What I was thinking was I could have the document open and we could just start at the top and start going through. That was one approach. The other approach is if there was an area that you thought needed a lot of conversation, we could start with that first so that we make sure that we get a good. Understanding of what the questions were on that. On that subject. 
**Sandra Rudloff** *[08:41]*: I'll let Kevin decide this one. This is his baby. 
**Kevin Baugh** *[08:46]*: Did you repeat the question, please? 
**Chris Trumble** *[08:47]*: So I think honestly some of the things are just notes or small clarifications. I think it probably makes sense to just go through it one by one. Okay. Yeah. Just off the top, if that's cool with you guys. I don't think there's like a section that is heavier or more complex. Like the. All the questions have to be answered, so. 
**Debbie Herbert** *[09:08]*: Right. 
**Sandra Rudloff** *[09:09]*: Okay. 
**Chris Trumble** *[09:09]*: Might as well just start to knock them out. 
**Debbie Herbert** *[09:12]*: All right, so can everybody see my screen? And is it big enough to see? Okay. All right, first comment here. And this is under revenue and cost recognition. That section, the first comment here looks like. Sandy, we just need to. State what the actual situation here is. That costs are matched and posted automatically when the lines are invoiced instead of this sort of nebulous proper time. 
**Sandra Rudloff** *[09:47]*: Correct. 
**Debbie Herbert** *[09:48]*: Okay. If it's okay with you. Like, oh, come on, get in there. I'll have to do it later. 
**Chris Trumble** *[10:01]*: I can. I can do it, Debbie. 
**Debbie Herbert** *[10:03]*: Okay. For some reason it's not letting me. Oh, wait, there we go. Yeah, that's sloppy. I'll fix it. Either Chris or I will fix it as we go. 
**Chris Trumble** *[10:25]*: Yeah. I'll take the notes on this one. Debbie will kind of switch if you want. 
**Helen Hamel** *[10:30]*: Okay. 
**Chris Trumble** *[10:30]*: If you want to drive it, I'll make adjustments and stuff. 
**Debbie Herbert** *[10:34]*: Okay, that'll work. Okay, so you've got this first one, right? 
**Chris Trumble** *[10:37]*: Yep. 
**Debbie Herbert** *[10:38]*: Okay, Second one here. We need a process, perhaps an item. That. We need a process to invoice prior to fulfillment, but when we want to post to AR example is progress billings. So. 
**Sandra Rudloff** *[10:59]*: Right. Yeah. So, you know, it could be. I know there's the whole deposit process, but that doesn't post anywhere. We do want something that can post to unearned revenue for progress billings, especially for our construction division. So. And like this is what we did in AX back in the day, we just had an item that we created that posted to unearned revenue was a non taxable item, allowed us to do that. So just as a side note, we. We do need to bill sometimes and not revenue, but we do need to invoice and post to AR prior to fulfillment. 
**Debbie Herbert** *[11:37]*: Okay. Yeah, that looks like the quote that we took out of one of the transcripts, kind of triggered that scenario with you. So what we can do with that one, Chris, is we need to. I think we need to just list that as a requirement. 
**Sandra Rudloff** *[11:55]*: Okay. 
**Debbie Herbert** *[11:56]*: Okay. So that's this one from Sandy. 
**Chris Trumble** *[12:02]*: Yep. 
**Debbie Herbert** *[12:02]*: Okay. The next one looks like. This is telling us what the journal entry would look like. Debit, cogs, credit inventory. 
**Connie Chung** *[12:21]*: Yes, that's my. My question is that I highlight when cost recognize. Is that mean we're going to debit cost and we go into credit inventory? 
**Debbie Herbert** *[12:32]*: That's. 
**Connie Chung** *[12:36]*: Go ahead a whip. Either inventory or you call it a whip? 
**Sandra Massey** *[12:41]*: Yes. 
**Debbie Herbert** *[12:41]*: Okay. When items are fulfilled. I think. I think, Chris, this one we need to just double check with Marcus on. 
**Chris Trumble** *[13:02]*: So are we trying to confirm that what it's actually going to do is. 
**Debbie Herbert** *[13:09]*: Is it going to debit cost of goods and credit, inventory or wip? 
**Chris Trumble** *[13:13]*: Inventory and wip. Or wip. Or wip. 
**Chris Trumble** *[13:17]*: Okay. Okay. 
**Connie Chung** *[13:19]*: So does inventory or web recognized when we receive the product or how does it. What is the joint entries? I'm kind of relating to what we currently processing right now. We receive the product is going to be accrued liability as a debit. Inventory and accrued liability. And when we invoice the ap, that's going to be a debit to cost additional and we credit out the inventory. But to my point that now the new process look like we go into accrue the revenue when cost is recognized but revenue not recognized. So just kind of. I want to go through the transaction. How does it work? Well, cost recognized, but revenue doesn't. 
**Debbie Herbert** *[14:08]*: Jeanine, are you on? 
**Sandra Massey** *[14:10]*: Yes, I am. 
**Debbie Herbert** *[14:13]*: Can you double check that? If we have a process flow for that. Yes. And then we'll be able to. If we don't, we can put one together and then we'll have the answer to that question. 
**Sandra Rudloff** *[14:27]*: Yep, absolutely. 
**Debbie Herbert** *[14:31]*: All right, the next one we have here. Connie, please give an example of unknown caller. She whiz. Stop. Gee, sorry about that. Please confirm. Please give an example of the scenario when cost is recognized but revenue is not recognized. Please confirm. This is the reversing je. Okay. Okay. So, Connie, you're just looking for. Clarification on what the reversal looks like. 
**Sandra Rudloff** *[15:16]*: Yes. 
**Debbie Herbert** *[15:17]*: Okay. Janine, I think this falls into the same boat as the one above. Check the process flows. 
**Connie Chung** *[15:26]*: Because in general, I would think when you accrue the revenue, you will recognize the AR aging. But if we recognize the AR aging, that's really impact. Our AR18 is not really invoiced. So increase the collection date, the age. Yeah. 
**Sandra Rudloff** *[15:48]*: Okay. 
**Debbie Herbert** *[15:52]*: All right. Coming up next. Okay, so, Connie, the question here is we just sort of loosely put designated approvers. But are you saying that this should fall under the Financial operation manager? 
**Connie Chung** *[16:12]*: It's just a question mark. I don't know who will be qualified for this. 
**Sandra Rudloff** *[16:16]*: Who. 
**Connie Chung** *[16:17]*: Someone needs to know the history of the sales order. The project to be able to approve it. 
**Chris Trumble** *[16:26]*: Yeah, so we. We have an approval workflow. We just work with you guys, determine who can actually approve that. So it's usually by. I think it can be by role or by individual with manager overrides. So we'd Be looking to you to tell us who approves that. 
**Sandra Rudloff** *[16:58]*: Yeah, we'll determine that once we get into it. Yeah. Because we'll want to have multiple approvers in case someone's out. 
**Debbie Herbert** *[17:05]*: Yeah, okay. Yeah, we get into that once we actually start. Going through the. More of the configuration process beyond just the setup that we started working on. 
**Chris Trumble** *[17:17]*: Yeah. 
**Debbie Herbert** *[17:18]*: All right, so that's fine. 
**Chris Trumble** *[17:21]*: And then if anything is not set, like I just set it to Sandy, like it's just Sandy's problem that's going to be hurt, you know. 
**Sandra Rudloff** *[17:27]*: I'm just kidding. 
**Debbie Herbert** *[17:33]*: Wow. 
**Sandra Rudloff** *[17:33]*: There's like no love there. 
**Chris Trumble** *[17:35]*: Don't. 
**Kevin Baugh** *[17:35]*: Don't run away yet. 
**Debbie Herbert** *[17:36]*: Serious there for a second. That's like the. I, I worked for a telecom company eons ago and I was a payroll accountant and there had been a, A. Let's see, what did they call it? There was this. Dumping. I forget what they called the name of the account, but there was like this dumping ground for stuff they couldn't reconcile and in salary expense. And I actually, I had been in that group for like four years and I only got it to reconcile one month. 
**Chris Trumble** *[18:12]*: So. 
**Debbie Herbert** *[18:13]*: Yeah, just. Just make it somebody else's problem. Okay. Oh, let's see. Connie, you can move on. 
**Connie Chung** *[18:20]*: It's the same thing we do. Step. Yeah. 
**Debbie Herbert** *[18:23]*: Yeah. Okay. All right, so moving on down. Okay. Sandy, using the quoted cost is only for internal labor, project management and design. All other costs should be at actual cost. Okay. 
**Sandra Rudloff** *[18:43]*: Yeah, the whole reconcile, you know, actualized to actual cost. I mean, the sales order should have the actual cost. 
**Chris Trumble** *[18:51]*: Real cost. 
**Sandra Rudloff** *[18:52]*: Yeah, you know, it. I think we talked about this before. So if during the AP process, our invoice, you know, the freight came in higher than what was on our sales order, we want to pay the app, you know, the amount invoiced, but we also want that cost reflected on the order. So is that the normal that you can adjust the cost of the sales order line during ap? 
**Chris Trumble** *[19:20]*: I don't think that's the normal workflow. 
**Sandra Rudloff** *[19:24]*: So what would happen if my invoice came in higher or lower than the PO amount? Because right now for us, it goes to the purchase price variance account, I believe. Right, okay, Helen. And it doesn't. I mean, so if you look at the project, you're not going to see that the cost came in higher or lower. And it also doesn't impact commission. So we want all actual costs with the exception of internal services. I'm not sure how that works. 
**Chris Trumble** *[19:54]*: Yeah, yeah, there's. There is like a cost variance count, and I'm not positive how all of that works, but yeah, I can get clarification on that one. But I don't think it's a complicated accommodation to make it be exactly what you've listed here. 
**Sandra Rudloff** *[20:11]*: Okay. 
**Chris Trumble** *[20:12]*: Yeah. 
**Debbie Herbert** *[20:19]*: Okay. Question on 3.0 2.05. Question on External services. 
**Sandra Rudloff** *[20:32]*: Yeah, I wasn't sure what you meant by that. Because external labor vendors still get a po. It behaves just like any product po. If there's a variance, you know, issue po, pay variance should be captured and back to the order and project. 
**Debbie Herbert** *[20:49]*: Okay. This is under the project accounting section, I guess. 
**Sandra Rudloff** *[20:55]*: What is a lot numbered inventory for tracking external services. Like I said, we would be issuing a po. 
**Chris Trumble** *[21:11]*: Oh, yeah. 
**Chris Trumble** *[21:12]*: So I, I think this is actually incorrect. 
**Chris Trumble** *[21:19]*: Like, this is just referring to the idea that there is a netsuite default item for external services and there might need to be more than one. It might be labor. It might be. Whatever it is. I don't know why it says lot numbered inventory. That's just the type of netsuite item that we use in general for the default items for a number of reasons that like, play out all through the, like the JSON process into finalization and everything. But when it's listed in this context, that is a little confusing. Like, it's not actually inventory. Right. It's it. It's just this item that is for external services that post to the right GL accounts. So I think it might be the fact that we listed here, like we're referring to the type of inventory item it is, but it doesn't. 
**Chris Trumble** *[22:08]*: It doesn't need to be listed here. So we're just using a default netsuite item for tracking external services. And depending on the number of external services you have, we can, you know, if they need to hit different GL accounts, we can accommodate that by just using the right set of items. 
**Sandra Rudloff** *[22:26]*: Okay. 
**Chris Trumble** *[22:26]*: So I can. 
**Chris Trumble** *[22:28]*: I can reword this. 
**Sandra Rudloff** *[22:30]*: Yeah. For taxation and also for gl. 
**Sandra Massey** *[22:33]*: So. 
**Sandra Rudloff** *[22:34]*: Okay. 
**Chris Trumble** *[22:34]*: Yeah. So any tax rule would necessitate a different type of item. 
**Chris Trumble** *[22:40]*: Yeah. 
**Chris Trumble** *[22:40]*: But we, yeah, when we make our items, we'll just say like, you know, it's. It's kind of interesting because it's like, you know, all Herman Miller furniture gets one item and it hits a GL the same. It starts to get a little bit more complex when you get into like those, like you said, taxable, different taxes and all that stuff. So I can rewrite this to be more clear. 
**Chris Trumble** *[23:03]*: Okay. 
**Debbie Herbert** *[23:05]*: Okay. The next one here. 
**Sandra Rudloff** *[23:11]*: It'S the same Comment as I had before. Yeah, we want actual costs not quoted with the exception of internal labor. 
**Debbie Herbert** *[23:19]*: Gotcha. Okay. Okay. Due to the number of partial invoices received, can we match exactly to the PO to limit variances? 
**Helen Hamel** *[23:45]*: So basically what I'm saying, there is right now because of the way our sales orders look and stuff. So we have, so we have a sub labor vendor that we're using. We have a quantity one for $1,000 for that job. But they partial invoice us, so we can't because we only round to two decimal places in D365. We always have a variance on that PO. So then it looks like there's not enough funds left on the PO when the last invoice comes in, sort of thing because it hits PPV. So my question is, how does that work in NetSuite? What does that look like? 
**Sandra Rudloff** *[24:25]*: And Helen, that's actually a wonderful point. Is it a two decimal place or three decimal? Because, I mean, we could do three. That would be so much more helpful. 
**Helen Hamel** *[24:35]*: Yeah, and it's really good on like the bigger. I, I mean it's not so big of a deal on the smaller ones, but we have a sub labor vendor. We have a, you know, a 2 million dollar PO that we have a 10% invoice or 10, you know, 15% invoice. And then you get into all these rounding issues and then, you know, I just had to do a big project that I had to do a reconciliation on. And it's a nightmare for us to figure out how much money is really left on those POS. 
**Chris Trumble** *[25:05]*: Is that a result of. Their pricing being beyond 2? 
**Helen Hamel** *[25:13]*: No, it's rounding. Yeah. Well, yes. And it's around. Yeah. It's because we only have two decimal points to work with in D365. Yes. 
**Chris Trumble** *[25:22]*: Yeah. So I remember there being a ton of discussion when were setting up the smart table of how many decimal places to go to on the smart table. And I thought we landed on four decimal points because that was like the biggest set that we saw of incoming prices across all manufacturers. So I'm pretty sure the smart table itself can handle four decimal places. I just want to double check like on that other side, like on the accounting side, how that flows through in rounds and everything else. Like there's provision for it. I want to make sure that it follows all the way through the system to the point that you're concerned about. 
**Helen Hamel** *[26:01]*: Perfect. 
**Chris Trumble** *[26:02]*: But we're not limited to two decimal places. There's no, there's no reason to be limited to that. So I'm going to mention decimal places here and get a little clarification on that. 
**Debbie Herbert** *[26:14]*: Okay. 
**Sandra Massey** *[26:22]*: I have a question around that. And Chris, correct me if I'm wrong, if this belongs to Orion. The. Discrepancies between your pr, between your purchase orders, your item receipts and your vendor bills are just minimal to decimal point or are bigger than that. 
**Chris Trumble** *[26:46]*: What do you mean? 
**Sandra Massey** *[26:48]*: Like if the amounts are greater than, say than $2 or $3 or are more than that. Not by decimals, by amount, total. 
**Chris Trumble** *[27:02]*: You're saying like, does it round up to the dollar and we're off by dollars instead of pennies or fraction. 
**Sandra Massey** *[27:08]*: Correct. 
**Chris Trumble** *[27:10]*: Yeah, I think, Helen, what you're saying is like any discrepancy whatsoever. Right. Like you don't really know. 
**Helen Hamel** *[27:16]*: Exactly. And we. But we could be off on some of these by hundreds of dollars. 
**Chris Trumble** *[27:21]*: Yeah. Depending on 10%. 10% of a 2 million dollar order, then you're off by dollars, tens of dollars. 
**Debbie Herbert** *[27:33]*: Okay, ready for the next one? Okay, so here we are still in the same category. We're talking about dual GP calculation. Question from Kevin. How do we true up if the official project GP is lower than the commissional gp, commissionable gp. 
**Sandra Rudloff** *[27:56]*: And actually I want to back in the day. And I don't know if this is how Orion would work. We invoice out an order, we get the vendor invoice, it's plus or minus. That difference would actually hit wip. And then at the end of every month, we got to clear cost WIP with revenue where that additional cost would then get cleared, hit cost of goods and impact commissions. So that's kind of how we did a true up after the fact. But all the cost, plus or minus would go into wip. So when we invoiced, that dollar amount would true up to the revenue. So I don't know if, I mean, is that kind of your process? If there's a cost discrepancy, does it go to wip? And then when we post, that gets cleared. By making sense at. 
**Chris Trumble** *[28:55]*: Yeah. 
**Kevin Baugh** *[28:55]*: So my question is just. Yeah, Sandy, I don't know. I'm not super familiar with the old process or whatever. I was just curious in our. In the inverse of this question could be true as well. How do we true up if GP is higher than, you know, if the opposite's true? Right. 
**Debbie Herbert** *[29:08]*: So. 
**Kevin Baugh** *[29:11]*: I'm not sure what that looks like. And it's almost like an internal control. My second question there, I was just curious, like, how do we make sure that we're not understanding our Expense, Right. To inflate GP and commissions. How do we make sure that we're, you know. Yeah, just my mind, like, how do we put. How do we protect ourselves here so that, you know, people aren't artificially, you know, inflating their, you know, GP or commissions and whatnot. 
**Sandra Rudloff** *[29:39]*: If your sales order had a fake low cost and we invoice it out and then, oh, look there, it wasn't a 30% margin, it was a 10. 
**Kevin Baugh** *[29:49]*: Right. 
**Sandra Rudloff** *[29:49]*: So it gets back to the whole thing about actual costs from vendors matching to revenue. 
**Chris Trumble** *[29:56]*: Yeah. So the first part of the true up. I'm not sure what the true up process is, but, you know, I've heard Marcus discuss that true up process. I can look into that. The second part is. The calculation of a commissionable GP at the project level. Like, as bills and everything are. Are coming in, you have this like, budget versus actuals table at the project level. And it's tracking, like, once the sales are created, it like draws a line in the sand and then all transactions that happen after that are like, that's like the realization process. Like how much of this has been realized. So it would show you. It would like, flag in red. Like, this is the quoted and this is what we actually, you know, these are the actual costs and it's tracking that over time. 
**Chris Trumble** *[30:52]*: But I think that the commissionable GP is looking at the actuals, not the quoted stuff. I mean, there's all kinds of rules we can write to properly calculate the commissionable gp. 
**Kevin Baugh** *[31:08]*: I've got another question, and this came up as were reviewing our aging reports. And currently we struggle with finance charges, Right? We struggle with sending finance charge invoices to our customers. And so oftentimes. We'Re a preferred dealer because we offer 0% financing, much to our detriment. And I'm wondering, like, if we have a customer who's basically getting zero percent interest financing from us, that's a cost, that's a true cost to pivot. Right. You know, our line of credit, we're paying interest on that loan. Is there a way to like, somehow calculate that into the project cost such that if I'm floating a customer for six months on a million dollars that's owed to us, that's an expense for that project that we're not fully capturing, if you follow. And I don't want our salespeople getting commission. Sorry. 
**Kevin Baugh** *[32:13]*: That should be factored into commissionable GP in my opinion. So just a thought. I don't know if it's possible to kind of reverse engineer that such that if we're ever floating a customer for free for 612 months, that's a real cost to us. How do we tie that back to a project? Is that possible? 
**Chris Trumble** *[32:33]*: Yeah, it is. So how do you arrive at what the actual hard cost of that is? 
**Kevin Baugh** *[32:41]*: I'd have to say how long has this customer not paid us, what's our interest rate, etc. Right. I mean we could do some math on that and say, you know, it was $20,000 in financing costs, whatever the number is. Right. $10,000 in financing costs to us that we ate on that project because this customer slow paid for six months. Yeah, but that's a cost that reduces GP on the project. 
**Chris Trumble** *[33:03]*: Yeah. So it's almost like. It'S almost like you add a formula line to that transaction that is a, you know, obviously a zero sell cost. You're putting in manually a cost in there. It's a line that doesn't print on any customer facing documents, but it's still affecting the GP over time. Now the only thing I, I don't know how we exactly would handle it. Like it's no problem to add a line that has a specific cost, but if that cost increases over time, it's like do you add a line for every month that this happens and you keep doing that until you get to the end of the project? I don't know how to like change the cost of that over time without like affecting other transactions. Like I think it's definitely something we could accommodate. I just don't know because it would change. 
**Chris Trumble** *[34:01]*: Like, like are, or are they offering it for six months up front so then you know the cost and you can put it all in one line or does, is there any like variability in that time frame? 
**Sandra Rudloff** *[34:14]*: How does the finance charge to customers appear? I mean so say you know, like Kevin's mentioning, you have a client is three months behind on paying their invoice. 
**Debbie Herbert** *[34:26]*: Yeah. 
**Sandra Rudloff** *[34:26]*: Would each statement have an accrued interest amount on it? 
**Chris Trumble** *[34:32]*: It could, yeah, it could. 
**Sandra Rudloff** *[34:33]*: And then. Well could we also then have an accrued interest cost associated with it? 
**Chris Trumble** *[34:40]*: If you are charging them for that, then that line would just have a cost and a sell on it. 
**Sandra Rudloff** *[34:46]*: Okay. 
**Kevin Baugh** *[34:47]*: Yeah. 
**Chris Trumble** *[34:48]*: If you're just tracking it internally to affect their revenue and you're not actually like charging the customer for it would be a cost only line. 
**Debbie Herbert** *[34:59]*: But. 
**Chris Trumble** *[34:59]*: It would just be like a manual. Line that somebody has to put into that transaction. 
**Sandra Rudloff** *[35:06]*: So natively, if we choose to have finance charges on Our invoices and statements. That's we have to manually do something. 
**Chris Trumble** *[35:16]*: Or so if it's going to be a standard, like they all get finance charges and there is some formula in which then we can automatically add it. But I didn't know if it was a case of like I'm selling this job, I'm starting off where we're not in that scenario. But if it gets to this point then we have to add that. Then you would add it manually. But if you want to add us, if you want to add a standard finance charge to every transaction, we can. 
**Chris Trumble** *[35:44]*: Set up a rule for that and. 
**Sandra Rudloff** *[35:46]*: Exclude by client or project. 
**Chris Trumble** *[35:49]*: Yes. The easiest way would be by client. A combination of client and order type. 
**Sandra Rudloff** *[35:55]*: Okay. 
**Chris Trumble** *[35:58]*: Project. A project just gets created automatically. I don't think you can, I don't know what you can do for a project, but would that work? A combination of client and order type. Like if you're doing something for like work from home or something that's like kind of automated. I don't know if you're doing a finance charge on something like that. That's why I thought order type. It's like if it's just a standard order, it's going to get a finance charge. 
**Sandra Rudloff** *[36:26]*: I guess we have to talk about how we want to approach finance charges because I mean doing it, putting a finance charge on the invoice to Apple or Google is useless. They're not going to pay. However, when Google doesn't pay us for six months because of their internal issues. Yeah, I could see Kevin wanting to, you know, assess the cost of basically financing that million dollar project for them over six months. 
**Chris Trumble** *[36:52]*: Right. 
**Sandra Rudloff** *[36:52]*: That might be something. Kevin, you know, we kind of talked about a project accounting almost position and you know, or someone maybe who's responsible for commissions or whatever else. Maybe that's when they start getting involved in the manually applying it. But again we want to make sure then it impacts commissions. So we got to figure that out. 
**Chris Trumble** *[37:12]*: Exactly. Yeah. 
**Kevin Baugh** *[37:15]*: I think it's suffice it to say there's room for improvement here. I think our current process and we need to. This needs to be on our roadmap moving forward. It's. 
**Chris Trumble** *[37:25]*: Yeah. 
**Kevin Baugh** *[37:25]*: Money's not free to us, unfortunately. 
**Chris Trumble** *[37:28]*: No, it's. No, it's not. And so would you see this as a day one. Customization? Like I mean probably if we write rules into it. 
**Kevin Baugh** *[37:38]*: Day one. Sandy, what do you think? I mean it if. Yeah, I'm not sure what the development time is on your side, but it. 
**Chris Trumble** *[37:45]*: Yeah. 
**Sandra Rudloff** *[37:46]*: I don't want to now. So. 
**Kevin Baugh** *[37:48]*: Yes. 
**Sandra Rudloff** *[37:49]*: Not having it go live isn't going to be changing our internal process. 
**Chris Trumble** *[37:54]*: Yep. 
**Debbie Herbert** *[37:54]*: All right. 
**Chris Trumble** *[37:54]*: I'll make some notes in here of what we're trying to accomplish, and then if we have to have another meeting about it and kind of scope out, if it's a pretty simple one, we might choose to have it for go live. But anything we have as an accommodate, we go through, like, a pretty short solution design process. We're like, oh, okay, that's actually just a customization of xyz. It's probably three hours, whatever it is. So I'll make notes to consider it and then we can revisit if we want to do it right up front or not. 
**Debbie Herbert** *[38:24]*: Okay. Okay. Banking. 
**Kevin Baugh** *[38:35]*: Oh, yeah, we answered this one. 
**Debbie Herbert** *[38:38]*: Yeah. 
**Helen Hamel** *[38:40]*: Yeah. 
**Kevin Baugh** *[38:41]*: The second one here, we just. I may have missed this, but we noticed a lot of FedEx reference in this document, so weren't sure. 
**Chris Trumble** *[38:47]*: Sure. 
**Kevin Baugh** *[38:47]*: Like Helen and I were kind of like, unclear as to why were specifically calling out FedEx. I. I may have missed this. 
**Chris Trumble** *[38:55]*: Now, I. Yeah, I don't know if you guys mentioned that you have a FedEx account early on, but it can be FedEx, UPS, whatever accounts. It doesn't matter. It doesn't. 
**Kevin Baugh** *[39:05]*: We do use FedEx. 
**Chris Trumble** *[39:06]*: Yeah. Okay. Yep. 
**Debbie Herbert** *[39:10]*: Okay. We good with that one? 
**Kevin Baugh** *[39:13]*: Yeah, I guess. But I, I don't know. Helen, are we clear as to. So supporting multiple FedEx accounts per warehouse location. What are we talking. We're talking about banking. What does that even. What are we getting at? 
**Sandra Rudloff** *[39:25]*: Yeah. 
**Chris Trumble** *[39:28]*: And why is it talking about FedEx in the banking section? It's a good question. 
**Helen Hamel** *[39:32]*: Well, why. Yeah, and why are there multiple FedEx accounts? 
**Kevin Baugh** *[39:36]*: I thought we should just add one. Yeah. 
**Helen Hamel** *[39:38]*: FedEx. 
**Chris Trumble** *[39:38]*: Yeah. So then maybe this isn't really even a requirement. 
**Debbie Herbert** *[39:43]*: Let's go back and check the transcript and see if it. 
**Connie Chung** *[39:46]*: Yeah, yeah. 
**Sandra Massey** *[39:47]*: Unless you want to integrate with FedEx, because there's an easy integration with them that will allow you to calculate shipping cost and all that stuff. That's probably what is making reference to not a bank configuration itself. 
**Sandra Rudloff** *[40:05]*: We have multiple accounts, but they all roll up to the single one for payment. But it was mostly for tracking purposes. It's, you know, who. Why is there a 300 charger? Who did it? And blah. And that's why we had multiple accounts. 
**Chris Trumble** *[40:19]*: But like, the rate tables are come from the parent account kind of. Right. Like if you need to calculate stuff on small package, it all rolls up to that one account. 
**Chris Trumble** *[40:29]*: So. 
**Sandra Massey** *[40:29]*: Okay, so the integration should be able to give you those options. 
**Chris Trumble** *[40:34]*: Yep. 
**Debbie Herbert** *[40:37]*: Okay. All right, the next question. From Helen. Credit card account recon. Is this an add on? 
**Helen Hamel** *[40:52]*: Yeah, I was just wondering, is this native to netsuite or is this something customized? 
**Sandra Massey** *[40:59]*: Which credit card do you currently have? 
**Helen Hamel** *[41:04]*: Which credit card we have Comerica, like. Well, and I also need to know the context. Is this to pay, you know, is this to pay from the system to vendors we have, or is this for our expense, like our credit, like our people that have corporate credit cards that we're paying? 
**Debbie Herbert** *[41:24]*: Yeah. 
**Sandra Massey** *[41:25]*: And so if you need to do a specific reconciliation, like match your vendor bills or your credit card transactions, there's ways for you to upload a file. It can be a QFX OFX or a vai and you will upload it and start reconciling that account. As far as payments that you do with that credit card, that will be loaded as an ACH on the expense reports. Kind of like that. 
**Debbie Herbert** *[42:04]*: So Sandra, I think you're saying this, it works. Well, first question is the credit card reconciliation is part of the out of the box functionality, is that right? 
**Sandra Massey** *[42:18]*: Yeah, that is correct. 
**Debbie Herbert** *[42:19]*: Okay. And then the, as far as the types of cards, whether it's used to. You know, in the two scenarios that were just described, that doesn't really matter, does. 
**Sandra Massey** *[42:36]*: Shouldn't. If you do it manually, but if there's an integration, say with Comerica that the system will do automatically bring the file from Comerica, then that will be a third party. 
**Debbie Herbert** *[42:48]*: That's. 
**Sandra Massey** *[42:49]*: Yeah, yeah. 
**Sandra Rudloff** *[42:50]*: Okay. 
**Debbie Herbert** *[42:51]*: Okay. So I think, Helen, to answer the question, it's. It's functionality that we just have to set up. Okay, Next from Kevin. How do we match items with 100% certainty? Sandra, we do this with just putting in specific tolerances, don't we? 
**Sandra Massey** *[43:24]*: Yeah, this is called, and this was what I was referring to Chris, before. If the tolerance is greater. So there's a way that you can have a two way process. We will match your purchase orders and your vendors. You establish the discrepancy level. Can be an amount or it can be a percentage. And the three way that will match your purchase orders, your items received and your vendor bills. And there's multiple ways that you can set up those discrepancies from the more specific to the most general meaning from the item or the subsidiary itself. 
**Chris Trumble** *[44:10]*: Yeah, I'm also going to post a kind of an informational page. It has a video on the Bank Feeds suite app. How exactly it works. Yeah, I'll post that both here and in the BRD but that's kind of a good overview of what the general idea of what the app is able to do. 
**Kevin Baugh** *[44:31]*: So does this automate cash posting? I guess again, maybe I like our current process. Right. We try to match to POS and POS listed in a. In a description for a payment. And I think what I was trying to say there is like the formatting of that can vary based on a customer's input. Right. So whether it's. If they're referencing a po, you know, 1, 2, 3, 4, 5, dash, 6, 7 or whatever, and then the next one or next customer inserts three spaces before or after the dash, you know, how does. You see what I'm saying? It's not like a universal input or format that I think we're seeing on. On that. As far as descriptions go. Correct me if I'm wrong, team. That's just my understanding. Right. I've seen different descriptions and ways customers are entering that information. 
**Kevin Baugh** *[45:19]*: So I wasn't sure like how the system would be smart enough to capture all those. Rules or variances. 
**Chris Trumble** *[45:28]*: Yeah. 
**Sandra Massey** *[45:28]*: So if you're talking about the three ways there's workflows that need to be installed in the account that will capture discrepancies. Major whatever amount of tolerance. I don't know, Chris is part of the Orion process, forgive me if I'm wrong or that's something that will be native of netsuite. 
**Chris Trumble** *[45:50]*: It's native. 
**Sandra Massey** *[45:52]*: Okay. So it's workflows. It's a bundle that will be installed and configured in your system. 
**Chris Trumble** *[45:58]*: Yeah. So you're more concerned about like. Yeah. If we have standard. Yeah. Not only in like the naming of it. 
**Helen Hamel** *[46:06]*: Yeah. 
**Chris Trumble** *[46:08]*: Yeah. 
**Kevin Baugh** *[46:09]*: Or does it spit out a list of hey, these errored out. We couldn't match. Please review manually type thing. 
**Sandra Rudloff** *[46:15]*: Yeah. 
**Sandra Massey** *[46:15]*: It will give you. It will give you. On the top of the transaction there's a discrepancy between the PO and it will post it as pending or as an exception of the transaction per the workflow. Whether there's a. When a discrepancy is present. And then if you have some sort of like vendor bill approvals, then it won't let you post it until you decide what you're going to do with that discrepancy. If you're going to accept it, then you can go and tell the system accepted and it will generate your discrepancy journal entries. 
**Helen Hamel** *[46:52]*: I actually think this question is around the AR side, not the ap. You're talking the AP side here. Yeah, this is. This question was on like AR on the AR side, apologies. 
**Sandra Massey** *[47:09]*: Payment. And then the question. Yeah, because I saw the word PO on that question and then I, I can afford. I kind of assumed that was it. There are match items with 100% PO number subscriptions with payments. That one I will have to go research. 
**Kevin Baugh** *[47:38]*: That's our only mechanism. I mean, correct me if I'm wrong team, but that is our, that is the only mechanism we have to match up to what's outstanding. 
**Sandra Rudloff** *[47:47]*: Correct. 
**Kevin Baugh** *[47:47]*: Is the PO listed on a payment. 
**Helen Hamel** *[47:51]*: So Joyce, do they PO or the. 
**Connie Chung** *[47:53]*: Invoice number or project id? Sometimes they refer to that. 
**Kevin Baugh** *[47:58]*: Okay, well that and so that's my point, right. It varies, right. Some people are maybe referring to an invoice number P.O. The way they, you know, every company is going to do it differently. Right. So in this case, as far as, because I mean automating cash posting or reconciliation here would be great. 
**Chris Trumble** *[48:15]*: But yeah. So basically what happens if it doesn't match up with anything that it can see in our system? Like does it stop and say, okay, we have this thing coming in externally. Like what is the process? Does it say, okay, which one of these internal documents do you want to match that to? Okay, cool, match it to that one. Now compare those two. Like I think that's how works. But we have to confirm that's like the logical way it would work. Right. Like I can't match it to anything. Help me match it. 
**Chris Trumble** *[48:45]*: Yeah, yeah. 
**Sandra Massey** *[48:46]*: Okay, Meaning is like ad hoc transaction. I'm just trying to get to understand. 
**Chris Trumble** *[48:54]*: No, it's like if. 
**Chris Trumble** *[48:57]*: Like. 
**Chris Trumble** *[48:58]*: Let'S say we're thinking of it in terms of PO number, but they're thinking in terms of invoice number and there's. They have it, you know, the syntax is wrong, it's not like matching perfectly. What happens. We know we have this outstanding thing we have to reconcile. Are we able to pick the internal document that it needs to reconcile against in that app? 
**Sandra Massey** *[49:24]*: Gotcha. 
**Sandra Rudloff** *[49:26]*: So how does that work with deposits? Because we would have a deposit invoice, but there's nothing to match on ar. Right. 
**Sandra Massey** *[49:34]*: So yeah, it will come as on deposit and then you'll have to check where it belongs and then deposit it to the correct account. There's this account called Undeposited Funds, which is a non posting account and you will see it on that account to decide where it goes. So we probably need to. Further research this to give you more clarity on it. 
**Kevin Baugh** *[50:05]*: Yeah, so I think my takeaway is like Will this, will we basically continue our manual process or can we really automate these things as stated here? Because we have people obviously internally who spend a lot of time on this and it would remove. Yeah, it would be fantastic if we could get this set up. But again, I don't know if that's kind of part of the, the basic package here that we're getting. 
**Sandra Rudloff** *[50:31]*: So we should also mention we use square for our online stores and that would be completely different because there's no cross reference to our order and we'd have to. They're all 100% deposits towards orders. So we'll have to just make that as a little asterisk. 
**Chris Trumble** *[50:52]*: Okay. Chris, I'll note that in here as well. Yes. 
**Debbie Herbert** *[50:59]*: So I'm just thinking, thinking about the data anomaly situation where, you know, maybe there's some. Preceding spaces or dashes or something that preclude a one to one match. Is there anything you could do with like a custom field that would help at least. Match you up to the right customer? Between the vendor and the customer? 
**Chris Trumble** *[51:32]*: Yeah. You just don't know the nature of the syntax error. 
**Chris Trumble** *[51:37]*: Right. 
**Helen Hamel** *[51:38]*: It's like. 
**Debbie Herbert** *[51:38]*: Yeah, exactly. 
**Chris Trumble** *[51:39]*: You have to like, it's like for a vendor, if, you know, like they always have three preceding zeros or something like that. It's like, okay, that's a rule for that customer that you can account for. Yeah, but then how many of those rules are in place? You know, it's like if you deal with X amount of vendors and each one of them has a few quirky rules, then you're like managing this table of exceptions. 
**Helen Hamel** *[52:06]*: Yeah. 
**Chris Trumble** *[52:06]*: So what I want to do is see what the mechanism by which they do the matching is, and maybe the mechanism is smart enough to handle that. You know, this is like one of the most downloaded and installed suite apps. Like, I'm sure they've thought of this. I just don't know what, I just can't speak intelligently about, like how they're actually doing that matching, you know? 
**Debbie Herbert** *[52:26]*: Yeah, okay, so we'll dig into that one. 
**Sandra Rudloff** *[52:29]*: It's like the old saying, you can't write code for stupid. 
**Chris Trumble** *[52:32]*: Yeah, right. Yeah. There's not a logical expression you can write. It's hard to account for. 
**Kevin Baugh** *[52:39]*: Same thing here, by the way. Like, like kind of logically, like, how do we. So, Helen, I don't know if you want to speak to this one, but on the credit card recon side, I mean, that would be Fantastic. Right? If we could automate that. Did you have anything you wanted to add on top of that? 
**Helen Hamel** *[52:55]*: No, I'd like to see if there's any option there. I'm not sure what it would look like. 
**Debbie Herbert** *[53:06]*: Project charges versus opex. 
**Helen Hamel** *[53:09]*: Yeah, so we have like we're talking about our corporate credit cards, our users. Some of them have project related chargers charges that are PO related. Some of them are just like expenses. So we just, I guess to see how we could reconcile that if we go with some option in the system that does an auto reconciliation for us. 
**Kevin Baugh** *[53:38]*: Yeah. So like is the system. How does. Is the system smart enough to basically tie a charge to a project versus just general opex? And I mean that like it almost sounds too good to be true to me. Like almost like you need manual intervention with a lot of this stuff. 
**Chris Trumble** *[53:54]*: But yeah, right. 
**Kevin Baugh** *[53:55]*: We're just not sure. 
**Debbie Herbert** *[53:57]*: I'm. I'm thinking of. Can't you remember which one it was now that we used but at a previous place you as the user you would select. If you, if you were attached to a project, you could select that project right off the bat. And it knew like it had items behind the scenes that directed things to where they needed to go. I think that one. 
**Sandra Massey** *[54:29]*: If I can add some information around that. Say an employee enters a expense report. There's a way when they enter the spend report to tag the project and to tag the task associated with that without a specific expense report. And so that will tag the expense to the corresponding process. I mean project. I can talk. 
**Kevin Baugh** *[54:54]*: So, sorry. One big assumption in that and that'd be great is that. And this is a problem that we currently have with expensify is one assumption in all this is we're assuming that our employees are correctly coding certain expenses right to the right. Right in. In the event that an employee selects the wrong GL or selects the wrong project or whatever like that. That's just my only concern with that. But someone's got to make a decision at some point. Right? I mean so I guess then it comes down to training and coaching and making sure that everyone understands how to use the system. So. 
**Chris Trumble** *[55:25]*: And then still like there is a process of on the finance side like somebody going in there and confirming that they are coding it correctly. Like that's an age old issue. 
**Helen Hamel** *[55:37]*: Yeah. 
**Chris Trumble** *[55:39]*: Guilty of it myself. 
**Sandra Massey** *[55:40]*: Let's say they don't know the GL category. The GL account. You can establish what we call GL accounting list on the accounting list. Accounting management. I Forgot the specific name. But you can tag expense categories. I'm sorry, I was forgetting the exact word. You can tag a GL account to that specific expense category. And so they only have to select the expense category. And then they will have to mess up with your GL so it will be more accurate. And then the other. 
**Debbie Herbert** *[56:14]*: They just need to know the name. They don't need to know all the coding behind the name. 
**Sandra Massey** *[56:19]*: Exactly. You just give it a name, say airfare or meals or whatever, and you'd tag it to the appropriate SPENDS account. 
**Debbie Herbert** *[56:32]*: Okay. All right. We will do the confirmation on that. And I think were just talking about the. Oh, no, this is a separate one now, Helen. Manually override payment files before sending them to the bank. 
**Helen Hamel** *[56:50]*: Yeah, it says here system automatically sends payment instructions to Comerica based on, I guess, what invoices we have aging on the system. But I'm sure there must be. 
**Debbie Herbert** *[57:02]*: There's a step in. 
**Helen Hamel** *[57:03]*: Yes, there's a step for me to like say, yes, go ahead and pay all those. 
**Sandra Rudloff** *[57:09]*: Right. 
**Debbie Herbert** *[57:09]*: Yeah, there is. 
**Helen Hamel** *[57:11]*: That was my only question there. 
**Debbie Herbert** *[57:13]*: Yeah, I think the intention of that statement is to say that you don't have to go to the bank portal, upload the file, watch it run, blah, blah. Once that approval is given, it should send the file off for you. Check reconciliation, bank recon, bank transactions import automatically. So, Connie, are you talking about check specifically? Are you just talking about the monthly. 
**Connie Chung** *[57:47]*: Respond in general check specifically? Yes. 
**Sandra Rudloff** *[57:52]*: Yeah. 
**Debbie Herbert** *[57:52]*: So there is a bank reconciliation tool and it will and Sandra, correct me if I mess up here, but it will match as many transactions as it can based on the rules that we've set up. And then anything else that it doesn't automatically match you would go in and match it up. I think the check numbers, Sandra, I think check numbers shouldn't really be a problem, should they? 
**Kevin Baugh** *[58:22]*: No. 
**Sandra Massey** *[58:22]*: No, they shouldn't. And then you can create what they call reconciliation rules. And the system also will suggest automatically if it's a transaction that occurs often, then they will create their own reconciliation rules. You just have to click run reconciliation rules and will match those rules that have been either set by you or set by the system. And so you will have the opportunity to review and then submit to be reconciled. 
**Debbie Herbert** *[58:55]*: Does that answer the question or did. 
**Sandra Massey** *[58:57]*: I go too fast? 
**Sandra Rudloff** *[58:58]*: Did I go too fast? 
**Sandra Massey** *[58:59]*: Apologies, sometimes I talk too fast. 
**Connie Chung** *[59:03]*: No, I'm good, thanks. 
**Sandra Massey** *[59:05]*: Okay, no problem. 
**Debbie Herbert** *[59:07]*: Okay, let's see. We are just about of time. How many more do we have in this? Okay, one more for this section. 
**Helen Hamel** *[59:13]*: Looks like you can skip that one because we just answered that above. 
**Chris Trumble** *[59:16]*: Okay. 
**Debbie Herbert** *[59:18]*: Okay, so this takes us into. The next section. 
**Chris Trumble** *[59:26]*: Yeah. 
**Debbie Herbert** *[59:26]*: No, it doesn't. Wait a minute. 
**Chris Trumble** *[59:28]*: I do have a one o' clock as well, so. 
**Debbie Herbert** *[59:31]*: Yeah, can we. 
**Chris Trumble** *[59:32]*: We have a session scheduled for Friday. Can we just continue this process? We're like 30% of the way through or something like that. So in the meantime, we can try to get clarification on as many of the outstanding ones as possible and then just kind of pick this up on Friday. 
**Debbie Herbert** *[59:48]*: Yes. Do we have. Friday is scheduled correct? 
**Sandra Rudloff** *[59:52]*: Yep. 
**Chris Trumble** *[59:53]*: Yep. 
**Debbie Herbert** *[59:53]*: Okay. Does that work for the pivot team? 
**Chris Trumble** *[59:57]*: Yep. 
**Sandra Rudloff** *[59:59]*: Joyce, Connie, I'll add you to the invite. 
**Helen Hamel** *[01:00:03]*: Okay. 
**Chris Trumble** *[01:00:04]*: Okay, perfect. 
**Connie Chung** *[01:00:05]*: Thank you. 
**Debbie Herbert** *[01:00:05]*: Sounds good. All right, well, this was really helpful. Thanks, everybody. We'll see you on Friday. 
**Kevin Baugh** *[01:00:10]*: Thank you. 
**Sandra Massey** *[01:00:10]*: Thank you. 
**Chris Trumble** *[01:00:11]*: All right, see you guys. 
**Debbie Herbert** *[01:00:11]*: Bye. 
