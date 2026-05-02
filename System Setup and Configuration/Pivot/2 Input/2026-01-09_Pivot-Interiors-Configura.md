# Pivot Interiors: Configuration Part 2

**Meeting Date:** 9th Jan, 2026 - 2:30 PM

---

**Sandra Massey** *[00:00]*: Happy new year. 
**Chris Trumble** *[00:01]*: Happy new year. Yeah. Hi, connie. 
**Sandra Massey** *[00:15]*: Good afternoon. Good afternoon. 
**Debbie Herbert** *[00:19]*: Happy Friday. 
**Yuridia Silvas** *[00:20]*: Happy Friday. 
**Debbie Herbert** *[00:24]*: Sorry, my printer is making a bunch of noise. It'll stop in a second. 
**Chris Trumble** *[00:28]*: A printer? A printer. What are you printing? 
**Debbie Herbert** *[00:35]*: I'm gonna have. I'm asking the HOA for approval to hang up some lights, so I have to print out the plaid. Even though the lights are on the house, they make you print out the plat and highlight where the lights are going to be. 
**Chris Trumble** *[00:54]*: Bizarre. 
**Debbie Herbert** *[00:55]*: But. 
**Chris Trumble** *[00:57]*: That'S why I live in the woods. 
**Debbie Herbert** *[01:00]*: You don't have to worry about that. 
**Sandra Rudloff** *[01:01]*: Right. 
**Chris Trumble** *[01:02]*: Yeah. 
**Debbie Herbert** *[01:03]*: Yeah, I. I would be okay with that. 
**Chris Trumble** *[01:07]*: All right, well, I'm going to lead us through some additional configuration. We did a lot of the heavy lifting last session, but, Debbie, is there anything you want to cover at the top before we get started in configuration? 
**Debbie Herbert** *[01:22]*: No, just that, you know, we had started this before the Christmas holiday and these are the first steps that we take to set preferences and enable different features. So some of these things that you're going to see are just pertain to netsuite in general and then if there is something that pertains particularly to Orion, we'll point that out. But this is the first step in getting the system initialized so that we can proceed with further configuration. So. Cool stuff. 
**Sandra Rudloff** *[02:01]*: We do have the accounting team on here, so if there's. I don't know if it's possible to focus on those first so we can let them go, but that would be great. 
**Chris Trumble** *[02:10]*: We. So we actually. Let me share my screen here. So from what I recall, we did go through these first five sections here. Company accounting, tax transactions. I think we're in a good place. I don't know if you want, like, scentsy. Accounting team is here. Do you think we need to go back through the accounting stuff? 
**Sandra Rudloff** *[02:35]*: Debbie had requested to have the team on, So I. Yeah, I'm not sure what. 
**Debbie Herbert** *[02:41]*: Yeah, I thought we still had a few topics that we would need them for. So let's just do a quick run through of the company and the accounting and then let's go back to employees, because I did. There are some things about expense and other things there and then I think the rest of the categories we could just do with the smaller team. 
**Chris Trumble** *[03:09]*: Okay. Yeah. 
**Gary Strickland** *[03:10]*: And Deb and Debbie, we have the accounting preferences as well that were going to cover today. 
**Connie Chung** *[03:14]*: So. 
**Chris Trumble** *[03:15]*: Yeah, we could do that. Yeah, we could actually do that too. We can. I'm prepared to do the. The actual accounting preferences as well, so we could take care of that. Because I think this stuff is all pretty standard in here. You guys don't do intercompany? We don't need, yeah, none of the intercompany stuff. Consolidated Payments is on. Just trying to think if there's anything out of the ordinary where we are. 
**Sandra Massey** *[03:42]*: Making decision, maybe amortizations. Do you amortize, say, transaction over time? 
**Sandra Rudloff** *[03:56]*: Not transactions, no, and definitely not for revenue. 
**Chris Trumble** *[04:01]*: Yeah, not revenue. 
**Sandra Massey** *[04:03]*: Not revenue. How about expenses. 
**Kevin Baugh** *[04:09]*: Like OpEx? 
**Connie Chung** *[04:11]*: I mean, like PPE? Like, yes, we do have the PPE amortization right now. We just have like a menu Excel, we track it monthly. 
**Sandra Massey** *[04:23]*: Okay. So in netsuite we have something called amortization schedules. And so we can set amortization rules based in different criteria. And what it does is that graphs whatever it is that you prepare and create some schedule for it. And then as it is, prepare will generate a journal entry monthly. It will be set up on your reminders on your dashboard. And then it will allow you to keep track of those amortizations if you run any in, you know, on a monthly basis or in a period base. And so that's basically what it means. And then you can enter that template and it can be changed as well. And even these amortization journals can be memorized if needed. 
**Connie Chung** *[05:22]*: And you not talk about depreciation. 
**Sandra Massey** *[05:24]*: Right? 
**Connie Chung** *[05:24]*: That's something different. 
**Sandra Massey** *[05:26]*: That's something different. Correct. 
**Connie Chung** *[05:27]*: Okay. 
**Sandra Massey** *[05:28]*: Yeah. 
**Debbie Herbert** *[05:29]*: Okay. Hey, Sandra, let's take a note on this one because it looks like, and I think this came up last time when were going through this. It may be that general amortization is set up here, even though it says revenue accounting. Let's take a, let's take a note for that and see if it does appear someplace else. They may have changed, you know, with the last release where they're showing it. So yeah, let's just take a note on this one. We can, if it's not elsewhere in the setup, then I, I, my question would be if Pivot is interested in setting up those schedules that allow for some of that automation of, you know, the drawdown on the balance and the creation of the journal entries. And you can retire some of those Excel spreadsheets. 
**Connie Chung** *[06:25]*: I just want to add another thing that we do track like a finance list and the operating list is that I can see the organization in here too, because I don't know if the two software will be linked together between the printer file now used to be this current. So normally I download the transaction from currentify and then upload into the current ERP system. So I don't know how that you can link the two together between the NetSuite and the printer PI. 
**Sandra Massey** *[07:01]*: Yeah. Is there a way for you to give us an example of that spreadsheet so I can take a look or we can take a look and then let you know what's the best course of action for that specific. For that specific transaction that you load into the system. 
**Connie Chung** *[07:21]*: This is like a standard journal entry that I download from CountryFi. It will telling me how much to amortize it every month and update the authorization schedule on a monthly basis as well. So I take the information and they create into the journal entry and upload it to the current erp. Okay, so let me know what you need. I can download basically just download the transaction form the crunchify. That's all the data I need. 
**Sandra Massey** *[07:53]*: And then is your intention to keep those in Printify or will you like to handle those in netsuite? 
**Connie Chung** *[08:03]*: I will leave it to Kevin. Is it something that you. 
**Kevin Baugh** *[08:06]*: I mean, our default answer to this entire project is whatever we can do in. In netsuite, we would prefer to do in netsuite. So I guess I'll throw that back at the. The team here to say what can we do in netsuite to. To stop these recurrent software subscriptions and redundant costs in our system? 
**Ken Baugh** *[08:25]*: Yeah, yeah. Do you. Does it. Does. Does netsuite have a lease amortization program that you know, for the new accounting rules around leasing that. That does all that? If it does, then we could look at, you know, we'd like to see that and see how that works. But you know, if that can be done within NetSuite and we don't need to do it within Crunchify, that would be fine. 
**Sandra Massey** *[08:52]*: The thing with that is that is included on the fixed asset management. That's how you will do your leases management. 
**Ken Baugh** *[09:06]*: I think for like all the ROU calculations and so forth. 
**Sandra Massey** *[09:13]*: Let me check on that because I'm used to handle those leases on the fixed asset managed. 
**Chris Trumble** *[09:22]*: Yeah, the fixed asset management module does do the ROU assets. 
**Sandra Rudloff** *[09:27]*: Okay. 
**Ken Baugh** *[09:29]*: Okay. Well that, you know, that's. And I don't know that our team has actually seen a demo of the fixed assets. 
**Chris Trumble** *[09:37]*: Yeah. 
**Ken Baugh** *[09:38]*: Capability. But if it can be done straight within there, that would be preferable. 
**Sandra Massey** *[09:42]*: Okay, now I have a question for Debbie. Was the fixed assets considered a phase two kind of process because it's not configured in the system yet. 
**Chris Trumble** *[10:01]*: Yeah. 
**Debbie Herbert** *[10:04]*: Okay, let's keep that internal note, Sandra, and then let's keep on going through the list. 
**Chris Trumble** *[10:13]*: So for the time being, we will turn this or Keep this off. But there is not a lot of risk in turning it on. If you. It's like a lot of these features, you turn them on. As long as you don't create a schedule, it doesn't do anything in the system. 
**Ken Baugh** *[10:28]*: So. 
**Sandra Rudloff** *[10:28]*: Right. 
**Chris Trumble** *[10:30]*: And then we decided not to have adjustment only books or extended accounting period closed practices. So that was in accounting. We can also hop in. 
**Kevin Baugh** *[10:40]*: Chris, quick question on that. That last comment you just made, I know in the BRD you had called out the 13 period accounting schedule. 
**Chris Trumble** *[10:49]*: Yeah. 
**Kevin Baugh** *[10:50]*: I don't know if that's what's meant with extended accounting period close. I think internally we've had discussion on this one and team, feel free to chime in here. I don't know that it makes sense to change everything over to a 13 period calendar. 
**Chris Trumble** *[11:06]*: Oh, okay. Yeah, we can. 
**Kevin Baugh** *[11:08]*: So I mean, feel free to. Yeah, yeah. I mean like as far as alignment with bank reconciliation and just everything else. Right. If we just kept the last period open longer as we do now. So that's a foundational preference that I want to address right now. So is that last checkbox there on the screen? 
**Chris Trumble** *[11:26]*: Well, this one. Yeah. This one says you're not required to individually close accounting books. You can continue to close all of your books at the same time. So I don't know. I think that's a little bit different. There's a few conditions that have to be met if you want this to be available. But I think making the decision on 12 or 13 periods is probably the first step to that. And then we can make the adjustments necessary for whichever decision that is. 
**Sandra Massey** *[11:57]*: I'm sorry, go ahead. 
**Connie Chung** *[11:59]*: So Kevin, what is the period 13? What is the purpose of having period 13 and 12 and the 13? So just so that I understand why we're not choosing additional 13, because I know that current ERP we do have period 13, but it's always like block. We hardly go to that. 
**Kevin Baugh** *[12:24]*: Right. So then I would just argue if we're not using it, then we don't need to set up the new system at the 13 year or, sorry, 13 period. 
**Connie Chung** *[12:30]*: What is the purpose for that? Right. 
**Kevin Baugh** *[12:35]*: Based on my research, I don't think it pertains to our industry and our process. Right. It's like high transaction retail type companies that want greater insight into like week to week variances are easier to justify having a 13 period calendar. Based on our industry and what we do. It's, it's like monthly, quarterly looks at the business. Right. So I don't think we need a 13 period calendar. 
**Ken Baugh** *[13:00]*: So Connie, just question. You said ours currently is set up that way, but it's locked and we never use the 13th period. Is that what you're saying? 
**Connie Chung** *[13:09]*: It's locked? Because what I'm thinking can probably the purpose of using the period 13 just so I can close the enrollment join entry. That's my fault. 
**Sandra Massey** *[13:19]*: I don't know why. 
**Connie Chung** *[13:20]*: But we don't open the period 13. It always. So I don't know what's the purpose of having the 13 for that is the purpose for close year end because I know that once a year I have to close all the transaction from the previous year and close out. 
**Ken Baugh** *[13:40]*: If we could. I think what. I understand what Kevin's saying. I think what I'd recommend is that we just check with our CPA firm on that, see if they have any. Any recommendation one way or the other. Because I don't know if they would. If they. So I think I would just like to have their input on it before we make that final decision. If that's. If we can make that after we just get a call from them. 
**Debbie Herbert** *[14:15]*: Standpoint. 
**Chris Trumble** *[14:16]*: Yeah, not a problem. Okay, so then standard for your reference, there's a few different places where you set these preferences. So the big one is in setup company. There's the company information that went through really early. That's just basic stuff like your website and your logos and all that stuff. There's Enable features, which is this entire section we're in right now. There's Enable features. And then for accounting, sales and marketing, there are a preference section for each one of those. Accounting and sales, ideally we set up today marketing. There's no adjustments that we need to make for that one. For this particular instance, the default settings are fine there. So since the accounting team is on we'll go. We'll hop out of this Enable features section. We didn't change anything, so we don't have to save it. 
**Chris Trumble** *[15:05]*: And then we'll go into the accounting preferences section. All right, let me bring up my handy reference guide here. 
**Connie Chung** *[15:24]*: What is the CAS basic reporting on the under general data? Is there anything I need to confirm? 
**Sandra Massey** *[15:32]*: I will allow you to the cash basis. 
**Kevin Baugh** *[15:36]*: We don't want that. 
**Sandra Massey** *[15:37]*: Yeah, you don't want that. Even though in the report itself there's an option to run as cash basis individually by rapport. You don't have to have this turned on if you need that kind of information. 
**Chris Trumble** *[15:57]*: Which one is that in reference to. 
**Sandra Massey** *[15:59]*: The cash basis reporting. So they don't have. They don't need. No, they can run it on the reports individually. 
**Sandra Rudloff** *[16:07]*: Okay. 
**Chris Trumble** *[16:09]*: Yeah. 
**Connie Chung** *[16:09]*: So first under the journal ledger, you click the due date. So what's the difference between the aging report, transaction date and due date? Is that more for ar? For arap. 
**Sandra Massey** *[16:23]*: Usually it's for ar and then it's how you want to base your reportings for aging. You can base it out of due dates. Say you have terms for a specific transaction or you can base it. On the transaction date. I can talk to the. And so that is based on the transaction when the transaction was created. That's the two differences. If you have terms or if you want to just base it on the transaction date. 
**Connie Chung** *[17:06]*: Yeah, I just want to clarify because sometimes based on the auditor, they sometimes request to see the agent report by transaction date and the due, especially the bank, the invoice date and the due date. 
**Sandra Massey** *[17:21]*: And so you can have one or the other the terms. Usually if you select terms, they will establish that by due date. If you don't establish a due date, you can run it by the transaction date itself. 
**Chris Trumble** *[17:42]*: Yeah, I think that's why it's defaulted to due date. 
**Connie Chung** *[17:46]*: Correct. 
**Chris Trumble** *[17:47]*: So that's the netsuite default behavior. And that's also what we have in our all of our demo environments set up as due date. That was the original intention. But just to not get ahead of ourselves, I want to just go through these one by one. Some of these are just basic settings that we need to turn on, like in the ledger, use the account numbers, the numbering scheme. Obviously we do that one. We want to use the legal name in the account. We want access to all transaction types and reconciliation. We want to be able to expand account lists. Currently we're not doing cash basis reporting. So is there any concern with. 
**Kevin Baugh** *[18:29]*: No, we don't want that one. 
**Sandra Massey** *[18:31]*: Yeah, the majority of my clients don't use that. 
**Chris Trumble** *[18:36]*: Yep. And then we're going to leave this one on due date for now. 
**Kevin Baugh** *[18:41]*: I mean, quick question on that. So we just instructed our AR team to go off of basically invoice date, not due date. Right. For a store our internal tracking on what's owed to us. 
**Debbie Herbert** *[18:52]*: So. 
**Kevin Baugh** *[18:52]*: And I know our bank also requests this information. Helen, Connie, others, are there any issues if we default to transaction date? 
**Connie Chung** *[19:02]*: See the problem because then sometime that I come across they asking for both the more leaning to the invoice date. 
**Sandra Rudloff** *[19:10]*: Okay, Chris, we could. It just depends on how couldn't we. 
**Helen Hamel** *[19:15]*: I mean that's what I'm wondering if we can manipulate the data in Excel or something to do it by. 
**Sandra Rudloff** *[19:22]*: Yeah, or do you have a report that we create for, you know, different. 
**Chris Trumble** *[19:26]*: Uses and you wouldn't have to create it in Excel. You could actually just create it as a Safe search in NetSuite and put it on dashboards or however you want to use it. You can always export to Excel. But yeah, creating that report's no issue. 
**Sandra Massey** *[19:40]*: One important thing is when you load your customers in NetSuite, you don't need to add the terms because then it's going to turn into a due date transaction. So you don't add terms for the customer record. 
**Chris Trumble** *[19:57]*: So I guess if they're training people to think in terms of transaction date, Sandra, what's the harm in setting it to transaction date? 
**Sandra Massey** *[20:07]*: There's not really a harm because you can always delete the terms and then just enter the date. So there's not really an issue with that. 
**Chris Trumble** *[20:16]*: Okay, so would you be more comfortable, Kevin, if we set it to transaction date to default can always be changed later? 
**Gary Strickland** *[20:24]*: Sure. 
**Kevin Baugh** *[20:25]*: We have our entire team on this call, so I don't want to throw a wrench in our system. Yeah, that's how I see it. But if we have the flexibility of kind of deriving both with an Excel spreadsheet or whatever, it seems like a moot point, right? 
**Chris Trumble** *[20:40]*: Yeah, yeah. 
**Sandra Rudloff** *[20:43]*: Actually a question on that. If we had the wrong due date on an invoice or you know, AP or ar, can you change that due date? 
**Sandra Massey** *[20:54]*: It depends on what which state there is. If it's a, let's say a, an invoice. Best practices. 
**Connie Chung** *[21:04]*: Yeah. 
**Sandra Rudloff** *[21:05]*: Like an invoice for customer. And you know, we're, you know, we have the invoice posted with net 10. It was supposed to be net 45. Could we change it there? So then the reporting, if we did it by transaction date would be, or, sorry, due date. It would be accurate. 
**Sandra Massey** *[21:23]*: As long as there is not any terms on the transaction, you will be fine. It will be based by the transaction date. Now, one thing, if you're referring to the transaction date, the transaction day will define in which period that transaction is going to be placed on. And so that's one thing about that. It doesn't matter any other due date like start day or end day. You will see that detail when we go to the invoices. But if you enter another day, another date is always going to go to whatever period is open for that specific month. 
**Sandra Rudloff** *[22:10]*: It wouldn't change transaction date, it would just be the sign invoices. 
**Sandra Massey** *[22:14]*: No, never does it won't change it during that case. You Will void a transaction and then create a journal entry with this, the other one and reverse it and then enter it in the. In the appropriate video. 
**Chris Trumble** *[22:35]*: Okay. So all that said, I want the accounting folks on both sides to tell me which one. Which one we should. Is it. Are we still leaving it at due date? What would be your guidance, Sandra? 
**Sandra Massey** *[22:52]*: I will leave it on transaction date because they cannot the terms on any specific transaction manually. So I will leave it on transaction date. 
**Chris Trumble** *[23:04]*: Okay. 
**Ken Baugh** *[23:07]*: I agree. 
**Chris Trumble** *[23:09]*: The next one void transactions using reversing journals. That just gives you the ability to do so. This is I think automating. Set reversal variance date equal to the reversing journal date. When voided transaction is in a closed period. We usually leave that one off. Unless you guys specifically need that. 
**Connie Chung** *[23:32]*: Reverse transaction day equal to reverse internal day, whatever the original day that we book the journal entry, the reversing journal. And when it reverses it will reverse it back. But what if the close period. That is correct. 
**Chris Trumble** *[23:49]*: Yep. So leave that one off. Require approvals on journal entries. 
**Connie Chung** *[24:00]*: Oh, this is something you consider to have data pool. It might delay. Yeah. 
**Sandra Rudloff** *[24:09]*: Can you do it based on either dollar amount or which account? Because I can see like right off to bad debt. We'd probably want approval. But for any of things Connie does, probably not. Or maybe over a certain dollar value. 
**Sandra Massey** *[24:23]*: You can set it by dollar value or by role, even by department if you like to do so. So it shouldn't have. We can only set up by the transaction and add it as a sage search on the approval workflow. But it depends. It depends on the requires requirements that you're thinking about. 
**Chris Trumble** *[24:49]*: So is that. Are those dollar amounts set somewhere else, Sandra? 
**Sandra Massey** *[24:56]*: Yeah, they're set on the workflow itself or the workflow. If it's a basic based on role, you can always add it at the employee center. Will they have approval roles by amount or by transactions? 
**Chris Trumble** *[25:16]*: Okay. Yeah. 
**Ken Baugh** *[25:17]*: So that question on the approvals, if we set the approvals, do those. I mean, does that go out as an email to the approver or is it need to be done like within Netsuite? 
**Chris Trumble** *[25:32]*: It can. It can be an email. Basically it's going to generate a report. So that report can show up either on a dashboard as a reminder in the system, or it can. It's not an either or. It can be both or it can be emailed to that person as well. 
**Ken Baugh** *[25:46]*: Okay. 
**Chris Trumble** *[25:48]*: Yep. 
**Connie Chung** *[25:48]*: The journal entry. I just want to know the journal entry. It could be AR journal, AP journal and manual journal entry. 
**Sandra Massey** *[25:56]*: Right. 
**Connie Chung** *[25:57]*: So can we just. 
**Ken Baugh** *[26:01]*: Maybe for like manual Journal entries because you get approvals on those mostly through email right now, right, Connie? And yes, it might be. Maybe it's cleaner if we do it through here. I don't know. But that isn't for everything like you say, it's for like manual journal entries and so forth. 
**Sandra Massey** *[26:22]*: That is correct. Go ahead, Chris. 
**Chris Trumble** *[26:26]*: No, go ahead. 
**Sandra Massey** *[26:28]*: So that is for manual journal entries. Now there's another types of journal entries that will be the ones that I created from a memorized transaction or from allocation configuration. Those ones need to have a different approval. This is just for the state standard ones. And then you have to keep in mind that even the manuals are going to be included in this and even the journal entries are uploaded into the system through a CSV record. Those will be subject to approvals as well. 
**Chris Trumble** *[27:10]*: Yeah. So as soon as we're doing approvals by workflow, then it kind of takes this option out of the discussion. Right. We don't need to set this one because the approvals are happening in a different place. Like this one says if you have enabled the journal entries approval and are using Suite Flow. This field doesn't even display. 
**Sandra Rudloff** *[27:32]*: Correct. 
**Connie Chung** *[27:32]*: Correct. 
**Sandra Massey** *[27:33]*: It's in another place. 
**Chris Trumble** *[27:34]*: Okay, so we'll get the. We'll have to like document, maybe work with you, Sandy, to document the exact approval rules and then we'll set up the workflow to reflect that. 
**Sandra Massey** *[27:49]*: To add to that, I'm going to send you a sample matrix for the approval. So you have an idea. Once I finish reviewing the financial management brd, I understand that. So you will have it like a point of view. I will send you a very simplistic one, but you can from that let us know what is needed. 
**Chris Trumble** *[28:13]*: All right. Allow user events on bulk journal approval that is normally not checked if you want to execute specific user events like Suite Script and Suite Flow after bulk journal approval. But that's not normally recommended unless there's a specific use case for that. And then we do want to allow GL custom segment deletion we normally turn on. Let's see here. Oh yeah, yours is a little bit different than our. Than our standard one. This one's usually turned on, right, Sandra? 
**Sandra Massey** *[29:02]*: Yes. 
**Chris Trumble** *[29:04]*: Okay. And then if there is. So the default minimum period is one and then you can set it if you need a different default minimum period besides one. Do you guys have any need for that? 
**Sandra Massey** *[29:26]*: Majority of clients just don't need that one because they go five fiscal year. 
**Chris Trumble** *[29:33]*: Yeah. Okay. Allow transaction date outside of posting period normally set to disallow the GL go Ahead. 
**Sandra Massey** *[29:49]*: There was a use case when you have to open the period to enter a transaction. Is that correct? At least that's what I remember from the past. Meeting the back day. Yeah, I remember you mentioning that you need to open the period to post a transaction if there was a discrepancy or something that you need to adjust for that period. 
**Connie Chung** *[30:18]*: For our we have like 11 store closed and one hard close. So normally I do that in December, like January, I still have it. And also like the audit, it will have to backdate it. I will open the period and then backdate it. 
**Chris Trumble** *[30:38]*: Yeah. 
**Connie Chung** *[30:38]*: So this one actually more likely for the end. 
**Sandra Massey** *[30:40]*: Yeah, yeah. 
**Chris Trumble** *[30:42]*: So this one actually talks about the saving of the transaction itself. So you can't save a transaction. So disallowing it. You can't save a transaction at all unless the transaction date is within the date range for the posting period. Or it can warn you and you can choose to still do it or you can always allow it. 
**Sandra Massey** *[31:06]*: Usually what I see in the majority of other projects is too warm. I should try to process that transaction outside the period. Yellow banner is going to come up and say, hey, this transaction is out of the period. Are you sure you want to process this? 
**Chris Trumble** *[31:24]*: Yeah, yeah, that's probably the safest one. And it's a big yellow banner at the very top of the page. So we can set that one to warn. 
**Connie Chung** *[31:35]*: Yes. 
**Helen Hamel** *[31:38]*: And to be clear with that warn, you can't move forward unless you click yes or no. Correct? 
**Chris Trumble** *[31:44]*: Correct. Yeah. 
**Helen Hamel** *[31:45]*: Okay. 
**Chris Trumble** *[31:45]*: Yeah. Okay. So these are some new setting like these check boxes, these five check boxes here, Sandra, these are new. These are not in our current Lux account. So these have not been set there. So I don't know if you have any guidance on the normal setting of these, but we don't even have these in our account that we provisioned a year back. 
**Sandra Massey** *[32:11]*: If they're not needed. Are we just here in. Now there's one that says allow quick closing periods. That is not recommended. Reason after that is the system won't go. It will allow you to close all the periods for sure, but it won't allow you to go through all the tasks in the closing period like arap, close, arn, AP and the subsequent task for that specific. For that specific period clause. And so for that I will just. Now I do turn it on when I'm loading historical trial balance because those months don't need a full closing, but I only enable it when I'm loading the historicals. For me to be Able to move into the next ones. 
**Chris Trumble** *[33:09]*: Yeah. 
**Sandra Massey** *[33:09]*: And so you will see add on, but I will disable it before you go into live on. Go live. 
**Chris Trumble** *[33:19]*: Yep. Yeah. So we leave it unchecked, you go in, check it, do your loading of trial balances, and then we uncheck it again. 
**Connie Chung** *[33:28]*: All right. 
**Gary Strickland** *[33:29]*: Okay. 
**Chris Trumble** *[33:31]*: As far as accounts receivable, apply payments to your top level customers only. That is set to no show only open transactions on statements. You'd hate to open a transaction and expect a not open transaction and not see it because of this checkbox in here. So usually that one off. 
**Debbie Herbert** *[33:56]*: Open. 
**Chris Trumble** *[33:57]*: So this has a couple options here. 
**Sandra Massey** *[34:00]*: Is the same as the due date and the transaction day. So if you send in statements to the customer, it will run at either by today or by a statement date, including all the transactions closed and open based on the featured app, the one that is updated before open transactions. 
**Chris Trumble** *[34:31]*: So the idea is if you're sending a statement, you want everything open as of today. That's the normal behavior. 
**Sandra Massey** *[34:37]*: Okay. 
**Gary Strickland** *[34:37]*: Okay. 
**Chris Trumble** *[34:39]*: Any concerns with that one, Connie? I'll see no customer credit limit handling. So if you do set up customer credit limits, it will warn you but allow you to proceed. Now this one customer credit limit includes. Is this open orders, Sandra. 
**Sandra Massey** *[35:09]*: Purchase orders. One thing about the credit limits is it will warn you. And then there's a feature that says hold. So it will hold a vendor bill and you won't be able to process a payment until that hold is checked off. Does the one thing with the. If you check that box in the vendor build, it says hold. 
**Chris Trumble** *[35:40]*: Okay. But we still recommend keeping it on warn. Right. 
**Sandra Massey** *[35:47]*: I believe you're going to have vendor bill approvals as well. Is that correct? 
**Chris Trumble** *[35:52]*: Yeah. 
**Sandra Massey** *[35:53]*: And so, yeah, that will take care of that. So there's no need. There's no need for that. 
**Chris Trumble** *[35:58]*: Okay. And then this one, it was saying in the credit limit, should you include orders to include or should you include orders that are entered but not yet billed? When you make credit limit calculations. 
**Debbie Herbert** *[36:17]*: Would. 
**Chris Trumble** *[36:18]*: You guys still want to bill them anyways or do you want to use the credit limit as like a hard line? 
**Helen Hamel** *[36:28]*: That one's tough, Ken, Kevin, you might want to come up with our policy internally for that because we're setting credit limits right now, but it's really not doing anything in the system to force orders not to go through. 
**Gary Strickland** *[36:51]*: And, and this will affect open sales orders. If you're bumping up, constantly bumping up against credit limits. 
**Sandra Massey** *[36:58]*: That is. 
**Ken Baugh** *[37:02]*: You know, one question I have just generally is like if we don't check that down, but we want to turn it on later. Even after we go live. Is it. Oh, I mean, is. Do we have the ability to change some of these? I know you want to get it all set up. Yeah, but that would. 
**Sandra Massey** *[37:25]*: Now to turn it off, you will have to process everything that has a hole in the system and then you can turn it off. 
**Chris Trumble** *[37:37]*: Yeah. Or you could just leave it off, see what you run into and decide to utilize that feature later. 
**Ken Baugh** *[37:46]*: Yeah, I'd say maybe leave it off for the time being. 
**Chris Trumble** *[37:52]*: Okay. 
**Sandra Massey** *[37:53]*: I think that's a wise decision. I'm sorry to interrupt. Chris, what you're saying. 
**Chris Trumble** *[37:58]*: No, I'm saying that makes sense to me. 
**Sandra Massey** *[38:00]*: Yeah. Because you're going to have your approvals and so that's kind of overkill if you ask me. 
**Chris Trumble** *[38:10]*: Yeah. This is whether or not you want a grace period for credit limits or if you, if you don't send anything, then as soon as they're over their credit limit, then it issues the warning. So this is how many days do you want to be graceful? By default being zero. And that's standard. 
**Gary Strickland** *[38:38]*: Usually. 
**Chris Trumble** *[38:42]*: Usually we do not include tax for term discounts or shipping. This one, there's a few ways to handle it maybe. Sandra, if you want to walk through the applyment of payments without invoice numbers. 
**Sandra Massey** *[38:57]*: Yeah. Say you receive a payment and then you don't know where that payment is going to be applied to. You can apply it to the oldest or you can pick and choose whenever where that payment is supposed to go to. And the other one is by aging difference, which is based on the date of the transaction and based of your aging preference as well. And so usually what I seen is they leave it on apply and then they go check. That's where you say, see down there? Keep on applying. Then you can review if you really want to put it or assign it or apply it to a different transaction. 
**Helen Hamel** *[39:48]*: Yes, I think definitely that. 
**Chris Trumble** *[39:52]*: Okay. Default payments, vendor payments. Print. 
**Connie Chung** *[39:58]*: Go ahead, go back. Do you still apply the payment to the audit? 
**Sandra Massey** *[40:01]*: No, not. No, no. 
**Connie Chung** *[40:03]*: We chose to keep it. Payment, payment and apply. 
**Sandra Massey** *[40:07]*: Yeah, yeah, that will go. That will go to a non posting account called undeposit Funds and then it will stay there until the payment is applied to an invoice. 
**Sandra Rudloff** *[40:25]*: Okay. 
**Chris Trumble** *[40:27]*: All right. And then, yeah, vendor credit limit warnings. That's for your vendors. And then again the same thing. Do you want your vendor credit limit to include existing orders? That's if you're keeping track of your own credit limits with your vendors. 
**Helen Hamel** *[40:48]*: Yeah, we Are not okay utilizing that. 
**Connie Chung** *[40:51]*: Okay. 
**Chris Trumble** *[40:55]*: Vendor prepayment account. 
**Sandra Massey** *[41:00]*: Prepayments. 
**Chris Trumble** *[41:02]*: Yeah. So yeah, this is just what account? Maybe walk them through this one. Sandra. 
**Sandra Massey** *[41:14]*: So it depends where you want to apply it. If there's money only on advances paid, that means on the vendor bill itself. If it's an asset, will I apply it to the asset? Or if it's, or if it's an order that is in transit, say it has been sent and they prepay it. Or the purchase return, no credit, so you haven't received the return and you haven't credited. Then you can apply it to whatever transaction is available to link to. And then the undeposited funds, it will allow you the same as the payments, the invoices, it will allow you to pick and choose where you want to. Where you want to allocate a prepayment to. And so that is entirely up to you. 
**Chris Trumble** *[42:20]*: So I've seen it commonly done into undeposited funds. But what happens if you don't pick an option here? 
**Sandra Massey** *[42:28]*: If you don't pick an option, the invoice will stay open and then the payment will stay as unapplied until it's applied to a transaction. 
**Ken Baugh** *[42:44]*: What, what if you use advances paid? I mean, where does that. Because these vendor prepayments, I mean, we just show them on our balance sheet as vendor deposits. Prepaid, correct? 
**Sandra Massey** *[42:59]*: Correct. 
**Ken Baugh** *[43:01]*: So. 
**Sandra Massey** *[43:02]*: Well, prepaids are a bit different because it's more like a. It was more like a, you know, like an amortization. You prepay those and then it's divided by a set amount of months or whenever, whatever the contract is. 
**Ken Baugh** *[43:24]*: So this is more of a prepaid expense. 
**Sandra Massey** *[43:27]*: Correct, Prepay expense, not vendor deposits. 
**Ken Baugh** *[43:32]*: So. 
**Connie Chung** *[43:35]*: I thought it's more like a VP payment account. So that's why we have an option at the bottom. If you scroll down, we will leave it there until we find the purchase order to apply. Right. It will sit into the deposit fund until we find the right purchase order to apply for that ppa, correct? 
**Ken Baugh** *[43:55]*: Yeah, we don't really have any. Well, I mean, the vendors that we have prepaid expenses would be like for a software contractor, that's going to be a 12 month contract, but we pay it all up front. Is that where this would be applied? 
**Sandra Massey** *[44:13]*: No, that would be another location. 
**Ken Baugh** *[44:15]*: Okay. 
**Helen Hamel** *[44:22]*: I'm not clear what this is. 
**Connie Chung** *[44:24]*: Okay. 
**Sandra Massey** *[44:27]*: I go ahead and say I have my Comcast bill and I send the invoices for like 50 bucks and I say 100. What they do is that they put that on the deposited funds and then Apply it to the next bill or the next purchase order that comes into the system. 
**Helen Hamel** *[44:57]*: Okay, so we've. If we've overpaid a vendor, is that correct? 
**Sandra Massey** *[45:02]*: Correct. That's exactly. 
**Helen Hamel** *[45:07]*: So I think. Yeah. Undeposited funds. Then we allocate it where. 
**Connie Chung** *[45:12]*: Correct. 
**Sandra Massey** *[45:12]*: You allocated where it has to be? Yeah. 
**Chris Trumble** *[45:15]*: Okay. All right. Auto apply vendor prepayments is normally utilized there? 
**Sandra Massey** *[45:25]*: Actually, no, because they want to select how they want to pay. Otherwise it will select the oldest purchase and they apply it. 
**Helen Hamel** *[45:41]*: Yeah, we don't want that because then our records are not going to match our vendor's records. 
**Sandra Massey** *[45:46]*: Got it. 
**Gary Strickland** *[45:47]*: Okay. 
**Sandra Massey** *[45:48]*: Even though in NepSwit every transaction is related. 
**Chris Trumble** *[45:52]*: Sure. Okay, so these classifications. Now there's two ways to make classifications on transactions mandatory, either at this level or at the field level. Normally we recommend not making them mandatory here, but if you want to make them mandatory when someone is entering a transaction, you make it mandatory there. It's easier to manage and you don't have to come back to the global preferences here in order to make those mandatory. 
**Connie Chung** *[46:28]*: So explain how is allowed per law department, because I know that over expense department is mandatory. Have to have the department in there. 
**Chris Trumble** *[46:39]*: Yeah. 
**Connie Chung** *[46:40]*: So meaning if the transaction doesn't have department when you click the allow per line and you can edit at the transaction and then before you post. 
**Chris Trumble** *[46:52]*: Yeah, so we make it mandatory at the field level, I'm pretty sure at. 
**Sandra Massey** *[46:57]*: The line level usually, or in case of a vendor bill and you want to apply it at the header level. But I don't see that case often. I see it at the line level. Okay, say you have a journal entry that goes to a different department or a certain class. Then you can add it at line level. If they go into a different segment in here. 
**Chris Trumble** *[47:22]*: Yeah. So basically what this one is doing is from an administration standpoint, once you check this box, then on the form that shows up, like we'll set up forms for you and they'll have these specific fields in these specific areas and you can hide, you can show hide and make mandatory. In this case, if you check the box, you will no longer be able to hide any of those fields on a custom form. That's really all it's doing. But we're making them mandatory anyways on the form, so it doesn't really matter. Unless you want to say like, okay, it'd be like you, Sandra, like, are you ever going to try to hide that field on the. On the form or accidentally hide the field? This, this box would stop you from doing that. So we can. I mean we can. 
**Chris Trumble** *[48:20]*: We can make it mandatory so they can't get hidden. That's fine. 
**Sandra Massey** *[48:28]*: That one is. Has to be checked. 
**Chris Trumble** *[48:30]*: Allow per line departments and classes. 
**Sandra Massey** *[48:34]*: Yep. 
**Chris Trumble** *[48:36]*: What about allow. Always allow per line classification on journals. 
**Sandra Massey** *[48:40]*: That has to be checked also. So the departments and classes will show on a transaction form. 
**Chris Trumble** *[48:48]*: Okay. And then what about non balancing classifications on journals? 
**Sandra Massey** *[48:54]*: So we have this thing called balancing segments. I don't think you're going to use that. So at this time, balancing segments is something. Some segment that you create and it allow you to enter in the transaction to balance a transaction if it's not balanced. Like journal entries, for instance, in netsuite, they have to be balanced. If you have to balance that application in certain way, then you can create a segment to apply to that transaction and it will show that expense or in the journal entry expense or revenue is applied to the correct segment. To be honest, I don't think you're going to need that. I see this more applied to the not for profits, but not for. In your case. 
**Chris Trumble** *[49:55]*: And then kind of same thing. We don't want to allow empty classifications on journals. No, we require classification. 
**Sandra Rudloff** *[50:04]*: And then. 
**Chris Trumble** *[50:04]*: Do you guys use elimination subsidiaries? I don't think you do. Right. 
**Sandra Massey** *[50:09]*: You only have one subsidiary and so if you have intercompany subsidiaries, elimination subsidiaries are mandatory. I believe you only have one subsidiary. Correct? 
**Ken Baugh** *[50:22]*: We only have one entity set up. 
**Gary Strickland** *[50:25]*: Yeah. 
**Sandra Massey** *[50:25]*: So you don't need that. 
**Chris Trumble** *[50:27]*: Okay. All right. That is the. Oh, no, there is actually additional purchase dis. All right, so this is all the setting of accounts. All right, let's see if there's anything that needs to be set in here. 
**Sandra Massey** *[50:46]*: Basically is if you want to set up the full account, you enter the transaction and then the fallout, the poll account will auto populate in there. And so you can set up, say sometimes I see. And setting up the vendor payment account if you had just a few. And that's where the payments go. But even if you set them up here, you can always change it as a transaction and apply it to a different account. So it's like not sent in stone. You can always change it. It's more like a, like, you know, like a kind of feature that you want to use or not. 
**Chris Trumble** *[51:31]*: Yeah. I'm trying to remember if we have their chart of accounts fully set up in the account too. If we don't, then it doesn't make any sense to go through and set these because it's only going to deal with the NetSuite default chart of accounts. 
**Sandra Massey** *[51:43]*: Yeah, the Majority of times I don't turn any of those out. So they can just pick and choose whichever account they want to pick. 
**Chris Trumble** *[51:52]*: Okay. All right. Anything else in here that needs to be set? Usually don't do much in this section. 
**Sandra Massey** *[52:09]*: So in Orion you don't lose the inventory or that stuff, right? 
**Sandra Rudloff** *[52:15]*: Yeah. 
**Connie Chung** *[52:16]*: Can you click on cost accounting inventory costing method. Are we using average Also? We're using Plus 5 4, right. Sandy? 
**Sandra Rudloff** *[52:27]*: We're currently standard. We're using standard costing, but that's due to our warehouse creation. I mean what, you know, with the Orion overlay and the product pricing, I mean what does it even matter what we choose? Because it's going to be based on what the line item cost is, correct? 
**Ken Baugh** *[52:49]*: Yeah, it's really specific project identification costing. 
**Sandra Massey** *[52:56]*: So. 
**Ken Baugh** *[52:58]*: Yeah, that's a good question. Does Sandy's question, does it even apply here? Because this we're really talking about work in process. 
**Chris Trumble** *[53:05]*: Yeah. 
**Ken Baugh** *[53:05]*: Projects. Right. So does this impact that? 
**Chris Trumble** *[53:09]*: I don't think it does, no. Okay. Yeah, yeah. This, yeah, this is like a setting for like wholesale distribution. Normally. 
**Ken Baugh** *[53:24]*: Yeah. But you can't, you have to choose one. It looks like. 
**Chris Trumble** *[53:28]*: Yeah, you have to choose one of them. Yeah. 
**Ken Baugh** *[53:32]*: And, and, but we don't, we won't really have anything going through that. This hits, I guess, right? 
**Chris Trumble** *[53:39]*: Correct. 
**Gary Strickland** *[53:39]*: Yeah. 
**Ken Baugh** *[53:39]*: Okay. 
**Sandra Massey** *[53:40]*: I will leave it as average as a simple to. To deal with and then you know, you have the grab the transactions, average the price and then calculate your real cost or reapply. Sorry. 
**Chris Trumble** *[53:59]*: Yep. And you guys aren't going to do this is normally through a web store. I'm going to uncheck gift certificate email makes things cleaner there duplicate number warnings or something already forcing it to not create duplicate numbers. So we can set a warning but I don't think that's even possible to occur. Okay, so default sales order status. 
**Connie Chung** *[54:34]*: If. 
**Chris Trumble** *[54:34]*: It'S going through a pending or it's going through approval process, the default sales order status is always pending approval. That's correct. We don't want to re. Require or require reapproval on edit of a sales order. A lot of these stuff are web store specific. The picking packing stuff applies. 
**Sandra Massey** *[55:04]*: Do you see that? The advanced shipment in here, were talking about it earlier. 
**Chris Trumble** *[55:11]*: Which one? 
**Sandra Massey** *[55:12]*: The advanced shipping. 
**Chris Trumble** *[55:17]*: Advanced shipping, yeah. 
**Sandra Massey** *[55:19]*: Let's look for that one. To look for it then. Okay, I, I show you the path for that one. 
**Gary Strickland** *[55:33]*: So Chris, scroll back up to this where you have the drop down for the pick pack ship. Unless there's going to be a. You see where it's got. 
**Chris Trumble** *[55:42]*: Yeah. 
**Gary Strickland** *[55:48]*: Okay. We're okay. 
**Chris Trumble** *[55:49]*: They're about. We. 
**Gary Strickland** *[55:51]*: You may want to talk about if we're just going to have everything go straight to ship so they don't have to do all three transactions. But we could talk about that as we do some uat. 
**Chris Trumble** *[56:01]*: Okay. 
**Sandra Massey** *[56:02]*: It just gives you more control if you have separate teams that it can be cheap. Yeah. 
**Gary Strickland** *[56:09]*: Since their inventory is always shipped to the site is pretty much just clear of the transaction. 
**Chris Trumble** *[56:14]*: Yeah. And I think that the ability to skip a step is set somewhere else. Right. This is just for like if they. 
**Sandra Massey** *[56:20]*: Were using set up on the form itself and you can just skip them and go straight to shift. 
**Chris Trumble** *[56:28]*: Yep. 
**Gary Strickland** *[56:28]*: Yep. 
**Chris Trumble** *[56:29]*: Okay. Nothing major through here. 
**Sandra Massey** *[56:39]*: Do you have employees that. That put expenses to transactions at all. And that's up. Are you going to use expenses in netsuite? 
**Connie Chung** *[56:58]*: That's. 
**Sandra Massey** *[56:59]*: That's. That's the other question. I know it was. There was a requirement on the financial management for us to demo that. 
**Chris Trumble** *[57:06]*: Yeah. 
**Sandra Massey** *[57:08]*: And so that allow expenses on purchases will allow you to. For the employees to allocate that specific expense say to a project or a regular travel time and that kind of. 
**Chris Trumble** *[57:25]*: Stuff like directly bill the customer for it. 
**Sandra Massey** *[57:29]*: Basically directly shown on the transaction. Like this is an expense for the client and it will be marked as expense. 
**Chris Trumble** *[57:41]*: Okay. 
**Sandra Rudloff** *[57:41]*: What we currently do is we say for our internal labor design, PM whatever if there was travel cost, they would put that in their internal cost. So it wouldn't be just be their hours. But you know, is that a process we would need to change to do this or so budget and not necessary. 
**Sandra Massey** *[58:03]*: Yeah. 
**Chris Trumble** *[58:03]*: Yeah. 
**Sandra Rudloff** *[58:04]*: Okay. 
**Chris Trumble** *[58:04]*: You could still put it as a line on the order. No problem. Just label it. Yeah. Okay. I don't have this on my list but I know sometimes this one comes into play. Bill in advance of receipt. 
**Connie Chung** *[58:29]*: Yeah. 
**Sandra Massey** *[58:30]*: You can. You can pay. This is receiving. 
**Chris Trumble** *[58:39]*: So. 
**Sandra Massey** *[58:42]*: Yeah, you can just pay and wait until you receive it. That's basically it. 
**Chris Trumble** *[58:47]*: Yeah. That one. I want to. I want to come. I just want to do a little research on that one. Come back to it. 
**Sandra Massey** *[58:51]*: Let me. Let me put it here. 
**Helen Hamel** *[58:54]*: Is this like doing a vendor prepayment. 
**Sandra Massey** *[58:58]*: Deposit for you to. 
**Chris Trumble** *[59:05]*: I think this is allowing you to bill a customer for something that you haven't received yet. 
**Sandra Massey** *[59:11]*: Oh, okay. 
**Kevin Baugh** *[59:13]*: Yeah. 
**Ken Baugh** *[59:18]*: Sandy, I mean how do we handle that now? Because I know we have a number of customers that want us to like they need the invoice to come in by year end and we haven't received the product yet. 
**Chris Trumble** *[59:33]*: Yeah. 
**Ken Baugh** *[59:33]*: Do we do that just as a like A memo invoice now, or I. 
**Sandra Rudloff** *[59:36]*: Mean, basically as a deposit invoice. And we can mock it up so it looks like a real invoice. But we do. We do post it. So it is on AR and just hits customer deposits. And then we. Yeah, go ahead. 
**Chris Trumble** *[59:52]*: This one actually is normally. Normally checked for us for that same reason you're describing, Cindy. Same thing with allow overage on item receipts. 
**Ken Baugh** *[01:00:05]*: Yeah. 
**Chris Trumble** *[01:00:08]*: Default receiving exchange rate. Use exchange rate. Well, you guys don't have to. You don't deal with this exchange rate at all. Right, Right. 
**Sandra Massey** *[01:00:16]*: Do you have any transactions, say, between U.S. and Canada or other countries. 
**Debbie Herbert** *[01:00:26]*: That. 
**Sandra Massey** *[01:00:26]*: Need currency revaluation and that stuff? 
**Sandra Rudloff** *[01:00:31]*: When we do just convert to US Dollars, we don't do multi currency. 
**Sandra Massey** *[01:00:36]*: Okay. So it will take whatever currency evaluation is for that day. And so that's how it'll be calculated in US Dollars. 
**Chris Trumble** *[01:00:49]*: If you want to use that, it is secure. 
**Sandra Rudloff** *[01:00:52]*: So I wouldn't do it. 
**Sandra Massey** *[01:00:54]*: Okay. 
**Chris Trumble** *[01:00:56]*: All right. So we will use the purchase order rate on bills. Default. This is the standard for default return authorization status. We also usually do refund or allow refunds in advance of the return. You don't have to do that, but we can allow it. Restock return items is turned on and then also credit in advance of vendor return. Is there a. Right. Well, again, we have to go come back through and do the accounts. So that's selection of an account that we don't have in the system yet. This is correct. Default transfer order incoterms. What's this one? 
**Sandra Massey** *[01:01:43]*: This usually for international shipping? Yeah, so that doesn't apply to them. 
**Chris Trumble** *[01:01:51]*: Okay. And then the default vendor bill status is set to approved. 
**Sandra Massey** *[01:01:58]*: Are you gonna have. Are you gonna have approvals on vendor bills? Is what you say, Chris? Yeah, the last one. 
**Connie Chung** *[01:02:09]*: Okay. 
**Sandra Rudloff** *[01:02:09]*: Yeah. 
**Sandra Massey** *[01:02:11]*: Oh, so it will be. Hold on. Yeah, yeah. So it will be pending approval in there. 
**Chris Trumble** *[01:02:22]*: Oh, pending approval. Okay. 
**Sandra Massey** *[01:02:24]*: Yeah. 
**Chris Trumble** *[01:02:25]*: All right, so for accounting of time and expenses, let's see. Automatically notify supervisor and copy service items are normally checked. This gets into a whole, like, automatically approve time. Like, I don't think you guys want to go through all of that. Like requiring someone to approve every single time entry. It's like we would rather give you a list of time entries that you can review. Let's see what else. Apply time threshold to vendor time is correctly check combine detail items and expense reports is normally unchecked. And then show warning message for taxable expense lines without receipt is normally unchecked. And then approval routing. 
**Sandra Massey** *[01:03:31]*: Will be. Yeah, this is if you're Going to use the workflows. 
**Chris Trumble** *[01:03:35]*: Yeah. 
**Sandra Massey** *[01:03:38]*: So in this case it would be journal entries, vendor bills, and not sure if you want to need purchase orders approvals or expense report approvals. 
**Chris Trumble** *[01:03:51]*: Yeah, and we can turn these on later as well, but those are the two. The two main ones. All right. That is the accounting preferences. 
**Kevin Baugh** *[01:04:03]*: Sorry, I think. Wouldn't we want to check expense reports there if we're kind of leaning towards going down that path or. 
**Chris Trumble** *[01:04:08]*: Yeah, yeah, we can do that. 
**Sandra Massey** *[01:04:09]*: You can uncheck it. Yeah, no problem. 
**Chris Trumble** *[01:04:12]*: Thanks. 
**Sandra Massey** *[01:04:12]*: It's not going to allow you. It's a saving. 
**Debbie Herbert** *[01:04:15]*: Yeah. 
**Chris Trumble** *[01:04:17]*: All right, so there's something that I missed that has a minimum date here, actually. I'm going to do this. Cancel that, try to save it's minimum period window size. Oh, that's the default is one. Yeah, that's right. So as soon as this one saves that kind of concludes all of the accounting settings. So you guys are more than welcome to stay on, but we're going to get back into the company setup now. 
**Sandra Massey** *[01:04:55]*: Now, one thing I'm going to stress, please don't touch the configurations because they're needed for Orion or for us. And so please stay away from the enabled features or accounting preferences. 
**Sandra Rudloff** *[01:05:10]*: Just. 
**Sandra Massey** *[01:05:11]*: Just saying. 
**Chris Trumble** *[01:05:12]*: Yep. All right. I'm gonna go back up to the top of my list here, talk about employees. 
**Helen Hamel** *[01:05:22]*: Okay, so we're done with the accounting stuff. 
**Chris Trumble** *[01:05:24]*: That's correct. Yep. 
**Sandra Rudloff** *[01:05:25]*: Yep. 
**Helen Hamel** *[01:05:25]*: Okay, perfect. Thank you. 
**Chris Trumble** *[01:05:27]*: All right, see you. Hello. 
**Sandra Rudloff** *[01:05:27]*: Thank you. 
**Connie Chung** *[01:05:29]*: Bye. 
**Kevin Baugh** *[01:05:30]*: See you, Connie. 
**Debbie Herbert** *[01:05:31]*: Thanks you all. 
**Chris Trumble** *[01:05:33]*: All right, employees. Okay, so we are allowing expense reports, we are allowing approval routings there. We're handling this different in Orion. So we don't enable the per employee billing rates or the billing rate cards, purchase requests. I recall having this discussion, but the idea of this is especially pertinent to like internal things that people need, supplies, things like that. You can allow people to make purchase requests and then whoever does the purchasing in house can then turn that directly into a purchase order. Do you guys have need for that? 
**Kevin Baugh** *[01:06:21]*: Seems like a useful feature. And again, I wish my team had not dropped off so quickly as this pertains to them. And I thought that might be the case. But yeah, this is something I think we'd want to explore and we've discussed even with our own system. Right. Is yeah, getting approval prior to purchases. So. 
**Chris Trumble** *[01:06:38]*: Okay. And then we use time tracking, but not weekly timesheets. Time tracking for CRM. We do allow global permissions. So we're going to enable this. We don't have to do anything with it. But if there does come a specific permission that you want to apply globally, that apply to every role, you can do that. Obviously there's, I don't know, a thousand other permissions in that suite. But if there is something is easy to set at a global level, in addition to the very granular role by role permissions. All right. 
**Sandra Massey** *[01:07:21]*: And then that one can also be entered on the employee record itself. Say somebody's in vacation on vacation and you want to assign certain function to somebody else, you can add it temporary on their employee network, Correct? 
**Connie Chung** *[01:07:37]*: Yep. 
**Chris Trumble** *[01:07:38]*: All right, so the vast majority of the features here, we do use NetSuite standard features. So all of these need to be turned on in order for Orion to work. Pretty much everything here. Okay. Advanced forecasting. This is forecasting. It just basically sets everything into buckets of high, middle and low forecast amounts. Any guidance on this one, Sandra? I don't see this one turned on often. 
**Yuridia Silvas** *[01:08:14]*: Understand a little bit more on that just because we have stages of how we're currently forecast. So it would be good to understand. 
**Sandra Massey** *[01:08:23]*: So basically, if you set up a quote for a vendor, I'm sorry, for a salesperson, sales teams or whatever, you can go into that quote that they have to match for a certain period of time and then they can do it, they can enter that quote ahead of time. And so when you run the forecast by what was the name of the function, it will allow you to forecast ahead of time. That's what I was trying to say. 
**Chris Trumble** *[01:08:59]*: Yeah. The only thing I would say to this is I think what it does is for the NetSuite default forecasting, it's going to turn on three different fields and you have to fill all three of those fields out. Now we're doing a lot of other forecasting and pipeline reporting that has nothing to do with the NetSuite default reporting. Like, we've stacked a lot of reporting on top of NetSuite. So I don't think this one is going to be needed with the type of pipeline. And then the other thing too is if there are sales forecast reports that you guys need specifically, we're building all of those custom for you guys. So I don't think you're going to be using the default NetSuite for sales forecasting reports. 
**Yuridia Silvas** *[01:09:44]*: Just for clarity, when you say quote, you really mean deal. Opportunity, right? 
**Chris Trumble** *[01:09:48]*: Yeah, deal. 
**Sandra Massey** *[01:09:48]*: Yeah. 
**Debbie Herbert** *[01:09:50]*: Okay. 
**Yuridia Silvas** *[01:09:50]*: Yeah. 
**Sandra Massey** *[01:09:51]*: Or a quote on a specific theme. Let's say you quote for the salesperson would be like. Yeah, yeah. 
**Yuridia Silvas** *[01:10:02]*: So, yeah, I know we're definitely look interested in looking to what the reporting is going to look like for the forecasting. I know right now we also do a lot of the reporting through Power bi. That's more on Kevin's area of responsibility. But yeah, it would be good to really just see how that's going to look like for future. 
**Chris Trumble** *[01:10:23]*: Yeah. As we get deeper into implementation too, like, we're going to be looking at some of those things. Like if there's a killer report that you guys are like, this is what my sales leadership needs. This is exactly it. It's working really well. Or this is a report that we'd like. It would be even better if we had XYZ on it. Then we're building those custom reports for you guys. 
**Yuridia Silvas** *[01:10:46]*: And a quick question on that. Is that going to be also part of a dashboard? Because I know at one point talked about the dashboard versus the reporting. Because as we're moving forward, I was saying this to Brian yesterday. I'm really thinking of what reports are critical as we're building. Building all this that we're gonna definitely need. 
**Chris Trumble** *[01:11:06]*: Yeah. And think of it as like we build a report that's either like a NetSuite default report or a saved search. We've talked about this a little bit in the past. You just have to decide a couple things where you want it to show up. Like, do you want that one on every sales leader's dashboard in the home screen first thing when they come in? That's what they're looking at. So it's like it's. It's just think of dashboards as. It's just putting all these reports in a specific place in front of people. And then we like to also say if that's the route you're going to go, publish those dashboards out to people so that they're not pulling their own numbers and forgetting to add something or leave a field out or whatever. 
**Chris Trumble** *[01:11:50]*: Just, you know, come up with a dashboard or come up with a report that you really like, make it a dashboard and then publish that out so that it is mandatory on people's screens. 
**Sandra Massey** *[01:12:00]*: Okay. 
**Chris Trumble** *[01:12:02]*: All right. So netsuite has a support, like a case system. I don't think we're using support cases, at least phase one for you guys. It does have, like, we used it extensively in E commerce where someone could just use email, a specific email address and they would create a case that would show up on someone's reminders. Portlet this. Even if you leave this checked, if you don't set up the email address, there's nowhere for IT to go, but I don't think we're going to currently use cases right now. And then the other one is, well, if you're not going to use cases, then you don't need automated case escalation. Knowledge base is for the website specifically. We're not publishing a knowledge base. I assume you guys have some kind of help desk tool that you're already using for your IT team. 
**Chris Trumble** *[01:13:02]*: I don't think I've ever met an IT team that loved the NetSuite version of help Desk. So if you guys have something already, stay with it, probably. 
**Sandra Rudloff** *[01:13:12]*: We do. 
**Chris Trumble** *[01:13:13]*: Yeah. There you go. 
**Yuridia Silvas** *[01:13:14]*: So Sandra, just for. Just for. It's a quick question to you. So thinking of current, whoever has any concerns or issues with Orion that would email the IT team and then you would establish like this committee to address the concern. Is that what we're talking about? 
**Sandra Massey** *[01:13:33]*: I guess that's a good question. 
**Sandra Rudloff** *[01:13:34]*: I mean, if people. 
**Sandra Massey** *[01:13:36]*: That is correct. 
**Connie Chung** *[01:13:38]*: Okay. 
**Sandra Rudloff** *[01:13:40]*: Yeah. We'd probably want to set up our own process for Orion question. So it goes to the core team. And because the last thing we want to do is have IT go to our current SOS system to be reassigned, it'll take too long. So that's a good conversation point. 
**Sandra Massey** *[01:13:54]*: And then you can assign a level of importance, low, median or high. And so that's really helpful to handle those also and escalations as well. Okay, yeah. 
**Chris Trumble** *[01:14:11]*: All right. And then in order for Orion to work, we need online forms, mail merge, CRM templates, We need to capture email replies. You guys don't have people subscribing to anything. Upsell Manager is a web store function. And then I would say this is something we can get into later. But it's like you can make campaigns. We have campaigns turned on. This opens a whole door to the sales reps where they can manage their own campaigns. I would. Yeah, it like takes the ownership out of like a centralized place and puts a campaign into the salesperson's hand specifically. If that is something that you guys want to get to into in the future, we can definitely talk about that. But it is a little bit complicated and hard to manage. Like, the concern is that things get really, I don't know, unbranded. 
**Chris Trumble** *[01:15:10]*: It gets a little rogue if you give them the responsibility directly. Whereas if you manage the campaigns at a high level, you can set up campaigns specifically for salespeople, but they don't have access to the templates or the body of the email. You can send it on their behalf without asking them to manage those. Those campaigns themselves. So overall, does leaving it unchecked seem like a reasonable approach? 
**Sandra Massey** *[01:15:37]*: I think so. 
**Yuridia Silvas** *[01:15:38]*: Right, Sandy? And we're also going to. Marketing is still going to continue to use HubSpot. So we have templates already there that are utilized in the same format. 
**Sandra Rudloff** *[01:15:48]*: Yeah, we'll look at the marketing, you know, post, go live. But yeah, I mean, that's pretty much what our marketing. They do the campaigns and they give the salespeople their own resources, I guess. Udi, do you see any need to have salespeople do their own or. No, no, no. 
**Yuridia Silvas** *[01:16:06]*: And what I'm saying is, right, because if we're gonna still continue to use HubSpot, that's already set up, marketing has already established those templates for sellers and they push out content when there is a campaign. But to Chris's point, right, branding's important. So we don't want salespeople trying to do their own quasi, you know, marketing. 
**Sandra Massey** *[01:16:28]*: So yeah, leave it up. Check. 
**Chris Trumble** *[01:16:30]*: Yeah, these are hard learned lessons over the course of a long marketing career. For myself, I was like, yeah, they could do what they can do whatever they want. And I've seen the, I've seen what happens. These last three sections should actually go pretty quick here. These are all pretty standard things. I don't think there's a lot of decisions to be made, but we'll walk through them. We use KPI Scorecards Suite Analytics Workbook. Powerful tool for building reports. We can use cache data in data sets, HTML formulas and search. We usually leave this one on. Nobody even knows that it exists. If they don't, if you don't tell them so they're not going to be. I don't see people like putting a ton of HTML formulas in there. But advanced users can use that if necessary. 
**Chris Trumble** *[01:17:27]*: And then web presence is pretty much no for everything because you guys are not, you guys are doing your website through suite. What's it called? Sweet. Some sweet web word. Yeah, for the website. 
**Yuridia Silvas** *[01:17:44]*: Yeah, but the what? The website. 
**Chris Trumble** *[01:17:48]*: Yeah, it's like if you wanted to run your website through NetSuite, there's like sweet Suite Commerce, Advanced and Suite Commerce. It's mostly like an actual web store. You can use it for other things. But you guys already have a great website. The what? Actually, the way that NetSuite interacts with your website, the main way is that any form that is on your website right now for collecting any kind of like customer inquiry, like a contact us form, you actually replace the one in your website with a NetSuite version, it can look exactly the same. And then when they input their data and submit it actually creates a lead in netsuite. But that's really like the owner, the only like intersection of NetSuite and your web store or your wet. Your website. 
**Sandra Massey** *[01:18:39]*: Oh, got it. 
**Yuridia Silvas** *[01:18:39]*: Okay. 
**Chris Trumble** *[01:18:41]*: All right, let's see. This one is actually just Suite Cloud. Let's see. We do need. We don't need item options. We do need custom records. We use advanced PDF templates. That drives it. All right. Remove personal information. This is kind of getting into. I'm sure you guys run into it in California. There's a lot of what is a GDRP in Europe. But the idea is that if you enable this, there's basically a function where someone with permissions can go in and clear out all of a customer's personal information at their request. You don't have to use it, but this is an easy way. It's like a PCI compliant and a legal way to remove personal information. It gets rid of it. I think it even like generates a little thing that confirms like, yes, we've removed all this person's personal information. 
**Sandra Rudloff** *[01:19:43]*: That actually would be great because we do get requests from our clients. Say, now that this is done, can you confirm you've done this? So anything to make it easier? Yeah, yeah. 
**Chris Trumble** *[01:19:52]*: I used to get a lot of that in E Commerce and they did not have this tool. So I'm like, I promise, like, here's your customer record. There's nothing on it. You know, like, there's no. Yeah, so that's good. Suite script is good. Server Suite script is good. Suite flow is good. We don't need, oh, we do need custom GL lines. We do not need custom transactions. See what else? We use all of these things internally to talk to your system. So open rest, we don't need suite sign on. We don't need open id. We don't. I mean, you guys could later on, like, if you guys have a single sign on for any remaining Microsoft 365 things like your IT team can make this a single sign on thing. 
**Chris Trumble** *[01:20:41]*: I think for the time being, especially as we're getting people up and running and getting their accounts provisioned, it's not something you tackle at the very beginning. We can do that later if necessary. 
**Sandra Rudloff** *[01:20:51]*: I was going to say, you know, I remember from our last conversation where I was getting the prompt for a unique IP address or allowed IP addresses and I guess we won't have one. I mean, between MFA and single sign on, I mean, is that something we can do basically add implementation. 
**Chris Trumble** *[01:21:12]*: Like doing single sign on for. 
**Sandra Rudloff** *[01:21:15]*: Right, that's the ideal. But then the second backup would be to do mfa, because I, I checked with Ted and he says not because we use a, you know, the VPNs and everything else. The single IP address wasn't going to be possible. 
**Chris Trumble** *[01:21:32]*: Oh, okay. Yeah. Maybe we can have another like that's not in the BRD for implementation, like the single sign on. But if that is something you guys want to explore, maybe we can have an offline conversation about doing that. 
**Sandra Rudloff** *[01:21:46]*: Yeah, that's preferred if it's, you know, we can also do mfa, but those would be the two options. 
**Chris Trumble** *[01:21:53]*: Okay. 
**Sandra Rudloff** *[01:21:53]*: Because right now I know when I log in I use my Authenticator app. So. 
**Chris Trumble** *[01:21:58]*: Yeah, yeah, Authenticator. And then, yeah, we just use basic password management. I mean we have to go in and out of a ton of accounts, so it's a little bit different. 
**Sandra Rudloff** *[01:22:08]*: Right. 
**Chris Trumble** *[01:22:09]*: But yeah, I've never actually had a client take advantage of the single sign on, but it'd be. Yeah, it'd be interesting to explore further. 
**Sandra Massey** *[01:22:19]*: The only thing I've seen for my clients is more like the two factor authentication because it's more secure. Right now the administrators are the only ones that have that, but you can also make it mandatory in other roles. 
**Chris Trumble** *[01:22:35]*: Yep. All right. We don't want to be an OIDC provider. We don't need telephony integration. We do need these two on. And we do need Suite app control center. Okay, so that is the entirety of the Enable features. We have eight. Does this go to four? Eight minutes left? 
**Sandra Massey** *[01:23:00]*: Yes, seven minutes. 
**Chris Trumble** *[01:23:02]*: Seven and now seven minutes. Okay, let me see. I want to see if there's anything critical for discussion in the sales preferences. I think that most of the sales preferences, well, they. Let me. Let's just dig right into it. There's not a ton in here. Yeah. So lead status. When you get a lead, like let's say example, were taking in leads from your website, for example. Or if somebody is like at a trade show and they're using the quick ad lead capture, what status do we want the lead to come in as? Do we want it to come in as qualified or unqualified? Usually unqualified. 
**Sandra Massey** *[01:23:56]*: Yeah. 
**Chris Trumble** *[01:23:56]*: Yep. For a new prospect in discussion. Now we can go back and also we're going to be changing all of these. So I don't really want to. Like these are going to reflect exactly what your statuses are. And then we can come back in here and pick the correct One. Yeah, but just be thinking about how you want a prospect to come in, whatever your current workflow is. And then at that point where we're defining the statuses, we're also defining, like, probability levels and things like that. So that's a whole different exercise. Yeah, it might actually better to just do all of this at the same time as we do, like, all of those statuses and stuff. 
**Debbie Herbert** *[01:24:37]*: Right. 
**Yuridia Silvas** *[01:24:38]*: And for this portion, Sandy, I mean, I have what current is, but. I know. And just conversations with Roy and Nick, they wanted to also just be a part of it. 
**Connie Chung** *[01:24:49]*: So. 
**Yuridia Silvas** *[01:24:50]*: Yeah, when we get through this next new update, and it'll be good to include it. 
**Chris Trumble** *[01:24:54]*: Yeah. All right, so we'll leave this here for now. We'll get your statuses in the system correctly, and then just a note for me to come back and we'll get that all set up. So. Okay. Well, actually, we got through the vast majority of the configuration, so that is a nice. A nice step in implementation. I know we still have some BRD stuff to work through and finalize. Sandra's working hard on that. And then. Yeah, and then we'll be kind of presenting to you guys the project plan for implementation. Getting into the realize phase, having lots of sessions, ideally two to three per week, and actually going through that. And that'll be all planned out. We'll tell you who to invite. We'll get it all scheduled out, and we'll be into implementation before we know it here. 
**Sandra Rudloff** *[01:25:41]*: I know you'll go into detail, but what's your ballpark guesstimate as far as when you'll need us two to three times a week? February, late January. 
**Chris Trumble** *[01:25:51]*: Yeah. Yeah. I would say, like, first week of February would probably be. Be just about it. Ideally, we can push that timeline a little bit. Like, I know for you guys, me and Marcus were talking about it, and we're like, okay. We have relatively aggressive timeline goal, and I'm kind of going to be dedicated to meeting as much as we need to in order to get this thing across the finish line in time. So, yeah, we probably have like a week or two weeks of just getting through all the BRDs, getting them signed. That's like the biggest milestone. And then I'll be highly focused on your implementation. 
**Sandra Rudloff** *[01:26:31]*: Okay. 
**Chris Trumble** *[01:26:33]*: So. Can't wait. Yeah. Yeah. You guys have a good weekend. Thanks for sitting through a long session today. We appreciate it, but I think we got a lot done. 
**Sandra Rudloff** *[01:26:46]*: Looks like it. 
**Chris Trumble** *[01:26:47]*: Yeah. All right, well, thank you guys very much. We'll talk to you soon. 
**Sandra Massey** *[01:26:51]*: Thank you very much. 
**Debbie Herbert** *[01:26:53]*: Have a good weekend. 
**Sandra Rudloff** *[01:26:55]*: Bye. 
