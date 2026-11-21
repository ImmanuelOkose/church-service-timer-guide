# Release notes

What changed in each version of Church Service Timer, newest first, in short. Update every phone, tablet and PC your team uses to the same version: from 0.28, program files, backups and sent programs can't be opened by 0.27 or earlier.

## 0.35.0 · 21 November 2026

**Full screen**

- **Gestures in full screen.** Double tap or double-click the right third of the screen for the next segment, the middle to pause or resume, and the left third to undo the last segment change. Each asks first, in the same small card as the keys and buttons. See [Second screen and full screen](second-screen-and-full-screen.html).
- **A control tray in full screen.** A single tap or click, a swipe up from the bottom edge, or the mouse at the bottom of the screen brings up a small tray: Pause or Resume, Next, −2 min, +2 min, Undo, Cues, Clock, Blank, End service and Exit. Every timer action in it still asks first. It hides after 6 seconds; Esc, Back or a swipe down puts it away. Nothing of it is sent to any stage screen.
- **Full screen stays on the end screen.** However the service ends, full screen stays open and shows the end screen, or the clock. The timer buttons grey out, while Cues, Clock, Blank and Exit keep working. It closes when the next service is set up.
- **Lock controls blocks all of it.** With the controls locked, the gestures and the tray do nothing, and a tap still shows Hold to unlock.

**On a PC**

- **A clearer line in Ready.** With a pre-service start time set, the line now reads "Timing has not started. The display shows the pre-service countdown until you start the first segment." in every layout.
- **Ready shows the timer you will have.** A service that is loaded but not started now shows each desktop layout's own timer, at the size and in the place it has once running, with the first segment's full time and not counting. The Ready form sits where the timer controls go. Keys shows its own strip in Ready. See [Run the service from a PC](run-the-service-from-a-pc.html).
- **The ring fills the middle pane at every window size** in Three panes and The dial, not only from 1920 × 1080, and Mission control's dial grows into spare height. A laptop, or a PC with display scaling, no longer has empty space above and below the ring.
- **The line of keys shows on laptop screens too.** Three panes and The dial now list the keys along the bottom wherever there is room, not only in a window 800 high: every common screen from 1280 × 720 up, 1366 × 768 and 1270 × 790 included. Only a window 600 high leaves it out.
- **Classic fits a laptop window.** In a window 1200 or more wide and less than 1000 high, Classic puts the controls beside the ring, so they are in view without scrolling.
- **Classic looks right in a window under 1200 wide,** which uses Classic whatever the choice: a 1366 × 768 screen at 125% scaling, or a 1024 × 768 screen. The ring is larger, under the segment's name or beside it, and the card fills the height. **Custom** stays on one line, the preview heading shortens to **PREVIEW** where it must, and cue names no longer break in the middle of a word.

**On every device**

- **No end screen: show the clock.** A program can end on the clock. In the Program editor the end screen card is now **When the service ends**, with **End screen** or **Clock**. **Settings › Display settings › Default end screen** has the same choice for new programs and Quick timers. With Clock, every display shows the clock when the service ends, Live says **Showing the clock**, and the End service question says so. See [Finish and hand over cleanly](finish-and-hand-over-cleanly.html).
- **Check for updates automatically.** A new switch in Settings › About, off to begin with. When on, the app checks at most once a day and never during a service, and a newer version shows a notice on Live with **See update** and **Not now**. Nothing is downloaded or installed without asking. See [Get started on Android](get-started-on-android.html).
- **The time on screens holds still, before the service too.** The countdown to a scheduled start, and the clock shown before it, no longer shift or change size each second on stage screens, the second screen, full screen, web screens and the Stage simulator. On a PC these screens, and the large time in the mini timer, now use the app's own font.
- **Release notes say how to install on Windows.** The lines under each release's notes now say which file is for Android and which for Windows, what to do if Windows says "Windows protected your PC", and that a PC on 0.34.0 or later can use **Download and install** instead.

**Keep every device on the same version**

- A backup or program file in which a program, or the default, is set to end on the Clock needs 0.35 or later to open. A paired phone or tablet on an earlier version still shows the clock.

## 0.34.0 · 21 November 2026

**Before and during a service**

- **Check this service.** One button runs a whole program through on the Simulator in about 18 seconds and lists every warning that fires, and any that cannot. Nothing reaches the stage and no report is saved. See [Build a reusable program](build-a-reusable-program.html).
- **Up next on stage screens.** A screen set to **Timer and up next** says who is next and for how long, such as "Next: Response · Worship team · 6 min 30 s". See [Pair a phone or tablet](pair-a-phone-or-tablet.html).
- **Full screen on the device running the service.** When your own screen is the one people watch, Live can show the stage countdown on it, with **F11** on a PC. A phone or tablet turns to landscape and turns back when you leave. Every timer action still asks first, in a small card over the stage. See [Second screen and full screen](second-screen-and-full-screen.html).
- **No warning the moment a segment starts.** A warning fires only when the countdown comes down to its time, so a 5-minute segment no longer begins with 5 MIN LEFT. TIME'S UP at 0:00 still fires at zero.
- **Choose what the Simulator simulates:** an LED sign or a stage screen. The chip reads **LED simulator** or **Stage simulator**. See [Choose the right display](choose-the-right-display.html).

