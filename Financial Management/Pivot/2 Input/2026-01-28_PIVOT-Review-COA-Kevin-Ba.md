# PIVOT Review COA"Kevin Baugh" <kbaugh1@pivotinteriors.com>

**Meeting Date:** 28th Jan, 2026 - 1:00 PM

---

**Chris Trumble** *[00:02]*: Hey, Sandra. 
**Sandra Massey** *[00:03]*: Hey, Chris. 
**Chris Trumble** *[00:05]*: How are you today? 
**Sandra Massey** *[00:06]*: I presentable lunch. 
**Chris Trumble** *[00:13]*: All right. Connie's in lobby, Sandy's in the lobby, and Ken and I think we're expecting Kevin also. Hi, Ken. 
**Sandra Massey** *[00:24]*: Hi, Ken. 
**Connie Chung** *[00:26]*: Hi, Debbie. 
**Ken Baugh** *[00:26]*: Hello. 
**Sandra Massey** *[00:29]*: Morning and good afternoon. 
**Chris Trumble** *[00:34]*: There's Kevin. 
**Sandra Rudloff** *[00:36]*: Kevin. 
**Chris Trumble** *[00:44]*: All right, I think we got everybody. So Sandra's going to walk us through the proposed chart of accounts ready and waiting with my install of the software. And as soon as we get this loaded up, we'll be good to go. 
**Sandra Massey** *[01:01]*: Okay, let me go ahead and share the chart of accounts proposal I did. And then what I would like to do is to answer your questions, unless you want to share with me if you have any annotations around this template I provided, that would be great as well. 
**Kevin Baugh** *[01:24]*: I can share my screen. 
**Sandra Massey** *[01:26]*: You can share your screen. Okay. 
**Kevin Baugh** *[01:27]*: We did notes prior to this call, so let me. 
**Sandra Massey** *[01:33]*: Yeah, that's what I figured. You're so organized. 
**Kevin Baugh** *[01:38]*: Oh, thanks. All right, so. We kind of went through prior to this call and highlighted some that we had questions on. I guess the first is, you know, that. That first cash account. I guess let me preface this whole discussion with, you know, the intent here is not necessarily to map one to everything that we currently have in our system. We have accounts in here that have been dormant for years. And as part of our D365 setup, we're created for one reason or another. And some of the accounts we have set up, too. I think there's still some open questions around process in Orion, which we'll talk about later. So, like this one that we have highlighted, Cash, for example, we're assuming that you're going to go ahead and create all these accounts. 
**Kevin Baugh** *[02:36]*: If we end up not using an account that you set up, do we have the ability to change the name of that account so that we can use it for something else? Okay. Do we have the ability to delete an unused account? 
**Sandra Massey** *[02:51]*: As long as it doesn't have transactions, you should be able to delete it. Correct. 
**Kevin Baugh** *[02:58]*: Okay. 
**Chris Trumble** *[02:58]*: And on occasion, even transactions, or even accounts that do have transactions, as long as they're good, you can also inactivate it, which would then not show up. So there's a toggle for showing actives or not. 
**Sandra Rudloff** *[03:13]*: Okay. 
**Kevin Baugh** *[03:15]*: So that helps. We're still discussing this cash account here, but it sounds like we, you know, that's. That's not mission critical. However, you know, perhaps more important is, I think when we originally sent over this file to you, we had not yet. We actually just recently created a new account for part of our health Insurance process. And it's this, we just called it 122000. It's an AR account for claims reimbursements. And so that's one addition that we threw in here as part of the setup and we will use that one. Ken and Connie, feel free to stop me at any point in time. So Orange was kind of just like, hey, we have questions on this one. So we have a lot of purchased materials accounts today. Ken and Connie, feel free to. 
**Ken Baugh** *[04:14]*: Yeah, some of the question here is a lot of these accounts and the number of accounts is set up based on the way that the 3, you. 
**Ken Baugh** *[04:24]*: Know, Dynamics 365 works. 
**Ken Baugh** *[04:28]*: But in Netsuite we may not need all of these accounts, but we don't really. At least I don't understand how like if we order a share on a project for a project, when that's received, is that considered work in process in. 
**Ken Baugh** *[04:48]*: NetSuite or is it considered inventory? 
**Ken Baugh** *[04:53]*: And if so, do we still need all of these inventory and working. And I think I remember one call that you, you do the terminology wise, you do map that to. 
**Ken Baugh** *[05:09]*: Inventory, not work in process. 
**Ken Baugh** *[05:11]*: But I know a lot of the. 
**Ken Baugh** *[05:12]*: Dealers call all of their inventory work in process, so. 
**Chris Trumble** *[05:16]*: Right. 
**Ken Baugh** *[05:17]*: It's just a little better understanding around how in the transaction, from the transaction side of projects, you know, in netsuite, Orion, how is that intended to, you. 
**Ken Baugh** *[05:32]*: Know, what accounts is that intended to hit? 
**Ken Baugh** *[05:36]*: That makes sense. 
**Chris Trumble** *[05:40]*: Yeah. Yeah. And I'm not sure that's. I have Sandra here to help me on the accounting side. Not my, not my strongest suit. If, Yeah, I guess I would need to understand your work in progress needs a little bit like are you handling it like most other dealers or would it just be, would going into an inventory account, would that work? 
**Ken Baugh** *[06:08]*: Well, that's the way we do it. 
**Ken Baugh** *[06:10]*: Currently. 
**Ken Baugh** *[06:13]*: And partially because in Dynamics 365. 
**Ken Baugh** *[06:18]*: That'S the way we had to do it. So. 
**Ken Baugh** *[06:21]*: But, but previously before were on. 
**Ken Baugh** *[06:23]*: Dynamics, when were on Chameleon, we, I believe we called it work in process. 
**Ken Baugh** *[06:30]*: So I guess if you look at the standard Orion template, how does that typically work on the, you. 
**Ken Baugh** *[06:42]*: Know, for a furniture dealer here? 
**Ken Baugh** *[06:44]*: The way that's set up and because again, we have a lot of inventory accounts set up here and we're really not using the WIP. 
**Ken Baugh** *[06:57]*: Accounts the same way. 
**Ken Baugh** *[06:58]*: So I don't know if these, you know, looks like some of these map to what we have here now. But my assumption is in Orion we're going to be doing it differently than. 
**Ken Baugh** *[07:09]*: We do it in dynamics. So. 
**Chris Trumble** *[07:14]*: If you want to do it differently like this is a good place to say like this is the ideal state and define. 
**Ken Baugh** *[07:22]*: But do you. But is there a. Is there a. Call it a standard setup for, you know, for Miller and old dealers that you've done. And what does that look like is we probably would want to, you know, follow that standard if it, you know. 
**Ken Baugh** *[07:41]*: If it makes sense for us, which I think it will. 
**Chris Trumble** *[07:44]*: Yeah, there is a standard set. I'm trying to see if I could pull just a standard one up. The quickest path to that would be. But yeah, there is a. There's a standard. 
**Sandra Massey** *[07:56]*: I think there's a tab, Kevin, at bottom that says Orion is standard. 
**Kevin Baugh** *[08:02]*: Yeah, right here. 
**Ken Baugh** *[08:05]*: So if you just look at inventory. So it looks like the standard. There's. 
**Ken Baugh** *[08:14]*: Three inventory accounts and you had. 
**Sandra Massey** *[08:16]*: The 1200, 1205, 1210. 
**Chris Trumble** *[08:22]*: Yeah. 
**Sandra Massey** *[08:24]*: And then after that you have the WIP. 
**Ken Baugh** *[08:26]*: Yeah, yeah. So again, if we order a truckload of product from. I mean, in this standard setup, you know, from. From. From Herman Miller and it shows up in our warehouse and we receive it in what account does that typically hit? 
**Sandra Rudloff** *[08:47]*: Yeah, I was wondering if it's possible to see all the accounts that are impacted by an order from, you know, receipt accounts payable, invoicing, you know, invoicing and I'm sorry, receiving and then even fulfillment. How the account flow for those transactions. Because I might be speaking out of term. I think the other accounts, like all of our expense and everything else is fine. The big question is really around orders, inventory, ap, you know, all those accounts. 
**Ken Baugh** *[09:19]*: See that and accounts payable. Again, we have currently a lot of different accounts payable, you know, accounts. But I don't. My assumption is we're not going to need that many in Orion. 
**Ken Baugh** *[09:33]*: Because the way. 
**Ken Baugh** *[09:34]*: I think you're right. 
**Ken Baugh** *[09:35]*: I like the way you're. 
**Ken Baugh** *[09:37]*: You couch that, you know, if you follow an order, typically through NetSuite, Orion. 
**Ken Baugh** *[09:45]*: What accounts does that hit on the inventory? Accounts payable side? Primarily those that we have under revenue and things like that too. But deposits. But. 
**Ken Baugh** *[09:58]*: That'S. That's what I'm. 
**Sandra Rudloff** *[10:00]*: A lot of these were set up strictly because of the way we have our warehouses set up. 
**Chris Trumble** *[10:06]*: Yeah. 
**Sandra Rudloff** *[10:06]*: And the in and out, you know, that we had to do. 
**Kevin Baugh** *[10:09]*: Right. 
**Sandra Rudloff** *[10:10]*: So like Kenna says, it's probably not needed in Orion. And if we could just see all the postings of an order that could really help us determine if any of these are not needed. 
**Chris Trumble** *[10:23]*: Yeah. I can compile that. What exactly? What accounts an order hits. I know there is some configuration that we do when we set up the actual items because we use the concept of generic netsuite items. So it's like all of Herman Miller furniture is actually only one inventory item in your system and it maps to a specific account and that's all configurable. But I could give you an example of like this is a common flow and this is how WIP is handled. I think Marcus might even have a document on that. I'm just kind of working in the background to pull some of that information. 
**Ken Baugh** *[11:05]*: Yeah, and is it. Yeah, because the costing on it, you know, the cost. Because this is where we've looked at. 
**Ken Baugh** *[11:16]*: A lot of different systems over the years. 
**Ken Baugh** *[11:17]*: And inventory, you know, costing, valuation is. 
**Ken Baugh** *[11:20]*: Always something that gets mixed because is. 
**Ken Baugh** *[11:22]*: It fifo, LIFO or whatever? And it's. No, it's not. It's specific to the project. So we just take that project cost. 
**Ken Baugh** *[11:30]*: And apply it to, you know, to the inventory or work in process, whichever nomenclature is, you know, is. Is kind of what's behind the basic setup here. 
**Chris Trumble** *[11:41]*: So and since we're not doing like FIFO or LIFO or anything, like the item is like lot numbered inventory, which is not necessarily serialized inventory, but it's like because it is a generic item, it doesn't has a lot number that is associated, that bypasses all of that LIFO FIFO stuff. 
**Ken Baugh** *[11:59]*: Okay. So I think we're just asking for. 
**Ken Baugh** *[12:04]*: Some clarity like Sandy said on those orders. 
**Ken Baugh** *[12:09]*: And you know, the key areas I think are. 
**Ken Baugh** *[12:14]*: You know, on the inventory slash WIP side, how that works. And correspondingly on the AP. Side, I guess those are the primary areas. Right. I mean obviously it's going to hit cost of sales once it's invoiced and so forth. 
**Sandra Rudloff** *[12:34]*: But it'd be great if you could do like the order, the messiest order. I mean, from in out, you know, we delivered it, came back into inventory, we had to do a credit memo. It. You know, all those transactions that could possibly happen. I know, I find that really helpful. 
**Chris Trumble** *[12:53]*: Yeah, yeah. And I think I can put together a pretty simple little flowchart of how exactly it works. And like I said, Marcus might even have something. I just don't have it in front of me at the moment. 
**Ken Baugh** *[13:07]*: But we. 
**Kevin Baugh** *[13:08]*: How long does that delay kind of this next step? Because Chris, I hear you at the beginning of this call, you know, we're ready to kind of roll here and get this going, does this add another week to our timeline or two days? 
**Chris Trumble** *[13:18]*: Yeah, no, I think we can. No, I don't think so. I don't think it would even add a week. 
**Sandra Massey** *[13:24]*: One thing to consider is if, even if we have to make account changes based on the GL impacts for those transactions, we can always change them or rename them. I mean, this is not like a set in a stone kind of chart of accounts. You can always, you can always make changes. Now, when it comes to historical trial balances, are you bringing any of those? 
**Kevin Baugh** *[13:54]*: Yeah, I mean, I don't think we're gonna be able to zero out all those accounts prior to the switch. Right. So therefore they would flow into the new system, which complicates things. 
**Sandra Massey** *[14:05]*: You will see your mouth. Meaning that you compiled any one account or. How are you going to do that? 
**Ken Baugh** *[14:14]*: Well, remind me, Sandy, we were going to do an import of. 
**Ken Baugh** *[14:21]*: Our data into. 
**Ken Baugh** *[14:25]*: Into Orion. 
**Ken Baugh** *[14:26]*: Krenachweek. 
**Ken Baugh** *[14:27]*: Correct. Not a, not a ramp up wind down. 
**Sandra Rudloff** *[14:32]*: No, we are, we're doing ramp up wind down. So, okay, the question will be we'll still do all the transactions that we have in G365, then at month end we'd want to do some kind of an upload for those transactions into Orion and then run financials out of Orion. Is that the intent? 
**Ken Baugh** *[14:53]*: We. 
**Ken Baugh** *[14:57]*: We might not need to do that. I'm thinking that we could do all of that integration within Adaptive, potentially. I mean, if we just set it up. But we want to just talk through. 
**Ken Baugh** *[15:10]*: That because. 
**Sandra Rudloff** *[15:14]*: We don't just have two closing and then merge the data. 
**Ken Baugh** *[15:22]*: Say that again. 
**Sandra Rudloff** *[15:23]*: So basically we'll have two closings in each system and then we'll merge that month in data and adapt it. 
**Ken Baugh** *[15:30]*: Yeah, I think so. 
**Ken Baugh** *[15:31]*: That's, that's kind of my thought on it. 
**Ken Baugh** *[15:33]*: I don't know again how much that's. 
**Ken Baugh** *[15:36]*: Been discussed, but that would be. 
**Sandra Rudloff** *[15:41]*: I. 
**Ken Baugh** *[15:41]*: Think that would be my suggestion or you could even be done in another tool. But Adaptive is one that we have that I think could do that. You have thoughts, Kevin, on that or. 
**Kevin Baugh** *[15:51]*: Well, we're trying to. I mean the discussions we've had is we're trying to utilize the planning and budgeting feature within NetSuite. 
**Ken Baugh** *[15:57]*: Right, right. 
**Kevin Baugh** *[15:58]*: So but as we make that transition. Yeah. We have the capability of compiling data from two systems and Adaptive. That's correct. 
**Sandra Massey** *[16:08]*: I think you will be able to achieve that. See, I'm sorry, it was a Connie or Sandy. 
**Connie Chung** *[16:14]*: Well, I mean as Sandy That I can combine the two into one template before I upload to adaptive pending. Right, Sandy. So hopefully the GL account doesn't map differently some of the handles. So at least I can combine the two together. So I only do one upload because I don't know how if I upload one and then another, they could override or not. 
**Kevin Baugh** *[16:41]*: I think it has to be combined into one file. 
**Connie Chung** *[16:44]*: Yeah, it had to be combined into one file. 
**Sandra Massey** *[16:48]*: Okay, meaning you're combining the accounts. The reason I'm asking is we load usually try balances either, but they change or by month. And so the accounts that still have a balance. I know, Kevin, you mentioned that you got balance and zero, but if you are going to combine them, makes it difficult for you to reconcile. I know you're using the netsuite planning and budgeting, but for the immediate transactions, immediate reports, usually we bring up the historicals, the historical summary and then we deactivate those because there would be trial balances only. 
**Ken Baugh** *[17:35]*: And so you would typically then if we're winding down our old system, you typically at month end still roll those numbers into. 
**Ken Baugh** *[17:44]*: Into netsuite. Is that what you're saying? 
**Sandra Massey** *[17:47]*: Yeah, we deactivate them. That doesn't allow you to post transactions to it, but you can still see the historical data for that specific account. 
**Ken Baugh** *[17:59]*: Okay. 
**Ken Baugh** *[17:59]*: And I think, you know, we just. 
**Ken Baugh** *[18:01]*: Have to walk through what that process would look like and understand it. 
**Ken Baugh** *[18:06]*: So anyway, gotten kind of back and. 
**Ken Baugh** *[18:08]*: Forth on the, you know, like the hard clothes, but that's fine. 
**Ken Baugh** *[18:13]*: And then we're gonna hopefully have everything, the bulk of everything flow through by. 
**Ken Baugh** *[18:18]*: You know, late in the year and then we do a clean cut off. Right, yeah, I remember that. 
**Sandra Rudloff** *[18:24]*: So you know, one approach might be that come May 1st, the only things we're doing within D365 are order related. And so every other transaction, you know, whether it's, you know, expense, AP or whatever, we've run it through Orion. So then you're looking at a small subset of data that we have to merge with Orion transactions, which is just basically cogs and revenue for the most part. 
**Ken Baugh** *[18:53]*: Yeah, it'd be our backlog and. 
**Ken Baugh** *[18:56]*: Our receivables and pay, all that stuff. Yeah, yeah, we'll have to map that out and coordinate that. But I think that makes sense. Like operating expenses could immediately go there. We could get payroll and things imported in there. So. 
**Kevin Baugh** *[19:14]*: Okay, so quick question. So I'm looking at these accounts here that we've highlighted and somewhat questioned in the new system. It sounds like because Our trial balance data will have values, historical data in these fields, and we will not have been able to zero out all these accounts for prior to upload. We're going to essentially have to clutter up our new system with these old accounts. Correct. 
**Ken Baugh** *[19:37]*: Well, we can. I think what I'm hearing is, yeah, we would keep them. 
**Ken Baugh** *[19:42]*: That's, that's making more sense as to. 
**Kevin Baugh** *[19:44]*: Why they would be in here. 
**Ken Baugh** *[19:46]*: But then we can, you know, we can make them inactive after they're kind of cleared out. But we still have, but we still. 
**Ken Baugh** *[19:52]*: Have the historical data there and we could even, you know, hide these lines that are dormant or not active. 
**Chris Trumble** *[20:00]*: Yep. 
**Sandra Massey** *[20:00]*: We can always. In terms of financial statements, we can always customize those reports so you won't show the accounts that are inactive. There's ways for us to establish different layouts for your income statement and the balance sheet. 
**Kevin Baugh** *[20:22]*: Yeah, got it. 
**Sandra Rudloff** *[20:25]*: Yeah. 
**Kevin Baugh** *[20:25]*: I mean, again, just kind of at a. Yeah. A perfectionist struggle is, you know, we're paying a lot of money to switch systems and unfortunately this is going to be in there and I. Even if we hide it, I mean, it's just, it's not truly a clean slate, per se. 
**Sandra Rudloff** *[20:40]*: Right. 
**Kevin Baugh** *[20:40]*: That's the, that's the struggle. 
**Ken Baugh** *[20:43]*: Well, I think, yeah, it's just kind of the messiness of our current system. 
**Ken Baugh** *[20:47]*: We gotta still let that flow through, so. 
**Kevin Baugh** *[20:52]*: Got it. We have some questions on it. 
**Ken Baugh** *[20:54]*: All right. Messiness. It's just, it's just a complicated system. 
**Kevin Baugh** *[20:57]*: Sure. 
**Ken Baugh** *[20:58]*: Okay. 
**Kevin Baugh** *[20:59]*: So that kind of. So again, just to summarize, we had questions on kind of new process, old process. These accounts here we highlighted in orange. Sounds like we'll keep them as is for this initial coding on the AP side. I know we had questions. We sort of talked about that as well. Do you want to. Do we want to talk about. 
**Ken Baugh** *[21:17]*: I think it's just kind of again, understanding how. Because we have, I mean, in. 
**Ken Baugh** *[21:23]*: Our current system, we kind of distinguish. 
**Ken Baugh** *[21:25]*: Between, you know, accounts payable for, like. 
**Ken Baugh** *[21:29]*: Our, you know, our operating expenses versus accounts payable, you know, for projects, project account payable. So again, just understanding how. How a project flows through. And if we have that under a separate accounts payable account, then, you know, our utility bills, for example, and then. 
**Ken Baugh** *[21:52]*: We have currently all of these purchase. 
**Ken Baugh** *[21:55]*: Price variances, accounts for each that correspond with, you know, all of our breakdown line items on the sales and COG side. And I guess I'm just wondering if that's. If we're gonna. 
**Kevin Baugh** *[22:12]*: Am I interpreting this correctly? That in the. In the Orion system there's only one PPV account essentially. Is that. Is that what that is saying on the. Right. 
**Chris Trumble** *[22:19]*: Okay. Yeah. 
**Kevin Baugh** *[22:21]*: So we would lose that breakdown. I think to answer your question. Right. We would just have one. 
**Ken Baugh** *[22:26]*: Well, and I don't know. I mean because these are usually small amounts. 
**Ken Baugh** *[22:30]*: Right. That are just being adjusted off when there's a discrepancy between the, you know, the vendor invoice and our po. 
**Kevin Baugh** *[22:38]*: Right. 
**Sandra Rudloff** *[22:40]*: Actually Chris, didn't we talk about this that if there was a variance in our PO price to what we're being invoiced that it would write back to the project and cost of goods? 
**Chris Trumble** *[22:50]*: Yeah, I believe it. I believe it does. 
**Sandra Rudloff** *[22:53]*: So the pb. This may be a moot point because we're not going to be recording discrepancies there. It goes back to the project. 
**Kevin Baugh** *[23:01]*: Yeah. 
**Ken Baugh** *[23:04]*: That'D be good to know. 
**Ken Baugh** *[23:05]*: And then, but then. Yeah. 
**Ken Baugh** *[23:08]*: Do we need to. I don't know that we would need to carry this forward maybe for the back, you know, project still in the backlog. We may under. You know, while we're winding down Dynamics. Okay. 
**Kevin Baugh** *[23:22]*: So we had some questions around kind of the groupings of admin versus operating expenses. I don't know if you want to. 
**Ken Baugh** *[23:29]*: Yeah. Just curious if we could you know. 
**Ken Baugh** *[23:34]*: Kind of play around this. 
**Ken Baugh** *[23:36]*: You know, maybe create some. 
**Ken Baugh** *[23:37]*: Some different roll ups. 
**Ken Baugh** *[23:40]*: I understand. I mean I. 
**Ken Baugh** *[23:42]*: Looks fairly straightforward the way it's set up but. 
**Ken Baugh** *[23:47]*: I assume we could. 
**Ken Baugh** *[23:49]*: We could recommend some. Just some other groupings that we'd like to see in terms of how the OPEX rolls up. 
**Ken Baugh** *[23:57]*: And then on those. On those accounts that are highlighted in. 
**Ken Baugh** *[24:00]*: Green like where you've got the operating expenses. 61000. 
**Ken Baugh** *[24:04]*: I assume that's just a roll up. 
**Ken Baugh** *[24:06]*: Some like a roll up account, summary account. Is that right? It's not a posting account or that. 
**Sandra Massey** *[24:11]*: That is correct. And just not to, you know, just to clarify stuff. It can be either posting or non posting. That's up to you. The way I have them rolling up right now are non posting. So you can post out of that level. The majority of. Or the leading practices is just use it as a summary account. I will just group certain accounts like you have marking there as the marketing as one roll up. And so that's how we will work. 
**Ken Baugh** *[24:43]*: Okay so if we. We can get back to you with. 
**Ken Baugh** *[24:47]*: Just our thoughts on how we'd like to have that rolled up then, correct? 
**Sandra Rudloff** *[24:53]*: Yes. 
**Ken Baugh** *[24:54]*: Okay, very good. And then scroll down. Kevin, I think at the bottom I had some questions around the. Again getting Back to kind of the work in process, Project labor offset. 
**Ken Baugh** *[25:15]*: Just wanted to understand if you know. 
**Ken Baugh** *[25:17]*: How these transactions flow through in netsuite and do we need to have them set up the same way as we, as we do it in. 
**Chris Trumble** *[25:30]*: So do you consider these departments in your business? 
**Ken Baugh** *[25:35]*: Well, like the pm, Design, PC. 
**Ken Baugh** *[25:39]*: Yeah, those are departments. 
**Chris Trumble** *[25:40]*: Okay. 
**Ken Baugh** *[25:42]*: But the. Yeah, and I was going to say it's fairly common for dealers to have. 
**Ken Baugh** *[25:54]*: These, you know, project offset accounts to transfer from, you know, like design expenses from design. We capture it as an operating expense, salaries and everything and then we transfer it to cost of sales through these project offset accounts. And does, I guess again, does Orion essentially work the same way on that? 
**Chris Trumble** *[26:17]*: Yeah. And as far as splitting them like the reason I asked about departments is because there are a few dimensions that are just native to the platform. So it can be one project labor offset with the dimension of a specific department that goes into the same account. 
**Ken Baugh** *[26:35]*: Yeah, I think that would work. We can still get reporting on those. 
**Ken Baugh** *[26:40]*: Dimensions and everything, right? 
**Chris Trumble** *[26:41]*: Exactly. Yep. 
**Ken Baugh** *[26:43]*: And that's probably another thing that we. 
**Ken Baugh** *[26:44]*: That I at least want to understand a little better is the, you know, how the dimensions are set up, are they similar to what we're doing now and so forth? 
**Ken Baugh** *[26:52]*: Yeah, but yeah, I think we potentially. 
**Ken Baugh** *[26:56]*: Then could just have one offset account as long as we have the dimensions behind it in terms of where that flows. 
**Ken Baugh** *[27:07]*: We currently, and we currently do have. Yeah, like we'll, we capture all. 
**Ken Baugh** *[27:16]*: Of our design expense under a design department and that pulls in from different locations. 
**Chris Trumble** *[27:22]*: Yep. 
**Ken Baugh** *[27:22]*: And then the project offset, you know, hits against that department so that we can see, you know, at the end of the day did the offset, you know, cover our expenses and so forth. But I assume with the dimension reporting we could see it that way. 
**Chris Trumble** *[27:39]*: Yep. 
**Ken Baugh** *[27:41]*: Okay. 
**Ken Baugh** *[27:43]*: And then the work and process part of this, and I think Connie, you said that because we don't, that this is just like automatic clearing account or something. 
**Ken Baugh** *[27:55]*: We don't see it actually show up. 
**Ken Baugh** *[27:57]*: On our P and L. But then. 
**Ken Baugh** *[28:00]*: I'd like to understand again, does it work the same way in Orion or do we even need those accounts in Orion? 
**Connie Chung** *[28:14]*: Sandy, you know how the, our upload work in D365 because these two are kind of relayed. 
**Sandra Rudloff** *[28:21]*: Right. But we won't be doing time uploads. It'll be basically straight time entry from the different departments. But that might be something else. Could we see, you know, from time entry to the order to, you know, offset you know, WIP and then eventually the cost of goods. Seeing that account flow would be helpful as well. 
**Chris Trumble** *[28:45]*: Yeah, Yeah, I can include that in there. 
**Ken Baugh** *[28:52]*: Yeah. And Sandy, you. I don't know. Yeah, you mentioned like it take a messy job, but if you could, you. 
**Ken Baugh** *[29:01]*: Know, created like a scenario project or something that we'd want to see just how all of those transactions flow through to the gl. 
**Ken Baugh** *[29:11]*: Right. 
**Sandra Rudloff** *[29:12]*: Yeah. 
**Connie Chung** *[29:13]*: Including. 
**Ken Baugh** *[29:13]*: Including labor and you know, internal labor. 
**Ken Baugh** *[29:16]*: External labor, you know, product etc. Trade. 
**Sandra Rudloff** *[29:22]*: Sure. I can do a little scenario because. Yeah, I can. I want to try and think of the messiest order possible. 
**Chris Trumble** *[29:28]*: Yeah. 
**Sandra Rudloff** *[29:28]*: How we would expect to see everything. 
**Ken Baugh** *[29:30]*: Yeah, yeah, that would be. 
**Ken Baugh** *[29:32]*: That'd be helpful for sure. 
**Sandra Rudloff** *[29:33]*: Yeah, sure. 
**Chris Trumble** *[29:36]*: And I sent you in the chat, Sandy, like a little thing I put together that came directly from the code base. It's like the high level overview, but it's still good to go through the like the messy order and fill in all the blanks for that one. 
**Sandra Rudloff** *[29:50]*: Got it. Yeah, I'll get that to you know, within the hour. 
**Chris Trumble** *[29:55]*: Okay. 
**Sandra Rudloff** *[29:56]*: That shouldn't be too hard to pull together. 
**Chris Trumble** *[29:58]*: I'll be with Marcus in the car for three hours tomorrow driving to Miller Knoll, so we'll have plenty of time to talk it through. 
**Ken Baugh** *[30:07]*: Now, hopefully the roads are not icy. 
**Sandra Massey** *[30:11]*: Quick question. Will the project accounts, the WIP accounts, will those have historical trials, balances or not? 
**Sandra Rudloff** *[30:22]*: I don't think we're going to bring those over. No. 
**Sandra Massey** *[30:25]*: Okay, so you're gonna make and see which accounts. Again, Sorry, if you could press print a spreadsheet again. Those are the last ones, I think. 
**Ken Baugh** *[30:39]*: Yeah, yeah. 
**Chris Trumble** *[30:40]*: One moment. 
**Kevin Baugh** *[30:41]*: Sorry, thought were done with that. 
**Sandra Massey** *[30:45]*: And so let's look for instance at your Project labor accounts in your current system. You're having like Project labor offset internal systems, offset PM offset design. Will those have historical trial balances that you would like to see on the system? And this is also considered in your budget in platform you're going to start using. 
**Ken Baugh** *[31:16]*: I think the answer is yes, we. 
**Ken Baugh** *[31:18]*: Want to have that historical information in there. 
**Sandra Massey** *[31:23]*: And so. 
**Ken Baugh** *[31:24]*: So then you would. Well, or as your question, could we. 
**Ken Baugh** *[31:29]*: Just have a roll up to one offset account as opposed to several? 
**Sandra Massey** *[31:34]*: That is correct. 
**Ken Baugh** *[31:35]*: Yeah. 
**Sandra Massey** *[31:39]*: One thing, it will make it really difficult for you to validate because you have them all bunch up into one. Usually what we do or what I do is create a custom field that will say legacy account equivalent to Dynamics or something like that within the account record. So that will facilitate your validation of your historical trial balances and kind of make those match. So that's what I'm bringing, I think. 
**Ken Baugh** *[32:13]*: Yeah, I think that makes sense to. 
**Ken Baugh** *[32:15]*: Show it as like a legacy account like that. 
**Sandra Massey** *[32:20]*: Yeah. And I can even put as department in class in our departments in there so you can, you know, validate this quicker. Yeah, I think that's the only questions you have as far as the division of your expenses into administrative and operational. Are those okay or I was far off from your current. 
**Ken Baugh** *[32:52]*: I think for the most part they're good. But we may want to just. 
**Ken Baugh** *[32:59]*: Show the groupings a little differently. Like I said. 
**Sandra Massey** *[33:04]*: That shouldn't be difficult to modify. And if we see all other types of groupings that you like to have, again, it's a very easy operation as long as they are the same NetSuite account type. So in other words, or request all the current assets should be other current assets for the pattern in the children. Right? 
**Ken Baugh** *[33:30]*: Yeah. 
**Ken Baugh** *[33:37]*: Yeah. So for example, he's got, Kevin's got like software licenses. I mean we group currently like our, you know, all of our IT related. 
**Ken Baugh** *[33:50]*: Expenses into one roll up like we do for like, you know, facilities expenses and things like that. So yeah, we, I guess if we. 
**Ken Baugh** *[34:03]*: If we just want to mock this. 
**Ken Baugh** *[34:04]*: Up and send it back to you with our, you know, suggestion or request. You can review it. 
**Sandra Massey** *[34:09]*: Yeah, yeah, I can review it with Chris, considering Orion's needs as well because you know, we need to be in tandem with what is needed for the second part of the software application that we're going to use. 
**Ken Baugh** *[34:27]*: Yeah. 
**Chris Trumble** *[34:31]*: Okay, so it sounds like we're close. We'll look for the updated version of this document. I don't think we have this version even so we'll get the updated version of this. Sandy will send us like the nightmare order scenario and then we'll provide feedback on both of those and then it should be close at that point. 
**Kevin Baugh** *[34:53]*: Chris, do we want to address the vertical or division part of this as well on this call or at least talk about that? 
**Chris Trumble** *[35:00]*: Yeah, yeah, we can do that. 
**Kevin Baugh** *[35:03]*: So I mean that's another kind of foundational decision on our end. Right. Do we want to keep reporting out the way we've been reporting or, you know, I guess so. Yeah, I don't know. 
**Ken Baugh** *[35:14]*: So yeah, I apologize. I haven't been in all the meetings but you know, for me, my understanding just kind of the financial dimension. 
**Ken Baugh** *[35:28]*: For example, right now we use location, we use vertical, we use departments, our departments considered, I assume a dimension in netsuite. Okay. 
**Ken Baugh** *[35:40]*: And location also. 
**Chris Trumble** *[35:41]*: Yes. 
**Ken Baugh** *[35:43]*: And then vertical is that. 
**Chris Trumble** *[35:45]*: Yeah, Vertical would be a vertical. We have a vertical custom segment. I just want to make sure that can tie back to the financials as well. 
**Ken Baugh** *[35:54]*: Okay. 
**Chris Trumble** *[35:55]*: The first two are standard. That's what we do every time. 
**Ken Baugh** *[35:57]*: Is there a. Is there a hierarchy to it? 
**Chris Trumble** *[36:01]*: Oh, like a parent child type of thing? 
**Ken Baugh** *[36:03]*: Well, yeah. I mean, like, what's the highest level of. I mean, like, so if it's. Or is it just like a matrix? So if I just wanted to see. 
**Ken Baugh** *[36:13]*: Everything in the design department roll up, I can see that. Or if I wanted to see everything in. In Los Angeles or Southern California, I could see that. Including all the different departments. 
**Chris Trumble** *[36:25]*: Correct. 
**Ken Baugh** *[36:26]*: Or if I looked at it by department, I could see for that department. 
**Ken Baugh** *[36:28]*: But including all locations, that's correct. 
**Chris Trumble** *[36:31]*: Yep. 
**Ken Baugh** *[36:31]*: Okay. 
**Chris Trumble** *[36:32]*: Both of those. And then I know for sure that the department, how it's set up, it's called Classes in Netsuite and rename it to departments. But that can have a hierarchy too. You can have like an administrative department, and that's like executive and marketing or however you want to set up. It can go one level deeper from a hierarchy standpoint as well. 
**Ken Baugh** *[36:55]*: Yeah. 
**Chris Trumble** *[36:55]*: And you can either do it on the individual or you can do it on the parent group as well. 
**Ken Baugh** *[36:59]*: Okay. 
**Ken Baugh** *[36:59]*: And is that. I mean, I assume that's all being set up as this goes now. So is there a, like a, you know, a screen, a printout or screenshot that we could see that shows how or have we provided that in terms. 
**Ken Baugh** *[37:17]*: Of what we want those dimensions to look like? 
**Chris Trumble** *[37:19]*: Yeah, I think we did discuss it in discovery. I got to look back at. Through some of the transcripts, but I think we do. We do have that, but we could, you know, it's not in a place where we can't change it. So if you go. 
**Ken Baugh** *[37:31]*: Yeah, but I mean, if that's something you could send us to review, I guess would be helpful for me is like, this is. 
**Ken Baugh** *[37:37]*: These are the dimensions that are, you know, currently or in the process of being set up. And we'll just verify if that is what we. What we need. 
**Chris Trumble** *[37:46]*: Yep. 
**Ken Baugh** *[37:47]*: And you said the vertical part of it is. 
**Ken Baugh** *[37:55]*: Can be done as well as a. As a. 
**Ken Baugh** *[37:59]*: Another category. 
**Chris Trumble** *[38:01]*: Yeah, we already have it in the system. I just want to make sure that it can be used as a. As a custom financial segment and what the impact of using just a regular custom field is for that. 
**Ken Baugh** *[38:12]*: Okay. Okay. 
**Sandra Rudloff** *[38:13]*: And that's the CRM side with forecasting as well. 
**Chris Trumble** *[38:18]*: Yes, I think. 
**Sandra Rudloff** *[38:19]*: Yeah. Okay, great. 
**Sandra Massey** *[38:22]*: So just to clarify, you have departments, locations, and is there another Segment that you have classes. Classes are usually considered as the line of business or you new strings. 
**Chris Trumble** *[38:38]*: Yeah, so we actually do it a little bit different. We're using as. As department. Yeah. Their other one was vertical market. 
**Sandra Massey** *[38:47]*: Yeah, Just keep me true, please. 
**Ken Baugh** *[38:50]*: We do have also we call them divisions, like a. 
**Ken Baugh** *[38:53]*: Like a separate, you know, business unit. 
**Ken Baugh** *[38:57]*: For a P L. Like we use. 
**Ken Baugh** *[38:59]*: That for our construction walting. 
**Ken Baugh** *[39:03]*: And would that be another dimension? 
**Kevin Baugh** *[39:06]*: Yeah, that's okay. 
**Chris Trumble** *[39:08]*: Yeah, another dimension. 
**Sandra Massey** *[39:09]*: Yeah, it's like you can add as many dimensions as you want. You don't have to only have those three. You can always additional segmentations as needed. 
**Kevin Baugh** *[39:20]*: I thought the verticals were the divisions, but that's incorrect. So like construction solutions would be a. A vertical or a division. 
**Chris Trumble** *[39:30]*: No, the vertical is the other way. It's like I think the vertical is being used and they're all just custom so we can use them however we want. Yeah, but I think the vertical is more like healthcare education, things like that. 
**Ken Baugh** *[39:42]*: If there's a. Yeah, I would just like to, you know, get a visual. 
**Ken Baugh** *[39:47]*: Of what, you know, how it's set up, when, make sure it aligns with what we're needing. 
**Chris Trumble** *[39:54]*: We'll give you what we have so far and then we can adjust it. 
**Sandra Rudloff** *[39:58]*: Okay. 
**Ken Baugh** *[40:00]*: Okay, perfect. 
**Ken Baugh** *[40:03]*: Sounds like, sounds like it's pretty flexible, which is good. 
**Sandra Massey** *[40:07]*: Yeah, yeah, it's flexible. 
**Chris Trumble** *[40:11]*: Yeah. 
**Ken Baugh** *[40:12]*: Okay. And that's good. 
**Sandra Rudloff** *[40:18]*: Okay. 
**Ken Baugh** *[40:19]*: All right. 
**Chris Trumble** *[40:19]*: So we both got a little bit of homework and then. Yeah, we'll try initially to just kind of do it over. Over email and teams and stuff. And if we need to come back together for a meeting, that's no problem either. 
**Kevin Baugh** *[40:31]*: Do you want to. I know we're like really itching to get going here, Chris. I mean like if you were to start the process, I mean, like how difficult is it? So within the operating expense section, right, like would you basically just kind of change the roll up of it Expense, sorry, software licenses, for example. Like in other words, could you start coding what we just reviewed and then we make the switches so you don't have to keep waiting for us? 
**Chris Trumble** *[40:54]*: Okay, yeah, we can do that. Yeah. 
**Sandra Rudloff** *[40:55]*: Okay. 
**Kevin Baugh** *[40:55]*: Because I mean you basically saw what those changes will be Like a few of those categories we might change the roll up, but I don't think that's going to really materially change your import process or whatever. 
**Sandra Massey** *[41:06]*: Now that depends on the type of account too because sometimes we cannot make changes. Let's say you have a roll up. We already created like say. 
**Connie Chung** *[41:18]*: All the. 
**Sandra Massey** *[41:19]*: Current asset or other current liability. Those are hard to create rollups because they not allow us to change the types. Let's say you want to use another account, say other current assets for another account number, and we have to virtually delete it and create a new one, because that's how NetSuite works. 
**Kevin Baugh** *[41:42]*: They were more P and L. I. 
**Ken Baugh** *[41:43]*: Think we're talking mostly just on the. 
**Sandra Massey** *[41:45]*: Operating the P and L. Ye. Yeah. Yeah. No, those are easy. Those are easy to. To. Yeah. 
**Kevin Baugh** *[41:52]*: So I guess for our team, I mean, we could meet again today. I'm just curious, like, I didn't see anything or hear anything that said. Chris, you can't start coding everything. And if we want to shift marketing to a. A kind of. 
**Ken Baugh** *[42:03]*: Yeah, I would just like to just. 
**Ken Baugh** *[42:05]*: Internally just do a, you know, a quick. 
**Ken Baugh** *[42:07]*: We went through that pretty quickly, but. 
**Ken Baugh** *[42:09]*: Just, you know, just validate what we want, then we can send that off. 
**Chris Trumble** *[42:12]*: Yeah, that's no problem. 
**Ken Baugh** *[42:13]*: Yeah. 
**Ken Baugh** *[42:14]*: Okay. 
**Sandra Rudloff** *[42:16]*: Okay. 
**Chris Trumble** *[42:18]*: Yeah, so we have a couple. Oh, yes, several action items. 
**Sandra Massey** *[42:20]*: So we'll. 
**Chris Trumble** *[42:21]*: We'll grab the transcript from this and just send it out so everyone knows what we're responsible for and then we'll get to work right away. 
**Kevin Baugh** *[42:30]*: Great. Hey, Random. 
**Sandra Massey** *[42:32]*: Yeah, go ahead. 
**Kevin Baugh** *[42:33]*: I'm sorry, random. 30 second question or 15 second question. 
**Chris Trumble** *[42:36]*: Yeah. 
**Kevin Baugh** *[42:37]*: Since we started this journey with you, I feel like a lot has changed within the AI space. Do you have any updates at all about future AI integration or tools that we didn't know about when we started this process? Like, is there anything there you can update us on? 
**Chris Trumble** *[42:53]*: Yeah. So a lot has changed. Even, like, you know, Marcus and I have been developing actual features and bug fixes and stuff. Not as developers, just as people who understand the customer's needs. 
**Kevin Baugh** *[43:07]*: Are you using, like, cloud code or cloud code? Because, I mean, literally, that is. 
**Chris Trumble** *[43:11]*: Yeah, we're using Claude code. And it's been interesting because obviously at one time we had 20 developers on the team, like, trying to get the software over the finish line, and now we're at a point where it takes me less time to develop the piece of software myself than it would to give a full spec document to a developer, have them churn through it, me go and quality check it. So we are shifting that way quite a bit. And then on the other side. 
**Sandra Rudloff** *[43:42]*: The. 
**Chris Trumble** *[43:43]*: Ability to have a chatbot in the platform that knows everything from the actual code itself to everything about NetSuite to what is Orion versus what is NetSuite itself, that has been developing really rapidly as well. So although we're not saying like this is for release right now. It won't be like a future version that gets the chatbot because, you know, like documentation gets aged very quickly and people tend to not trust it and they don't go back and they don't read it and they don't spend the time. But if they can just interact with something that can tell them, okay, this is based on where the software is at right now. I think that's going to be a lot more helpful to users than, you know, 100 pages of Orion documentation and then all of the NetSuite help documentation. 
**Chris Trumble** *[44:33]*: So, yeah, things are changing very quickly in that space. 
**Kevin Baugh** *[44:37]*: I'm envisioning a future state where I can interact or we can feed like all of our corporate invoices or project related invoices, any invoice to a, an AI kind of bot or whatever and just have it. And so I was just curious, right as we're looking at our process and reviewing BRDs like have there, you know, are you creating any programs within the program, so to speak, for addressing some of these things? 
**Chris Trumble** *[44:58]*: Yeah. The other thing, how it's really manifested is things like, you know, I would normally have to walk every user through setting up their user preferences. There's 96 user preferences and we have a suggested setting for each one of those 96 user preferences. So either me or someone in your team has to say, okay, user, go in there and this is exactly the set. So look at the set of 96. They set it all. We have a little, it's like a JavaScript snippet where you literally. They go to a page for their personal settings. They say, set all my settings to Orion standards. It literally does it in 10 seconds and then they save it and they're done. 
**Chris Trumble** *[45:41]*: It's like we're finding a lot of ways to just make it easier on the users to do little things like that where we would have to spend a lot of time in the past. So lots of little tricks like that are coming to fruition. 
**Kevin Baugh** *[45:57]*: Awesome, thanks for the update. 
**Chris Trumble** *[45:58]*: Yeah, absolutely. All right, we will, yeah, we'll get to work on our side. We'll look for the feedback from you guys and we'll talk soon. 
**Ken Baugh** *[46:09]*: Thank you. 
**Sandra Rudloff** *[46:10]*: Thank you, everyone. 
**Sandra Massey** *[46:11]*: Thank you. 
**Chris Trumble** *[46:12]*: Bye. 
**Sandra Massey** *[46:12]*: I. 
