# Highva Privacy Policy

**Effective date:** Oct. 7, 2026 · **Last updated:** Oct. 10, 2026
**Who we are:** Highva is an iPhone app made by Koby Hilbig ("we", "us"). Contact:
support@highva.app.

## The short version

- **Almost everything stays on your iPhone.** Your goals, check-offs, streaks, journal, vision board, chats
  and profile are saved in the app on your phone. We don't keep a copy on our servers.
- **The AI coach is optional and off until you agree.** When you turn it on, the data it needs is sent
  through our server to our AI provider, Anthropic, to write your coaching. Our server passes it along and
  doesn't store it. Anthropic doesn't use it to train its AI models.
- **We count how the app is used, never what you write.** The app sends anonymous usage events (like "a task
  was checked off" or "the journal was opened") to our analytics provider, PostHog, and our server keeps
  anonymous totals (like how many tasks are about exercise). Never your journal, chats, goal names, task words
  or "About you" answers. You can turn this off in **Account → Privacy**. No session recording.
- **No ads, no tracking across apps, no selling.** We don't sell your data or share it for advertising.

## 1. What's stored on your iPhone

Highva saves the following inside the app, on your phone:

- **Goals and daily tasks:** names, why they matter, categories, colors, deadlines, which tasks you checked
  off or missed each day, the reasons you gave for misses, streaks, streak freezes, vacation days, and your
  city's progress.
- **Your journal:** how you felt, what made the biggest difference, tomorrow's top priorities, any notes you
  write, and the coach's advice on each entry.
- **Your profile:** your name, your onboarding answers (why you joined, life areas, your 5-year vision, what
  holds you back, what drives you, how you want to be coached) and your "About you" answers (sex, age,
  relationship status, career stage, height and weight if Physical is one of your life areas, religion).
  Every "About you" question has "Prefer not to say", so you never have to share these details.
- **Your vision board:** the photos you add from your library, pins from a Pinterest board you connect,
  photos you add from Unsplash (saved as links), captions, which goal each image is for, and the AI's short
  description of each photo (when the AI coach is on).
- **Coach chats**, your **profile picture**, your **settings**, and small app records (for example which day
  a celebration last played, or the day signs of distress were last noticed; see section 9).

This data stays on your phone. Deleting the app deletes it. If you back up your iPhone (iCloud or your
computer), Apple's backup may include it, under Apple's privacy policy.

## 2. The AI coach (optional)

The AI coach writes your chat replies, journal advice, journal analysis, morning advice, the Roast, goal
tips, suggested tasks, your goal-achieved message, and short descriptions of your vision board photos.

**It's off until you turn it on.** The first time, and whenever what's shared changes, the app shows
exactly what will be sent and asks you to agree. You can turn it off anytime in **Account → AI Coach**.

**What's sent when it's on:**

- your goals, tasks, streaks, check-offs and miss reasons
- your journal answers, and your journal notes unless you turn notes off (Account → AI Coach → Include
  journal notes)
- your vision board captions, which goal each image is for, and each vision board photo, once, so the coach
  can describe it
- your name, your onboarding answers and any "About you" details you shared, including sensitive ones
  like religion, height or weight if you entered them
- what you write to the coach in chat

When the coach answers a chat message, it also gives the message a general topic from a fixed list (like
"motivation" or "fitness"). Our server keeps only a weekly count per topic, never the message or who sent it
(see section 5).

The Roast uses your goals, tasks and your numbers (streaks, completion, counts). It never reads your journal's words.

**Who receives it:** our AI provider, **Anthropic** (the company that makes Claude), in the United States.
It travels through our server (see section 3), which passes it to Anthropic and doesn't keep it. Under
Anthropic's terms for business customers, Anthropic **does not use it to train its AI models** and deletes
it within 30 days, except when it must keep it longer to investigate misuse of its services or because the
law requires it. Anthropic's privacy policy: https://www.anthropic.com/legal/privacy

If we ever switch AI providers, the app turns the AI coach off and asks you again, naming the new provider,
before anything is sent to it.

**AI can be wrong.** The coach can make mistakes. It isn't a therapist, a doctor or a crisis service, and its
advice isn't medical, legal or financial advice.

## 3. Our server

Highva uses a server run on **Supabase** (hosted on Amazon Web Services in the United States, Ohio region).
It does these things:

- **An anonymous account.** The first time the app contacts our server, it creates an account with a
  random ID. It has no name, email or password. That happens when the app checks which AI provider to name
  on the AI coach screen (before you decide), when the AI coach is on, or when you use Explore. If you say
  "Not now" to the AI coach, nothing of yours is sent to the AI.
- **Daily limits.** To keep the service fair and affordable, the server counts how many times a day each
  account uses each AI feature (and how much AI processing it used), and how many photo searches it makes.
  These counts are kept with the random ID. **Usage counts are deleted automatically after 90 days**, and
  anonymous accounts that haven't been used for 12 months are deleted with everything linked to them.
- **Passing requests along.** AI requests go through it to Anthropic, and photo searches go through it to
  Unsplash. The **content of these requests isn't stored or logged.**
- **Anonymous totals** (section 5): counts with no account ID attached.
- **Subscriptions** (section 6): your subscription's status and history, kept with the random account ID, so
  Premium works and so we can count trials and cancellations.

Like most online services, the hosting provider keeps short-lived technical logs (for example the time of
a request and the network address it came from) for security and to fix problems.

## 4. Product analytics (PostHog)

To learn which parts of Highva help people and where they get stuck, the app sends **usage events** to
**PostHog** (PostHog, Inc., United States; we use its US data center). It's **on by default**, and you can
turn it off anytime in **Account → Privacy → Share usage analytics**. When it's off, nothing about how you
use the app is sent.

**What's sent:**

- which screens you open (as the screen's type, like "a goal page", never which goal), and actions like
  creating a goal, checking off or missing a task (with the reason you picked: no time, forgot, low energy,
  other), saving a journal entry, opening the vision board, or viewing the paywall
- numbers and yes/no details about those actions, like how many tasks a new goal has, its category (such as
  "Physical"), how many priorities a journal entry has, whether a note was written, or how many days since
  you started
- which onboarding screens you saw, whether you allowed notifications, which plan you picked on the
  paywall, and whether the AI coach is on
- technical details: the app version, your iPhone model (like "iPhone 16"), iOS version, language, time zone,
  and a **random analytics ID** the app makes (not your name, email or Apple ID)

**What's never sent to PostHog:** what you write anywhere in the app (journal notes, chat messages, typed
priorities, captions), your goal names, your task titles, your name, your photos, and your "About you"
answers (sex, age, relationship status, career stage, height, weight, religion). The app only sends events
and values from a fixed, pre-approved list, and checks every event before it leaves your phone.

**Also not used:** no session recording or screen recording, no tracking of where you tap, no crash reports
that could include text, and no advertising. No event ever records that crisis resources were shown.

PostHog is set to **discard your network (IP) address**. It may still estimate an approximate country from
it before discarding it. We keep analytics events for up to one year. To have analytics data about you
deleted, email support@highva.app with the analytics ID shown in **Account → Privacy → What's counted**.
PostHog's privacy policy: https://posthog.com/privacy

## 5. Anonymous totals

Our server also keeps a few **anonymous totals**: counts with no account ID, no text and no exact dates
(weeks or months at most). We never show a group of fewer than 10 people.

- **Task topics.** When you add a task, the app sorts it **on your phone** into a general topic (like
  "exercise", "reading and learning" or "money and finances") using a built-in word list, and sends only the
  topic. Tasks picked from Highva's built-in suggestions are counted by that suggestion. **Your task's words
  never leave your phone.**
- **Coach topics.** When the AI coach is on, each chat message gets one general topic (like "procrastination"
  or "fitness") from a fixed list, and our server adds 1 to that week's count. Nothing is counted for a
  message that showed crisis resources, or while the coach is in its gentler mode.
- **About-you totals (only if you opt in).** If you switch on **"Count my answers in Highva's anonymous
  totals"** (on the About-you screen or in Account → Privacy; **off by default**), the app sends your answers
  as broad groups (for example an age group like 25–34, never your exact age or your height and weight) at a
  few moments (when you finish onboarding, after a week, after a month, when a trial starts, and once a
  month while you use the app). They're counted on their own and next to simple usage facts (like goal
  categories or whether you're on Premium), never two "About you" answers together. This includes religion
  only if you opt in.

Totals and analytics are on by default except the About-you totals, which need your opt-in. Turning off
**Share usage analytics** stops task and coach topics too. Because totals aren't linked to anyone, they can't
be deleted for one person, and they stay if you delete your data.

## 6. Purchases and subscriptions

Highva Premium is sold through **Apple's App Store**. Apple handles payment; we never see your card or Apple
ID. We use **RevenueCat** (RevenueCat, Inc., United States) to manage subscriptions. RevenueCat and our server
receive purchase details from Apple: the product, transaction IDs, dates (start, trial, renewal, expiry),
price and currency, cancellation reason when Apple gives one, and the random account ID. We use them to
unlock Premium and to count trials, renewals and cancellations. Subscription events are also sent to PostHog
with your random analytics ID. RevenueCat's privacy policy: https://www.revenuecat.com/privacy

## 7. Other services the app connects to

- **Unsplash** (suggested photos on the Explore page): your search words go to Unsplash through our server.
  Searches are built from your goals' life areas and can reflect "About you" details you shared (for example
  an age group, or a place of worship for your religion). No name or account is sent. The photos load
  straight from Unsplash's servers, and when you add one, Unsplash is told it was added, as its rules
  require. Unsplash's privacy policy: https://unsplash.com/privacy