**Cues and warnings**

- **New cues and warnings to start with:** seven cues on keys 1 to 7 (WRAP UP, TIME'S UP, SPEAK UP, SLOW DOWN, MIC OFF?, FINAL SONG and SEE ME) and four warnings (5 MIN LEFT, 2 MIN LEFT, WRAP UP and TIME'S UP). Cues and warnings you changed are left alone. See [Prepared cues and automatic warnings](prepared-cues-and-automatic-warnings.html).
- **Cues on screens.** A cue can have a colour (White, Amber, Red, Green or your theme's colour), sit in a **banner at the top or bottom** while the countdown stays in view, **wrap** onto up to 3 lines, and scroll at its own **Speed on screens**. A coloured cue that fills the screen sits on warm charcoal with a band of its colour. The LED sign is not changed by any of it.
- **Five new effects:** Flash then hold, Pulse, Slide in, Countdown bar and Screen flash. Flash and Pulse show long text a few words at a time; Slide in, Countdown bar and Screen flash scroll on the LED sign when the text is too wide for it.
- **A clearer cue editor.** The **LED sign | Stage screen** switch over the preview also chooses which settings are shown, and the panes beside Stage cues and Warnings & alerts show what your display will show.
- **A clearer warning editor,** set out as When, What it shows, Where, How long and On or off: two columns on a PC, the whole screen on a phone. "Operator + phone notification" is now **Operator only**.
- **Smoother scrolling cues** on a second monitor, web screens and the simulators.

**On a PC and a tablet**

- **Install an update from the app.** On Windows, **Check for updates** offers **Download and install**. The installer is checked, and started only after you confirm. The Windows installer is now published beside the Android app. See [Get started on Windows](get-started-on-windows.html).
- **Tablet layout.** A 10-inch or larger tablet in landscape gets the wide layouts, under **Settings › Tablet layout**. Phones no longer show a desktop layout setting.
- **Mission control is the layout a new install starts in.** If you already use the app, your layout stays as it is.
- **Live makes better use of a large screen** in every desktop layout except Keys.
- **See the second screen on Live.** While the stage shows on a projector or second monitor, the Display preview holds a small live copy of it.
- **The mini timer button is at the top of every page,** and the mini timer opens with no service running, showing the time of day. **Click the app's name, the service's name or your church's name** on any tab to go back to Live.
- **More keys listed.** The line of keys includes **J Jump to segment**, and Three panes and The dial list the keys too.
- **Clicker and foot pedal works on a PC.** Switched off, Space, B, Page Down and → do nothing, from a clicker or the keyboard. See [Keyboard, clicker and Commands](keyboard-clicker-and-commands.html).
- **A calendar for the reports date filter** on a PC, with ready-made ranges and a dot on each day that has a report. See [Read, export and print reports](read-export-and-print-reports.html).
- **Dates and times the way the app writes them:** "Fri 20 Nov 2026", 20/11/2026, a 24-hour clock, and weeks that start on Monday.
- **Fixed:** the buttons under the Keys rundown in a 1200 × 600 window, and **New program** jumping into place on Programs.

**Keep every device on the same version**

- A backup or program file with any of the new cue settings (a colour, a banner, wrapped text, its own screen speed, a new effect, long Flash or Pulse text, or more than six cues) needs 0.34 or later to open.
- A paired phone or tablet on an earlier version shows every cue in white and full screen, with the new effects as steady text.

## 0.33.0 · 19 November 2026

- **The second screen is on Live.** One line and one button under the display preview: **Show on second screen** or **Stop**. The app remembers the screen, can open it when a service starts, and lets you choose what it shows.
- **Keyboard shortcuts and a clicker test.** **?** or **F1** lists every key. **Settings › Warnings & alerts › Test a clicker or pedal** names the key each button sends, on phones, tablets and PCs. See [Keyboard, clicker and Commands](keyboard-clicker-and-commands.html).
- **The countdown beside the Windows clock** while a service runs: point at the icon to read the time, click it to bring the app forward.
- **Check for updates** in Settings › About. It checks only when you press it.
- **Drop a program file on the window** to import it on a PC, and **print from the Live home**.
- **Fixed:** the second screen and the app's window on PCs whose screens use different scaling in Windows, and a stage countdown that shifted slightly each second.

## 0.32.0 · 19 November 2026

- **Pages use the room in a wide window:** the Live home before a service, Settings in two columns with previews, Screens & devices in three areas, Reports and the Program editor. Phones look exactly as before.
- **Dialogs, not sheets,** for Quick timer, Print, Export, Version history, Segment library, Recover time and Edit upcoming on a PC.
- The app says "click" on a PC where a phone says "tap".
- **Warnings on a PC are silent again.** Turn on **Play the Windows notification sound** if you want the sound. See [Get started on Windows](get-started-on-windows.html).

## 0.31.1 · 19 November 2026

- **Desktop layout is easier to find:** it has its own row in Settings, and searching Settings for "layout" finds it.

## 0.31.0 · 19 November 2026

- **A Windows version.** The same app on a Windows 10 or 11 PC, with the same programs, reports and backups. It has a resizable window, keyboard keys that each ask before they act, a **second screen** for a projector, silent warnings, and it keeps the PC awake during a service. See [Get started on Windows](get-started-on-windows.html).
- **Desktop layouts** for a wide window: **Three panes**, **Mission control**, **The dial**, **Keys** and **Classic**, with **Saved looks**. See [Run the service from a PC](run-the-service-from-a-pc.html).
- **Number keys send cues**, **Commands (Ctrl+K)** lists everything you can do now, and more keys work on Live.
- **Mini timer** on Windows: a small window that stays on top of your slides.
- **Programs and Reports use the whole window** on a PC.
- **A stage screen that joins is no longer left waiting without a reason:** Live offers **Show on stage screens**.

## 0.30.1 and 0.30.2 · 11 November 2026

- **A new app icon:** a countdown ring that ends in a cross.
- **Privacy policy** row in Settings › About, and **Guided practice** opens Live when started from About.

## 0.30.0 · 10 November 2026

- **Quick timer.** A single countdown for a prayer meeting, a break or a talk, started from Live with no program and no Ready step. Choose 5, 10, 15, 30 or 45 min or a custom length, and optionally a name. Nothing is saved unless you turn on **Save as a report**. See [Operate a live service](operate-a-live-service.html).
- **Swipe between tabs.** Swipe left or right to move between Live, Programs, Reports and Settings; each tab keeps its place. Live stays put while a service is loaded or running.
- **Logo and banner crop what you frame**, and keep a transparent background.
- **Print options you can always tick.** Ticking the watermark or banner turns Ink-saving off.
- **Themes.** Graphite and Paper & Ink are back to their original colours, and **Paper & Ink (blue)** is new.

## 0.29.0 · 9 November 2026

- **Church logo**, cropped square, shown at the top of every page; the banner is cropped to 3:1 in the app.
- **Reports speak one language:** "On time", "4 min over", "4 min under", a **Last live service** tile, dates under each bar of the graph, and **Print report** in the report's summary card.
- **Lengths of time in words** everywhere ("45 min", "5 min 30 s"); running timers stay as clocks.
- **Guided practice** points to each control as you go, and an invitation on Live offers it to new operators.
- Settings, Programs, Live, pairing and web screens tidied throughout, with UK spelling and sentence case.

## 0.28.0 · 8 November 2026

- **Requests from the stage** work in landscape.
- **About › Your data** explains what the app keeps on the phone.
- A clearer **paired operator view** and program editor.

## 0.27.0 · 7 November 2026

- **Guided practice:** a built-in practice service with a coach card, on the Simulator, that saves nothing.
- **Requests from the stage** (off by default): a presenter can quietly tap **Need 2 minutes**, **Ready to finish** or **Microphone issue** on a stage screen, and the operator answers on Live.
- **Join slide** in several sizes, a steady colon on the LED sign, and **Exit full screen** on stage screens.

## 0.26.0 · 7 November 2026

- **Web screens:** any browser on the same Wi-Fi (laptop, smart TV, tablet) can show the timer, using an easy `.local` name, a QR code or the phone's address, with a guest code or team code. Styled quick messages and scrolling text work there too. See [Pair a phone or tablet](pair-a-phone-or-tablet.html).
- **Network changes:** while sharing, the host shares again by itself at a new address, for example when its hotspot is turned on.
- **Programs:** send a program to a paired phone, version history, a segment library, and import from any spreadsheet.
- **Share** programs and reports by Bluetooth, messaging or email, and open files sent to you.
- **Change program in Ready**, and Back twice to leave the app.

## 0.25.0 · 5 November 2026

- **Settings PIN**, to stop accidental changes to Settings.
- **Saved passwords in backups**, optional, encrypted with a passphrase you choose.
- **Pre-service countdown** to a scheduled start, and **clicker and foot-pedal** support.
- **Wi-Fi rejoin** for paired phones, a faster start, reworked Settings pages, **Screens & devices**, and five new themes.

## 0.24.0 · 5 November 2026

- **Lock-screen controls:** the notification shows the current segment with a live countdown, and Pause and Next segment.
- **Watch-friendly warnings**, a **battery check** before the service, and reconnecting indicators.
- **Review notes** on reports, and **delete selected** reports.

## 0.22.0 · 4 November 2026

- **Live redesign.**
- A new Android application ID, so 0.22 installs alongside earlier builds: move your setup across with **Backup & restore**.

## 0.19.0 to 0.21.0 · 26 October 2026

- **Show clock** in 12- or 24-hour format, messages after a service, and **Jump to segment**.
- Durations to the second (each segment up to 59 min 59 s), bulk program export and import, and press-and-hold menus.
- **Layout density**, high contrast, reduced motion and divider styles.
- **Export selected** programs, and **Reconnect display**.

## 0.18.0 and earlier

The handbook was first written for 0.18.0. Earlier versions were prototypes.
