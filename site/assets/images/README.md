# Screenshot provenance

These PNG files come from reviewed automated app previews in Church Service Timer's test/goldens directory. The whole set was refreshed for the 0.34.0 handbook from the previews on the app's main branch, and again once the new starting cues, warning editor, cue effects, Check this service and the PC update had been added. They illustrate example states with sample data and do not show real phone or PC sessions. No live pairing code or QR, revealed password, raw device log, or user-supplied photograph is included.

Every file was re-compressed without loss (oxipng), so the pixels match the preview. Three files differ from a plain copy, as noted in the second table. reports-desktop.png and mini-timer.png were not rendered again in the second refresh; the screens they show had not changed.

For the 0.35.0 handbook, every file in both tables was compared, pixel for pixel, with the preview on the app's main branch (6d3f0c6). Thirteen had changed and were copied again: program-editor.png, stage-layout.png, desktop-mission-control.png, desktop-mission-control-large.png, second-screen-live.png, full-screen-confirm.png, stage-simulator.png, shortcuts.png, commands.png, cue-banner.png, cue-editor-switch.png, stage-cues-desktop.png and desktop-three-panes-laptop.png. Six more were added for the clock in place of an end screen, Classic in a narrow window and the line of keys on a laptop. Before those, twelve were added: the full-screen tray on a PC and a phone, About with the automatic check on a phone and a PC, the update notice on Live on a phone and a PC, Ready in each of the five desktop layouts, and Three panes in a laptop-sized window. All of these were re-compressed without loss with Pillow, as oxipng was not to hand, and each was checked to match its preview pixel for pixel. The version numbers they show ("0.33.0 is available", "Version 0.0.0 (test)") are sample data.

For the 0.36.0 handbook, every file in both tables was compared, by its pixels, with the preview on the app's main branch (release 0.36.0, cb2602b). Fifteen had changed and were copied again: full-screen-tray-phone.png, full-screen-tray.png, desktop-mission-control.png, desktop-mission-control-large.png, desktop-three-panes.png, desktop-three-panes-1366.png, desktop-dial.png, desktop-keys.png, desktop-ready-keys.png, second-screen-live.png, stage-simulator.png, shortcuts.png, commands.png, desktop-classic-narrow.png and desktop-classic-1024.png. The rest matched. desktop-classic.png, scaled from its preview, was compared after scaling and matched. reports-desktop.png and mini-timer.png are rendered for the handbook and were not rendered again. Five were added: whats-new-notice.png and whats-new-notice-pc.png (the Updated to notice), full-screen-tip-phone.png and full-screen-tip.png (the gestures tip), and send-message-stage.png (Send message with the switch on Stage screen). All were saved without changing a pixel and re-compressed without loss with Pillow. The version in the notice, 0.36.0, is the release itself.

For the 0.37.0 handbook, every file in both tables was compared, by its colour values (red, green, blue and alpha, not only its size), with the preview on the app's main branch (release 0.37.0, 70094f6). Seventeen had changed and were copied again: stage-layout.png, appearance.png, screens-devices.png, full-screen-tray-phone.png, full-screen-tip-phone.png, send-message-stage.png, desktop-three-panes.png, second-screen-live.png, second-screen-settings.png, full-screen-confirm.png, full-screen-tray.png, stage-simulator.png, cue-banner.png, cue-editor-switch.png, default-end-screen-pc.png, full-screen-tip.png and stage-cues-desktop.png. The rest matched. desktop-classic.png, scaled from its preview, was compared after scaling and matched. reports-desktop.png and mini-timer.png are rendered for the handbook; their previews have not changed since 0.36.0, so they were not rendered again. Twenty-one were added, listed in the third table. All were saved without changing a pixel and re-compressed without loss with Pillow.

