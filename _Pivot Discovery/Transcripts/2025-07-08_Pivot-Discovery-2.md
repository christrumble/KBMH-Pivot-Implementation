# Pivot Discovery 2

**Meeting Date:** 8th Jul, 2025 - 11:01 AM

---

**Marcus Dallacqua** *[00:00]*: Any questions or comments from yesterday's session? 
**Marcus Dallacqua** *[00:07]*: Okay. 
**Marcus Dallacqua** *[00:10]*: Deal. 
**Marcus Dallacqua** *[00:12]*: We sent that follow up email out yesterday as well. Thank you for sending the documentation that you send. 
**Marcus Dallacqua** *[00:17]*: We've already started collecting that. 
**Marcus Dallacqua** *[00:19]*: We have a SharePoint folder associated with. 
**Marcus Dallacqua** *[00:22]*: Your project that we're collecting all that. 
**Marcus Dallacqua** *[00:24]*: Info into then also, I think I've. 
**Marcus Dallacqua** *[00:27]*: Mentioned this before, but we use Claude. 
**Marcus Dallacqua** *[00:29]*: AI and we use that to document everything as well. That allows us to quickly create content. 
**Marcus Dallacqua** *[00:37]*: Like follow up notes, you know, the. 
**Marcus Dallacqua** *[00:39]*: Follow up from the sessions. And also it helps us just keep. 
**Marcus Dallacqua** *[00:43]*: Track of things a bit better. 
**Marcus Dallacqua** *[00:46]*: So we've incorporated that all into our. 
**Marcus Dallacqua** *[00:48]*: Cloud project as well. 
**Marcus Dallacqua** *[00:50]*: All right, I can now share. 
**Marcus Dallacqua** *[00:52]*: Let me share my screen. 
**Marcus Dallacqua** *[00:53]*: We're actually going to be in the. 
**Marcus Dallacqua** *[00:54]*: PowerPoint for a minute here because we're. 
**Marcus Dallacqua** *[00:58]*: Going to be jumping into a couple of our topics. 
**Marcus Dallacqua** *[01:02]*: There we go. 
**Marcus Dallacqua** *[01:02]*: So today again, focused on setup, configurations, a lot of the stuff that we started yesterday. 
**Marcus Dallacqua** *[01:07]*: We're going to go a little bit. 
**Marcus Dallacqua** *[01:08]*: Deeper today, especially on data migration and revisiting some of this stuff. 
**Marcus Dallacqua** *[01:15]*: Company structure, chart of accounts, system preferences, segmentation and user management and security. Talking specifically about roles and permissions and things like that. 
**Marcus Dallacqua** *[01:26]*: That's what we're going to cover today. Including that data migration really could be. 
**Marcus Dallacqua** *[01:30]*: Another bullet point here. But we're going to focus a bit more, I think, towards the end on data migration because we want to really. 
**Marcus Dallacqua** *[01:36]*: Start that conversation early and see how. 
**Marcus Dallacqua** *[01:38]*: Quickly we can get to strategy. There's going to be some big decisions that need to be made, all of. 
**Marcus Dallacqua** *[01:43]*: Them having cost implications, especially since there's. 
**Marcus Dallacqua** *[01:48]*: Multiple pieces of software that we probably have to migrate from. So we have to consider how much. 
**Marcus Dallacqua** *[01:52]*: Data we're going to pull and migrate or versus how much data we might. 
**Marcus Dallacqua** *[01:57]*: Leave in those systems. 
**Marcus Dallacqua** *[02:00]*: There's a cost analysis there that you'll have to make because sometimes some of those systems might not be that expensive. 
**Marcus Dallacqua** *[02:05]*: It might make sense to leave it. 
**Marcus Dallacqua** *[02:06]*: In the system, depending on which system it is, and sometimes it makes a. 
**Marcus Dallacqua** *[02:10]*: Lot of sense to get it out. So we'll talk about all of that. 
**Marcus Dallacqua** *[02:12]*: And I believe too, you have a. 
**Marcus Dallacqua** *[02:14]*: Data warehouse in Susan. We want to talk some more about that as well. All right, so I'm going to turn. 
**Marcus Dallacqua** *[02:20]*: That off and we're going to jump into my outline and you're going to have. Just forgive me, if you don't mind, I want to make sure I get through all the points on my outline. It's going to be a little bit. 
**Marcus Dallacqua** *[02:33]*: Redundant from some of the things we talked about yesterday. 
**Marcus Dallacqua** *[02:36]*: So I might just Be asking you questions that we've already talked about and forgive me for that, but I just want to make sure that I hit. 
**Marcus Dallacqua** *[02:41]*: Every point and we have it on the, in the transcript so we can access it later. 
**Marcus Dallacqua** *[02:49]*: Okay, so just pull this over here and just see. I, I caught myself in the camera. 
**Marcus Dallacqua** *[02:55]*: The other yesterday and it looks like. 
**Marcus Dallacqua** *[02:57]*: I'm kind of going like this all the time. So I do have, I have four screens actually here with things all over on every screen. So I'm looking around, I'm not distracted. 
**Marcus Dallacqua** *[03:06]*: I'm actually, I am focused on what we're doing here. In just a moment. I have a lot of screens. 
**Marcus Dallacqua** *[03:12]*: All right, so company structure and subsidiaries. Sandy, please remind me, and again, forgive me right now for asking the same question over again. I'm sure I'm going to. That's going to happen a lot today. I'll try to make sure that doesn't happen going forward. 
**Marcus Dallacqua** *[03:26]*: But subsidiaries, how many legal entities do you currently have? 
**Sandra Rudloff** *[03:30]*: Just one. 
**Marcus Dallacqua** *[03:31]*: Just one. 
**Marcus Dallacqua** *[03:32]*: Okay. 
**Marcus Dallacqua** *[03:32]*: And do you currently have the functionality for subsidiary management or companies inside of. 
**Marcus Dallacqua** *[03:39]*: D365 and are you utilizing it? 
**Sandra Rudloff** *[03:42]*: We do have it and we aren't. 
**Marcus Dallacqua** *[03:44]*: You aren't. Okay. All right, very good. 
**Marcus Dallacqua** *[03:47]*: Moving on. Currency. Are you just using US Currency? 
**Marcus Dallacqua** *[03:53]*: Yep. 
**Marcus Dallacqua** *[03:54]*: Any need for Canadian or anything else? 
**Marcus Dallacqua** *[03:57]*: No. 
**Marcus Dallacqua** *[03:57]*: Great. 
**Marcus Dallacqua** *[03:59]*: We'll keep it easy. 
**Marcus Dallacqua** *[04:00]*: I believe you sent over all the documentation for departments and locations, is that correct? 
**Sandra Rudloff** *[04:06]*: I did. Divisions, locations, and our chart of accounts. 
**Marcus Dallacqua** *[04:10]*: Okay, great. What about the departments? Can we get that as well? I think we gave you ours. 
**Marcus Dallacqua** *[04:18]*: Yeah. 
**Sandra Rudloff** *[04:19]*: Okay, let me. 
**Marcus Dallacqua** *[04:19]*: Yeah, I'll pull that. 
**Marcus Dallacqua** *[04:21]*: Okay, great. 
**Ken Baugh** *[04:22]*: And I'm not familiar with the structure in Microsoft we use dimensions for a lot of that, so. And I don't know if it's set up in a similar way in netsuite, but it's nice if you can kind of slice and dice if you've got the granularity in terms of departments and locations and then just roll it up depending on how you want to report it. That would be, I think, the way we'd want to go. 
**Marcus Dallacqua** *[04:51]*: Yeah, we did talk about that a bit yesterday and it seems. 
**Marcus Dallacqua** *[04:54]*: To be set up very similar to how Netsuite is. So I think it's going to be almost a one to one migration. Unless. 
**Marcus Dallacqua** *[05:02]*: Unless there's some upgrades that you want. 
**Marcus Dallacqua** *[05:03]*: To do on all these. 
**Marcus Dallacqua** *[05:04]*: But we'll. 
**Marcus Dallacqua** *[05:05]*: You'll have an opportunity to let us know if that's the case. 
**Marcus Dallacqua** *[05:08]*: One quick question about segmentation. Dimensions are you tracking that at the transaction body level, or are you also. 
**Marcus Dallacqua** *[05:16]*: Tracking it at the line level? 
**Sandra Rudloff** *[05:18]*: Line level. 
**Marcus Dallacqua** *[05:19]*: Okay. 
**Marcus Dallacqua** *[05:19]*: For everything. 
**Marcus Dallacqua** *[05:20]*: Yeah. 
**Marcus Dallacqua** *[05:21]*: Okay, great, thanks. 
**Marcus Dallacqua** *[05:23]*: Netsuite has that same capability, and we. 
**Marcus Dallacqua** *[05:25]*: Have it enabled on almost everything. So I just wanted to confirm. 
**Sandra Rudloff** *[05:27]*: Question about segmentation. How many can we have? I mean, if we really want to slice and dice deeply, it's really unlimited. 
**Marcus Dallacqua** *[05:36]*: The only thing I would say is the primary purpose of that custom segmentation is really for the financial reports. 
**Marcus Dallacqua** *[05:47]*: It rolls up to the financial reports. 
**Marcus Dallacqua** *[05:49]*: Otherwise, you can get that without creating. 
**Marcus Dallacqua** *[05:52]*: Those custom segments just in a regular report. 
**Marcus Dallacqua** *[05:55]*: So if you have. 
**Marcus Dallacqua** *[05:56]*: That's where they kind of. That's where we kind of differentiate. If you have the need that you want it at the income statement level. 
**Marcus Dallacqua** *[06:01]*: Or the balance sheet level, then let's do it. Otherwise, we can just get the information for you in the report. 
**Ken Baugh** *[06:07]*: But is that customization? You said customer. I mean, is that a. Is that considered a customization? 
**Marcus Dallacqua** *[06:14]*: Yeah, but there's. It's a different level of customization. It's considered a point and click customization. In other words, netsuite gives you this. 
**Marcus Dallacqua** *[06:20]*: Little admin interface to create custom things like that. 
**Marcus Dallacqua** *[06:23]*: There's no additional cost for that, or. 
**Marcus Dallacqua** *[06:26]*: Like, any user could technically do that had permissions. 
**Marcus Dallacqua** *[06:29]*: Okay. 
**Marcus Dallacqua** *[06:29]*: Yeah, so that's a good question, Ken. I try to differentiate between personalizations and customizations, so I'll do my best to say that. So that would be like a personalization, something that, like, Sandy could go in. 
**Ken Baugh** *[06:45]*: The system and, like a setup issue. 
**Marcus Dallacqua** *[06:47]*: Yeah. Yeah. 
**Ken Baugh** *[06:48]*: Okay. 
**Marcus Dallacqua** *[06:49]*: Yeah, yeah, perfect. Okay. 
**Marcus Dallacqua** *[06:53]*: And then we sent over. Chris, did we send over the chart of accounts? You're there. 
**Marcus Dallacqua** *[07:02]*: You're on mute. Oh, sorry, I was muted. 
**Marcus Dallacqua** *[07:04]*: Yes, we did. 
**Marcus Dallacqua** *[07:04]*: We did send over the chart of accounts yesterday. 
**Marcus Dallacqua** *[07:06]*: Okay. 
**Marcus Dallacqua** *[07:07]*: And I. And I doubt, Kevin, you had time to look at that, but I just. 
**Marcus Dallacqua** *[07:11]*: Wanted to check to see if by chance you did. 
**Kevin Baugh** *[07:13]*: We got it. Yeah, we didn't. We didn't solidify anything. Apologies there, but we did receive. Sent over. 
**Marcus Dallacqua** *[07:18]*: Yep. 
**Marcus Dallacqua** *[07:19]*: Yeah, Yeah, I didn't think. I didn't think you'd have time to. 
**Marcus Dallacqua** *[07:21]*: Be able to do that on a. 
**Marcus Dallacqua** *[07:22]*: Day'S notice, but just let me know if there's things that you want to. 
**Marcus Dallacqua** *[07:26]*: Talk through on that. That's. 
**Marcus Dallacqua** *[07:28]*: It's the starting point. What about statistical accounts for cost allocation? 
**Marcus Dallacqua** *[07:36]*: Do you currently use those? 
**Ken Baugh** *[07:40]*: Explain what that is a little more. 
**Marcus Dallacqua** *[07:44]*: Yeah, there's sub accounts, and specifically for cost allocation, you can set up cost allocation schedules. Like, a good example would be, like, I want. Every department has an Employee count and. 
**Marcus Dallacqua** *[07:58]*: I want to allocate costs for each employee across departments and I'm going to use some methodology for doing that. 
**Marcus Dallacqua** *[08:05]*: You have the ability in netsuite to do that? I wasn't sure if you currently had that ability. 
**Ken Baugh** *[08:13]*: We do some of that within Adaptive, but I think if we could do some of that within netsuite it would be. So I understand what you're saying now. It's like metrics and things like that. So yeah, we could. I think that's something we would want to look into. 
**Marcus Dallacqua** *[08:27]*: Okay, great. 
**Marcus Dallacqua** *[08:28]*: So as an action item, we're going to send you a PDF document, statistical accounts for cost allocation. So you have some reading. It'll be a PDF document but also. 
**Marcus Dallacqua** *[08:40]*: A link to the help docs inside NetSuite. 
**Marcus Dallacqua** *[08:43]*: So NetSuite has a. 
**Marcus Dallacqua** *[08:44]*: Or it's really Oracle Help center, but. 
**Marcus Dallacqua** *[08:47]*: There'S a link in there that can. 
**Marcus Dallacqua** *[08:49]*: Somebody can read up on that to make sure that's the functionality that. 
**Marcus Dallacqua** *[08:53]*: You want and that's public and actually. 
**Marcus Dallacqua** *[08:56]*: I'm going to throw that in the chat right now. Yeah, I have it right here too. Markus, do you have the PDF as well? 
**Marcus Dallacqua** *[09:03]*: Either way, go ahead and throw those two things into. 
**Marcus Dallacqua** *[09:06]*: The chat and we'll save ourselves an action item. 
**Marcus Dallacqua** *[09:10]*: What's the rule? If you can do something in two. 
**Marcus Dallacqua** *[09:12]*: Minutes or less, do it. I don't know if that applies here. 
**Marcus Dallacqua** *[09:18]*: If we can do it like maybe here it's 30 seconds or less. 
**Marcus Dallacqua** *[09:21]*: We can do 30 or less. Let's do it. 
**Marcus Dallacqua** *[09:24]*: Great. 
**Marcus Dallacqua** *[09:26]*: All right, so we have that open. 
**Marcus Dallacqua** *[09:28]*: Action item with the chart of accounts. We're going to do system preferences of features. I've already talked about walking through. Let's talk for a moment about auto. 
**Marcus Dallacqua** *[09:39]*: Generated numbers and transactions. 
**Marcus Dallacqua** *[09:42]*: How have you guys managed that up until this point? 
**Marcus Dallacqua** *[09:44]*: And do you have a particular strategy. 
**Marcus Dallacqua** *[09:46]*: And have you, do you have any. 
**Marcus Dallacqua** *[09:48]*: Ideas if you want to upgrade that or make changes to that? 
**Sandra Rudloff** *[09:52]*: Well, we use SMART numbering, basically our project number. You know, six digit. We can have up to 99 sub projects under that. And that sub project is what flows through on our quotes order confirmations. That becomes the quote order number. And then all of our purchase orders use that sub project as the prefix and then after that it's just a numerical sequence. 
**Marcus Dallacqua** *[10:20]*: Okay, so that's a little bit different than how netsuite does it. Is that working well for you? 
**Marcus Dallacqua** *[10:30]*: Oh yeah. 
**Sandra Rudloff** *[10:31]*: Ever since went to AX back in the day, we had a chameleon before. This was a huge help, especially for the Warehouse when you get, you know, they could group things and they could find things easier than just a random PO number. 
**Marcus Dallacqua** *[10:46]*: Gotcha. 
**Marcus Dallacqua** *[10:48]*: Now, we currently have. So our project record has a naming. 
**Marcus Dallacqua** *[10:51]*: Convention that you can kind of predefine. 
**Marcus Dallacqua** *[10:53]*: But it doesn't actually impact. 
**Marcus Dallacqua** *[10:56]*: Any of the transactions that are associated with it. 
**Marcus Dallacqua** *[10:59]*: So in other words, my project can be made up of a number and a name. So I can name the project and. 
**Marcus Dallacqua** *[11:04]*: I can have a prefix number for. 
**Marcus Dallacqua** *[11:06]*: It, and then that project is found on every transaction. 
**Marcus Dallacqua** *[11:10]*: Like there's a link to that project. 
**Marcus Dallacqua** *[11:11]*: On every transaction but the transaction number. 
**Marcus Dallacqua** *[11:14]*: So let's say the purchase order number. 
**Marcus Dallacqua** *[11:16]*: Is really independent of the project. Now when we send over a PDF. 
**Marcus Dallacqua** *[11:21]*: To your vendors with the po, we. 
**Marcus Dallacqua** *[11:25]*: Can concatenate the two. We can say, here's the PO number and here's the project. You can simply do that. But would that be sufficient? 
**Brian Hagerty** *[11:33]*: Or. 
**Marcus Dallacqua** *[11:36]*: Is it more like you actually. 
**Marcus Dallacqua** *[11:38]*: Want it embedded in the number? 
**Sandra Rudloff** *[11:40]*: It would be great if it could do that. I mean, like in D365, when you create a sales order, it generates its own sales order number. And what our documents print is only the sub project number. So when people look at things, they're not referring to the system generated sales order number, they refer to the project number or the sub project number. 
**Marcus Dallacqua** *[12:01]*: Okay. 
**Sandra Rudloff** *[12:02]*: It would be great if the purchase order could be embedded that way as well. So if you're looking for pos, you don't have. So I'm, I issue 100 pos on a sub project. It'd be nice to be able to enter that sub project in your, you know, all open POS to look at things against it rather than having to query up each individual PO number. Yeah, I know that'll be a, that will be a customization. But I think we'd be interested in how much it would take because. Because it really does help a lot of different departments. 
**Marcus Dallacqua** *[12:36]*: Yeah. 
**Marcus Dallacqua** *[12:36]*: Can you give us some, can you give us some examples of that? Even if it's screenshots and maybe an. 
**Marcus Dallacqua** *[12:43]*: Example of a PDF, just so we can wrap our minds around that and be really clear. 
**Marcus Dallacqua** *[12:46]*: I mean, right now, the way that. 
**Marcus Dallacqua** *[12:47]*: The numbering works inside NetSuite is for. 
**Marcus Dallacqua** *[12:50]*: All of the transactions. 
**Marcus Dallacqua** *[12:51]*: It's sequential. 
**Marcus Dallacqua** *[12:52]*: And you can do a prefix, you can do a suffix, but those are fixed. In other words, I can do a prefix for my sales orders and the prefix might be so. And the PO might be po, or. 
**Marcus Dallacqua** *[13:04]*: The purchase order might be po. 
**Marcus Dallacqua** *[13:07]*: Those prefixes or suffixes can't Be dynamic natively, but we can do some things around that. So I do think we probably need. 
**Marcus Dallacqua** *[13:17]*: To have a deeper discussion on this because I know that numbering and naming of transactions is important. 
**Marcus Dallacqua** *[13:24]*: How do you currently know? 
**Sandra Rudloff** *[13:25]*: Oh, sorry, I was gonna say, do you want me to send you PDFs of each of the documents? Like, you know, quote sales order, purchase orders, invoice? 
**Marcus Dallacqua** *[13:33]*: Yeah, that'd be great. 
**Marcus Dallacqua** *[13:34]*: Okay. 
**Marcus Dallacqua** *[13:35]*: And then, and then screenshots, if you don't mind, of inside the system of. 
**Marcus Dallacqua** *[13:39]*: What it looks like as well. Sure. Great. 
**Marcus Dallacqua** *[13:44]*: Action items, Sandy. It'll load you up and then what's the, what is the convention for your projects? Do people manually name or number those or. 
**Marcus Dallacqua** *[13:55]*: Well, that's. 
**Sandra Rudloff** *[13:57]*: We start the project in workfront and it's a six character or six digit number that's assigned by the system. It's just the next sequential number. And then if it become gets to the point where we need to quote a client, then they're going into D365 and manually entering that project number and creating a project. 
**Marcus Dallacqua** *[14:19]*: Oh, okay. So you have two, really, you have two projects. You have your work from project and. 
**Marcus Dallacqua** *[14:23]*: Then you have your D365 project and. 
**Marcus Dallacqua** *[14:25]*: There'S no automation that links them or anything. 
**Marcus Dallacqua** *[14:28]*: They're just, they're linked by the number. 
**Sandra Rudloff** *[14:30]*: That's it. Yeah, some of our reporting that we do utilizes that. But yeah, there's no integration of any type. 
**Marcus Dallacqua** *[14:39]*: Okay, so as long as people are careful to make sure that they copy. 
**Marcus Dallacqua** *[14:42]*: The number correctly, you're okay. 
**Sandra Rudloff** *[14:44]*: Yeah, that has happened a few times where people transpose a number and use the wrong one. And unfortunately with D365, as soon as you make a financial transaction, you're committed to. 
**Marcus Dallacqua** *[14:54]*: So it. 
**Sandra Rudloff** *[14:55]*: We've had to have people either go and work front and adjust the number and if it hasn't had any, like if I do a deposit invoice now, you can't do anything. You are committed. 
**Marcus Dallacqua** *[15:05]*: Okay, gotcha. Okay. Yeah. 
**Marcus Dallacqua** *[15:08]*: The way that our project record works. 
**Marcus Dallacqua** *[15:10]*: You have, you really have the ability. 
**Marcus Dallacqua** *[15:12]*: To change the project name at any point. 
**Marcus Dallacqua** *[15:16]*: So we'll come back. We need, we will. Once we get those samples, we'll set. 
**Marcus Dallacqua** *[15:20]*: Up a session and we'll go a little bit deeper on this and come up with strategy for the naming of the project record and the numbering of the transactions. 
**Marcus Dallacqua** *[15:32]*: All right, very good. 
**Marcus Dallacqua** *[15:36]*: I also want you to know too that you can change the default naming. 
**Marcus Dallacqua** *[15:40]*: Of the records and we actually do a little bit of this. 
**Marcus Dallacqua** *[15:43]*: So Netsuite by default calls what we call it the quote, they call it the estimate. And so for some dealers, we've renamed that to quote. Most, we rename it to quote somewhat Proposal. 
**Marcus Dallacqua** *[15:54]*: What do you call it currently in your system? 
**Sandra Rudloff** *[15:57]*: Quotes, Quotation, Quotes. 
**Marcus Dallacqua** *[15:59]*: Okay. 
**Marcus Dallacqua** *[15:59]*: Quotes or quotations. 
**Sandra Rudloff** *[16:01]*: It prints as a. It prints quotation, but we refer to it internally as quotes. So we can definitely just make it quotes. 
**Marcus Dallacqua** *[16:08]*: We can make it quotes. Okay, great. 
**Sandra Rudloff** *[16:09]*: And actually one step backwards, which may have an impact on the numbering. We really want to take advantage of the SharePoint integration for all of our document storage. 
**Marcus Dallacqua** *[16:18]*: Yeah. 
**Sandra Rudloff** *[16:19]*: And I think were talking, you know, either it's by client and project or strictly project number, but I think that'll come into play too, to be able to group those in folders as we start doing this. 
**Marcus Dallacqua** *[16:32]*: Yeah, absolutely. And when we get into the CRM. 
**Marcus Dallacqua** *[16:36]*: Is when we'll talk a bit more about that. 
**Marcus Dallacqua** *[16:38]*: And I'll bring in Chris maybe, if you just want to make a note, or Debbie, we just need to bring. 
**Marcus Dallacqua** *[16:44]*: In Tyler for that discussion because Tyler is kind of the. 
**Marcus Dallacqua** *[16:48]*: The guru at setting that up because we can automatically create that folder structure. 
**Marcus Dallacqua** *[16:52]*: Inside of the SharePoint integration. 
**Marcus Dallacqua** *[16:54]*: So we'll. 
**Marcus Dallacqua** *[16:54]*: We'll do like a quick little demo. 
**Marcus Dallacqua** *[16:56]*: And then we could talk about what that. What that setup should be. 
**Sandra Rudloff** *[17:01]*: So it looks like at Pivot, we get to start up those lovely document storage meetings. Yeah, we'll have to do that soon. 
**Marcus Dallacqua** *[17:10]*: Okay. 
**Marcus Dallacqua** *[17:11]*: Are you guys using SharePoint currently? 
**Marcus Dallacqua** *[17:14]*: Yes. 
**Marcus Dallacqua** *[17:15]*: Okay. 
**Sandra Rudloff** *[17:16]*: But not for our document storage. They're kind of like, we've got a lot in iq, obviously. Like, Marie was going over. We've got them in D365. We've got them in Workfront. 
**Marcus Dallacqua** *[17:28]*: Oh, D365 doesn't natively use SharePoint. 
**Sandra Rudloff** *[17:32]*: Not that I'm aware of. 
**Ted Lo** *[17:34]*: Well, we started doing it like early days of dating 365. And I think it. They set up some weird connection and there were storage limits. But yeah, I mean, you know, maybe that demo can be done for our document team as well. So then everybody knows. 
**Marcus Dallacqua** *[17:58]*: Yeah, for sure. 
**Marcus Dallacqua** *[18:01]*: Yeah. 
**Marcus Dallacqua** *[18:01]*: We'll have to plan that accordingly because it's typically part of CRM if we. 
**Marcus Dallacqua** *[18:06]*: Want to handle that outside of CRM. 
**Marcus Dallacqua** *[18:08]*: So you can have. 
**Marcus Dallacqua** *[18:09]*: Sounds like maybe we should do that. That way you can have the IT. 
**Marcus Dallacqua** *[18:12]*: Team part of that. 
**Marcus Dallacqua** *[18:16]*: Yeah. 
**Marcus Dallacqua** *[18:17]*: So, Debbie, let's. We'll set up another separate session just. 
**Marcus Dallacqua** *[18:20]*: For the SharePoint integration. 
**Marcus Dallacqua** *[18:22]*: Got it. 
**Marcus Dallacqua** *[18:24]*: Okay, great. 
**Marcus Dallacqua** *[18:28]*: What is your fiscal year? 
**Marcus Dallacqua** *[18:31]*: Is it Calendar? 
**Marcus Dallacqua** *[18:33]*: Yeah. 
**Marcus Dallacqua** *[18:33]*: Okay, nice and easy. 
**Marcus Dallacqua** *[18:35]*: And then are you doing 12 periods. 
**Marcus Dallacqua** *[18:36]*: Or are you doing 13. 
**Marcus Dallacqua** *[18:38]*: 12. 
**Marcus Dallacqua** *[18:39]*: 12. Okay. 
**Marcus Dallacqua** *[18:40]*: Any desire to do 13? 
**Marcus Dallacqua** *[18:41]*: Or you could with the 12, you just post your. 
**Marcus Dallacqua** *[18:43]*: On the last day of the year, your journal entries. 
**Marcus Dallacqua** *[18:46]*: Or do you need a 13th period? Or would you like a 13th period? 
**Sandra Rudloff** *[18:51]*: I'll let Ken answer that one. Or Kevin. 
**Ken Baugh** *[18:53]*: Yeah, we've always used 12, so I don't know, we'd have to maybe understand the advantage of using the 13 period, but currently we're using 12. 
**Marcus Dallacqua** *[19:05]*: Yeah. 
**Marcus Dallacqua** *[19:06]*: Really, the only advantage is there's things that you post on 1231 that naturally happen on 1231, and then things you post on 1231 that are the typical. 
**Marcus Dallacqua** *[19:19]*: End of the year adjustments. 
**Marcus Dallacqua** *[19:20]*: Yeah. 
**Ken Baugh** *[19:20]*: So 13th period, you would just use that to capture all the. That might be something we want to consider. We haven't been doing it that way, but that might be. 
**Marcus Dallacqua** *[19:30]*: Be. 
**Ken Baugh** *[19:31]*: Be a cleaner way to do it. 
**Marcus Dallacqua** *[19:32]*: So. 
**Marcus Dallacqua** *[19:33]*: Yeah, it helps you differentiate. 
**Ken Baugh** *[19:36]*: Yeah, let's put that as a to be determined. But Kevin, we can. And Connie, we can. Connie, what? Do you think that would be helpful? I don't know if you've. 
**Connie Chung** *[19:48]*: Yes, I think would be helpful, Ken, because the period 13 is where we make the adjustment at the year end. I think that's how we set up in the 365 to. Yes. 
**Marcus Dallacqua** *[19:57]*: Yeah. 
**Marcus Dallacqua** *[20:00]*: Okay. 
**Marcus Dallacqua** *[20:01]*: We'll come back on that and get a confirmation. We talked yesterday about the vertical markets, and you guys. I think you call them something different. So vertical markets for us are like health care. And I think. Actually, Chris, I think I saw you. 
**Marcus Dallacqua** *[20:19]*: Send this health care education, those types of things. 
**Marcus Dallacqua** *[20:22]*: What do you call them in your system? 
**Sandra Rudloff** *[20:24]*: Divisions. 
**Marcus Dallacqua** *[20:25]*: Divisions. 
**Marcus Dallacqua** *[20:27]*: Are you okay with calling them vertical markets? 
**Ken Baugh** *[20:31]*: Yeah, I think, Ryan, I think from a terminology standpoint, it doesn't matter. Are those. Is that like an additional field or. I mean that. Like a dimension, I guess, or is it. Okay. Yeah, just again, so. So that we can, you know, sort and report on different things. 
**Marcus Dallacqua** *[20:53]*: Yeah, exactly. 
**Marcus Dallacqua** *[20:55]*: Oh, sorry. 
**Marcus Dallacqua** *[20:56]*: Yeah. 
**Ken Baugh** *[20:56]*: If they're called verticals, that's. I think that's fine. 
**Marcus Dallacqua** *[20:59]*: Okay. 
**Ken Baugh** *[21:00]*: And is there a. I assume that's kind of a unlimited. Not that we'd have a ton of them, but is there any limitation on those? 
**Marcus Dallacqua** *[21:08]*: No. Okay. 
**Marcus Dallacqua** *[21:10]*: Now you can have hundreds. 
**Marcus Dallacqua** *[21:12]*: And these do flow all the way up to the, like things like the income statement. 
**Marcus Dallacqua** *[21:15]*: So you can have a P and L just for. Of those vertical markets. 
**Marcus Dallacqua** *[21:19]*: Got it. 
**Ken Baugh** *[21:19]*: Okay. 
**Marcus Dallacqua** *[21:21]*: And then. I'm sorry, Sandy, did we already ask. 
**Marcus Dallacqua** *[21:24]*: You for a list of those? 
**Sandra Rudloff** *[21:26]*: Yeah, I sent those over. 
**Marcus Dallacqua** *[21:27]*: Awesome, thank you. 
**Marcus Dallacqua** *[21:29]*: We already talked about sales locations, and we got those in the warehouse locations, vendor categories. Do you guys have categories for your vendors? 
**Sandra Rudloff** *[21:41]*: Kind of. I mean, we have a handful. Just, you know, product versus expense versus labor. 
**Marcus Dallacqua** *[21:47]*: Okay, what about like things like contractor, 1099, contractor, you categorize them that way? 
**Sandra Rudloff** *[21:56]*: I think contractor as a category. I don't know how often we're using it in our vendor setup. 
**Marcus Dallacqua** *[22:02]*: Okay. 
**Ken Baugh** *[22:02]*: I think we would probably want to use that and maybe rethink the way we're doing some of it now. But having that capability I think would be handy. For example, employees are all, you know, we're getting checks to employees for expenses and things like that. You know, employees could be a category of vendor, I guess. I'm not sure how that works in the system, but. 
**Marcus Dallacqua** *[22:33]*: Yeah, yeah, they're contractors. 
**Marcus Dallacqua** *[22:35]*: Yeah, yeah, yep. Okay, great. 
**Marcus Dallacqua** *[22:41]*: Maybe what we'll do then is we'll send you the current list that we have, the default list, because it does. 
**Marcus Dallacqua** *[22:45]*: Drive some of the business processes inside of Orion. 
**Marcus Dallacqua** *[22:49]*: So we'll collaborate and have a quick discussion. If you send us your list, we'll send you our list and then we'll. 
**Marcus Dallacqua** *[22:54]*: Get one of the meetings. The followings will collaborate and have a discussion on that. Great. 
**Marcus Dallacqua** *[23:03]*: I do just want to mention, I'm assuming this is the case in V365, but in some of the other dealers that we've talked to, they don't have this capability. But netsuite by design is an extensible system and it's designed to be personalized. 
**Marcus Dallacqua** *[23:20]*: I'm going to use my personalized word. 
**Marcus Dallacqua** *[23:22]*: In other words, you can create unlimited custom fields. 
**Marcus Dallacqua** *[23:25]*: You can even create custom records and custom transactions. 
**Marcus Dallacqua** *[23:28]*: So just know that if there's data that you need to track on these. 
**Marcus Dallacqua** *[23:32]*: Different types of entities, records or transactions. 
**Marcus Dallacqua** *[23:35]*: You have unlimited ability to track that. Now if you want to track that and report all the way up to the P and L, that is considered a segment. 
**Marcus Dallacqua** *[23:44]*: But as far as custom fields, as many as you want. 
**Marcus Dallacqua** *[23:47]*: Now with that, it's kind of a double edged sword. We kind of always preach caution like don't overwhelm, like you don't want to. 
**Marcus Dallacqua** *[23:54]*: Just create a bunch of custom fields. 
**Marcus Dallacqua** *[23:56]*: Because I can tell you over time those custom fields build up, they get unused and there's maintenance that has to happen. So I've been part of a lot of optimization projects for companies that have been on NetSuite for 10 plus years. 
**Marcus Dallacqua** *[24:10]*: And there's a lot of work to kind of clean things up. 
**Marcus Dallacqua** *[24:12]*: So it's really good to have some. 
**Marcus Dallacqua** *[24:14]*: Processes right at the beginning to make sure that if you are creating custom fields and custom records, it's very intentional. 
**Marcus Dallacqua** *[24:22]*: And there's somebody kind of owning that. In fact, in my company, I had a team of people that managed things. 
**Marcus Dallacqua** *[24:30]*: Like custom fields, custom records, forms. It was our operations team and it was an E commerce business, so it was different. But somebody kind of needs to own all that. 
**Marcus Dallacqua** *[24:41]*: And we've talked a little bit about. 
**Marcus Dallacqua** *[24:43]*: Those NetSuite power users or eventually some type of NetSuite administrator. 
**Marcus Dallacqua** *[24:49]*: And we're going to talk next about roles and permissions. 
**Marcus Dallacqua** *[24:52]*: But that admin or power user is also the one who helps out with roles and permissions. 
**Marcus Dallacqua** *[24:57]*: Because I can just tell you netsuite. 
**Marcus Dallacqua** *[24:59]*: Does a great job of making the permissions granular. 
**Ken Baugh** *[25:02]*: Okay, so I was going to ask. So the typical. I mean, you could control that at the user level in terms of who can personalize what, right? 
**Marcus Dallacqua** *[25:12]*: Yep, yep. 
**Marcus Dallacqua** *[25:14]*: And that's. But whenever you have that level of granularity, it also equals complexity because there's a lot. So permissions in general are just a challenge. So with that, how many roles would. 
**Marcus Dallacqua** *[25:28]*: You say you currently have inside of D365? 
**Sandra Rudloff** *[25:34]*: Quite a lot. And the way it works there is you have to layer rolls on top of a person to get them the right level. So like an order entry person has, you know, order taker, purchasing agent, etc. That's how it kind of works there. 
**Marcus Dallacqua** *[25:51]*: And they have to flip between the roles. 
**Sandra Rudloff** *[25:53]*: No, it's just you keep layering. So like, I have admin, but so say Amanda might actually have 10 roles associated to her, and so that allows her to do all her work. So the problem is they're not very good at telling what each role does. Does. So we had to. Yeah, we had to layer quite a few onto people to make sure they had the right access. And then of course, going taking them away when they change job roles is a challenge. 
**Marcus Dallacqua** *[26:21]*: It is, yeah. 
**Marcus Dallacqua** *[26:23]*: Okay, so as I mentioned Yesterday, we have 25 roles specific to furniture that. 
**Marcus Dallacqua** *[26:27]*: We created with their own permission sets. Guarantee those permission sets will not correspond to how you guys are set up, because they never do. 
**Marcus Dallacqua** *[26:35]*: But we have a baseline. 
**Marcus Dallacqua** *[26:36]*: That we start with. 
**Marcus Dallacqua** *[26:38]*: And it sounds to me like what you have is you have three D365 roles that actually equal what the permission set. 
**Marcus Dallacqua** *[26:47]*: One permission set for somebody, like, they need these three roles to actually be able to. 
**Marcus Dallacqua** *[26:51]*: But so theoretically you could have created one role that would have encompassed all. 
**Marcus Dallacqua** *[26:55]*: Three of those permission sets. 
**Sandra Rudloff** *[26:58]*: We never got into that. 
**Marcus Dallacqua** *[27:00]*: Okay. Okay. 
**Ken Baugh** *[27:01]*: So in the 25 that you have. Those are not layered, I assume. So they're like, in their specific roles. That would encompass multiple functions, but you just define it that way. 
**Marcus Dallacqua** *[27:15]*: Yeah, okay. Yep. Yeah. 
**Marcus Dallacqua** *[27:18]*: And netsuite does allow you to assign. 
**Marcus Dallacqua** *[27:20]*: Multiple roles to one user. The problem is you have to switch between roles and we don't like doing that because every time you switch between roles, your menu system. 
**Marcus Dallacqua** *[27:31]*: Well, your menus don't change. 
**Marcus Dallacqua** *[27:32]*: Sorry. But your dashboards change. 
**Marcus Dallacqua** *[27:35]*: So we have worked really hard to try and create. Here's one role with all the permission. 
**Marcus Dallacqua** *[27:41]*: Sets that this person would need to be able to do their work. 
**Marcus Dallacqua** *[27:46]*: In a lot of NetSuite implementations, we will take a role and we'll copy it and then we'll add a couple. 
**Marcus Dallacqua** *[27:52]*: Permissions, name it something different, and that's now a new role, and that's how we build those out. 
**Marcus Dallacqua** *[27:59]*: Building out those roles and permissions specific to Pivot is. 
**Marcus Dallacqua** *[28:02]*: Is going to be. It's going to take a little bit of work. 
**Marcus Dallacqua** *[28:04]*: Do you have the capability of exporting. 
**Marcus Dallacqua** *[28:08]*: Out the permission sets from D365 per. 
**Marcus Dallacqua** *[28:13]*: Each role and then we can have a larger conversation? 
**Ken Baugh** *[28:17]*: Well, I was wondering if. Because ours are kind of layered, that might be hard, but could you provide us with the 25 that you have and then we could maybe use that as a starting point to. 
**Marcus Dallacqua** *[28:28]*: Yeah. 
**Ken Baugh** *[28:28]*: See if that. I mean, how did you think that would work, Sandy? 
**Sandra Rudloff** *[28:33]*: Yeah, I think that makes sense because they're probably already configured for furniture. So it may not be Project Coordinator, it could be Order Entry, but it's probably the same functions. And I'll take a look. And I was just going to check now if there's a way for me to export that. And, Ted, since it does user Setup, do you know if there's any kind of a matrix or. 
**Ted Lo** *[28:55]*: Well, I remember when we did D365 setup, there was a spreadsheet. I'm actually trying to look to see if that folder is still there. It was on SharePoint. I actually just saw it on SharePoint when we're doing cleaning up last year. And I believe we kept it because I didn't want to delete that. So I'll try to dig for it. 
**Marcus Dallacqua** *[29:24]*: Actually, there's a tool, too. It's called XRM toolbox that is for D365 that lets you export it, but it is a separate tool. 
**Sandra Rudloff** *[29:36]*: And I'm going to share my screen really quick just to see if this is. It's more of. You can see how all the different things. And then this is the, you know, these are the people who have that role. Don't know if I can do it backwards to say, okay, for this person, what all roles does she have? 
**Marcus Dallacqua** *[29:58]*: Oh, okay. 
**Sandra Rudloff** *[30:00]*: So Ted, I guess my question is it that, is this how you assign roles to people? You go through this screen and it's more, you know, you set up a user or take a role and add a user. Or is it you take a user and you add a role. 
**Marcus Dallacqua** *[30:16]*: We. 
**Ted Lo** *[30:19]*: We click into the user, then there are roles that we picked. 
**Marcus Dallacqua** *[30:25]*: Okay. 
**Sandra Rudloff** *[30:26]*: So another question is, can I. And you can see there's quite a lot on here. I'll see if I can export it somehow. 
**Marcus Dallacqua** *[30:35]*: I wonder if the concept of roles, like if you were to click into one of those roles, do those have a permission set? 
**Ted Lo** *[30:45]*: I, yeah, I believe so. I vaguely remember if it's. I don't think it's here, but it's like on another screen because you had. 
**Marcus Dallacqua** *[30:54]*: So many there that almost looked like permissions themselves. 
**Marcus Dallacqua** *[30:58]*: Yeah. 
**Sandra Rudloff** *[30:59]*: It's kind of crazy. 
**Marcus Dallacqua** *[31:01]*: Yeah. 
**Marcus Dallacqua** *[31:02]*: Yeah. I mean, yeah. 
**Marcus Dallacqua** *[31:04]*: In general, roles and permissions are challenging. 
**Marcus Dallacqua** *[31:05]*: That's why I like to have this. 
**Marcus Dallacqua** *[31:07]*: Conversation real early and start the process real early. 
**Sandra Rudloff** *[31:10]*: Okay, I'll see what I can do about exporting. 
**Marcus Dallacqua** *[31:13]*: Okay. 
**Sandra Rudloff** *[31:13]*: No promises, no worries. 
**Marcus Dallacqua** *[31:16]*: In our end, we're going to do the same thing. 
**Marcus Dallacqua** *[31:19]*: I'm going to sneeze, I'm going to turn myself off camera for a second. Hold on. Those roles and permissions are in the follow up email that I sent yesterday as well. Sandy. 
**Marcus Dallacqua** *[31:33]*: Okay. 
**Marcus Dallacqua** *[31:35]*: But not the permissions. 
**Marcus Dallacqua** *[31:36]*: Right? Just the role names. Just the roles. The role names, yeah. Not the permission set. Yeah, but we'll get you the permission set as well. 
**Marcus Dallacqua** *[31:43]*: We've just, we've been tweaking them as we go. 
**Marcus Dallacqua** *[31:45]*: So we'll log into our system to get the most updated permission set. It's a lot to analyze. 
**Marcus Dallacqua** *[31:52]*: Yeah. 
**Ken Baugh** *[31:53]*: Quick question. I'm going backwards a little bit here. I just. Kevin forwarded me the chart of accounts. I was looking at it. Are the account numbers limited to four characters? 
**Marcus Dallacqua** *[32:03]*: Nope, that can be anything you want. 
**Ken Baugh** *[32:05]*: Okay, good. 
**Marcus Dallacqua** *[32:06]*: Thanks. Okay. Yeah. 
**Marcus Dallacqua** *[32:12]*: So an action item for us is to get the most up to date. 
**Marcus Dallacqua** *[32:16]*: Permission set out of Netsuite and we'll send that to Sandy for analysis. 
**Marcus Dallacqua** *[32:25]*: We used to have this big, huge. 
**Marcus Dallacqua** *[32:26]*: Spreadsheet with all of the roles and permission sets. It's overwhelming. We're gonna try, we'll figure out some way to try and make it a little bit easier. 
**Marcus Dallacqua** *[32:34]*: But this is one of Those topics where it's like, oh, boy, that's a hard one. You know, so we'll have to. We'll tackle it early and give ourselves some time. A couple other things, too. Do you. Do you ever limit or restrict access based on locations? 
**Marcus Dallacqua** *[32:57]*: No. 
**Marcus Dallacqua** *[32:59]*: Okay. 
**Marcus Dallacqua** *[33:02]*: Or divisions, or what we call divisions, like business units. Doesn't sound like you're doing any of that. 
**Marcus Dallacqua** *[33:07]*: Okay. 
**Marcus Dallacqua** *[33:08]*: Any need to do that? We have it available. 
**Sandra Rudloff** *[33:11]*: I can't imagine. 
**Ken Baugh** *[33:15]*: Maybe. Let's hold that thought. I mean, I guess I'm just thinking. 
**Sandra Rudloff** *[33:18]*: Of. 
**Ken Baugh** *[33:20]*: You know, like, if we have a division for our service operations, do they need to have access to. I don't know. I mean, I. I think that's something we have to look at. 
**Marcus Dallacqua** *[33:31]*: Yep. 
**Sandra Rudloff** *[33:32]*: Can all these permissions have read only as an. An option? Because, like what Ken mentioned, you know, maybe Service Ops needs to look at all orders placed, but we don't necessarily want them to modify all orders. 
**Marcus Dallacqua** *[33:46]*: Yeah, yeah, you have. Yeah, you have View. So it's. 
**Marcus Dallacqua** *[33:51]*: View would be the same as read only, View, edit, create and delete. 
**Sandra Rudloff** *[33:56]*: And you can do that at the division level. So I'm in Division 50. I can only edit mine, but I can't edit someone in Division 20. An order under Division 20. 
**Marcus Dallacqua** *[34:10]*: I'll have to check on that. I don't think it works that way. I think it's. Yeah, I think it works more like I have View permission across the board. 
**Marcus Dallacqua** *[34:23]*: And then if you restrict me by division, I can't even see anything in that division. It's kind of. It's more of an all or nothing at that point. 
**Marcus Dallacqua** *[34:31]*: Now, we've done a lot in the past where you can take it to the next level. 
**Marcus Dallacqua** *[34:36]*: Like, if you have some really unique permissions that NetSuite doesn't cover natively, we can create workflows that can govern those permissions. So if you do run in anything that you need, we can. We can accommodate. I'm just thinking right now kind of natively, what netsuite has out of the box and how it works. All right. 
**Marcus Dallacqua** *[35:02]*: I mentioned this a little bit ago, but vendor management, 1099 tracking, we're going to get you the categories, but do you send out of D365? Do you send the 1099 invoice information to your contractors? 
**Marcus Dallacqua** *[35:19]*: Yeah. 
**Sandra Rudloff** *[35:19]*: Connie, you want to talk about. 
**Connie Chung** *[35:22]*: Yes. I think we download based on what we set up in the vendor setup. If they require 1099, then we download just that portion and send it to the third party to do the 1099 return for us. The Beginning of the year. Yes. 
**Marcus Dallacqua** *[35:40]*: Got it. 
**Marcus Dallacqua** *[35:41]*: Okay, so you're doing that right through D365. 
**Marcus Dallacqua** *[35:45]*: All right. 
**Marcus Dallacqua** *[35:46]*: Yeah, we do have a method for tracking that in the report that you. 
**Marcus Dallacqua** *[35:49]*: Can send out or a report that generates. You can send out the information from that. 
**Marcus Dallacqua** *[35:53]*: So sort of make note of that. And then we already talked about the item master data classification set up yesterday. We talked about conceptually how the item catalog is significantly smaller. 
**Marcus Dallacqua** *[36:07]*: We're looking at somewhere between 30 and 50 items. 
**Marcus Dallacqua** *[36:10]*: Those items get reused. We have other ways of making sure. 
**Marcus Dallacqua** *[36:14]*: That the information on the transactions are unique, including option code, option description, UUID and lot numbers. 
**Marcus Dallacqua** *[36:21]*: So we unique ify if that's a word. We unique ify the heck out of every item, make sure that it's unique. And then really the item master, it's really all about what GL account do. 
**Marcus Dallacqua** *[36:31]*: You want that item to post to? That's really what it comes down to. And if it's taxable or not. 
**Marcus Dallacqua** *[36:38]*: So we have to do some things there. So maybe talk a little bit more about the item. The process that we have right now is we have the catalog code manager. 
**Marcus Dallacqua** *[36:47]*: Utility inside of Orion. 
**Marcus Dallacqua** *[36:50]*: So we have this utility and we load in as part of the initial installation of orion. 
**Marcus Dallacqua** *[36:59]*: It's about 300 vendors. 
**Marcus Dallacqua** *[37:01]*: And we got this vendor list specifically from Solomon Coil. And we're identifying these vendors and these vendors then get associated with your catalog codes. Now one thing we need to do is when you bring, we bring in. 
**Marcus Dallacqua** *[37:14]*: Your vendor list from D365, we have. 
**Marcus Dallacqua** *[37:17]*: To make some mapping because the default vendor list that we have from Solomon. 
**Marcus Dallacqua** *[37:23]*: Coil might not include Ink, but yours does, or there might be something that differentiates. 
**Marcus Dallacqua** *[37:29]*: So the likelihood that the names match. 
**Marcus Dallacqua** *[37:31]*: Exactly is going to be very low. 
**Marcus Dallacqua** *[37:34]*: So we have to make some. We have to be a little bit. 
**Marcus Dallacqua** *[37:36]*: Careful when we're doing that data migration. Make sure we're not creating duplicates because some of those will already exist. 
**Marcus Dallacqua** *[37:43]*: But the benefit is then you have that information inside of Orion that says, here's the vendor, here's all the catalog codes for this vendor, and. 
**Marcus Dallacqua** *[37:51]*: Here is the default item for this vendor. 
**Marcus Dallacqua** *[37:54]*: So when you do your import of your SIF file or what any other file type they might be using, whether. 
**Marcus Dallacqua** *[38:01]*: And we'll talk more about SIF files, what types you're using. 
**Marcus Dallacqua** *[38:03]*: But when you do your SIF import file, we say, oh, okay, here's the catalog code, here's the vendor, but here's also the item. 
**Marcus Dallacqua** *[38:12]*: So we're helping you find the appropriate Item as well. 
**Marcus Dallacqua** *[38:15]*: So that's from a high level. 
**Marcus Dallacqua** *[38:17]*: That's how that's working for my benefit. 
**Ken Baugh** *[38:19]*: Because I missed that yesterday. What is the item specifically? Is that like. I mean, you said you have like 30, 35. Would that be like a chair, a task chair? Would that be an item or. 
**Marcus Dallacqua** *[38:32]*: It's actually even more generic than that. 
**Marcus Dallacqua** *[38:34]*: It's. 
**Marcus Dallacqua** *[38:35]*: It really comes down to this. 
**Marcus Dallacqua** *[38:37]*: The. 
**Marcus Dallacqua** *[38:37]*: The GL account you want the product to post to. So, like our items. Right now we have Herman Miller furniture. 
**Marcus Dallacqua** *[38:44]*: Yeah. 
**Marcus Dallacqua** *[38:45]*: Or other furniture. 
**Ken Baugh** *[38:47]*: Because, I mean, yeah. One thing I've wanted to have. We don't have it is, you know, if we wanted to see for last year, how many lateral files we sold or height adjustable tables or task chairs, we don't really get that because. And I think the constraint there is in cap probably correct, Sandy, because there's not a field in there for that. And so we. We can't import that in. But that would be a great analytical tool for us to have is just, you know, how many. How many conference tables did we sell last year? I have no idea. 
**Marcus Dallacqua** *[39:23]*: Right. Is it. 
**Marcus Dallacqua** *[39:25]*: Is there any. Anything in the CIF file that would identify that? 
**Marcus Dallacqua** *[39:30]*: Because we can capture anything from the. 
**Sandra Rudloff** *[39:31]*: CIF file only if we have it as a tag or an alias. 
**Marcus Dallacqua** *[39:36]*: Okay. 
**Sandra Rudloff** *[39:38]*: But it's also the generic code. Well, the Herman Miller generic code is great, but it's obviously only, you know, portion of our sale. So if we're doing other vendors, they're not going to have a generic code that would map to it. 
**Marcus Dallacqua** *[39:52]*: So it would be a little extra. 
**Marcus Dallacqua** *[39:53]*: Work for your team. 
**Marcus Dallacqua** *[39:55]*: But if they do put it into a specific tag, if we segmented a certain tag, just so you know, we. We give you the ability to do. 
**Marcus Dallacqua** *[40:03]*: Custom groups in this, in the smart table. 
**Marcus Dallacqua** *[40:06]*: So you're not just limited to those. 
**Marcus Dallacqua** *[40:08]*: Tags for doing things like PO splitting. 
**Marcus Dallacqua** *[40:10]*: And. 
**Marcus Dallacqua** *[40:12]*: Invoicing and things like that. 
**Marcus Dallacqua** *[40:14]*: So we give you unlimited. Unlimited custom tags or custom groups, really. So, but if you were to say, let's. Let's say tag three is going to. 
**Marcus Dallacqua** *[40:23]*: Be just for grouping by these, if. 
**Marcus Dallacqua** *[40:25]*: You want to call them families or. 
**Marcus Dallacqua** *[40:26]*: Whatever you want to call them, we can bring that into NetSuite and build reports around all that. 
**Marcus Dallacqua** *[40:39]*: Okay. 
**Marcus Dallacqua** *[40:40]*: So Item master. So I just kind of did that quick review of how the item is interacting with that catalog code manager utility. Do you have something like that currently? 
**Sandra Rudloff** *[40:48]*: Right now, that's exactly what we do. In fact, let me share real quick. Just. Yeah, so we're on the same page. So obviously our CAP codes, the Vendor name. And then here, the item groups is where we start to say, okay, ancillary. Go down to null or something. We've got, you know, null. We do have to break out freight differently because of taxation rules within here. But yeah, pretty much we just go through. We say, you know, everything we do is an item. We don't do hourly. You know, these are the categories, whether or not it's a billable item. And this new site warehouse, like I mentioned, where we have to create an individual warehouse for every item. 
**Marcus Dallacqua** *[41:38]*: Yeah, it's. 
**Sandra Rudloff** *[41:39]*: It works. It sounds pretty much same thing that you're talking about. 
**Marcus Dallacqua** *[41:45]*: Well, you have a little bit. 
**Ken Baugh** *[41:47]*: We're not going to have to create that in visual warehouse. 
**Sandra Rudloff** *[41:50]*: No, yeah, that was. 
**Marcus Dallacqua** *[41:53]*: Yeah. 
**Sandra Rudloff** *[41:53]*: Just strictly part of D365. But, you know, one of the things is if we go here to like the categories, these are the ones we currently have, which are probably, you know, not a huge amount. 
**Marcus Dallacqua** *[42:10]*: Which we'll have. 
**Sandra Rudloff** *[42:11]*: To see if we want to break it up more like, you know, one of the changes we made was we wanted to track intermarket sales versus just subcontract sales. Do we want to do any more groupings like that? So these do. Map then to the GL codes that I sent you. 
**Marcus Dallacqua** *[42:27]*: Okay. 
**Marcus Dallacqua** *[42:29]*: All right, so a couple things to consider here. You're the first dealer that we ran into that has anything more than what we already have. But I want you to know that the catalog code utility that we have, we can additional columns in the table and track all kinds of information. So I think what we would need here is if you don't mind sending us either a screenshot or a CSV. 
**Marcus Dallacqua** *[42:55]*: Export of this and then let us. 
**Marcus Dallacqua** *[42:58]*: Know if there's any columns that you don't need anymore. 
**Marcus Dallacqua** *[43:00]*: Or maybe. 
**Marcus Dallacqua** *[43:02]*: And maybe if you don't mind just. 
**Marcus Dallacqua** *[43:04]*: Doing a quick definition for each column. 
**Yuridia Silvas** *[43:06]*: Sure. 
**Marcus Dallacqua** *[43:06]*: And how it's used. And if you need it or not, I assume you need everything. So the exception would be if you. 
**Marcus Dallacqua** *[43:12]*: Don'T need it anymore. 
**Marcus Dallacqua** *[43:15]*: The other thing I wanted to ask is because we did have this request recently, was from a contract standpoint and discounting standpoint, would it be helpful to track any of that information here? 
**Sandra Rudloff** *[43:32]*: Contract info. Not sure what you mean, like contract numbers? 
**Marcus Dallacqua** *[43:38]*: Yeah, either the contract numbers or the discount percentages. 
**Sandra Rudloff** *[43:44]*: Well, I mean, obviously it wouldn't work with Miller Noel because of all their contracts and even with other vendors, I. I'd be worried. I mean, the capped spec would rule all. I mean, is it if we didn't have a discount There would be a default. 
**Marcus Dallacqua** *[43:59]*: Yeah, yeah, okay, exactly. 
**Marcus Dallacqua** *[44:01]*: It would be like a default discount. Something to consider. Somebody brought it up. 
**Marcus Dallacqua** *[44:07]*: It was a dealer. 
**Marcus Dallacqua** *[44:07]*: So. 
**Marcus Dallacqua** *[44:10]*: Something we could. We could easily. I mean, basically it's just a table with. 
**Marcus Dallacqua** *[44:13]*: You put data in it. So it's like, it's pretty basic, but something to consider. 
**Marcus Dallacqua** *[44:21]*: Okay, great. So another action item to Sandy is. 
**Marcus Dallacqua** *[44:23]*: Going to be the. 
**Marcus Dallacqua** *[44:24]*: What do you guys call that table? 
**Sandra Rudloff** *[44:27]*: Vendor cross reference. 
**Marcus Dallacqua** *[44:28]*: Vendor cross reference. Okay, so the data from the vendor. 
**Marcus Dallacqua** *[44:31]*: Cross reference, we're going to take that. 
**Marcus Dallacqua** *[44:32]*: We'Re going to map it to our. 
**Marcus Dallacqua** *[44:35]*: Catalog code manager and discuss potentially adding. 
**Marcus Dallacqua** *[44:39]*: More columns of information into our catalog code manager to continue tracking that same information. 
**Sandra Rudloff** *[44:44]*: And I guess, Ken, do you want to look at, you know, expanding any of these categories? Again, it's mostly for mapping to the gl. I don't know if you want to break things out more than we already do or get rid of them. 
**Ken Baugh** *[44:59]*: Yeah, I mean, that's what I was just thinking. We may want to try to streamline it a little more, but it's good to know what the capabilities are and the options and then we can decide how we want. 
**Sandra Rudloff** *[45:15]*: When I do the export of the categories, I'll go ahead and CC you and Kevin in on it so you can take a look at the. A lot of them we aren't even using. So I think it just. We need to do some tidying. 
**Marcus Dallacqua** *[45:26]*: Okay. Yeah. Okay. 
**Marcus Dallacqua** *[45:31]*: I'm just going through my list here. I want to make sure I cover everything. 
**Marcus Dallacqua** *[45:38]*: We're getting closer to data migration. Let's talk about taxes for a moment. I know you're currently working with Avalara. We have some time today so we. 
**Marcus Dallacqua** *[45:49]*: Can go into a deeper discussion about taxes. 
**Marcus Dallacqua** *[45:51]*: So we introduced the idea of you have Avalara, but you also have Sweetax available to you. Suite tax is NetSuite's tax platform. It does tax calculation. It itemizes it all the way down to the municipality. It also does tax exempt certificate management. So you load in, you create the record, you load in the tax exempt certificate, and then any other transaction for. 
**Marcus Dallacqua** *[46:20]*: That client is tax exempt. 
**Marcus Dallacqua** *[46:23]*: NetSuite gives you the ability to override taxes using Sweet Tax. So what I would consider basic tax functionality. 
**Marcus Dallacqua** *[46:35]*: It's good. 
**Marcus Dallacqua** *[46:36]*: Avalara is kind of the gold standard, right. They have more sophisticated tax calculation rules than what Sweet Tax is going to have. They have the automation for tracking things like economic nexus, tax registration, tax filing. 
**Marcus Dallacqua** *[46:51]*: It's a service and that's really what you're paying for, is the service. 
**Marcus Dallacqua** *[46:56]*: Personally, I've used both. Personally, I've brought people on Avalara and I've taken people off Avalara and bought them on the Sweet Tax. 
**Marcus Dallacqua** *[47:03]*: It really just kind of comes down to what is going to work best for your organization. 
**Marcus Dallacqua** *[47:08]*: I can also tell you that depending on your tax jurisdictions and how finicky they are, Avalara has done a good job of creating these kind of custom tax rules that help govern some of that where Sweet Tax is not that sophisticated. So I've run into this in like we had an E commerce company and they were selling into Alabama and there was a specific place in Alabama that was for like a year giving tax breaks. Like no tax charge on E Commerce. 
**Marcus Dallacqua** *[47:41]*: Being shipped to that particular part of Alabama. 
**Marcus Dallacqua** *[47:44]*: Well, Avalara is going to track things. 
**Marcus Dallacqua** *[47:47]*: Like that and Sweet Tax is not going to track things like that. 
**Marcus Dallacqua** *[47:51]*: So depending on your business needs, Avalara. 
**Marcus Dallacqua** *[47:54]*: Might be the best decision for you. 
**Marcus Dallacqua** *[47:58]*: So with all that being said, talk to me a little bit about your experience with Avalara. Are you happy? How's their service? 
**Marcus Dallacqua** *[48:07]*: Yeah, we've been pretty happy. 
**Sandra Rudloff** *[48:08]*: I mean there have been a couple glitches where they didn't file for some reason. We collect for 37 states. 
**Marcus Dallacqua** *[48:16]*: Okay. 
**Sandra Rudloff** *[48:16]*: So there's quite a lot of returns to do. Obviously the bulk's California, but quite a lot other than that. I mean it's been really helpful when we've had our California sales tax audits, which one will be probably coming up next year, to be able to pull that information out easily because you know, they did want it at the line item level and to do their own analysis. I'd say overall, I think from what I've seen, pretty happy for the calculations and everything else. There have been some hiccups with the connectors through D365 and installing new connectors has been a pain. We've had to use our consultants to basically do it in test, debug and then production. So I don't know if you know, you have a connector that we have to update frequently or is it just a different connection with Avalara? 
**Marcus Dallacqua** *[49:13]*: Yeah, it's a suite up that gets installed and there's two versions of the suite app. 
**Marcus Dallacqua** *[49:19]*: One is being deprecated. Like there was like this full fledged. 
**Marcus Dallacqua** *[49:23]*: Avalara suite app and they had their. 
**Marcus Dallacqua** *[49:25]*: Own tab at the top of Netsuite. 
**Marcus Dallacqua** *[49:27]*: And it's kind of, in my opinion it was kind of just like its. 
**Marcus Dallacqua** *[49:31]*: Tentacles were everywhere inside in that suite. 
**Marcus Dallacqua** *[49:34]*: The new version now you actually have. 
**Marcus Dallacqua** *[49:36]*: The suite tax platform there's two pieces to suite tax. It's the platform and there's an engine. 
**Marcus Dallacqua** *[49:41]*: And so now you always have the suite tax platform but you can plug. 
**Marcus Dallacqua** *[49:45]*: In different engines and Avalara is now a tax calculation engine. 
**Marcus Dallacqua** *[49:49]*: So it's a little bit cleaner now and a little bit easier and really. 
**Marcus Dallacqua** *[49:52]*: It'S just a matter of you're using. 
**Marcus Dallacqua** *[49:55]*: Something sending information out of Alera to. 
**Marcus Dallacqua** *[49:57]*: Do the tax calculations and then the information comes back. 
**Sandra Rudloff** *[50:00]*: I do want to ask Connie something because in D365 we only have one sales tax account however. So I would think Connie, reconciliation can be tough if you find a discrepancy to go state by state to find that discrepancy. Does NetSuite also have just a single tax, sales tax, or can you have it by state for easier reconciliation? 
**Marcus Dallacqua** *[50:23]*: It's automatically by state. 
**Marcus Dallacqua** *[50:25]*: Nice. 
**Marcus Dallacqua** *[50:25]*: So whenever you set up a nexus. 
**Marcus Dallacqua** *[50:27]*: Inside of NetSuite it automatically creates a GL account for that state. 
**Sandra Rudloff** *[50:31]*: So Connie, what other challenges have you had with Avalara or Kevin? 
**Connie Chung** *[50:38]*: So every month when I do the Celtic reconciliation, I haven't had any issue because basically I just kind of compare download all the transaction. If the transaction match then I'm good. I don't go by the state level. The state level would I only review the summary of this payment now what is the variant like Washington occupancy, those kind of detail level so far. So I don't think necessary we do it set up by the state. It might be more complex when you set up or know Sandy when you do the building if you set up by the state. 
**Marcus Dallacqua** *[51:25]*: Well, it wouldn't. 
**Sandra Rudloff** *[51:26]*: I don't think, I don't think it'll make an impact on. It'll just be. It's probably just based on, you know the calculation that we get back from Avalara. So yeah, I don't think it'd be any more work for us. 
**Marcus Dallacqua** *[51:43]*: Okay. 
**Marcus Dallacqua** *[51:44]*: Just more granularity in the reporting and yeah. Because everything posts automatically to it. 
**Connie Chung** *[51:55]*: Have a think about it. Seti Would it be easy if we set up by this day that I don't have to worry about going to the Avalara and do the vlookup between the two report. So that would be the question we have to get back. But the more I think about it, probably set up by individual state might be easier to do comparison between the two report next week with the Avalara. 
**Marcus Dallacqua** *[52:28]*: Okay. 
**Marcus Dallacqua** *[52:29]*: So it sounds like Avalara is working well for you and doesn't sound like there's A compelling reason to try and. 
**Marcus Dallacqua** *[52:36]*: Move away from it. 
**Sandra Rudloff** *[52:38]*: Yeah, moving away would be an impact because obviously we'll have to file our own returns payments. It would be with 37 states. Some are quarterly, annually. 
**Marcus Dallacqua** *[52:51]*: Yeah. 
**Connie Chung** *[52:52]*: And some state that we're not talking about. Very aggressive, like Washington state. Some state that we do further return as the detail level, like district, county. So I don't know next. We have capability for doing that right now. We still have. 
**Marcus Dallacqua** *[53:11]*: Yeah, it does, but I'm sure Avalara. 
**Marcus Dallacqua** *[53:16]*: Has that as well. 
**Connie Chung** *[53:17]*: Right, Avalarius? 
**Marcus Dallacqua** *[53:20]*: Yeah. Yep. 
**Marcus Dallacqua** *[53:23]*: Okay. 
**Connie Chung** *[53:23]*: We talked about tax. Can we go back to 1099 a little bit? Do we have capability that we have all the data in the nets with? We can just export and then file return on our own. Because I think 1099 should be very straightforward so we don't have to rely on the third party file the return for us. 
**Marcus Dallacqua** *[53:44]*: You know, I'm thinking about doing our. 
**Connie Chung** *[53:46]*: Own, like all the. We have all the data, we can send it to the vendor. 1099. 
**Marcus Dallacqua** *[53:54]*: Yeah, I have to check on that. 
**Marcus Dallacqua** *[53:55]*: Maybe. 
**Marcus Dallacqua** *[53:55]*: Debbie, if we can just make a note. We have it on the transcript too, but we'll get you some documentation on the functionality around a 1099. I know it's changed a few times over the years. 
**Marcus Dallacqua** *[54:07]*: Yeah. 
**Marcus Dallacqua** *[54:07]*: So we'll work on getting that for you. 
**Marcus Dallacqua** *[54:10]*: Okay, I got it. 
**Marcus Dallacqua** *[54:11]*: Thank you. 
**Connie Chung** *[54:12]*: Thank you. 
**Marcus Dallacqua** *[54:14]*: Welcome. 
**Marcus Dallacqua** *[54:16]*: So are we at the point? Are we making our first decision here as far as. Are we at the point? We talked about a lot of things that we already make in our first decision in regards to Avalara. We're going to keep it. 
**Ken Baugh** *[54:26]*: Yeah, I think it makes sense to stick with it just given the nature of the number of states we deal with and the service part of it is. Has been helpful. 
**Marcus Dallacqua** *[54:38]*: Good, good. 
**Marcus Dallacqua** *[54:40]*: All right, so what I'll do is I will engage Avalara. We have a. 
**Marcus Dallacqua** *[54:47]*: We're a partner. 
**Marcus Dallacqua** *[54:48]*: We're an Avalara partner because we'll have. 
**Marcus Dallacqua** *[54:50]*: To work with them to do the migration and get you guys set up for NetSuite. 
**Marcus Dallacqua** *[54:53]*: But hey, that's the first decision of hundreds that we'll be making over the. 
**Marcus Dallacqua** *[55:00]*: Next number of months. 
**Marcus Dallacqua** *[55:01]*: So congratulations to us. 
**Marcus Dallacqua** *[55:05]*: All right. 
**Marcus Dallacqua** *[55:06]*: And we are just coming up to the top of the hour. Maybe now's a good time to take. 
**Marcus Dallacqua** *[55:10]*: A quick five minute break and then. 
**Marcus Dallacqua** *[55:12]*: We'Ll come back in five minutes and we'll pick up and start talking about a big topic, data migration. 
**Marcus Dallacqua** *[55:20]*: Okay. 
**Marcus Dallacqua** *[55:21]*: All right, see you guys in a couple minutes. 
**Brian Hagerty** *[01:00:01]*: Just walked through a cobweb in the office, nothing wakes you up like that. 
**Sandra Rudloff** *[01:00:08]*: Did we get a good scream out of you? 
**Brian Hagerty** *[01:00:11]*: No, no scream. Just rubbed my face about 753 times. 
**Sandra Rudloff** *[01:00:17]*: It would have screamed. 
**Marcus Dallacqua** *[01:00:18]*: Yeah. 
**Marcus Dallacqua** *[01:00:26]*: We'Re waiting for everybody to come back. I just, I posted a link in the chat to NetSuite's public documentation. It was only recently that they made this public. 
**Marcus Dallacqua** *[01:00:37]*: Recently a few years back, but used. 
**Marcus Dallacqua** *[01:00:40]*: To be had to be logged into NetSuite to have access to this, but now you have complete access to this. So feel free to go to that. 
**Marcus Dallacqua** *[01:00:51]*: Help center if you have any questions about Netsuite. 
**Marcus Dallacqua** *[01:00:54]*: I was looking at stuff as were talking 1099 and look at that documentation. But you have full access to that. Just keep in mind that we're using about. It's kind of 50. We're using 50% Netsuite and 50% Orion. So like if you were to look up projects inside of the NetSuite Help center, they're going to talk to you a lot about suite projects and stuff like that. 
**Marcus Dallacqua** *[01:01:17]*: We're not even using that. We're using our own project record that's specific to furniture. 
**Marcus Dallacqua** *[01:01:20]*: So just be aware as you get further into the project, you'll be able to start figuring out what. 
**Marcus Dallacqua** *[01:01:27]*: Is netsuite and what's Orion. 
**Marcus Dallacqua** *[01:01:28]*: Because they're kind of, they're intermixed, kind of intertwined. And we do that for a good. 
**Marcus Dallacqua** *[01:01:33]*: Reason too, because we, when we do that, we Inherit all of NetSuite's security practices and all that. So we wanted to do that. 
**Marcus Dallacqua** *[01:01:40]*: But feel free to go crazy in there. 
**Marcus Dallacqua** *[01:01:42]*: There's videos, release notes, all kinds of stuff. 
**Marcus Dallacqua** *[01:01:47]*: Sandy, quick question for you. Kind of a side note question as everybody's coming back because of your company size, do you have a specific tier. 
**Marcus Dallacqua** *[01:01:58]*: Or edition of D365 that you're on. 
**Marcus Dallacqua** *[01:02:02]*: From a performance standpoint? 
**Sandra Rudloff** *[01:02:05]*: I guess I don't get the question. An additional tier. 
**Marcus Dallacqua** *[01:02:09]*: Yeah. Because D365 is hosted in the cloud. 
**Marcus Dallacqua** *[01:02:13]*: Correct. 
**Marcus Dallacqua** *[01:02:15]*: Well, this is what I'm curious about. So netsuite has tiers for different size companies. And so you guys are in like. 
**Marcus Dallacqua** *[01:02:25]*: That premium performance tier because of just the number of employees and the number of traffic transactions that you're going to have on a yearly basis. 
**Marcus Dallacqua** *[01:02:33]*: Does D365 have anything like that or. 
**Marcus Dallacqua** *[01:02:35]*: Is it just one size fits all type thing? 
**Sandra Rudloff** *[01:02:38]*: I think it's really just. 
**Marcus Dallacqua** *[01:02:39]*: Yeah. 
**Sandra Rudloff** *[01:02:39]*: By users, but I don't think it has anything to do with performance. 
**Marcus Dallacqua** *[01:02:43]*: Okay. 
**Ted Lo** *[01:02:44]*: It's pretty much one size. One size. 
**Marcus Dallacqua** *[01:02:47]*: Okay. Got It. 
**Marcus Dallacqua** *[01:02:48]*: Yeah, I think. I think netsuite did a few of these things back with the Oracle acquisition. 
**Marcus Dallacqua** *[01:02:53]*: To actually reduce the price for smaller companies. 
**Marcus Dallacqua** *[01:02:58]*: So there's things like that. 
**Marcus Dallacqua** *[01:03:00]*: So I'm just curious if. 
**Marcus Dallacqua** *[01:03:03]*: You guys just to note, you are on the premium tier. That gives you better performance, but also. 
**Marcus Dallacqua** *[01:03:10]*: Gives you more. 
**Marcus Dallacqua** *[01:03:12]*: Integration capabilities, script queues, like, everything kind of under the hood. 
**Marcus Dallacqua** *[01:03:17]*: Runs a little bit better just based. 
**Ken Baugh** *[01:03:20]*: On the user count we have. 
**Marcus Dallacqua** *[01:03:23]*: Yeah, it's. There's like four factors that would push you into that next tier, and one of those factors is 100 employees, 100 users. 
**Marcus Dallacqua** *[01:03:31]*: Yeah. 
**Marcus Dallacqua** *[01:03:32]*: Another one would be the number of transaction lines that you have, which every. 
**Marcus Dallacqua** *[01:03:37]*: Furniture dealer has a lot. So, yeah, once you get to your size, you for sure push there. 
**Marcus Dallacqua** *[01:03:45]*: All right, next topic, and it's a big one, is data migration. I know we've had this conversation a few times today. We'll get everybody caught up to speed on data migration. 
**Marcus Dallacqua** *[01:03:58]*: We'll go a little bit deeper today. We have an hour so we could talk more in depth about it. 
**Marcus Dallacqua** *[01:04:07]*: Talk to me first, Sandy, about the. 
**Marcus Dallacqua** *[01:04:09]*: Data warehouse and how you guys have that set up and how you're leveraging it. 
**Sandra Rudloff** *[01:04:13]*: We don't export everything into it. It's mostly, we think, definitely everything around orders, customers, vendors, trying to think. And Kevin, you might know, did we export the. We did export the GL details, right? 
**Kevin Baugh** *[01:04:32]*: Yes. 
**Marcus Dallacqua** *[01:04:33]*: Okay. Yeah. 
**Sandra Rudloff** *[01:04:35]*: So what we don't have what. We don't export things like, you know, AR cache posting or vendor check data, that sort of thing. And part of it was size limitations. And you do. We do suffer performance issues for our orders. We refresh those every hour and for about five minutes at the top of the hour, the system is slower. The bigger transactions, like GL invoicing, that sort of thing, we do one nightly, one time. So the. The order information's current within an hour. Everything else is within 24 hours. 
**Marcus Dallacqua** *[01:05:19]*: What's the primary purpose of the data warehouse? 
**Sandra Rudloff** *[01:05:22]*: Reporting? Kevin is our power bi guru. He's created a ton of gorgeous reports. I do good old business objects, crystal reports, where we have status reports and customer reports for our clients that are emailed out on the schedule. 
**Marcus Dallacqua** *[01:05:40]*: Okay, gotcha. 
**Marcus Dallacqua** *[01:05:44]*: So I'm just trying to wrap my mind around. So the data warehouse at the top. 
**Marcus Dallacqua** *[01:05:48]*: Of the hour, it's doing a big export to the data warehouse to make sure the information synced. 
**Marcus Dallacqua** *[01:05:53]*: Yeah. 
**Marcus Dallacqua** *[01:05:54]*: Okay, so D365 is always real time. 
**Marcus Dallacqua** *[01:05:57]*: It's. 
**Marcus Dallacqua** *[01:05:57]*: It's the. 
**Marcus Dallacqua** *[01:05:58]*: The data warehouse that's getting updated on the hour. 
**Sandra Rudloff** *[01:06:01]*: Right. 
**Marcus Dallacqua** *[01:06:01]*: Got it. 
**Marcus Dallacqua** *[01:06:04]*: Then the primary purpose of that is so you have all the. 
**Marcus Dallacqua** *[01:06:06]*: Information accessible for Power bi. 
**Marcus Dallacqua** *[01:06:09]*: So you probably have dashboards and reports in Power bi. 
**Kevin Baugh** *[01:06:14]*: Yeah, we love the customization piece of it. I've actually created a number of tables that we're not exporting through D365, just using Alteryx. I'm going in, pulling data, we're blending stuff. I'm creating custom tables that have enabled certain types of reports and views that we didn't have before. So and that's one thing for me is like, can we access the back end data here? Can we create our own tables in this environment? Certainly. I would venture to say the out of the box solution isn't going to cover everything that we like to look at. Maybe it will, I don't know. But having the ability to, you know, tap into it, create tables, blend data, et cetera would be fantastic for us. 
**Marcus Dallacqua** *[01:06:52]*: Yeah, yeah. 
**Marcus Dallacqua** *[01:06:53]*: So there's a number of ways to get the data out. I mean I think that the. They still even have ODBC drivers available. 
**Marcus Dallacqua** *[01:07:01]*: To get the data out and there. 
**Marcus Dallacqua** *[01:07:04]*: Is a Data warehouse that NetSuite provides. 
**Marcus Dallacqua** *[01:07:07]*: At additional cost and so there's a. 
**Marcus Dallacqua** *[01:07:10]*: Few options other than that too. We also have the ability to get. 
**Marcus Dallacqua** *[01:07:16]*: Things out via scripting. We do a lot of that where we're going to just extract information using. We have web services and things like that. 
**Marcus Dallacqua** *[01:07:26]*: So. 
**Marcus Dallacqua** *[01:07:29]*: But it's. 
**Marcus Dallacqua** *[01:07:29]*: So I think what it sounds like you want to continue doing that same thing, right? Because you want to have the ability. 
**Marcus Dallacqua** *[01:07:34]*: To use Power BI specifically to do the reporting. 
**Kevin Baugh** *[01:07:39]*: We really like Power bi. Tableau is great, but I mean Power BI is fantastic. We're Microsoft customers, right. We're going to keep using Office and I know based on the demos I've seen there are some native charts and whatever within the NetSuite platform. But again, I, I don't know, maybe a question for Ken and Danny, but I really like having the ability to pull stuff out and do stuff in Power bi. 
**Marcus Dallacqua** *[01:08:03]*: So that would be great. 
**Ken Baugh** *[01:08:04]*: I guess it really kind of depends on how robust the reporting is within native netsuite. I don't really know that, but I'm guessing it probably isn't as robust as we want. And that's my guess. 
**Marcus Dallacqua** *[01:08:21]*: Yeah. 
**Marcus Dallacqua** *[01:08:21]*: I think there's two things to consider there. 
**Marcus Dallacqua** *[01:08:24]*: The reporting is robust, the visualization is not as robust as what you're going to get in Power bi. 
**Marcus Dallacqua** *[01:08:30]*: The other thing in Power BI is the ability to control and like what. 
**Marcus Dallacqua** *[01:08:36]*: You'Re doing is creating your own tables. 
**Marcus Dallacqua** *[01:08:38]*: From blended Data and things like that. What that allows you to do is take the need of having a developer. 
**Marcus Dallacqua** *[01:08:47]*: To do all of that in NetSuite or working with NetSuite and you're able to do that all yourself in Power Bi. 
**Marcus Dallacqua** *[01:08:54]*: So I could definitely see the advantage. 
**Marcus Dallacqua** *[01:08:56]*: To continuing to do what you do. 
**Marcus Dallacqua** *[01:09:01]*: Really the question is going to be what's the best method of getting the. 
**Marcus Dallacqua** *[01:09:03]*: Information out of NetSuite into your current data warehouse? 
**Marcus Dallacqua** *[01:09:07]*: Because I imagine you're going to keep. 
**Marcus Dallacqua** *[01:09:08]*: The current data warehouse. 
**Sandra Rudloff** *[01:09:11]*: That's a great question. 
**Marcus Dallacqua** *[01:09:12]*: Ted. 
**Sandra Rudloff** *[01:09:13]*: Will have to get involved with it. What, as far as what makes the most sense? I don't know if we want. 
**Ken Baugh** *[01:09:18]*: We certainly want to be able to retain the data. I mean the data. So whether we convert the data to a new data warehouse or keep the existing one, I guess that would be a question. 
**Kevin Baugh** *[01:09:29]*: That's a pretty simple process for me. I've done this with all of our old data, Sandy, with the tables we've selected, like we can just simply connect via alteryx and I can write out to this environment that doesn't take that long. You know, some of our entities or tables are, you know, a million records long. And I mean that's just a one and done, right? I pull the data, we write it out to the new data warehouse and we're done and it's in there forever. So yeah, we don't need to maintain like a subscription to keep that data and because we can pull it out and just. And be done with that'd be great. 
**Ted Lo** *[01:10:04]*: Well, do we still need a data warehouse though, if we can pull everything out of NetSuite real time? 
**Kevin Baugh** *[01:10:12]*: I think if we want to do custom work, Ted, like for example, the table that I've seen and worked within our data warehouse, like I've worked with Sandy to create new views and tables and things like that. That's where it's like, I just don't know what's available on the back end. For example, when we log into it, what tables do I see? What entities do we see? 
**Marcus Dallacqua** *[01:10:31]*: What's there? 
**Kevin Baugh** *[01:10:31]*: I don't know. 
**Marcus Dallacqua** *[01:10:35]*: You're talking about in NetSuite, correct? 
**Marcus Dallacqua** *[01:10:37]*: Yeah. 
**Marcus Dallacqua** *[01:10:38]*: So you can write a query which is in netsuite is called a saved. 
**Marcus Dallacqua** *[01:10:42]*: Search because you can save it and reuse it. 
**Marcus Dallacqua** *[01:10:45]*: You can write a query and access almost any table. There's a few exceptions of things that are not accessible now. So there's a couple levels. So you have that saved search which historically over the years everybody uses and it powers a lot of like the. 
**Marcus Dallacqua** *[01:11:01]*: Dashboarding and things like that. 
**Marcus Dallacqua** *[01:11:03]*: And then just recently NetSuite came out with Suite QL, which is basically SQL inside of NetSuite. So you can, so you can bypass. 
**Marcus Dallacqua** *[01:11:12]*: The application layer and run SQL statements directly on the database and get information that way as well. 
**Marcus Dallacqua** *[01:11:19]*: And that's quicker. And the table structures are a bit different, but you have access to more and it's quicker. So those are the two methods inside of the system to get that. 
**Marcus Dallacqua** *[01:11:32]*: And everything you generate can be exported out. On top of that you can do web queries. And then as I mentioned before, you can do scripting that would basically execute a query. 
**Marcus Dallacqua** *[01:11:48]*: Now you're using code, but to execute. 
**Marcus Dallacqua** *[01:11:50]*: A query you have with Suite script, you have even more capabilities and more access to information. 
**Marcus Dallacqua** *[01:11:57]*: All that being said though, like, there's. 
**Marcus Dallacqua** *[01:11:59]*: Only a few exceptions anyways for safe searches and SQL. 
**Marcus Dallacqua** *[01:12:05]*: But then you can automatically drop that file or that query, you know the results of that into. It can go to an API endpoint or you can drop it, you can use SFTP and drop it somewhere. So you have a lot of capabilities. 
**Marcus Dallacqua** *[01:12:21]*: That way as well. 
**Marcus Dallacqua** *[01:12:22]*: There are other, the ODBC drivers is. 
**Marcus Dallacqua** *[01:12:24]*: Really the other way to get the information out. 
**Marcus Dallacqua** *[01:12:27]*: People are still using that, even though it's slow. They're still using it to extract information. 
**Marcus Dallacqua** *[01:12:32]*: Out and drop it somewhere. 
**Ken Baugh** *[01:12:35]*: I'm guessing that the back end tables in. I don't know. I know in D365 there's just. I don't know how many. There's thousands of them probably. And in Netsuite I'm guessing that's a little more simplified than D365. But it's just my assumption, you know. 
**Marcus Dallacqua** *[01:12:56]*: There'S a little bit of complexity sometimes because you have synthetic tables, which is kind of like what sounds like, Kevin, what you're doing is basically you're building. 
**Marcus Dallacqua** *[01:13:04]*: A custom table from information from two other tables. 
**Marcus Dallacqua** *[01:13:09]*: So then there's this table of data. 
**Marcus Dallacqua** *[01:13:11]*: Inside NetSuite that you can sometimes query but not extract. 
**Marcus Dallacqua** *[01:13:15]*: It's kind of weird. So there are some like little quirks like that. But for the most part getting the. 
**Marcus Dallacqua** *[01:13:21]*: Information out is not all that difficult. 
**Marcus Dallacqua** *[01:13:24]*: And it sounds like based on what. 
**Marcus Dallacqua** *[01:13:28]*: Cindy described, it's somewhat standardized basic information that you're extracting. 
**Ken Baugh** *[01:13:34]*: Yeah, and that's kind of the purpose of the data we, One of the purposes is just to pull the data we need and there's just a lot of other data that we like, individual warehouse locations that are created on every order. Things like that we just don't need. 
**Marcus Dallacqua** *[01:13:55]*: So it sounds like it makes sense to keep the data warehouse that you. 
**Marcus Dallacqua** *[01:13:58]*: Have because it's already set up with and you have the historical data in there. 
**Marcus Dallacqua** *[01:14:01]*: Right now the question is how do we get the what connection or what type, what way or what method are. 
**Marcus Dallacqua** *[01:14:08]*: We going to use to extract the data on NetSuite to populate your current data warehouse? 
**Marcus Dallacqua** *[01:14:14]*: Yeah. 
**Sandra Rudloff** *[01:14:14]*: And how deep do we want to go? 
**Marcus Dallacqua** *[01:14:17]*: Does that make sense? 
**Ken Baugh** *[01:14:18]*: Kevin? 
**Kevin Baugh** *[01:14:19]*: Well, sorry, so what I envision is tapping into the, or you know, the NetSuite data warehouse. And so again, I don't know that we don't need to maintain our dynamics data warehouse. We need to just how we've done for the AX data Sandy and others is literally via alteryx. It's just a one and done poll. Like what is the historical data we want to pull out of our existing data warehouse and drop it into the Oracle system. That's pretty easy using alteryx. I mean I can do that pretty fast. 
**Marcus Dallacqua** *[01:14:48]*: Right. 
**Kevin Baugh** *[01:14:48]*: So then we, so then we shut down D365. We're not paying the subscription fees on that. We don't need to. I mean assuming we can pull all the data correctly. 
**Marcus Dallacqua** *[01:14:57]*: Right. 
**Kevin Baugh** *[01:14:58]*: And put it in the new data warehouse, I don't see us maintaining our existing data warehouse. We shut it down once we can confirm again that we pulled all the data correctly. 
**Marcus Dallacqua** *[01:15:09]*: Yeah. 
**Marcus Dallacqua** *[01:15:10]*: Kevin, I want to apologize, let me. 
**Marcus Dallacqua** *[01:15:12]*: Back up a bit because I know. 
**Marcus Dallacqua** *[01:15:13]*: I started the conversation saying we're going to talk about data migration and I. 
**Marcus Dallacqua** *[01:15:16]*: Immediately went into data warehouse which really what you're doing is you're using, you're. 
**Marcus Dallacqua** *[01:15:20]*: Doing, you're doing a data extraction so. 
**Marcus Dallacqua** *[01:15:22]*: You can do the reporting. 
**Marcus Dallacqua** *[01:15:24]*: And so let's, let's do the data migration to NetSuite. 
**Marcus Dallacqua** *[01:15:28]*: Let's keep that aside for a moment. 
**Marcus Dallacqua** *[01:15:31]*: And just talk about how you foresee. 
**Marcus Dallacqua** *[01:15:34]*: You continuing that reporting using Power bi. 
**Marcus Dallacqua** *[01:15:37]*: Okay, so yeah, there's likely information that you've pulled and you've created your own custom tables and that's living in your data warehouse, right? 
**Kevin Baugh** *[01:15:49]*: Correct. 
**Marcus Dallacqua** *[01:15:50]*: Okay, yep. 
**Marcus Dallacqua** *[01:15:52]*: And it sounds like you're going to want to continue to do the same thing. Pull information from NetSuite from different tables. 
**Marcus Dallacqua** *[01:15:59]*: Combine it, make your own reports, build stuff on top of that. That's what I, I thought that I was hearing. Is that how you're thinking too? 
**Kevin Baugh** *[01:16:05]*: Right. So I mean like one simple example, we have a report that shows, and again this could be, perhaps there's something native in this new solution here that we don't need to do this. But like every year we come up with a plan for each of our divisions or vertical markets as you call them. And you know, we have a Power BI report that pulls in real time every single day. You know, orders and invoicing sales to those new plan numbers. And I go in there and update these kind of master, we'll call them forecasting tables each year. 
**Marcus Dallacqua** *[01:16:34]*: Yep. 
**Kevin Baugh** *[01:16:36]*: So that's an example of where we're using a custom table which is like our forecast data and I'm joining it with our real time orders and invoicing data. And then you know, because there isn't like a native forecasting table in D365, I had to create that. So it's things like that right. Where you're creating. I mean we have vendor reports where I've had to create some custom vendor views. So yeah, I mean it's just sometimes we use what's in there plus like a one off table to kind of blend the data and get it how we want to see it in Power bi. 
**Marcus Dallacqua** *[01:17:06]*: Okay, got it. 
**Marcus Dallacqua** *[01:17:08]*: Yeah. 
**Sandra Rudloff** *[01:17:08]*: Like Marcus, one thing though, you know, on the other side, which is I'm doing a lot of the, I do all the crystal reports that we email to our clients and all that is kind of more needs. I mean the reporting that D365 had was not very user friendly to like a client. They also didn't have a way to schedule out. So like this hospital wants it every morning it 6am so that's why we have to use these other sources. So for a Data warehouse on NetSuite side for everything like order related that we're using crystal reports for, it would be great if that there are reports that we could either create within NetSuite and I don't know if you can schedule out, but that would eliminate a need for the data warehouse from my perspective of all the order information that we do. 
**Sandra Rudloff** *[01:17:57]*: So I mean we still need one for Kevin and for a lot of the financial analytics. But on the other side, let's call it client and or user reports, status reports. It may not be needed for me as much if we can do it within NetSuite. 
**Marcus Dallacqua** *[01:18:15]*: Okay, so let's address that real quick. So yeah, NetSuite by default gives you the ability to generate, schedule and automatically. 
**Marcus Dallacqua** *[01:18:22]*: Email reports or save searches. 
**Marcus Dallacqua** *[01:18:27]*: However if you need to, if we. 
**Marcus Dallacqua** *[01:18:30]*: Need to generate a custom report from scratch, like all the native reports can. 
**Marcus Dallacqua** *[01:18:35]*: Be customized which means you can customize it, personalize it I should say personalize it and then schedule it. 
**Marcus Dallacqua** *[01:18:42]*: Not a problem. 
**Marcus Dallacqua** *[01:18:42]*: Save searches, create it from scratch, schedule it. 
**Marcus Dallacqua** *[01:18:45]*: Not a problem. 
**Marcus Dallacqua** *[01:18:46]*: But if we need, if you need to like, say, I need this piece of information, this piece, and it's not related inside the backend in NetSuite and you need to pull that all into one report. Well, we can do that and we could schedule that, but that would be. 
**Marcus Dallacqua** *[01:19:02]*: That would be a customization, that would be like a custom report that we. 
**Marcus Dallacqua** *[01:19:05]*: Built using code now. So that's. It depends is my answer, unfortunately. So we probably have to review each. 
**Marcus Dallacqua** *[01:19:14]*: One of those reports that you're sending. 
**Marcus Dallacqua** *[01:19:15]*: So I can understand the information that you're getting, you're gathering, and I'll know. 
**Marcus Dallacqua** *[01:19:21]*: Where it's going to be coming from. 
**Marcus Dallacqua** *[01:19:23]*: Yeah, so maybe the next step for that is gather some of those reports. 
**Marcus Dallacqua** *[01:19:27]*: And we can review them and talk them through. 
**Marcus Dallacqua** *[01:19:32]*: Going back to the data. 
**Marcus Dallacqua** *[01:19:35]*: Internally for your company that you want to store. 
**Marcus Dallacqua** *[01:19:37]*: I think it's going to kind of be something similar, Kevin, where we could probably get you all of the information that you want and even create. I mean, netsuite gives you the build. 
**Marcus Dallacqua** *[01:19:47]*: The ability to create custom records so in custom tables. 
**Marcus Dallacqua** *[01:19:51]*: So like, we could write scripts that. 
**Marcus Dallacqua** *[01:19:52]*: Run every hour, every night that populate those tables with the information, similar to how you're doing it. 
**Marcus Dallacqua** *[01:19:58]*: The thing, though is if you do it outside of netsuite and you have. 
**Marcus Dallacqua** *[01:20:02]*: Power BI on top of it, now. 
**Marcus Dallacqua** *[01:20:03]*: You can now you're in control of. 
**Marcus Dallacqua** *[01:20:06]*: The visualizations and the dashboarding and things like that. So that's something else to consider is, you know, does. 
**Marcus Dallacqua** *[01:20:14]*: Does it make sense to still. To give you that control over the visualizations? 
**Marcus Dallacqua** *[01:20:18]*: It does still make sense to extract the information from NetSuite and put it somewhere. 
**Marcus Dallacqua** *[01:20:22]*: Ted? Yeah. 
**Ted Lo** *[01:20:24]*: So I have a question. I know we email out these reports to our customers and there happened instances where, you know, our customers got hacked and they looked at these reports and got some of the sensitive information and started attacking us. And I'm just wondering if there's a way, you know, and this is probably the internal conversation that we need to have about maybe stopping emailing reports out and just have some sort of dashboard that our customers can log in to look at their orders, their status and things like that. Does, I'd assume, necessary, that does have functionality like that, right? 
**Marcus Dallacqua** *[01:21:11]*: Yeah. So. Well, NetSuite has a customer portal. They have two customer portals, actually. The standard basic one that comes with netsuite default is terrible. And then there's another one called My account, which is technically part of suite commerce, but it doesn't have to be. 
**Marcus Dallacqua** *[01:21:30]*: And that's nice. 
**Marcus Dallacqua** *[01:21:32]*: But what we've done is we created. 
**Marcus Dallacqua** *[01:21:33]*: A customer portal specific for furniture dealers. 
**Marcus Dallacqua** *[01:21:37]*: That gives us the ability to put anything in there that we want, especially. 
**Marcus Dallacqua** *[01:21:41]*: A lot of the custom records that we created around work orders, punch and things like that. 
**Marcus Dallacqua** *[01:21:47]*: And it also has the ability to have reports. So at any point customer could log. 
**Marcus Dallacqua** *[01:21:53]*: Into their customer portal. 
**Marcus Dallacqua** *[01:21:55]*: And by the way, all the credentials. 
**Marcus Dallacqua** *[01:21:56]*: Is controlled by you in the NetSuite backend. 
**Marcus Dallacqua** *[01:21:59]*: They can log in, they could see and filter by different record types. And we're basically using. 
**Marcus Dallacqua** *[01:22:06]*: I don't know if you've seen the smart table yet, but it's basically like this interactive table. 
**Marcus Dallacqua** *[01:22:11]*: We're using that and allowing them to visualize and to filter and things like that. What we don't have is like dashboarding visual reports, but we certainly could create. 
**Marcus Dallacqua** *[01:22:24]*: A report like a PDF report and publish it as a link in there. 
**Marcus Dallacqua** *[01:22:28]*: So there are some things that we. 
**Marcus Dallacqua** *[01:22:30]*: Could do if you want to avoid the emailing of reports. 
**Marcus Dallacqua** *[01:22:36]*: Okay. 
**Marcus Dallacqua** *[01:22:40]*: I'm going to throw this in the chat for Kevin or anybody else. 
**Marcus Dallacqua** *[01:22:43]*: Who might be interested. 
**Marcus Dallacqua** *[01:22:44]*: This is a link to NetSuite's data warehouse information. I have not dug a lot into. 
**Marcus Dallacqua** *[01:22:51]*: This, just to be honest. 
**Marcus Dallacqua** *[01:22:54]*: And now that I pull it up and look at it, I'm kind of like, oh, yeah, there's actually. There's actually quite a bit here. I think I need to familiarize myself with it a bit more. So Netsuite, by the way, has got. 
**Marcus Dallacqua** *[01:23:03]*: Gone away from PDFs and they have a bit more interactive websites. 
**Marcus Dallacqua** *[01:23:07]*: So if you look across the top there's some tabs that take you through there. And then I think there's some. There are some data sheets at the. 
**Marcus Dallacqua** *[01:23:15]*: Bottom on the analytics, where. Yeah, there is one there. 
**Marcus Dallacqua** *[01:23:19]*: There's a lot of information there. 
**Marcus Dallacqua** *[01:23:20]*: User guides, blogs and stuff like that. 
**Marcus Dallacqua** *[01:23:22]*: Feel free to look at that, Kevin. They'll give you better. Some better insight. I'll do the same. 
**Marcus Dallacqua** *[01:23:27]*: I think I need to do some homework on this too. And if it would be helpful for. 
**Kevin Baugh** *[01:23:33]*: Me to demo to you either on this call or offline, like I could just kind of show you at a very high level, like what the kind of existing structure looks like. We're using SQL Server Management Studio, kind of some of the tables that are getting published nightly or whatever, the ones that we're creating custom. Just what it looks like. I don't know if that would help. Just to show you how we're using it. 
**Marcus Dallacqua** *[01:23:53]*: Yeah, it would help. I think I would just want to bring my colleague Luke on the call. 
**Marcus Dallacqua** *[01:23:57]*: He's more technical than me. 
**Marcus Dallacqua** *[01:23:58]*: He's really the architect on Orion. So, Debbie, let's schedule a session with myself, Luke and Kevin and anybody else on the pivot side. 
**Marcus Dallacqua** *[01:24:09]*: Yeah, for sure. 
**Kevin Baugh** *[01:24:10]*: Sandy on that one. Sandy, one thing we want to address as well is in our data warehouse we have these custom views that one of our consultants have built out for us that we just want to make sure that we can, well, either internally just replicate what they've done for us. Sandy, I think we can do that. Yeah, we can create views. 
**Marcus Dallacqua** *[01:24:28]*: It's just. 
**Kevin Baugh** *[01:24:29]*: That's another thing we should talk about. 
**Marcus Dallacqua** *[01:24:31]*: Yeah, yeah. 
**Sandra Rudloff** *[01:24:34]*: Question about the portals, the customer one that you said is actually part of the E commerce. Is that something we can have at Go Live? Because we can't just stop sending the data to our customers. So if we can't have something available right then and there, we're going to need to export it to the data warehouse, you know, recreate all the crystal reports pointing to the new tables and fields so we can, you know, keep business going as usual. 
**Marcus Dallacqua** *[01:25:03]*: Yeah. 
**Marcus Dallacqua** *[01:25:04]*: Well, I guess the first question is it a hard. Are we doing a hard stop on emailing reports? Is that because those reports typically can. 
**Marcus Dallacqua** *[01:25:14]*: Be recreated inside netsuite? 
**Sandra Rudloff** *[01:25:16]*: I guess we have to see, you know, how they look and just get a little bit more feel for the reports, hopefully. I mean, they're all pretty based the client facing ones that are scheduled, they're all status reports. So I've never seen, you know, what your standard status report is for the furniture dealers. So that would be a good start. If I could see that. Then I can also share what we do and see if there's a happy medium. 
**Marcus Dallacqua** *[01:25:42]*: Yep. Yeah. 
**Marcus Dallacqua** *[01:25:45]*: So action item for me is to get with Tyler to get a copy. 
**Marcus Dallacqua** *[01:25:48]*: Of the status report and then but. 
**Marcus Dallacqua** *[01:25:51]*: Just so you know, like the way that NetSuite is set up. So NetSuite has what's called the Advanced PDF Template Generator. And we can either visually drag and drop things and kind of create a layout, or we can use code including HTML CSS and then free marker which allows us to pull in tags and. 
**Marcus Dallacqua** *[01:26:14]*: Make the report dynamic. 
**Marcus Dallacqua** *[01:26:15]*: So I can use a free marker. 
**Marcus Dallacqua** *[01:26:17]*: Tag and say give me the first name of the customer or the company or things like that. 
**Marcus Dallacqua** *[01:26:22]*: So we can really recreate anything. 
**Marcus Dallacqua** *[01:26:25]*: Like it can be any way you want. 
**Marcus Dallacqua** *[01:26:29]*: So. And that's typically what we do. We have kind of some standard ones. 
**Marcus Dallacqua** *[01:26:32]*: But Nobody ever wants to use a standard. 
**Marcus Dallacqua** *[01:26:34]*: They want their, you know, they want. 
**Marcus Dallacqua** *[01:26:35]*: Them branded and personalized, which is. Which is great. NetSuite's designed to do that. 
**Marcus Dallacqua** *[01:26:39]*: So we'll get you the status report and then you get us your. We'll have another session. 
**Marcus Dallacqua** *[01:26:44]*: We'll talk about those reports. 
**Marcus Dallacqua** *[01:26:47]*: Marcus. 
**Marcus Dallacqua** *[01:26:48]*: Yeah. 
**Marcus Dallacqua** *[01:26:49]*: The attendees for the previous topic. You, Luke, Kevin and Sandy. 
**Marcus Dallacqua** *[01:26:57]*: Yes. 
**Marcus Dallacqua** *[01:26:58]*: Anybody else? You guys. Or they could. You guys can forward it to whoever. 
**Marcus Dallacqua** *[01:27:00]*: Else you might want to be on that call. 
**Kevin Baugh** *[01:27:01]*: Yeah, I'm not sure if Ted needs to join that one or would like to join that one. Just anything related to our data warehouse, Ted. 
**Marcus Dallacqua** *[01:27:09]*: Sure. 
**Ted Lo** *[01:27:09]*: I know I got a couple from Sandy, and I have quite a few invites, so I don't know if it's one of those. 
**Kevin Baugh** *[01:27:18]*: This would be something. This is a new one just to kind of go over. 
**Marcus Dallacqua** *[01:27:21]*: Yeah. 
**Kevin Baugh** *[01:27:21]*: The existing layout and design of our data warehouse. 
**Marcus Dallacqua** *[01:27:24]*: Yeah. 
**Kevin Baugh** *[01:27:25]*: How we're using it. 
**Marcus Dallacqua** *[01:27:27]*: Okay. I can put you as optional, Ted. 
**Marcus Dallacqua** *[01:27:30]*: Sure. 
**Marcus Dallacqua** *[01:27:31]*: Okay, thank you. 
**Marcus Dallacqua** *[01:27:33]*: Thanks. 
**Marcus Dallacqua** *[01:27:37]*: Okay, let's move on to actual data migration. So let's talk about the three levels of data migration that we offer. So level one is what's pretty typical. It's bringing over all of the entity information. So all of your customers, contacts, vendors, employees, influencers. How are you tracking influencers right now in D365? 
**Sandra Rudloff** *[01:28:01]*: We aren't. That's in HubSpot. 
**Marcus Dallacqua** *[01:28:04]*: Oh, that's enough. 
**Marcus Dallacqua** *[01:28:04]*: Spot. 
**Marcus Dallacqua** *[01:28:05]*: Okay. 
**Marcus Dallacqua** *[01:28:07]*: So all that information can come into NetSuite. We use. If you can get it out into a CSV file, we have a CSV import wizard. And every netsuite consultant has done this a million times. 
**Marcus Dallacqua** *[01:28:19]*: So it's pretty standard fare for us. 
**Marcus Dallacqua** *[01:28:21]*: We actually like to include you in on some of that because getting information out and getting information back in the netsuite is a very good skill to have. 
**Marcus Dallacqua** *[01:28:28]*: And so we like to teach you how to do that. But so we do that. 
**Ken Baugh** *[01:28:32]*: So we do in that. I mean, I just kind of sanitize the data because, I mean, sometimes we have to duplications and things like that. So we don't want to. We don't want to import, you know, bad data or garbage. Right. So, I mean, I don't know, Sandy, what you think about that, but a lot of times, you know, just stuff builds up and you want to clean it up before we import it in. 
**Sandra Rudloff** *[01:28:59]*: Definitely, you know, one time use vendors and clients. Clients. Like, do we really want to bring all that in? So, yeah, we probably need to do a lot of cleanup. 
**Marcus Dallacqua** *[01:29:10]*: Yeah. Yep. Yeah. 
**Marcus Dallacqua** *[01:29:12]*: And exporting the Information and sanitizing the data, that is your responsibility. We certainly can help. But yeah, that is, and that's part. 
**Marcus Dallacqua** *[01:29:22]*: Of the data migration and then, and. 
**Marcus Dallacqua** *[01:29:24]*: Then organizing the data into the new. 
**Marcus Dallacqua** *[01:29:27]*: Structure that netsuite will accept. And basically it's just a matter of having the right headers in the CSV file. Everything's named a little bit differently. 
**Marcus Dallacqua** *[01:29:37]*: We work with you on that. There's other, there's other ways to do. 
**Marcus Dallacqua** *[01:29:40]*: It too because we can create a CSV import map. 
**Marcus Dallacqua** *[01:29:42]*: And so let's just say for your customers, inside of D365 it's called customer name. And inside NetSuite I think it's called company name. We can create a map and then once we made that connection, we can just reuse that map. You know, you export over here, clean up, import it, we reference that map. 
**Marcus Dallacqua** *[01:30:03]*: Netsuite knows exactly where the information needs to go inside the system. 
**Marcus Dallacqua** *[01:30:07]*: So we have some shortcuts. In fact, those maps are really important because we do a lot of that data migration kind of early on in. 
**Marcus Dallacqua** *[01:30:14]*: The project, validate it and then save. 
**Marcus Dallacqua** *[01:30:18]*: Those maps because later on, just before. 
**Marcus Dallacqua** *[01:30:20]*: Go live, we do it again for. 
**Marcus Dallacqua** *[01:30:22]*: Any new data that has happened transpired. 
**Marcus Dallacqua** *[01:30:25]*: In the past few months. So we do kind of a couple rounds of that data migration, but all. 
**Marcus Dallacqua** *[01:30:30]*: The entity information in and then financial information and we typically do end of the month trial balance for the past two to five years or seven years, whatever you want. And it's. 
**Marcus Dallacqua** *[01:30:44]*: Those are journal entries. 
**Marcus Dallacqua** *[01:30:45]*: The reason why we do those is because we need to have that, you want to have that financial period over. 
**Marcus Dallacqua** *[01:30:50]*: Period, reporting, looking back historical. 
**Marcus Dallacqua** *[01:30:55]*: So that's level one. That's pretty typical for a NetSuite implementation. Now for furniture dealers, we've created level two which also allows you to bring in line item information on sales orders. 
**Marcus Dallacqua** *[01:31:08]*: So you have some of this historical data inside NetSuite. 
**Marcus Dallacqua** *[01:31:13]*: So the way that we've created Orion. 
**Marcus Dallacqua** *[01:31:15]*: And we had that architecture, since we. 
**Marcus Dallacqua** *[01:31:18]*: Have a couple people that are technical on the call, just real quick, what we're doing is we're not using NetSuite's item sub tab because that is pretty heavy. It's, you know, and you guys might. 
**Marcus Dallacqua** *[01:31:29]*: Have a thousand lines on a transaction. 
**Marcus Dallacqua** *[01:31:32]*: What we're using instead is we import that CIF file and we create a. 
**Marcus Dallacqua** *[01:31:36]*: JSON file that's attached to the transaction. 
**Marcus Dallacqua** *[01:31:39]*: And then our smart table is displaying. 
**Marcus Dallacqua** *[01:31:41]*: All the information that's in that JSON file. 
**Marcus Dallacqua** *[01:31:44]*: Eventually it does get constituted on the NetSuite item sub tab. But initially we're doing that JSON file. Well, we can bring in that sales history from your system because you can. 
**Marcus Dallacqua** *[01:31:55]*: Export it from your system and we. 
**Marcus Dallacqua** *[01:31:57]*: Can convert it to JSON and it just comes in as a JSON file and then displays in the smart table. And then from there you can reference it, you can generate a PDF, you. 
**Marcus Dallacqua** *[01:32:06]*: Export it to cifs, you can kind of do what you want with it. 
**Marcus Dallacqua** *[01:32:09]*: So you can bring in sales history into NetSuite. I just want to tell you that's not typical NetSuite data migration because bringing in line item information is tough and time consuming. 
**Marcus Dallacqua** *[01:32:21]*: But because of this architecture, it makes it pretty simple. 
**Marcus Dallacqua** *[01:32:26]*: So that's level two and then level three, which I think we talked about and I don't think you need this. 
**Marcus Dallacqua** *[01:32:31]*: But I just want to make sure that you're aware of it is a full data archival. 
**Marcus Dallacqua** *[01:32:35]*: And we've worked with Sunset Software. You may have heard of him, he's familiar in the furniture space and he's got some tools and some little robots. 
**Marcus Dallacqua** *[01:32:46]*: That he's built that actually go into your system and spider the system, extract the information, it puts it into a. 
**Marcus Dallacqua** *[01:32:54]*: SQL database, but then also generates AI friendly PDFs. So you've archived the data into readable PDFs and in your SQL database and then he puts an AI on top of that, wherever you decide to store it. 
**Marcus Dallacqua** *[01:33:09]*: Most likely would be in SharePoint. 
**Marcus Dallacqua** *[01:33:10]*: He puts an AI on top of it and you can query the AI. 
**Marcus Dallacqua** *[01:33:13]*: The AI can look through all the PDFs if you have questions. Like, a good example would be, what. 
**Marcus Dallacqua** *[01:33:19]*: Did Facebook buy from us in 2010? And it can go back and show. 
**Marcus Dallacqua** *[01:33:27]*: You all the sales orders from 2010 related to Facebook automatically and give you links to those specific PDFs which would. 
**Marcus Dallacqua** *[01:33:34]*: Then have screenshots from your old system. 
**Marcus Dallacqua** *[01:33:37]*: Of exactly what it looked like in your old system. 
**Marcus Dallacqua** *[01:33:42]*: Pretty, pretty cool functionality I don't think you guys need, especially since you already. 
**Marcus Dallacqua** *[01:33:46]*: Have the data in a data warehouse. 
**Marcus Dallacqua** *[01:33:48]*: So if you turn off D365, you have most of the data that you. 
**Marcus Dallacqua** *[01:33:52]*: Need already archived, right? 
**Ken Baugh** *[01:33:53]*: Yeah, I mean some of the data is that we have to access for old things like that are, you know, the drawings, the CAD files and stuff, which you wouldn't, I assume you wouldn't. We would just keep those separate. 
**Marcus Dallacqua** *[01:34:08]*: Yeah, yeah. 
**Sandra Rudloff** *[01:34:11]*: We have to have a conversation about, you know, how do we. Sunset, IQ, Workfront, HubSpot, especially IQ and Workfront, because there's so many documents in there, like you're talking about the drawings and files so that'll be another. Another conversation. 
**Marcus Dallacqua** *[01:34:30]*: Yeah. 
**Marcus Dallacqua** *[01:34:31]*: Well, as far as D365, do you kind of see it the same way as I do that you've already kind of archived all that data? 
**Sandra Rudloff** *[01:34:38]*: We haven't, but I've already had started a conversation with our consultants who, you know, telling them we're going off D365, we're going to want to archive it. So that'll probably be a project they'll need to do because, like I mentioned, you know, sales tax audit. Well, that's going to happen sometime next year. They're going to want invoice copies I won't be able to reprint, you know, for. Not on the system. So it's like, okay, how do. What do we need to export out to make sure that we can satisfy the state on, you know, documentation? 
**Marcus Dallacqua** *[01:35:09]*: Yeah. 
**Sandra Rudloff** *[01:35:09]*: So, yeah, I'll probably have to have that conversation of getting everything exported. And then Ted and Kevin, the conversation will be, where do we store the data? Do we keep it on the local server? I don't know what you might want to do with that, but that's going to be the same thing with Workfront and iq. There's a lot of documents and a lot of data. Where are we going to store it? 
**Marcus Dallacqua** *[01:35:39]*: Okay, so it sounds like to me the archiving of the data in D365 is going to be handled by your consultants. 
**Marcus Dallacqua** *[01:35:46]*: Yeah. Okay. 
**Marcus Dallacqua** *[01:35:48]*: Another decision we make. Got it. So check that one. Let's go through the other pieces of software. 
**Marcus Dallacqua** *[01:35:56]*: Just so I understand. 
**Marcus Dallacqua** *[01:35:57]*: So with Workfront, I know there's data to be archived. Is there any data that needs to. 
**Marcus Dallacqua** *[01:36:01]*: Be migrated to NetSuite from Workfront? 
**Sandra Rudloff** *[01:36:05]*: That's a tough one. 
**Marcus Dallacqua** *[01:36:08]*: Okay. 
**Sandra Rudloff** *[01:36:09]*: I think until we can see kind of how projects are set up and the whole like task assignment. Yeah, for work, I mean, we're not going to bring the documents over, I guess. Brian UD Marie, what do you think about Workfront data? Does it need to. With the intent it's all going to be in Orion at some point. Is there data you think we need to bring over? 
**Brian Hagerty** *[01:36:35]*: I think it would be like active project based. In my head, like project is actually currently still happening. Do we need labor quote, documents, things like that? Like if we are going to say Workfront stops on a Friday and netsuite starts on a Monday, there are going to be working documents and working items that will be necessary to the success of the project that will need to get transferred. 
**Sandra Rudloff** *[01:37:00]*: One of the things I was thinking of is do we, if we can go live, May 1st, we still have full access to workfront and IQ for a while until, you know, our next renewal comes up. Do we just try to wind them down in those systems and then when we cut the cord, we manually replicate in Orion or we'd look at. To do the import at that point. I don't know if that's possible. Marcus, to. 
**Marcus Dallacqua** *[01:37:28]*: Yeah, okay. 
**Marcus Dallacqua** *[01:37:29]*: Yeah. So typically you're. Typically you're running parallel systems for a time. So whatever projects and work you have in D365, you would run out. Well, I'm sorry, the May 1 deadline, is that because you don't want to renew D365? 
**Sandra Rudloff** *[01:37:47]*: Let's see. I think Workfront is in July. 
**Ken Baugh** *[01:37:50]*: Yeah, I was just looking at that. Workfront goes through July 23 of 26. 
**Marcus Dallacqua** *[01:37:58]*: Okay. 
**Sandra Rudloff** *[01:37:59]*: And IQ is kind of a month to month thing, right? 
**Marie Guerrero** *[01:38:02]*: Yeah, it's a month to month thing. I was going to say that all of the documents that are in IQ are actually in Workfront because the issue. Yeah, because they create. Our team creates an issue with the documents that get uploaded into iq. So we might want to explore whether or not we need the documents that are in there since, you know, we launched Workfront Compass. 
**Marcus Dallacqua** *[01:38:28]*: What about receivers though? 
**Brian Hagerty** *[01:38:29]*: Because like receiving paperwork only lives only receiving. 
**Marie Guerrero** *[01:38:32]*: You're right, receiving paperwork only. But like drawings and any project related documents are come from Compass. But Brian's absolutely correct regarding receiving tickets. 
**Sandra Rudloff** *[01:38:41]*: I think documents in both would be migrated to a SharePoint site. Ted, is that what do you think? 
**Ted Lo** *[01:38:50]*: Yeah, I think that's what we talked about in the document on the document team and yeah, we just need to finalize that. 
**Marcus Dallacqua** *[01:39:00]*: Right? Yeah. 
**Sandra Rudloff** *[01:39:02]*: So Workfront and IQ non document data. 
**Marcus Dallacqua** *[01:39:07]*: That's. 
**Sandra Rudloff** *[01:39:08]*: I guess that we kind of need to identify what we'd want or if we even want it in Orion Historical. 
**Marcus Dallacqua** *[01:39:16]*: Let me go back to D365. 
**Marcus Dallacqua** *[01:39:18]*: When do you see D365 shutting. Shutting off, turning off. 
**Sandra Rudloff** *[01:39:23]*: Ted, do you know when that renews the year? 
**Ted Lo** *[01:39:27]*: So if we. 
**Ken Baugh** *[01:39:28]*: Calendar year? 
**Ted Lo** *[01:39:29]*: Yeah, end of the year. 
**Sandra Rudloff** *[01:39:30]*: Yeah, end of the year. 
**Marcus Dallacqua** *[01:39:32]*: Okay. 
**Marcus Dallacqua** *[01:39:32]*: Okay. 
**Marcus Dallacqua** *[01:39:34]*: So it sounds like we get to May. Whatever's still left in D365 will continue. You have Workfront until July. 
**Marcus Dallacqua** *[01:39:43]*: End of July. 
**Marcus Dallacqua** *[01:39:44]*: Anything new is going into Orion? It doesn't sound like we need. 
**Sandra Rudloff** *[01:39:49]*: I was actually hoping that. 
**Marcus Dallacqua** *[01:39:53]*: Open orders. 
**Sandra Rudloff** *[01:39:53]*: In D365 would be migrated into Orion because working in two systems is so hard for employees and for our customers, they don't want to get two separate status reports. Yeah, that would be ideal. And then we have we wouldn't process any more in B365 once we start May 1st. 
**Marcus Dallacqua** *[01:40:11]*: Okay. 
**Marcus Dallacqua** *[01:40:12]*: So you want a hard cut over. 
**Sandra Rudloff** *[01:40:14]*: I think that's the easiest for everybody. 
**Ken Baugh** *[01:40:16]*: You know, when HubSpot is trying to find it. Do you know when HubSpot renews there's. 
**Ted Lo** *[01:40:22]*: A renewal in I want to say July in the summer and then there's another renewal in October. 
**Marcus Dallacqua** *[01:40:31]*: Okay. 
**Sandra Rudloff** *[01:40:31]*: One for like marketing and one for. 
**Ted Lo** *[01:40:33]*: Yeah, one's for marketing, once for sales. 
**Marcus Dallacqua** *[01:40:36]*: Yep. 
**Ted Lo** *[01:40:36]*: Let me. Let me just grab the dates really quick. 
**Ken Baugh** *[01:40:42]*: We should just get a schedule and just publish it for you guys. That shows all of our software expiration dates. 
**Marcus Dallacqua** *[01:40:49]*: Yeah. 
**Ken Baugh** *[01:40:50]*: Renewal. 
**Marcus Dallacqua** *[01:40:50]*: I mean if we're doing the hard cutover. 
**Marcus Dallacqua** *[01:40:54]*: Yeah, yeah. 
**Marcus Dallacqua** *[01:40:55]*: I mean. 
**Marcus Dallacqua** *[01:40:57]*: Because to do the hard cutover. So let me just say this out loud for the sake of the transcript. 
**Marcus Dallacqua** *[01:41:01]*: So. 
**Marcus Dallacqua** *[01:41:01]*: So there's going to be approximately 2,500. 
**Marcus Dallacqua** *[01:41:04]*: Open orders for projects right at that time. 
**Marcus Dallacqua** *[01:41:08]*: Yeah. 
**Marcus Dallacqua** *[01:41:09]*: Okay. 
**Marcus Dallacqua** *[01:41:09]*: So that's a lot. So we'll have a little army of people that are going to be. Some of it's because it's going to be a combination of CSV imports. We might be able to script some things but there's a lot of manual. 
**Marcus Dallacqua** *[01:41:23]*: Value validation that we're going to have to do and probably some manual creation of. Of things. 
**Marcus Dallacqua** *[01:41:28]*: So. 
**Marcus Dallacqua** *[01:41:30]*: So that's something we're going to. Debbie, we're going to need to do significant planning on. 
**Marcus Dallacqua** *[01:41:37]*: That's. 
**Marcus Dallacqua** *[01:41:37]*: That is significant. So I think one of the very first things we should do for that Sandy is we should have a sit down with one of our consultants that can help us scope out what it would. 
**Marcus Dallacqua** *[01:41:51]*: What the level of work is going to be for each one of those projects. 
**Marcus Dallacqua** *[01:41:55]*: I think what you're going to need to do is walk somebody through your process of here's our project, here's our transactions in D365. 
**Marcus Dallacqua** *[01:42:07]*: This is. 
**Marcus Dallacqua** *[01:42:07]*: And this is how we can get the information out. 
**Marcus Dallacqua** *[01:42:11]*: And then here's the other software that has. 
**Marcus Dallacqua** *[01:42:16]*: Adjacent information related that needs to come over because if we're going to replicate. Have a hard cutoff and replicate all that. 
**Marcus Dallacqua** *[01:42:24]*: Yeah. 
**Marcus Dallacqua** *[01:42:25]*: It's going to be some information from. 
**Marcus Dallacqua** *[01:42:26]*: HubSpot, some information from Workfront, a lot of information from D365, some from IQ Coordinator. 
**Marcus Dallacqua** *[01:42:37]*: And I'm not saying it's impossible. I just want you to know that's. 
**Marcus Dallacqua** *[01:42:40]*: That's significant. So we just want to make sure that we do proper planning on that. 
**Sandra Rudloff** *[01:42:45]*: I want to ask the team. I mean kind of my thought was yeah, hard stop for D365, but for the other two systems, not workfront and IQ especially, not necessarily bring that into Orion, but just kind of run our business like we currently are, you know, financial and order transaction and Orion, the dispatch and the, you know, remaining tasks due on those projects in those systems until we get to a point where it's like, okay, workfront renewals in July, so come June we need to start manually recreating anything that's left, I guess. What are your thoughts? 
**Yuridia Silvas** *[01:43:26]*: Yeah, I have a question, Sandy. I'm sorry Brian, real quick. Typically, right when we have done this in the past, how long or what type of access are we going to have to Workfront to be able to reference? Because I'm sure we're not going to want to, you know, transfer everything over. You know, currently, just depending on how the teams work, we should have a document of final, you know, approvals and you know, ideally those would be that one folder we would be able to transfer over. Maybe thinking of specific clients that we would want to capture some of that information in Orion. But again, right, yeah, what does that look like? 
**Sandra Rudloff** *[01:44:05]*: So I had asked Sherry about sunsetting Workfront and she said here are the options. Manually export everything out of Workfront and drop it into a SQL database. There's something called AT App, it's a vendor that we're using that he would extract it and put it in a more digestible format is what she said, mostly documents. Third option is basically go down to the minimum fee of 10,000 annually and that gives us four licenses to have full access. So it doesn't allow us any work to be done, it's just mostly search and extracting. So yeah, those are the three options and I never got the info from IQ about sunsetting them. So we need to ping people again, try and get that. Or maybe Marie, you have a contact who can talk about it. 
**Connie Chung** *[01:45:03]*: Potentially. 
**Marcus Dallacqua** *[01:45:05]*: Okay. 
**Sandra Rudloff** *[01:45:08]*: I would probably just use Jennifer McKinney, but yeah. 
**Brian Hagerty** *[01:45:16]*: So Sandy, going back to your question of would we use Orion just as our financial system and finish things out in workfront and IQ? 1 thought I had, and this is going back to remembering a little bit about the demo, but I know in the demo, or at least I believe in the demo, the way that line items from Orion were actually picked, packed, delivered was by project management selecting line items to be pulled and making those a part of a poll in a work order. 
**Brian Hagerty** *[01:45:53]*: So I think that we would need to understand would we do a manual pick pack versus I think that there could be the way that netsuite operates is so different from the way that we operate today that it may be worthwhile that if we move that order to NetSuite, that we follow the process in NetSuite through closure from that point on. 
**Sandra Rudloff** *[01:46:15]*: Okay, yeah, that makes sense. What we would need then is. I'm trying to think, because we're talking about the Orion tasks assignment, kind of like what we do in Workfront. Do we need to bring over those tasks into the project in Orion? 
**Marcus Dallacqua** *[01:46:36]*: That's actually pretty easy to do if you want to. 
**Marcus Dallacqua** *[01:46:38]*: I mean, you can import those pretty easily. 
**Marcus Dallacqua** *[01:46:40]*: If you can export them out of. 
**Marcus Dallacqua** *[01:46:41]*: Workfront, it's very easy to import in. Into. That's sweet. So no manual recreation of that. 
**Brian Hagerty** *[01:46:48]*: I think if we're looking at like, tasks, like the true tasks that we have in Workfront versus like issues in Workfront, which are more like action items, there's a lot of value in the action that we have in Workfront, but once they're in a completed status, I don't know that there is too much that we need other than the things I was thinking of is like labor quotes or things like that. That could be historical data that we. 
**Marcus Dallacqua** *[01:47:16]*: Need to pull over. 
**Brian Hagerty** *[01:47:18]*: But if I think of our list of tasks in Workfront, I don't see any value in. Okay, exporting, importing, anything like that. 
**Sandra Rudloff** *[01:47:28]*: Really. Issues, not updates. Probably right. 
**Brian Hagerty** *[01:47:33]*: Probably not. I think we could investigate updates, but I mean, I. I don't think so. 
**Yuridia Silvas** *[01:47:40]*: It would be good to still just take a look at those three areas just to validate. Right before we make that decision. 
**Marcus Dallacqua** *[01:47:48]*: Yeah. Okay. 
**Marcus Dallacqua** *[01:47:50]*: Amy, one other quick question. Not off topic, but as far as. 
**Marcus Dallacqua** *[01:47:56]*: Workfront goes, I remember meeting with someone who was kind of overseeing Workfront and I'm sorry, I don't. Sherry. That's right. 
**Marcus Dallacqua** *[01:48:03]*: And she mentioned something to me. She was kind of like, we do want to see how you guys are doing tasks in Orion, but it's possible that we don't need to do as many tasks because I don't want to. 
**Marcus Dallacqua** *[01:48:14]*: Put words in your mouth, but that's. 
**Marcus Dallacqua** *[01:48:15]*: This is the sense that I got from her. Maybe you guys are already doing stuff in the system, so that's part of the natural flow. 
**Marcus Dallacqua** *[01:48:21]*: So we don't have to have a task for it. Because there's nothing worse than like, here's the. 
**Marcus Dallacqua** *[01:48:25]*: Here's the natural action that you're doing, but here's another task saying that go do it and now you have to complete it even though you're naturally doing. 
**Marcus Dallacqua** *[01:48:31]*: It kind of thing. 
**Marcus Dallacqua** *[01:48:32]*: Exactly. 
**Marcus Dallacqua** *[01:48:33]*: I think that's how I understood it. So I guess one thing to consider here is how much task management are you. Do you want to do in Orion? 
**Ken Baugh** *[01:48:47]*: We want to do the tasks and not have to. I mean, what we've created in workforce is a little extra work because tax tasks have to be checked off that are. That is not a byproduct of doing the task. It's an extra step. 
**Marcus Dallacqua** *[01:49:06]*: Right. 
**Sandra Rudloff** *[01:49:07]*: And it also has to do, you know, an example would be one of our sales coordinators, who's basically sales assistant, will create a task for a project coordinator, say this quote is ready to be converted to an order. And then so they get all the information, they do the order entry. Now the project coordinator goes back and has to close that. They did their job. I mean, that's one where it's like, well, okay, it's. Yeah, it's my job. I have to enter the order. Why do I have to, you know, checkbox the tasks? Okay, so those are the. I think some of the things she was talking about where it's to trigger the work, but do we really need to go back and close it? 
**Marcus Dallacqua** *[01:49:46]*: So that's where. 
**Marcus Dallacqua** *[01:49:47]*: And I mentioned this before, but reminders on those portlets, that's what those are used for. So they're not actually tasks or reminders. 
**Marcus Dallacqua** *[01:49:54]*: And there's something in the system that is the trigger that says, oh, it's time for me to do work. So it shows up on my reminders dashboard and then I go do the. 
**Marcus Dallacqua** *[01:50:02]*: Work and it automatically comes off. Okay, so I think. 
**Marcus Dallacqua** *[01:50:08]*: True task, isn't it? 
**Marcus Dallacqua** *[01:50:09]*: Yeah, yeah. 
**Marcus Dallacqua** *[01:50:11]*: So that'll reduce the task load. So I do think, by the way, I'm a task guy, I like tasks. So I like the fact that you guys are project oriented and task things out. I think we'll just make decisions on. 
**Marcus Dallacqua** *[01:50:24]*: What makes the most sense, what the system can kind of handle natively and. 
**Marcus Dallacqua** *[01:50:28]*: What needs to be tasked. So I just wanted to bring that up. As we're thinking about how many of. 
**Marcus Dallacqua** *[01:50:34]*: Those tasks we're going to bring over. 
**Marcus Dallacqua** *[01:50:37]*: You probably have to think about what's actually going to be necessary to task. 
**Marcus Dallacqua** *[01:50:40]*: Out in netsuite versus what won't be. 
**Sandra Rudloff** *[01:50:42]*: I think the feedback from Brian and it does make sense not to bring tasks over at all, but we have what's called issues, which are they're not a bad thing. But it's, you know, like I'll create an issue to the project manager to say, hey, was this work completed? Can we pay the vendor? And then they'll reply. So that Might be more of a task within Orion that we. And those are the types of things we'd probably want to bring over in some format, depending on how the whole, you know, work assignment goes. 
**Marcus Dallacqua** *[01:51:13]*: That almost sounds like a communication tool. 
**Marie Guerrero** *[01:51:17]*: Yeah, it's kind of like it's called an issue, but it's really a request. Like it's a request to get a project on the schedule. It's a request for the estimator to provide a quote. 
**Sandra Rudloff** *[01:51:28]*: There really are requests market. 
**Brian Hagerty** *[01:51:31]*: It's, I think a really good way to put it is it's a custom form. So in our issues, there's a few different options. You can choose of which issue you want to send to somebody, and it creates a custom form of the information that you need to transmit to them so that they can be successful in completing that task. 
**Marcus Dallacqua** *[01:51:48]*: Got it. 
**Sandra Rudloff** *[01:51:49]*: And it's. So that there's a dashboard with, you know, so I'm in accounts payable. I say, oh, we need issue deposits to these vendors. So rather than sending an email, it's on your dashboard at the work you have to do. 
**Marcus Dallacqua** *[01:52:00]*: Yeah, yeah. And then in Orion, we have tasks which would be like, you need to take. Somebody needs to take action, and it might be me. I might create a task for myself. 
**Marcus Dallacqua** *[01:52:10]*: Because, you know, I want something to prompt me to take action. Then we have issues which are problems. 
**Marcus Dallacqua** *[01:52:16]*: Those are related to like Bill Price. 
**Marcus Dallacqua** *[01:52:19]*: Discrepancies or acknowledgement issues or punch is an issue. 
**Marcus Dallacqua** *[01:52:23]*: They are kind of considered bad things. 
**Marcus Dallacqua** *[01:52:25]*: That have to be resolved inside of Orion. And then we have requests. 
**Marcus Dallacqua** *[01:52:29]*: Then we have that request engine that allows you to generate any kind of. 
**Marcus Dallacqua** *[01:52:33]*: Request template or form that you might need. 
**Marcus Dallacqua** *[01:52:36]*: So the standard ones are labor quote. 
**Marcus Dallacqua** *[01:52:39]*: Requests, design requests, new project request. Joe's favorite. 
**Marcus Dallacqua** *[01:52:44]*: If you remember Joe Keller, when he did his demo, I need donuts requests like, so you can really actually make. 
**Marcus Dallacqua** *[01:52:50]*: Anything you want and populate it with fields. 
**Marcus Dallacqua** *[01:52:52]*: There's an ad. 
**Marcus Dallacqua** *[01:52:53]*: There's an admin panel for you to build those out. 
**Marcus Dallacqua** *[01:52:56]*: So we'll have to. That'll be part of change management though, right? Is getting people to understand the new terminology because it's so similar, but they're different. 
**Marcus Dallacqua** *[01:53:08]*: So we'll have to. 
**Marcus Dallacqua** *[01:53:09]*: We'll take note of that as we go. 
**Marcus Dallacqua** *[01:53:11]*: All right, so. 
**Marcus Dallacqua** *[01:53:12]*: So to recap, I think I got this D365 hard cut over in May. 
**Marcus Dallacqua** *[01:53:17]*: We're going to reproduce any of the. 
**Marcus Dallacqua** *[01:53:19]*: Open projects and transactions inside of NetSuite. I do want, as I'm thinking about this too, Sandy, I want you to know, because we. There's not much of that work that. 
**Marcus Dallacqua** *[01:53:29]*: We can do up front. 
**Marcus Dallacqua** *[01:53:31]*: Right. 
**Marcus Dallacqua** *[01:53:31]*: When you think about it's kind of like as of Friday, here's the open projects. So we'll have to think, yeah, Debbie and Chris and I will take this away and we'll think about what kind. 
**Marcus Dallacqua** *[01:53:41]*: Of army we need to be able to do that. So. 
**Marcus Dallacqua** *[01:53:45]*: And then. 
**Marcus Dallacqua** *[01:53:46]*: But that's going to primarily be it. There might be a few other things that we bring over, but nothing major. We're going to let the other systems. 
**Marcus Dallacqua** *[01:53:53]*: Kind of run out. 
**Sandra Rudloff** *[01:53:54]*: So you are talking, you know, project sales orders, quotes, purchase orders so that know the. Should we everything happen. Like Brian says, we need to do a pick pack for a delivery on Tuesday and we need to pay bills and all that. It's all there. A.R. Open A.R. 
**Marcus Dallacqua** *[01:54:14]*: All that. 
**Marcus Dallacqua** *[01:54:16]*: That's what. 
**Marcus Dallacqua** *[01:54:17]*: Yeah, we. 
**Marcus Dallacqua** *[01:54:17]*: Yes. That sounds like that's what you want. 
**Marcus Dallacqua** *[01:54:19]*: Yeah. 
**Marcus Dallacqua** *[01:54:20]*: Yeah. 
**Marcus Dallacqua** *[01:54:21]*: Okay. 
**Sandra Rudloff** *[01:54:21]*: Just want to make sure I'm not. 
**Marcus Dallacqua** *[01:54:22]*: Going to back to you because. Yeah, because that's a big decision. 
**Marcus Dallacqua** *[01:54:25]*: Just so you know, that's a big one. 
**Marcus Dallacqua** *[01:54:28]*: And I'm not saying it's bad or anything. It's just that is a, it's a, it's challenging because of the timing of it. Like it's as of Friday, that all. 
**Marcus Dallacqua** *[01:54:41]*: Has to be in the system for Monday morning. 
**Marcus Dallacqua** *[01:54:43]*: Right. 
**Ted Lo** *[01:54:44]*: I, I got a question. 
**Marcus Dallacqua** *[01:54:47]*: Yeah. 
**Ted Lo** *[01:54:47]*: How, I mean, how much would, how much more would it take to just literally migrate everything over, especially if we have the data fields mapped out? 
**Marcus Dallacqua** *[01:54:59]*: Right? 
**Marcus Dallacqua** *[01:55:01]*: Well, it's the, it's challenging because of the way that netsuite and everything, all the records and lines in netsuite are interconnected. That's the challenging part. So like for example, on a sales order you have, let's say you have. 
**Marcus Dallacqua** *[01:55:15]*: 10 lines on a sales order and. 
**Marcus Dallacqua** *[01:55:17]*: Then you generate a purchase order. There's 10 lines on that purchase order. 
**Marcus Dallacqua** *[01:55:21]*: Let's just make it easy. 
**Marcus Dallacqua** *[01:55:22]*: Well, there's actually an invisible connection between the lines and the sales. 
**Marcus Dallacqua** *[01:55:27]*: Order and the po. 
**Marcus Dallacqua** *[01:55:28]*: And so but if I were to. 
**Marcus Dallacqua** *[01:55:30]*: Import or import, whether that's a CSV import or imported via code, a sales order and a purchase order, I need. 
**Marcus Dallacqua** *[01:55:39]*: To, I need to stitch together all. 
**Marcus Dallacqua** *[01:55:42]*: The lines as well. 
**Marcus Dallacqua** *[01:55:46]*: Otherwise a PO is standalone. Well, that's the case actually for item fulfillments, invoices, pos, bills, everything is interconnected that way. So it's that stitching under behind the scenes that needs to happen. Now I can easily do that if I go to the sales order and. 
**Marcus Dallacqua** *[01:56:03]*: I generate the po. 
**Marcus Dallacqua** *[01:56:04]*: Netsuite automatically natively can. 
**Marcus Dallacqua** *[01:56:06]*: Makes that connection. 
**Marcus Dallacqua** *[01:56:08]*: So I can manually kind of recreate. 
**Marcus Dallacqua** *[01:56:10]*: The project and date things a certain way. So. 
**Marcus Dallacqua** *[01:56:14]*: So it looks just like it did. 
**Marcus Dallacqua** *[01:56:15]*: In D365, but most of that has to be done somewhat manually. 
**Ted Lo** *[01:56:20]*: Got it. 
**Brian Hagerty** *[01:56:21]*: Okay, Marcus, what about sales order numbers and purchase order numbers? Like, if we recreate from D365 to Orion, is there going to now be a different purchase order number in Orion than there previously was in D365? 
**Marcus Dallacqua** *[01:56:38]*: Yeah. So the way we typically handle that. 
**Marcus Dallacqua** *[01:56:40]*: Is we have legacy numbers that will. So you could. 
**Marcus Dallacqua** *[01:56:44]*: But, yeah, because the numbers will likely be different and a lot of times it's different because clients take a new. 
**Marcus Dallacqua** *[01:56:52]*: Numbering strategy or we can't number the exact same way from one system to the other. But we just. 
**Marcus Dallacqua** *[01:56:57]*: We have a legacy order number that we populate and people are aware of it, and then eventually we. 
**Marcus Dallacqua** *[01:57:05]*: That's one of those types of custom fields that eventually goes away because it's not necessary anymore. We hide it or something. 
**Marcus Dallacqua** *[01:57:14]*: All really good questions. 
**Ted Lo** *[01:57:16]*: I was going to say then to look up orders, we would just have the D365 exporter sitting there with Kevin's magic. And we can do it that way. 
**Marcus Dallacqua** *[01:57:30]*: Yeah, because that's in a custom field that. That you can throw that into the global search and find it. 
**Marcus Dallacqua** *[01:57:35]*: Or when you do a query or anything else, you can easily find it and reference it. 
**Marcus Dallacqua** *[01:57:41]*: Yeah. 
**Marcus Dallacqua** *[01:57:44]*: All right. So we just hit the top of the hour. I think we made really good progress. We will send out another summary. We actually have some decisions we made, so we'll call that out in our. 
**Marcus Dallacqua** *[01:57:54]*: Summary as well, which is fun to make decisions. 
**Marcus Dallacqua** *[01:57:57]*: And then behind the scenes, we'll do some work. Sandy. To begin the planning specifically for the data migration and some of the other things. And I know Debbie will be. Right now, she's just keeping a tally of all the other sessions that we're going to need to schedule. We'll go through our round of everything first and then we'll kind of loop. 
**Marcus Dallacqua** *[01:58:18]*: Back and schedule some of these other ones. 
**Marcus Dallacqua** *[01:58:20]*: Okay. 
**Sandra Rudloff** *[01:58:21]*: And I know I've got some things to deliver to you guys. Put that out today. 
**Marcus Dallacqua** *[01:58:25]*: Perfect. All right, thanks, everybody. 
**Marcus Dallacqua** *[01:58:27]*: Have a great Tuesday. 
**Marcus Dallacqua** *[01:58:30]*: Thanks, everyone. Thank you. 
**Ted Lo** *[01:58:33]*: I know were talking about doing a demo for SharePoint Connection. We actually have a document team meeting next week. I'm just wondering if that's a good opportunity to show it to our document team. 
**Marcus Dallacqua** *[01:58:52]*: You know, I think Tyler's actually on site next week, isn't he, Chris? 
**Marcus Dallacqua** *[01:58:54]*: He is, yeah. 
**Marcus Dallacqua** *[01:58:56]*: So yeah. Next week's probably not going to work. Our guru is. We can get somebody else to do it, but he's just. 
**Marcus Dallacqua** *[01:59:03]*: He's the guru on it. I prefer. Yeah. 
**Marcus Dallacqua** *[01:59:06]*: Because you guys will have hard questions for him, right? Yeah. 
**Marcus Dallacqua** *[01:59:09]*: Yeah. 
**Ted Lo** *[01:59:09]*: If you can give us some availabilities, that would be great. And I can chat with the document team and see if we can set that up. 
**Marcus Dallacqua** *[01:59:17]*: Yeah. 
**Marcus Dallacqua** *[01:59:17]*: Chris, do you mind doing that one instead of Debbie? Just because you're connected to Tyler pretty easily. 
**Marcus Dallacqua** *[01:59:22]*: Yeah, okay. Of course. 
**Marcus Dallacqua** *[01:59:25]*: Awesome. 
**Ted Lo** *[01:59:25]*: Thank you so much. 
**Marcus Dallacqua** *[01:59:26]*: Thank you. 
**Marcus Dallacqua** *[01:59:27]*: Thanks, Ted. 
**Sandra Rudloff** *[01:59:28]*: Thanks. 
**Marcus Dallacqua** *[01:59:28]*: See you, Sandy. 
**Marcus Dallacqua** *[01:59:29]*: Bye. 
