# Privacy policy

**Church Service Timer by I-Proton** · Last updated **10 November 2026** · Applies to the Android app, version 0.30.0 and later

Church Service Timer is a timer for running church services. It is built to work offline, on your church's own phones, screens and LED sign. This page explains, in plain words, what the app does with information. If anything here is unclear, write to us (see [Contact](#contact)).

## The short version

- **No account, no cloud, no ads, no tracking.** There is nothing to sign in to. The app contains no advertising, no analytics and no tracking of its own, and it does not send your services, programs or reports to us or to any server.
- **Your data stays on your phone.** Programs, service reports, review notes, cues, messages, settings, and your church's name, logo and banner are stored only inside the app on your phone.
- **It talks only to devices in the room.** The app connects to your LED sign, to phones and tablets you pair, and to browsers showing a web screen, all on the same Wi-Fi or hotspot.
- **You decide what leaves the phone.** Backups, exports, printouts, shared program files and feedback emails are only made when you choose to, and only go where you send them.

## What is stored on your phone

Everything you create in the app stays in the app's private storage on your phone:

- programs, segments, speakers and private operator notes, and their version history
- service reports, review notes and activity history
- prepared cues, quick message presets, warning settings and appearance
- your church's name, logo and banner
- the list of paired devices and saved LED signs

Some of this is protected further:

- **LED sign passwords** (its Wi-Fi password and its connection password) are stored encrypted, using Android's secure key storage.
- **The Settings PIN** is never stored as typed; only a salted hash of it is kept, so it cannot be read back.
- **Pairings** with other phones and tablets are stored encrypted.

## The local network: the sign, paired devices and web screens

To show the timer on stage, the app connects only to equipment on the same local network as the phone (your church's Wi-Fi or a hotspot). It does not need the internet for any of this.

- **The LED sign.** The app connects to the supported LED controller over its Wi-Fi to send the countdown, cues and messages.
- **Paired phones and tablets.** A phone or tablet joins with a six-digit code or a QR code, and you approve it on the host phone. After that, the two devices talk over an encrypted connection.
- **Web screens.** A browser on the same network (a laptop, smart TV or tablet) can show the timer by opening the phone's local address, for example `http://192.168.1.20:8080` or `http://your-phone-name.local:8080`, and entering a team code or guest code. The `.local` name is only announced on your local network, so devices elsewhere cannot see it.

Android's "Internet" permission is what allows these local connections; the app doesn't use it to reach online services.

## Permissions, and why the app asks for them

- **Location (precise and approximate):** Android only lets apps read the name of the Wi-Fi network you are on if they hold location permission. The app uses it to check that you are on your LED sign's network and to rejoin it. It never reads or stores where you are.
- **Nearby Wi-Fi devices, Wi-Fi and network state, change Wi-Fi state, Wi-Fi multicast:** Finding and joining the LED sign's Wi-Fi, finding paired devices, and announcing the `.local` name for web screens on your network.
- **Camera:** Only to scan a pairing QR code. No photos or video are taken or stored.
- **Notifications, foreground service, wake lock, exact alarms, vibrate:** Keeping the timer running during a service, warnings at the right moment, and the Pause and Next controls on the lock screen.

The app does **not** ask for access to your photos. When you choose a church logo or banner, Android's own file picker lets you pick one image, and the app keeps only the cropped copy.

## QR code scanning (Google ML Kit)

Scanning a pairing QR code uses Google's ML Kit, which reads the code on the phone itself. To keep it working well, ML Kit may send Google limited technical information: the device model and Android version, and performance and error information about the scanner. Google says this is encrypted in transit and not shared with third parties. Camera images and the contents of QR codes are processed on the phone and are not sent. This only happens when you use **Scan QR code instead**; pairing with the six-digit code doesn't use ML Kit. See [Google's ML Kit data disclosure](https://developers.google.com/ml-kit/android-data-disclosure) for details.

## Backups, exports and sharing

These happen only when you choose them, and the file goes only where you send it:

- **Backups** (Settings › Backup & restore) contain your programs, reports, cues and settings. Saved LED sign passwords are included only if you tick that option, and then they are encrypted with a passphrase you choose. Pairings and the Settings PIN are never included.
- **Exports** of programs and reports (CSV, JSON or PDF), **printouts**, and **programs sent to another phone** go only to the place, app or person you pick.

Files you share are then handled by the app or person you shared them with, under their own terms.

## Feedback and diagnostics

- **Feedback.** The Feedback centre opens your own email app with a message addressed to us. Nothing is sent until you press send in your email app. You can read and change everything first, including your contact details.
- **Diagnostics in feedback.** You can choose to attach diagnostics. You see them before sending. They contain app settings and error categories only (for example the display type, connection state and notification settings), not your programs, reports, notes or names.
- **Service metrics.** **Record service metrics** in Settings › Diagnostics measures how the app performs during one service. It records memory use, battery level and temperature, how smoothly the screen draws, timer accuracy, how promptly warnings fire, and reconnections. It is off until you turn it on, records one service, then switches itself off. It records no program, segment, church or people names, notes or messages, and stays on the phone unless you tap **Share recording**.

## Children

The app is a tool for church volunteers and staff and is not directed at children. It does not collect personal information from anyone.

## Keeping or deleting your data

Because your data lives only on your phone, you are in control of it:

- Delete programs and reports in the app at any time.
- Uninstall the app, or clear its storage in Android settings, to remove everything it has stored.

We hold no copy of your data, so there is nothing for us to delete. Emails you send us are kept only as long as needed to answer them; ask us to delete them at any time.

## Changes to this policy

If the app changes how it handles information, we will update this page and its "Last updated" date before the change is released.

## Contact

Questions about privacy, or anything in the app: **[immanuelproton@gmail.com](mailto:immanuelproton@gmail.com)**, or use the Feedback centre in the app (Settings › Feedback centre).