For the 0.38.0 handbook, every file in the tables was compared, by its colour values (red, green, blue and alpha, not only its size), with the preview on the app's main branch (release 0.38.0, 596491e). The navigation has a new tab, Slides, so most screens that show it had changed. 35 were copied again: live.png, standing-by.png, practice.png, reports.png, update-notice.png, whats-new-notice.png, send-message-stage.png, desktop-mission-control.png, desktop-mission-control-large.png, desktop-live-home.png, desktop-three-panes.png, desktop-dial.png, desktop-keys.png, desktop-ready-mission-control.png, desktop-ready-three-panes.png, desktop-ready-dial.png, desktop-ready-keys.png, desktop-ready-classic.png, desktop-three-panes-laptop.png, second-screen-live.png, stage-simulator.png, shortcuts.png, commands.png, desktop-classic-narrow.png, desktop-classic-1024.png, desktop-three-panes-1366.png, update-notice-pc.png, whats-new-notice-pc.png, programs-desktop.png, reports-dates.png, finish-console-live.png, finish-denim-live.png, papery-live.png, keep-awake.png and send-message-too-wide.png. desktop-classic.png, scaled from its preview with Lanczos resampling, was compared after scaling and had changed, so it was scaled again. reports-desktop.png, which is rendered for the handbook, was rendered again from the same fixture as desktop-date-range.png without the calendar open (only the header with the tabs differs from the old file); it now shows five tabs. The rest matched. mini-timer.png has no navigation and its preview has not changed, so it was not rendered again. Twelve were added, listed in the fourth table. All were saved without changing a pixel and re-compressed without loss with Pillow. slides-live-button.png keeps the preview's transparency (the header on a phone is partly see-through), so it is saved with its alpha channel; the others are RGB.

## Phone and tablet

| Public filename | Original fixture |
| --- | --- |
| live.png | phone-live.png |
| program-editor.png | program-editor.png |
| choose-display.png | display-destination-chooser.png |
| stage-layout.png | stage-up-next-1080.png |
| cues.png | settings-stage-cues.png |
| warnings.png | warnings-settings-phone.png |
| quick-message.png | quick-message-composer.png |
| seen.png | stage-seen-request.png |
| recover-time.png | recover-time-review.png |
| standing-by.png | standing-by-last-report.png |
| report.png | report-detail-phone.png |
| print.png | print-service-sheet.png |
| appearance.png | appearance-phone.png |
| practice.png | practice-coach.png |
| church-profile.png | church-profile-custom-phone.png |
| reports.png | report-list-phone.png |
| screens-devices.png | settings-screens-devices.png |
| warning-editor-phone.png | warning-editor-phone.png |
| tablet-layout.png | layout-setting-tablet.png |
| about-auto-update.png | auto-update-about-phone.png |
| update-notice.png | update-notice-live-phone.png |
| full-screen-tray-phone.png | host-full-screen-tray-phone.png |
| no-end-screen-phone.png | no-end-screen-editor-phone.png |
| whats-new-notice.png | whats-new-notice-live-phone.png |
| full-screen-tip-phone.png | host-full-screen-tip-phone.png |
| send-message-stage.png | send-message-stage-phone.png |

## PC (wide window) and stage

| Public filename | Original fixture |
| --- | --- |
| desktop-mission-control.png | desktop-mission-control-1080.png |
| desktop-mission-control-large.png | desktop-mission-control-1440.png |
| desktop-live-home.png | desktop-standing-by-1080.png |
| desktop-three-panes.png | desktop-three-panes-1080-paper.png |
| desktop-dial.png | desktop-dial-1080.png |
| desktop-keys.png | desktop-keys-1080.png |
| desktop-classic.png | desktop-classic-1440.png, scaled from 2560 × 1440 to 1920 × 1080 |
| desktop-layout-settings.png | desktop-layout-settings.png |
| desktop-ready-mission-control.png | desktop-mission-control-ready-1080.png |
| desktop-ready-three-panes.png | desktop-three-panes-ready-1080.png |
| desktop-ready-dial.png | desktop-dial-ready-1080.png |
| desktop-ready-keys.png | desktop-keys-ready-1080.png |
| desktop-ready-classic.png | desktop-classic-ready-1080.png |
| desktop-three-panes-laptop.png | desktop-three-panes-ready-1270.png (1270 × 790, the window a 1920 × 1200 screen gives at 150% scaling) |
| second-screen-live.png | desktop-second-screen-live.png |
| second-screen-settings.png | desktop-screens-devices.png |
| full-screen-confirm.png | desktop-host-full-screen-confirm.png |
| full-screen-tray.png | desktop-host-full-screen-tray.png |
| stage-simulator.png | desktop-stage-simulator-live.png |
| shortcuts.png | desktop-shortcuts-sheet.png |
| commands.png | command-palette.png |
| clicker-test.png | desktop-clicker-test.png |
| cue-on-screens.png | desktop-cue-editor-screens.png |
| cue-banner.png | stage-cue-amber-banner.png |
| cue-effects.png | desktop-cue-effect-list.png |
| cue-editor-switch.png | desktop-cue-stage-preview.png |
| cue-red-full.png | stage-cue-red-full.png |
| cue-wrapped-bar.png | stage-cue-wrapped-bar-1080.png |
| warning-editor.png | warning-editor-desktop-1920.png |
| service-check.png | desktop-service-check.png |
| update-pc.png | desktop-update-available.png |
| about-pc.png | desktop-settings-about.png |
| no-end-screen-pc.png | desktop-no-end-screen-editor-1366.png |
| default-end-screen-pc.png | desktop-settings-display-end-screen.png |
| desktop-classic-narrow.png | desktop-classic-1154.png |
| desktop-classic-1024.png | desktop-classic-1024.png |
| desktop-three-panes-1366.png | desktop-three-panes-1366.png |
| update-notice-pc.png | update-notice-live-1366.png |
| whats-new-notice-pc.png | whats-new-notice-live-1366.png |
| full-screen-tip.png | host-full-screen-tip-1920.png |
| stage-cues-desktop.png | desktop-settings-stage-cues-stage-screen.png |
| warnings-desktop.png | desktop-settings-warnings.png |
| programs-desktop.png | desktop-programs.png |
| reports-dates.png | desktop-date-range.png |
| reports-desktop.png | Rendered for the handbook by the fixture behind desktop-date-range.png (the same sample reports, dated 2026), without the calendar open |
| mini-timer.png | Rendered for the handbook by the fixture behind mini-timer.png, at twice the pixel density (760 × 300) |

