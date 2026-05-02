# Pivot: Review Prep for Commissions Session

**Meeting Date:** 25th Aug, 2025 - 9:30 AM

---

**Marcus Dallacqua** *[00:08]*: Hey, Jason, how are you? I can't hear you. Good morning, Chris. Hi, Debbie. 
**Debbie Herbert** *[00:30]*: Good morning. Hey, everybody. 
**Chris Trumble** *[00:33]*: Are you in sunny Florida, Debbie? 
**Debbie Herbert** *[00:35]*: I am, yes. 
**Jason Billington** *[00:38]*: Nice. How'd the move go? 
**Debbie Herbert** *[00:41]*: They cleaned out the house pretty fast. I still have some stuff in the garage in the basement that I'm not taking, so I didn't finish going through all that yet. Yeah, but. But yeah, they packed everything up. They left Saturday afternoon. They should be here sometime between today and the fourth, so, you know, pretty big spread there. 
**Marcus Dallacqua** *[01:01]*: Yeah. 
**Debbie Herbert** *[01:02]*: And I drove all day yesterday. I had to stop twice because I was falling asleep, so. But I got here 8:30 last night and finally got my mouse working, so it's all good. 
**Marcus Dallacqua** *[01:13]*: Congrats. 
**Debbie Herbert** *[01:14]*: Yeah, thank you. So, Marcus, welcome back. Hope you had a good week last week. 
**Marcus Dallacqua** *[01:22]*: It was a week. 
**Debbie Herbert** *[01:23]*: It was a week. Okay, well. And it's a Monday. 
**Marcus Dallacqua** *[01:26]*: It's Monday. 
**Debbie Herbert** *[01:28]*: So we have a session with pivot at 11 to talk about commissions. And the three of us met last week because weren't sure if you were going to be able to attend the session or not. So I think, Jason, did you have a chance to kind of collate some of that stuff that Chris gave you maybe to help use as an outline or. Do you even need that, Marcus? 
**Marcus Dallacqua** *[01:55]*: Yeah, I think I do. Because if I remember correctly, she already sent over all their commission plans. 
**Debbie Herbert** *[02:00]*: Yes. 
**Marcus Dallacqua** *[02:01]*: And so I was hoping. Do we have that in a project yet in. Claude. 
**Debbie Herbert** *[02:15]*: You are on mute, Jason. 
**Chris Trumble** *[02:18]*: Well, he's not on mute, but it's. The mic's not working. 
**Debbie Herbert** *[02:21]*: Oh, okay. If it's not in there, we can put it in there. We've got a little time before 11 o'. 
**Marcus Dallacqua** *[02:34]*: Clock. Yeah, I need to get it in there. Then we can do a quick analysis on them, organize them, and then I do have. Well, do we have a brief on specifically what the outline is for today? 
**Debbie Herbert** *[02:48]*: No. Well, unless Jason put that together. We talked about that on Friday, but I don't have. I don't have a status on it. 
**Marcus Dallacqua** *[02:56]*: All right, let's see what we got because we do have the commissions module up in Orion, so we can review it with them. 
**Debbie Herbert** *[03:07]*: Okay. 
**Marcus Dallacqua** *[03:11]*: Hey, Jason, can you hear us? 
**Chris Trumble** *[03:17]*: Those dang headphones. 
**Debbie Herbert** *[03:20]*: Doesn'T look like it. Let me just put something in the chat. 
**Chris Trumble** *[03:29]*: Yeah, so I think that, like, we have theirs. I think one of the questions is like, are you taking this as an. Are you taking this discovery as an opportunity to significantly change your commission structure? 
**Marcus Dallacqua** *[03:45]*: Yeah, that's the big question. 
**Chris Trumble** *[03:46]*: That's a big question. So then it's like yeah, go ahead. 
**Debbie Herbert** *[03:50]*: They did say that they have a meeting on Wednesday where they're talking about that specifically. 
**Chris Trumble** *[03:54]*: Yeah, yeah, so they're open to it. But what does that mean? Is it like consolidating other plans or whatever it is. So I think it's like an aspect of showing them, you know, this commission module is pretty flexible. It would be good to go through their plans and say, okay, this is difficult or this is easy. You know, kind of give them a little bit of guidance and then they're going to go away and make some decisions. 
**Marcus Dallacqua** *[04:23]*: I don't think we have a solution designed for the current iteration of the commission module. Do you have access to cursor in the Orion code base right now, Chris? 
**Chris Trumble** *[04:33]*: Yes, I'm doing the VS code or whatever. 
**Marcus Dallacqua** *[04:39]*: Yeah, that's fine. We just ask it to search the code base to create a client friendly solution design that outlines and focuses on the features and functionalities of the commission module and how a furniture dealer could potentially use it, something like that. That way we can give them the document so when they have their meeting on Wednesday, they can reference that because they're probably, they're kind of probably be looking at like, okay, we have, I don't know how many commission modules that they have or commission plans that they have, but they're probably going to be looking at. Okay, well if their system can do this, maybe we should consider standardizing everybody on this type of commission plan. But I'd like to have analysis of the commission plans. 
**Debbie Herbert** *[05:30]*: Yeah, okay. I think Jason's having technical trouble, so I'll try to call him. And then I'm gonna, in the meantime, I'm gonna put all their stuff in. Claude, if he hasn't done it already. 
**Marcus Dallacqua** *[05:45]*: Just go ahead and create another project for commissions and pivot conditions. And then. Yeah, and then once you have that, just shoot me a message. I'll do a quick analysis and I'll have that for the meeting as well. 
**Debbie Herbert** *[05:56]*: Okay, that sounds good. 
**Chris Trumble** *[05:58]*: So Marcus, do you know what repo is? The right one. This is like the Orion repo. 
**Marcus Dallacqua** *[06:02]*: That's why that's that one. 
**Chris Trumble** *[06:04]*: Okay, now if I go into documentation. 
**Marcus Dallacqua** *[06:06]*: No, don't do that. 
**Jason Billington** *[06:07]*: What? 
**Marcus Dallacqua** *[06:08]*: Which one? Just go to the top level. Orion. Okay, Click on that. Yeah, tell it to search the code base. I don't want to search documentation, I want to search the code. 
**Chris Trumble** *[06:19]*: Oh, yes, look at the actual code. 
**Jason Billington** *[06:20]*: Okay. 
**Marcus Dallacqua** *[06:21]*: Yeah. 
**Chris Trumble** *[06:23]*: I only have to point it as far as this root folder here. 
**Marcus Dallacqua** *[06:26]*: Yeah, okay. Yeah, it takes a little bit Longer to find it, but it's fine. Now. The only other thing you don't have is you don't have the Orion UI folder, but I think you can add it here because it really is. It's a combination of the back end and the front end. 
**Jason Billington** *[06:42]*: Yeah. 
**Debbie Herbert** *[06:45]*: Marcus, I'm sorry. I keep talking over you guys. Sorry. Is there anything about commissions in your outline that I can put in here also? 
**Marcus Dallacqua** *[07:10]*: You check. I'm sure there's a couple questions in there, but let me see. 
**Debbie Herbert** *[07:18]*: Hey, Jason, are you back? Can you hear us? We can't hear you. Yes. Yeah. So quick question for you. Did you have a chance to do any review of the commission files that we talked about on Friday? 
**Jason Billington** *[07:42]*: I did. I did. 
**Debbie Herbert** *[07:43]*: Okay. Did you. Is it. Where did you locate that? 
**Jason Billington** *[07:48]*: What do you mean located? 
**Debbie Herbert** *[07:49]*: Did you. Did you. 
**Jason Billington** *[07:51]*: Yes, I made a presentation for it. Like, what do you want me to tell you? 
**Debbie Herbert** *[07:53]*: Well, just like notes or anything electronic on it. Okay, you want me show. You want to show it? 
**Jason Billington** *[07:59]*: Yeah. 
**Debbie Herbert** *[08:00]*: Okay. 
**Jason Billington** *[08:03]*: All right. 
**Chris Trumble** *[08:03]*: It's cloning that repo, Marcus. I found the UI one too. 
**Marcus Dallacqua** *[08:07]*: Okay. 
**Chris Trumble** *[08:12]*: It's taking a long time. 
**Marcus Dallacqua** *[08:20]*: I don't have anything in the master outline. 
**Debbie Herbert** *[08:22]*: Okay. 
**Marcus Dallacqua** *[08:22]*: But that's okay. There's really just a. We'll be fine. 
**Debbie Herbert** *[08:26]*: Okay. Now I was just thinking if there was something else we could pull in. 
**Jason Billington** *[08:36]*: I've had to go back to one screen because it wouldn't let me get. So I just created like a little presentation. I don't know, hopefully this will give them. But I just wanted to kind of let them know what. How it would be triggered off of. I guess how the commission bubble up starts. It'll come off of the invoice, save date or a payment received date, project status. So it kind of gives you ways in which the commission could be structured and triggered off of. Then it tells you how often it will refresh, which will be helpful. 
**Marcus Dallacqua** *[09:13]*: And then also, Jason, I don't. Where did you get this information from? I'm not sure it works that way. 
**Jason Billington** *[09:21]*: That was from the convention, how Orion works, or that documentation that you guys sent out. 
**Debbie Herbert** *[09:29]*: That was. Yeah, that was from last week's chat. Yeah, that. So, Chris, where did you find. Well, first, before we go looking, is this. Is this not accurate or what you were expecting? 
**Marcus Dallacqua** *[09:43]*: No, I mean, it looks great. I'm just not sure that it's. That it's active. If you go back to the previous page. 
**Jason Billington** *[09:50]*: It does not trigger off those things. 
**Marcus Dallacqua** *[09:55]*: It does not trigger off project status change or custom search results. I don't believe. 
**Jason Billington** *[09:59]*: Does it, Chris, that is flips trigger review. 
**Chris Trumble** *[10:06]*: No, I don't think so. 
**Marcus Dallacqua** *[10:07]*: Okay, so what. Okay, so Jason, I just instructed Chris to look at the code base to create a solution design basically to do what you. What you've already done, which is. This is great. So the only problem is, I think is that we should have reviewed the code base that has all the most recent changes. 
**Jason Billington** *[10:27]*: Yeah. 
**Chris Trumble** *[10:28]*: So I gave him a solution design and the solution. It probably changed significantly between the solution design and what actually got coded. 
**Marcus Dallacqua** *[10:35]*: It has, it has. 
**Jason Billington** *[10:37]*: Okay. 
**Marcus Dallacqua** *[10:40]*: Did you do this in. So this is in Claude? 
**Jason Billington** *[10:42]*: Yes. 
**Marcus Dallacqua** *[10:42]*: Okay, so Chris, can you. So Chris is getting us an updated solution design. We can, we can probably fix this pretty quick. Let's go ahead and keep going. 
**Jason Billington** *[10:50]*: Okay. Yeah, once I have that, I can update it obviously. 
**Marcus Dallacqua** *[10:54]*: Yeah. 
**Jason Billington** *[10:57]*: All right. And then this kind of just tells them how they will calculate their. Their obviously the commissions for it. So obviously revenue minus direct project cost and then that defines the direct project cost. So actual versus remaining budget. And then, so those are the. And then you can do it based on project total invoiced amount or cash received. So it kind of gives them some flexibility on the commission structure part of as well. And then there's also a true up part of it. Or they can do a callback or write offs if things potentially posted later than they expect. As far as cost concerns, they can do write offs or then they can do clawback if they do an overpayment as well. So it kind of gives them flexibility. 
**Marcus Dallacqua** *[11:53]*: So. Got it. By the way, I love the fact that you're using cloud this way. This is great. Jason. So this is actually a much. So this is this actually, Chris, now I think about it like we could do this instead of PowerPoint slides. 
**Jason Billington** *[12:09]*: Yeah. Yeah. 
**Marcus Dallacqua** *[12:12]*: The only thing that we need to do, Chris, is we need to get a design system. So we're all doing it the same way. But this is great. 
**Jason Billington** *[12:20]*: Yeah. So if there's a template, is that what you're kind of meaning, like a PowerPoint template in the background that kind of looks similar? I think it would look like such. Is there something. 
**Marcus Dallacqua** *[12:32]*: A design system is really just a set of. It's like guidelines for when you give it and you give it to Claude and Claude will design based on those guides. So we all will have the same color scheme, the same fonts and all that stuff? 
**Jason Billington** *[12:44]*: Yeah, yeah, exactly. Okay, good. 
**Marcus Dallacqua** *[12:45]*: Yep. 
**Jason Billington** *[12:46]*: Good. Yeah. So do we have a template that we currently use for GSI when we're presenting? 
**Chris Trumble** *[12:53]*: I have a PowerPoint template. But it's. I'll have to give it something that Claude can digest. 
**Jason Billington** *[13:00]*: Right. Right. Yeah, sometimes. 
**Debbie Herbert** *[13:04]*: And to carry that a little further, Andy sent something out about. I think his message was really directed at Angela. It was a little terse. 
**Jason Billington** *[13:13]*: Yeah. 
**Debbie Herbert** *[13:14]*: But yeah, having, like something that we can use that. That works with Claude and that can be standardized across all the projects. So that'll. That'll be the next step of that. 
**Marcus Dallacqua** *[13:27]*: Yeah. 
**Jason Billington** *[13:28]*: Yeah. 
**Debbie Herbert** *[13:29]*: Okay. 
**Marcus Dallacqua** *[13:30]*: Okay. I'm trying to. We could. We could stop here for a moment. What time's our session with them? 
**Debbie Herbert** *[13:34]*: 11. 
**Marcus Dallacqua** *[13:35]*: Okay. So, Chris, if you can work with Jason, because we can lead with this. We just need to get the. The updated solution design. There's a couple things in here that are not accurate based on the new. The way it functions. So you need to get the new solution design. You and Jason can work together to get this updated and a design system, if you have one, or you can create one pretty quick. And then we can use it. We can. We can lead with it in the 11 o' clock session. 
**Chris Trumble** *[14:02]*: Yeah, I lost all my repos here and this code having some troubles. 
**Jason Billington** *[14:12]*: So I'll. 
**Chris Trumble** *[14:12]*: I'll just keep working on this. 
**Jason Billington** *[14:14]*: Okay. 
**Debbie Herbert** *[14:15]*: Okay. 
**Chris Trumble** *[14:16]*: So I'm gonna. I'm gonna be working on it during the. 
**Jason Billington** *[14:23]*: Yeah, I got. 
**Marcus Dallacqua** *[14:23]*: I'll take. I got the 10 o' clock and the 10:30. I need to be at those anyways. I got those. You and Jason can just work on this from now till 11. That'll be great. Okay. So that. The. The plan will be. We'll lead with this. And Jason, you could do the walkthrough on that call. We'll lead with this. We'll pop open Orion, we'll show them the actual commission record. I need to do analysis on the commission records themselves. So just let me know, Debbie, when you have everything in the project. 
**Debbie Herbert** *[14:50]*: Yeah. 
**Marcus Dallacqua** *[14:51]*: And then after we do all that. So we'll. It's going to be show and tell. Like, we'll show a couple things. I'll give them. I'll show them the report and the analysis on their commission report, and then we'll talk to them about if they want to standardize onto some type of commission plan and what their intentions are. But I have a feeling this is going to be us giving them information for their Wednesday meeting. 
**Debbie Herbert** *[15:14]*: Yeah. Okay. The seven files that Jason gave me are in a project called Pivot Commissions. 
**Marcus Dallacqua** *[15:21]*: Perfect. 
**Jason Billington** *[15:24]*: Great. So I'll wait for. The updated instructions are actually how it works. Yep. And then. And then the template. And then I'LL start updating the system and then I'll go through the presentation and then you want to step. Take it from there, Marcus, and just do a walk through inside of this. 
**Marcus Dallacqua** *[15:43]*: Yeah. But I do need you to do a walkthrough with Chris first to make sure that Claude doesn't. Yes, Claude didn't miss anything and there's not anything that's inaccurate in there. 
**Jason Billington** *[15:51]*: Okay, we'll do. 
**Marcus Dallacqua** *[15:52]*: And then, Chris, when you. When you're also done, will you solution design we just send it to me too. I'm going to throw it in the commissions project and do that analysis there. 
**Debbie Herbert** *[16:02]*: Cool. 
**Marcus Dallacqua** *[16:03]*: Okay. Awesome, guys. 
**Debbie Herbert** *[16:06]*: See you. 
**Jason Billington** *[16:06]*: Bye. 
**Debbie Herbert** *[16:07]*: Bye. 