- **Wikipedia and Wikimedia Commons** (quote authors' photos and facts, Habits of the Greats): the app asks
  Wikipedia for the person's page and loads their photo. Only the person's name is sent. Wikimedia's privacy
  policy: https://foundation.wikimedia.org/wiki/Policy:Privacy_policy
- **Pinterest** (only if you connect a board): the app loads that public board's feed and its images from
  Pinterest. Pinterest's privacy policy: https://policy.pinterest.com/privacy-policy

These services can see your device's network address when the app connects to them, like any website you
visit.

## 8. Notifications

Morning briefings and evening reminders are scheduled **on your phone** (no notification server). They can
show your tasks, your top priorities and coaching advice on your lock screen. You can change what's shown in
your iPhone's notification settings, or turn them off in Account → Notifications.

## 9. Crisis safety

If something you write in the coach chat or your journal shows signs that you may be in crisis, the app
shows crisis resources (such as 988 in the US). This check happens on your phone. When the AI coach is on,
the AI can also notice it. The app then remembers **only the date** on your phone, for a week of gentler
coaching. This isn't reported to us or anyone else, and it's never counted in analytics or totals.

## 10. What we don't do

- We don't sell your personal information.
- We don't show ads or share your data for advertising.
- We don't use advertising tools, and we don't track you across other companies' apps or websites. Our
  analytics (section 4) only counts how Highva itself is used, and is never combined with data from others.
- We don't record your screen or sessions.
- We don't use your data to train AI models, and neither does our AI provider.

## 11. Your choices and rights

- **AI coach:** turn it off anytime (Account → AI Coach). Nothing more is sent after that.
- **Analytics:** turn off **Share usage analytics** anytime (Account → Privacy). **About-you totals:** off
  unless you switch them on (Account → Privacy).
- **Journal notes:** keep them out of what the coach sees (Account → AI Coach → Include journal notes).
- **About you:** change any answer, or pick "Prefer not to say" (Account → Your answers).
- **Photos:** remove vision board photos anytime; Highva only accesses the photos you choose.
- **Delete your data:** delete the app to remove everything stored on your phone. To delete your anonymous
  account, its usage counts and its subscription records on our server right away, tap **Account → Privacy →
  Delete my server data** (this also turns the AI coach off and gives the app a new analytics ID).
  Otherwise they're deleted automatically (see section 3). Analytics already sent to PostHog: email us with
  your analytics ID (section 4). Your App Store purchase history stays with Apple.
- **Your rights:** depending on where you live (for example under the GDPR in Europe or privacy laws in
  California), you may have the right to access, correct, delete or get a copy of your personal data, to
  object to or limit its use, and to withdraw consent. Since almost all of it is on your phone, you can do
  most of this in the app. For anything else, email support@highva.app. You can also complain to your local
  data protection authority.

**Why we use your data (legal bases, for the GDPR):** to provide the app you asked for; with your consent
for the AI coach, for About-you totals, and for any sensitive details you choose to share (you can withdraw
it anytime); and our legitimate interest in keeping the service secure and affordable (daily limits,
technical logs) and in understanding how the app is used to improve it (product analytics and anonymous
totals, which you can turn off).

## 12. Children

Highva isn't meant for children under 13, and we don't knowingly collect data from them. If you think a
child has used Highva, use **Delete my server data** on their phone, or contact us.

## 13. Security

Connections to our server and our providers are encrypted (HTTPS). The keys for the AI provider and Unsplash
are kept on our server, never in the app. (The app does contain PostHog's project key, which can only send
events, not read them.) Our server's database only accepts requests from our own server
code. Your on-phone data is protected by your iPhone's own security (your passcode and Face ID).

## 14. Changes

If we change this policy, we'll update the "Last updated" date at the top. If a change affects what's sent to
the AI coach, the app will ask for your agreement again before sending anything new.

## 15. Contact

Questions or requests: **support@highva.app** (subject "Highva Support").

When you email us, we receive your email address and whatever you write. If you use **Send feedback** (Account
→ Help & support), the email draft also includes, at the bottom, the app version, your iPhone model and your iOS
version, to help us fix problems. Nothing else is added (no name, goals or journal), and you can delete those
lines before sending. We use emails only to answer you and improve Highva.