## Added for 0.37.0

| Public filename | Original fixture |
| --- | --- |
| flip-clock.png | flip-clock-wide-12h.png |
| flip-clock-24h.png | flip-clock-wide-24h.png |
| flip-clock-phone.png | flip-clock-phone-12h.png |
| layout-timer-only.png | countdown-timer-wide.png |
| layout-segment-name.png | countdown-current-wide.png |
| layout-up-next.png | countdown-next-wide.png |
| layout-up-next-only.png | countdown-only-wide.png |
| stage-warning.png | countdown-warning-wide.png |
| stage-overtime.png | countdown-overtime-strong-wide.png |
| stage-light-theme.png | countdown-light-current-wide.png |
| layout-tiles.png | layout-tiles-desktop.png |
| layout-tiles-phone.png | layout-tiles-phone.png |
| overtime-alert.png | desktop-settings-display-overtime.png |
| finish-tiles.png | finish/appearance-finish-dark-1366.png |
| finish-tiles-phone.png | finish/appearance-finish-light-phone.png |
| finish-console-live.png | finish/live-console-subtle-light-phone.png |
| finish-denim-live.png | finish/live-denim-subtle-light-phone.png |
| papery-live.png | finish/papery-paper_ink-full-live-phone.png |
| papery-appearance.png | finish/papery-appearance-note-paper_ink.png |
| keep-awake.png | desktop-settings.png |
| send-message-too-wide.png | send-message-wide-static-stage-phone.png |

## Added for 0.38.0

| Public filename | Original fixture |
| --- | --- |
| slides-page.png | lyrics-page-1366.png |
| slides-page-phone.png | lyrics-page-phone.png |
| slides-add-song.png | lyrics-add-song.png |
| slides-bible-verse.png | lyrics-scripture.png |
| slides-announcement.png | lyrics-announcement.png |
| slides-aurora.png | lyrics-slide-aurora.png |
| slides-photo.png | lyrics-slide-photo-northern-lights.png |
| slides-linen.png | lyrics-slide-linen.png |
| slides-backgrounds.png | lyrics-backgrounds-1920.png |
| slides-live-button.png | lyrics-live-button.png |
| slides-live-button-pc.png | lyrics-live-button-1920.png |
| slides-countdown-corner.png | lyrics-chip.png |

## Adding or replacing an image

- Copy the preview, or render it from the app's own test fixtures. Do not edit the pixels.
- Look at it before publishing: no pairing code, QR, password, address of a real network or real person's name.
- Keep it PNG (the site's check allows nothing else), compress it without loss, and keep wide shots at 1920 pixels across unless the larger size is the point.
- Give it alt text that says what the screen shows; the site uses the same words as the caption.

Future photo placeholders: replace only with an authorized, credential-free photograph of the church's actual operator desk or stage screen. Keep captions explicit about examples versus real equipment.
