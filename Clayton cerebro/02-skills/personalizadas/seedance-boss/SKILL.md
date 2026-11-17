---
name: "seedance-boss"
description: "Seedance 2.5 prompt system (Rick Miura/FilmBoss): film-like cuts, Higgsfield @tags, per-line acting, auto-splitting long scripts into ~30s parts. Use for any Seedance prompt, scene, take or roteiro."
---

# Seedance Boss — Seedance 2.5 Prompt Writer (Rick Miura / FilmBoss)

Use whenever the user wants a Seedance prompt, a cinematic shot or scene, to turn a script/roteiro/beat into video prompts, to split a long script, to set up or link Higgsfield tags, to use a previous take as reference, to edit or extend a video on Seedance, or asks about Seedance prompting. Trigger on "prompt pro Seedance", "Seedance 2.5", "Higgsfield", "tags", "cena", "take", "roteiro", "próxima parte", "continua", "edita esse vídeo", "make a scene where…", "build a shot". Always consult this skill before writing any Seedance prompt.

Turn scripts, scenes, and ideas into Seedance 2.5 prompts. Block, light, and pace each shot like a film. The goal is always a scene that looks like it was cut from a movie, never "a little video".

**Output: always a single standalone prompt in a code block — English only inside the block, nothing else (no title, no notes, no translation), so one click copies exactly the prompt.** Any context, note or Portuguese translation goes outside the block.

This file has two layers: the **validated base** (everything up to CAMERA / LIGHT / COLOR) and the **BOSS LAYER** of house rules below it. Read both before writing. Long playbooks (splitting, series continuity, tags onboarding, previous-take reference, video editing, music when asked) live in the **PLAYBOOKS appendix** at the end of this file.

---

## CORE PRINCIPLE: WRITE THE VISIBLE

The model reacts to what can be **seen and measured**, not to mood words.

Translate every abstraction into something observable.
- ❌ "tense scene" → ✅ "man freezes, slowly clenches his fist, light only from the side, half his face in shadow"
- ❌ "cool cinematic shot of a car, epic, fast" → ✅ "low tracking shot alongside the car as it powers through a wet curve, headlights glowing, spray off the tyres, hard buffeting camera shake"
- ❌ "make the movement more natural" → ✅ "the body undulates like a worm in the air with every wingbeat; right after surfacing it shakes its head like a dog shaking off water, the twist traveling down the neck as a spiral wave"

Write in plain, clear, instruction-style language. Fewer precise words beat many vague ones.

**Lean on what 2.5 does well** — write these confidently instead of avoiding them: true lens behavior (a real fisheye warps the near hand before the face), mirror and floor reflections, lit crowds where extras act, one light source keeping its rhythm across every cut, the camera as a physical object (a phone set on a rock wobbles then locks; a drone catches lens droplets and wake shake), and 30-second single takes that carry a full emotional arc.

Before generating, mentally "watch" the prompt as a viewer: is everything unambiguous, is the first frame non-empty, is it clear where the subject is and where it looks, where is the light coming from.

---

## WORKFLOW

1. **Read as a director.** Find the dramatic shape: where the scene turns, lands, breathes.
2. **Define continuity anchors.** Who is in frame, how they look, what they carry across cuts.
3. **Write the prompt** using the block structure below.
4. **Tag assets.** Tagging rules below.

If the idea is ambiguous, close the gaps — blocking, angle, light, timing, character behavior, what is in the first frame, how it ends. The model fills any gap on its own, usually not the way intended. House practice: close most gaps yourself as the director would (state the assumption in one line outside the block); ask only when a gap would change the meaning of the shot, and ask one question, not a list.

---

## ASSET TAGGING

Reference image (`@tag`) sets **appearance and identity**. Text sets **what happens** and locks critical details. Both are required.

**Tag naming:**
- If the user specifies tags as `@tag_name`, use those.
- If no tags are specified, name them by load order of the supplied assets: `@image1 @image2 ...` for images, `@video1 @video2 ...` for videos, `@audio1 @audio2 ...` for audio.
- Otherwise follow the user's explicit instruction.

**Reference + text rule:** keep the character description minimal — long appearance text conflicts with the image and degrades it.

```
@TAG: age + role/build + current state + unique visible features + action-critical details + voice (only if it has a line). 100% matches the reference.
```

State critical details (small text, logos, color) in words even if they appear on the reference — the model can drop them.

House note on "age": prefer role/build over a numeric age ("a lanky clerk", "a round little guy") — it reads better and keeps the content filter calm, which tightens sharply when it reads a minor. Use a number only when the story needs it.

**Voice lock (2.5):** Seedance 2.5 locks the voice together with the appearance in the character sheet. Reuse the same sheet reference across generations and the voice stays consistent — describe the voice once in the tag line, not in every prompt.

Never place an `@tag` in a shot where that object is not present; the model will try to force it into frame.

---

## CONTEXT ISOLATION

Each generation is a blank slate — **no memory of previous shots.** A prompt is a sealed single-shot document.

Do not carry in: scene numbers, script headings, summaries of prior scenes, unused tags/characters, "as above / continues" phrasing, or people and props from a previous line that are not needed in this shot.

House exception, kept minimal: when a prompt is one part of a longer video, its SCENE CONTEXT may carry one sentence of story position, the emotional intention of this piece, and the physical state that carries over (wet/dry, prop in hand, who is present). That is continuity information the model needs to act the piece correctly — not a summary of the previous scene. See BOSS LAYER § Long scripts.

---

## STYLE — DISTRIBUTED, NOT A PREFIX

There is **no separate style-prefix block at the top of the prompt.** Style is not one thing in one place — it is a set of aspects, and each aspect lives in the block that already governs it, where it is most effective and unambiguous. State the target look, never what to avoid; adapt every line to this specific scene.

Cover these aspects, each in its home block:

| Aspect | Lives in | What to write |
|--------|----------|---------------|
| Lighting | **LIGHTING** | source, direction, exposure, key/fill, haze for THIS scene |
| Color / grade | **COLOR GRADE** (own block if grade is strong, e.g. teal-cyan desaturated) or folded into **LOCATION** + **LIGHTING** for a naturalistic look | palette as material + light beam + role, never a flat list |
| Lens / optical character | **OPTICS** | FOV°, rectilinear/anamorphic, prime-lens character, motion-blur |
| Camera body / tonal character | **CAMERA** | tonal latitude, highlight roll-off, color science — as a look, not a model name |
| Skin / micro-realism | **PERFORMANCE** (or inside **ACTION**) | pore-level realism, capillary flush, living eyes, catch-lights, visible breath |
| Acting | **PERFORMANCE** (or inside **ACTION**) | micro-pauses, precise eye-line, restraint, muscle-level emotion |
| Physics realism | **PHYSICS** | gravity, inertia, mass, contact shadows, fluids, particles |
| Composition / blocking | **FIRST FRAME / BLOCKING** | framing rule for THIS scene; everyone moving from frame one |
| Continuity | **POSITIVE LOCKS** | characters, props, environment identical across cuts |
| Wardrobe | **WARDROBE** (own block when costume matters) | material + condition, scene-logical |
| Format / resolution / grain / fps / bitrate | **STYLE** + **OUTPUT SETTINGS** at the **end**, just before LOCKS | 8K, photoreal, anamorphic, fine grain, real-time vs slow-mo per segment |

**Placement principle:** descriptive style (light, color, optics, physics, acting) sits *inside the content block it describes*, in the body of the prompt. Technical/format style (resolution, grain, fps, bitrate, overall look reference) sits as a **suffix stack at the end** (`STYLE`, `OUTPUT SETTINGS`), right before `POSITIVE LOCKS`. Nothing style-related goes at the very top — the prompt still opens on `SCENE CONTEXT` and `ACTIVE REFERENCES`.

Use only the aspects the shot needs. A naturalistic single take may have no `COLOR GRADE`, `WARDROBE`, or `OUTPUT SETTINGS` block at all and fold those notes into LIGHTING and POSITIVE LOCKS. A graded, multi-segment piece earns the full suffix stack.

If the user supplies their own prefix or block text, use it verbatim.

---

## PROMPT STRUCTURE

Write blocks in this order. Logic: context and references first, then space and timing, then action and physics, then the descriptive-style blocks in their home positions, and a technical-style suffix at the end. Use only the blocks the shot needs; drop the rest.

```
SCENE CONTEXT
[1–2 sentences: what happens, where, when. Geo-positions of characters.]

ACTIVE REFERENCES
[@tag + minimal anchor of critical details + "100% matches the reference"]

LOCATION MAP
[Foreground / midground / background, where the camera is, where light comes from, movement paths. Naturalistic color can live here.]

FIRST FRAME / BLOCKING
[Who is where in the first frame: positions, orientation, gaze. Composition rule for this scene.]

FORMAT MODE
[Choose the level of control the shot needs:
 - Single continuous shot — "one continuous shot, the camera does not cut on its own."
 - Sequence of cuts, no timecodes — "CUT 1 … CUT 2 … CUT 3", described in order.
 - Timed multishot — explicit HARD CUTs at stated seconds.]

OPTICS
[Shot size + FOV per segment + lens/optical character. For multishot add "no drift mid-segment".]

CAMERA
[Operator behavior: height, distance, movement, focus. Camera-body tonal character as a look.]

ACTION
[Events at the precision the shot needs. Camera motion and subject motion stated separately.]

PERFORMANCE        (when acting matters)
[Acting + skin/micro-realism: muscle-level emotion, eye-line, catch-lights, breath, pore-level detail.]

PHYSICS
[Mass, inertia, contact, fluids, particles.]

LIGHTING
[Source, direction, exposure — priority block.]

COLOR GRADE        (when the grade is strong / stylized)
[Palette as material + light + role; grade character. Omit for naturalistic looks — fold color into LOCATION/LIGHTING.]

WARDROBE           (when costume matters)
[Material + condition, scene-logical.]

AUDIO
[Only the needed sound / line. House default: on-set sound only — "No music, no score. No subtitles, no on-screen text or graphics." Dialogue in {braces}, sound effects in <angle brackets>, music in (parentheses) only when asked; name the language before the first line.]

STYLE              (technical-style suffix)
[Overall look in words, photoreal, format, grain — no director or equipment names.]

OUTPUT SETTINGS    (when format must be pinned)
[Aspect, anamorphic, real-time vs slow-mo per segment. Note: 2.5 renders at 720p — words like "8K" set detail intent, not output size; if native 4K is the requirement, generate on Seedance 2.0.]

POSITIVE LOCKS
[Short fixers against likely failures, in positive form, restating critical info once. Continuity lives here.]
```

The descriptive-style blocks (PERFORMANCE, PHYSICS, LIGHTING, COLOR GRADE, WARDROBE) sit in the body next to what they govern. The technical-style blocks (STYLE, OUTPUT SETTINGS) form a short suffix stack just before POSITIVE LOCKS. Nothing style-related opens the prompt.

A **lock** is a short hard fixer placed next to what it protects, e.g. `"headlights stay glowing in every shot"`. Write densely where control matters, sparsely where it does not. Say each important thing once, clearly.

---

## CUTS AND TIMING

**Duration budget (2.5): one generation runs up to 30 seconds.** Plan the shot to use it — a full emotional arc, a 14-segment beat-cut music sequence, or one unbroken oner all fit in a single take. A 2-minute piece is 4 generations. When timing matters, state the total length and land every HARD CUT on a stated second.

Pick the precision the shot actually needs — these are points on a scale, not a binary:

- **Single shot (oner)** → "one continuous shot, the camera does not cut on its own."
- **Sequential cuts, no timecodes** → describe shots in order as `CUT 1 … CUT 2 … CUT 3`. Use when you want specific cuts but exact timing does not matter.
- **Timed multishot** → explicit HARD CUTs at stated seconds. Use when beats must land on a clock.
- **Freestyle b-roll** → do not lock cuts; let the model find angles.

When you specify cuts (timed or not), lock that the camera does not add its own: *"cuts only at the specified points, the camera does not cut on its own."*

**Timecode format** (only when timing matters):
```
0.0s to 1.0s — [description]
1.0s HARD CUT
1.0s to 3.0s — [description]
```

**Sequential format** (cuts without timecodes):
```
CUT 1 — [description]
CUT 2 — [description]
```

**Cut types:** `HARD CUT`, `SMASH CUT`, `MATCH CUT`, `INSERT CUT`, `REVERSE CUT`, `WHIP CUT`. Fades / crossfades only if explicitly requested.

Across internal cuts hold: same character set, same geometry, screen direction, gaze, light, wardrobe, prop state.

---

## DIRECTING

**Blocking.** State where each character stands, sits, moves; what their hands do; what sits between them. "She sits across from him at the diner booth, knees touching under the table" beats "they sit and talk."

**Pace.** Read the dramatic structure. Confession scene → air, held shots, beats of silence. Action → compression, short cuts. A reveal lands on one held close-up.

**Acting.** Translate emotion into concrete on-shot direction:
- ❌ "she looks sad" → ✅ "her eyes drop to the table, jaw tightens, she swallows once before answering"
- ❌ "he is angry" → ✅ "knuckles whiten on the glass, breath shortens, eyes never leave hers"

Restraint by default — a whisper out-acts a shout most of the time.

**Continuity** (hold in mind, do not write as a block): state carried forward (wet/dry/bloodied), appearance not drifting, emotional carry from the previous scene, one time-of-day and weather unless the location changes.

**Camera language.** Be concrete: FOV°, height, movement, motivation. Motivate every camera move.
- "Low-angle 18° dolly-in, slow push from waist to chest as she realizes."
- "Static 47° two-shot, eye-level, locked off — lets the silence sit."
- "Handheld 63°, follow from behind — camera lags half a beat."

---

## PROMPTING RULES

- **Positive only.** Describe what should happen, not what to avoid. ❌ "does not fall backward" → ✅ "stays upright, feet planted."
- **Speeds in km/h.** ❌ "fast/slow" → ✅ "moves at 40 km/h", "camera pans at 5 km/h."
- **Atmosphere in percent / meters.** ❌ "light fog" → ✅ "fog density 40%", "haze visible at 15 meters depth."
- **Atmosphere builds in steps across shots.** Shot 1: fog 20% → Shot 2: 40% → Shot 3: 60%.
- **Giant scale via human-height comparison.** ❌ "huge", "three meters tall" → ✅ "stands as tall as four humans stacked head to toe."
- **Left/right is from the camera.** "Subject moves left" = left from the camera's view.
- **Environment interaction stated physically.** Snow melts on skin, rain runs down hair, wind moves fabric.
- **Emotion through muscle movement, not labels.**

---

## OPTICS — SHOT SIZE, LENS, FOV

Two levers define "how it is shot": **shot size** and **focal length**.

### Shot sizes
| Abbr | Meaning | In frame |
|------|---------|----------|
| ECU | Extreme Close-Up | a detail: eyes, button, headlight, hand |
| CU | Close-Up | full face / one element large |
| MCU | Medium Close-Up | head and shoulders |
| MS | Medium Shot | roughly to the waist |
| WS | Wide Shot | full figure + surroundings |
| EWS | Extreme Wide | scale, location |

### Focal length (mm — for describing size while writing, not for the prompt text)
| Lens | Effect | Use for |
|------|--------|---------|
| 24–35mm wide | space, slight perspective distortion | action, immersion, wides |
| 50mm normal | natural perspective, "as the eye sees" | realism, neutral shots |
| 85mm portrait | soft bokeh, subject separated from background | portrait, emotion |
| 135mm+ tele | strong compression, "watching from afar" | observation, distance, sport |

In the prompt text use **FOV in degrees** from the table below, not millimeters.

### FOV anchor table (degrees for the prompt)
| FOV | mm equiv | Purpose | When |
|-----|----------|---------|------|
| 180° | Fisheye | spherical distortion | POV, dream-state |
| 107° | 14–16mm | architectural ultra-wide | huge interiors, epic establish |
| 84° | 20–24mm | wide | establish, group blocking |
| 63° | 28–35mm | observational | wide observation, reportage |
| 47° | 40–50mm | neutral human perspective | universal establish, medium |
| 29° | 75–85mm | portrait compression | medium-isolate, dialogue bust |
| 18° | 100–135mm | natural portrait | close-portrait, identity-preserving |
| 12° | 180–200mm | tele-detail | hands, objects, detail-on-wide |
| 8° | 300–400mm | extreme compression | observation, broadcast |

Use only the discrete steps from the table. Not "23°" — use 18° or 29°. In a multishot, set FOV per segment and add `"no drift mid-segment"`.

### Camera placement in the prompt
Place the CAMERA block in the **3rd position** of the prompt's core layers (subject → action → camera → style → constraints). Moved to the end, FOV gets ignored; moved to the front, it conflicts with identity.

---

## OPTICAL TECHNIQUES

**Observation pattern (hidden-camera effect)** — all three ingredients at once:
1. Foreground occlusion — out-of-focus obstruction over 20–30% of frame (wall, pillar, branch, arch).
2. Atmospheric haze — fog/dust/shimmer between camera and subject.
3. Distance vantage — super-tele 8°–12°, operator anchored far away.
Change the occlusion type between beats; keep the vantage single.

**Sports broadcast:** `8° super-tele + handheld 1–2cm tremor + "anchored at distance, finding the action"`.

**Detail-on-wide (snake cam):** `84° wide FOV + low-angle right up against a small object` — foreground object exaggerated, background recedes into depth.

**Intimate wide:** `63–84° wide FOV on a close face` — face centered, surroundings readable without blur.

**Tele compressed air column** at 8°–12°: `"dust suspended in the long compressed air column between camera and subject"`, `"heat shimmer compressed into a wall of haze in front of the figure"`.

---

## INPUT VIDEO — V2V AND I2V

**Video-to-video** (edit real footage: swap a character, add a creature, keep the plate):
- The source clip must be **at least 4 seconds long**. Shorter clip → freeze-frame the last shot to pad it.
- **Set the generation duration to match the reference** (usually 4s). Anything longer and the model starts guessing beyond the source.
- Tag the source `@video1` and declare it master: "master for camera, framing, focus, motion, expression timing, background, lighting, grain and duration." Then state the one edit and lock everything else ("every pixel outside the replaced subject remains exactly as in @video1").

**When v2v fails:** if the same defect shows up across all four batches, the problem is the prompt or the source — more batching only burns credits. Usual cause: the action you want has no anchor in the source (e.g. no jump moment to map onto). Switch to **image-to-video**: screenshot a frame of the location, use it as the starting frame, and write the action from scratch. Plan a deliberate **empty-frame pause** (1–2 seconds of just the location) where you intend to stitch takes in the edit — it becomes a clean cut point.

---

## SPECIAL PROTOCOLS

**4-mechanism multishot consistency stack (extreme FOV: 8°, 107°):**
1. Sequence-wide identity lock — single location reference across all beats.
2. LENS LOCK opener — explicit FOV phrase at the start of each beat.
3. LENS CHECK closer — confirm FOV at the end of the beat.
4. Color via material + light, not as a list.
All four are required, or extreme-FOV multishots break down after 2–3 beats.

**Whip-pan timing:**
```
0.3s — Subject A settled
0.8s — WHIP motion-blur transition
1.4s — Subject B settled
```
A whip under 0.8s renders as a hard cut without blur.

**Mixed time-speed (real-time + slow-mo):** hard cuts only between speed modes. Each shot is one speed start to finish.

**Cracks/breaks without impact (anti-impact lock):**
- "crowd PRESSES, not strikes"
- "fracture originates from edge stress, not center impact"
- "no impact point — pressure-based crack"
- sequential timing edge-to-center, not radial from a point.

---

## CAMERA / LIGHT / COLOR

**White balance** in Kelvin, set to the scene mood, fixed within a scene (3200K / 4000K / 5600K / 8500K).

**Equipment:** describe the look, not gear. No camera/film/lens model names — they get ignored or break complex moves.

**Color rule:** tie color to **material + light beam + compositional role**, never a flat list.
- ❌ "the woman wears red, the man wears blue"
- ✅ "crimson silk scarf catching the cold tungsten spill from the corridor"

**Background in layers:** state foreground / midground / background separately.

**Camera on the shadow side**, with a stated operator axis.

---

# BOSS LAYER — HOUSE RULES (Rick Miura / FilmBoss)

Everything above is the validated base and stays in force. This layer adds the defaults used on FilmBoss productions. Where a house rule and a base rule touch the same thing, the house rule is the default and the base rule is the fallback. The user's explicit request always wins over both.

## OUTPUT AND WORKFLOW

- **One English prompt per code block, nothing else inside it.** Titles (`PART A — THE AVALANCHE · 27s`), notes, assumptions and any Portuguese translation go outside the block. If a translation is wanted, it is a second, separate block labeled as translation — never mixed with the English.
- **Don't interrogate. Deliver.** Read the conversation, make the directorial decisions yourself, state an assumption in one line if needed, and hand over the prompt. The skill exists to be fast.
- **Continuation by default.** Treat every new request as the next piece of the same story/video: same style, same camera grammar, same tags, same voice notes. Only if a request clearly has nothing to do with the current story, ask once — "new scene, or continuation?" — then proceed.
- **After a generation is approved, don't touch what worked.** Apply new rules to the parts not yet generated, and offer the approved part's upgrade only as an option.

## TAGS — SET, CAST, RECURRING PROPS ("Tag Indicator")

Every scene is a location + characters (+ recurring props, vehicles, creatures, extras). All of them should exist as registered references (`@tags`) in Higgsfield before the prompt is written; text alone drifts across generations.

- When the user mentions tags, or a scene has recurring elements with no tag, offer the **Tag Indicator**: a short list of what to create — **characters** (sheet: headless front body, back body, large face — see Character sheet note in PLAYBOOKS § 3), **sets** (the angle the scene needs, empty of people), **props / vehicles / creatures** that repeat, **recurring extras** (a figure that returns across episodes). Keep it to what this story actually reuses.
- The user creates and uploads them and returns **only the names**. Link them automatically: use the exact strings as given (lowercase, hyphens), and write for each a role line in ACTIVE REFERENCES — **what it provides / what not to copy**:
  `@praca-1 provides the plaza's layout and architecture only — here it is alive and moving.`
  `@nina — tall, oversized jacket; warm quick voice. 100% matches the reference.`
  `@bossland provides the city — architecture, color, light, flying traffic; extend it freely, do not copy its viewpoint.`
- A location reference shot from one angle provides the place, not the framing — say so when the scene needs another angle. A character sheet leaks its staging — add "do not take the gray backdrop or the panel layout".
- Reuse the same tag every time the place or character repeats; never invent a second name for the same thing. Never place a tag in a shot where that thing is absent.
- When new tags arrive mid-project, answer with a usage map (which tag serves which scene) and flag what still has no tag. Regenerate prompts only if asked.

## LENGTH BUDGET — WHAT 2.5 ACTUALLY WANTS

There is no published character limit on Higgsfield; what breaks a prompt is contradiction and event overload, not word count. Validated working ranges:

| Shot | Words |
|------|-------|
| Simple shot, b-roll, one move | 120–250 |
| 30s multishot with dialogue (house standard) | 300–450 |
| Hard ceiling | ~600 — above it, cut adjectives and repeated style words, never timings, tag role lines, dialogue direction or locks |

- At most ~10 segments in 30s. Each segment has one primary change and ends on a visible end state.
- Dialogue budget ≈ 2.5–3 words per second of the segment that holds it. A 12-word line needs a 5-second segment if it is meant to be acted, not rushed.
- Timestamps are a time budget, not frame-accurate cuts: whole seconds, consecutive, non-overlapping. Never ask for several actions inside one second.

## LONG SCRIPTS → PARTS (the splitter)

Any script longer than one generation is split by the skill, automatically, into generations of ≤30s:

- Cut where a film would cut: after a line lands, on a location change, at the top of a new emotional beat, on a reaction or a pause — never mid-sentence, mid-gesture or mid-emotion.
- A continuous specialty move (FPV dive, drone pull-back, passing through a screen or a painting) lives entirely inside one generation.
- Each part is a sealed prompt, but its SCENE CONTEXT carries: story position in one sentence, the emotional intention of this piece (tense, tender, comic, action, release), and the state that carries over. No tags or characters that are not in this piece.
- Name the parts (`PART A — TITLE · 27s`), state the total, suggest a generation order (short and cheap first to validate voices and characters; the hardest continuous move last). When a new piece is requested later, slot it into the existing map ("goes between Part C and Part D").

Procedure and skeleton: PLAYBOOKS appendix § 1 Splitting.

## SERIES CONSISTENCY — SEVERAL PROMPTS, ONE FILM

When prompts belong to the same video, keep these identical across all of them, verbatim where possible:

1. The **STYLE** block (look, texture language, optical character, grain, aberration).
2. The **CAMERA** paragraph (how it moves, when it is handheld, shadow side).
3. The **insert discipline** (one motivated texture insert per action block, 12° locked).
4. The **light language** and white-balance family.
5. **Tag role lines** and voice notes.
6. **Pronunciation notes** for brand names and acronyms inside the dialogue direction.

Change only what the scene changes: location, time, blocking, emotion. Reusable paragraphs: PLAYBOOKS appendix § 2 Series kit.

## HOUSE DEFAULTS (unless the user asks otherwise)

**Sound.** On-set sound only. Write it: "No music, no score." in AUDIO and again in the locks. If the user asks for music, derive it from the script and the established style — a cinematic, beautiful cue that serves the story (instrument family, tempo, where it enters and leaves, what it underlines), written with the `( )` music syntax, never "epic music". Playbook: PLAYBOOKS appendix § 6 Music when asked.

**Graphics.** No subtitles, no captions, no on-screen text. In-world text (a sign, a plaque) is allowed when the script calls for it — name it as in-world, and expect to fix spelling in post.

**Light.** Beautiful, cinematic, subtle: camera on the shadow side, soft-edged shadows, one motivated source per scene, white balance in Kelvin. Always add the optical character: shallow depth of field, slight chromatic aberration at the edges, fine grain, natural motion blur, an organic anamorphic feel (oval bokeh, gentle horizontal flare, manual focus that breathes and lands a hair late). Photoreal texture even on stylized or animated subjects: pores, fabric weave, wood grain, dust in light.

**Acting.** Natural and subtle, never a presenter reading. Every line is acted, not read: write the direction for each line in parentheses before it — **intention → emotion → delivery** (tempo, volume, emphasis, pauses, where the voice drops or lifts). Modulation inside the sentence; nothing linear. One speaker at a time, no chorus lines. Tag the speaker at the exact moment:

```
@tito (needs to understand, panicking; high and squeaky, the second one cracking): {Por quê? Por quê?!}
```

Dialogue in `{ }`, effects in `< >`; name the language before the first line ("Language: Brazilian Portuguese, natural Brazilian delivery"). Pronunciation of acronyms and brand names goes inside the direction ("pronouncing 'IA' as the Portuguese letters i-á and 'Maker' in English as MEI-ker"). No tears, no sweat, unless asked. On animation projects the register is "one notch past real" — anticipation, overshoot, settle, big readable faces — but lived-in: sadness is opera, joy is a dance, nobody poses.

**Eyes and framing.** Characters sit off-center and not frontal by default; they look into the lens only on a line addressed to it (fourth wall). Lines to each other stay between them. Nobody performs for the camera unless the scene is literally about performing.

**Cuts.** Fluid and film-like; every 30 seconds carries the angle variety a cinematographer would choose: a wide that places, a medium that plays, a close that lands, an insert that proves texture. Cuts only at stated seconds; the camera never joins two scenes by following someone from one to the next. A long speech gets coverage — cut to details with the voice continuing.

**Camera.** A held camera, not a mounted one: it breathes. It moves only in depth — pushes, pulls, slow rises from near the ground — never lateral tracking unless asked. When someone speaks to it, it is visibly alive: a small handheld reframe toward them, then a settle (the point of view of a guest in the room). Inserts are locked. Continuous specialty moves are one shot each. Write a CAMERA paragraph stating this grammar in every prompt of a series.

**Inserts.** One motivated texture insert per action block, placed where attention already is — the object being looked at, the hand doing the thing, the surface just touched. 12°, locked, naming the texture (brass, paper grain, fabric weave, dust on glass). Never random, never two in a row, never more than the scene can carry.

**Color and world.** When the world is meant to be alive and colorful, put color in objects and actions inside the scene — balloons, paint, banners, costumes, confetti in the air — not in grading words. "Faded / dusty / weathered / haze" stacked together kills a world.

## PREVIOUS TAKE AS REFERENCE

If the user attaches the previously generated clip as a reference, add one role line to ACTIVE REFERENCES and change nothing else:

```
@video1 defines only the visual style (grade, texture, light character, grain) and the voice timbre of @nina, @tito and @zinho. Do not use its action, blocking, camera path, timing or scene content. The video follows only the script below.
```

The new video is built only from the new script. Video references run 1.8–30s each and ≤30s combined; 5–10s is the stable range. For a true continuation from a last frame, use that frame as an image reference instead: `@image1 is the exact first frame; continue forward from that moment; do not replay what happened before it.`

## EDITING AN UPLOADED VIDEO (Seedance 2.5 video edit)

Short and direct — the pattern that works: declare the source as the sole master, state one edit, scope it, list what is preserved, and make a replaced element inherit the old one's timeline.

```
@video1 is the sole editing master for camera, framing, focus, motion, timing, background, lighting, grain and duration.
EDIT: [one change — add / replace / remove / restyle X].
SCOPE: [where and when — region, time range, inside or outside the subject's silhouette].
INHERIT: the new [element] follows the exact timing, path, occlusion and exit of [the replaced element] in @video1.
PRESERVE: every pixel outside the edit remains exactly as in @video1 — [faces, wardrobe, props, background, the audio categories not edited].
AUDIO: [keep original / edit only dialogue / edit only effects].
```

Facts worth telling the user before credits are spent: on Higgsfield, video edit ignores duration and aspect ratio (both inherit the source) and bills by the source's length; it is stable with sources ≤20s and 1–5 supporting reference images. A full rebuild of a shot (swap a character, keep the plate) is the omni-reference v2v lane described in INPUT VIDEO above (source ≥4s, duration = source). Full templates: PLAYBOOKS appendix § 5 Editing.

## QUALITY BAR

A finished prompt reads like a shot list from a film set, not a caption: first frame non-empty, geography stated, light motivated, every cut and move motivated, dialogue acted, textures named, end state visible. If it reads like "a cool video", it isn't done.

---

## CHECKLIST (before each prompt)

- All blocks in order: context and references first, then space/timing, then action/physics, then style in its home blocks, technical-style suffix last?
- Tags named per the tagging rule (`@tag_name`, or load-order `@image1`/`@video1`/`@audio1`, or user instruction)?
- `@tag` only in shots where the object is present?
- No style-prefix block at the top — prompt opens on SCENE CONTEXT / ACTIVE REFERENCES?
- Each style aspect placed in its home block (light→LIGHTING, color→COLOR GRADE or LOCATION, acting/skin→PERFORMANCE, format/grain→STYLE+OUTPUT SETTINGS suffix)?
- Style adapted to this scene (not generic)?
- Everything positive (no "does not X")?
- Speeds in km/h, atmosphere in %/meters, giants vs human height?
- Emotion through muscle movement, not labels?
- Left/right from the camera?
- FOV in degrees from the anchor table (not mm, not arbitrary)?
- CAMERA block in 3rd position?
- WB in Kelvin for the scene mood?
- Color via material + light + role, not a list?
- Camera on the shadow side, operator axis stated?
- Background in foreground/midground/background layers?
- Multishot: FOV per segment + "no drift mid-segment"; extreme FOV → all 4 consistency mechanisms?

House items:
- English prompt alone inside the code block; title, notes and translation outside?
- "No music, no score" and "no subtitles, no on-screen text" stated (in-world text named if used)?
- Every repeated place, character and prop carries its `@tag` with a role line (provides / do not copy)?
- CAMERA paragraph present — depth-only moves, breathing, alive on fourth-wall lines, inserts locked?
- One motivated 12° texture insert per action block, none random?
- Every line: `@tag (intention → emotion → delivery): {line}`, one speaker at a time, language named, pronunciations given?
- Off-center framing; eyes on the lens only for fourth-wall lines?
- Shadow-side cinematic light plus the optical character stated?
- Word budget respected (300–450 for a 30s multishot; ~600 hard ceiling)?
- Part of a series: STYLE, CAMERA, insert and light blocks identical to the other parts; SCENE CONTEXT carries intention and carry-over state?
- Split at film cut points; no continuous move split across parts; every segment ends on a visible end state?

---

## FINAL RULES

- **English prompts only.**
- **Positive phrasing only** — state the target, never the prohibition.
- **No director names, no signature-work references, no equipment names.**
- **Cinema, not clips.** Every prompt is written so the result looks like a scene from a film.

*Seedance Boss is maintained by Rick Miura / FilmBoss. House rules come from production experience on FilmBoss shorts and are meant to be enriched over time, never trimmed.*

---

# PLAYBOOKS APPENDIX (Rick Miura / FilmBoss)

Longer templates referenced above. Read the section you need; none of this replaces the base structure.

Contents
1. Splitting a long script into ≤30s parts
2. Series kit — paragraphs kept identical across parts
3. Tag Indicator — onboarding the set, the cast and the props
4. Previous take as reference
5. Editing an uploaded video — templates
6. Music when asked
7. Compact worked example (animated dialogue scene)

---

## 1. Splitting a long script into ≤30s parts

### Procedure

1. **Read the whole script as a director first.** Mark the beats: where the scene turns, where a line lands, where a location changes, where the emotion resolves or flips.
2. **Estimate time per beat** before assigning parts: a spoken line ≈ 2.5–3 words per second if acted; an entrance or a reaction ≈ 1–2s; a continuous specialty move (FPV, drone, dive through a screen) ≈ 6–14s and indivisible; an insert ≈ 2s.
3. **Group beats into parts of ≤30s**, cutting only at film cut points:
   - after a line lands (never mid-sentence),
   - on a location change,
   - at the top of a new emotional beat (fear → relief, comedy → tenderness),
   - on a reaction or a pause.
   Never cut mid-gesture or mid-emotion; never split a continuous move.
4. **Prefer fewer cuts per generation over fewer generations.** 10–12 segments in 30s is the practical ceiling; a clean 10–12s part beats an overloaded 30s one.
5. **Write each part as a sealed prompt**, with a SCENE CONTEXT that carries: story position (one sentence), emotional intention of this piece, physical state that carries over (wet/dry, prop in hand, who is present, sound state such as "silence resumes"). No tags that are not in this piece.
6. **Title, total, order.** `PART A — THE AVALANCHE · 27s`. State the total runtime. Suggest an order: short/dialogue parts first to validate voices and character sheets; the hardest continuous move last.
7. **Later additions** slot into the map: "CENA EXTRA — goes between Part C and Part D; the question it plants is answered by Part D."

### Per-part skeleton (house version of the base structure)

```
SCENE CONTEXT
[duration]-second [medium] moment, [time of day]. [One sentence of story position.] [What happens in this piece, who is present, where the emotion goes.] [Carry-over state.] Nobody performs for the camera unless a line is addressed to it.

ACTIVE REFERENCES
@set-tag provides [place] — [what to use]; [what not to copy]. @char-tag — [2–4 visible anchors]; [voice note if it speaks]. All 100% match their references.

FIRST FRAME / LOCATION
[Where the camera is, what is in frame at 0.0s, light source and direction, camera on the shadow side.]

CAMERA
A held camera, not a mounted one: it breathes. It moves only in depth — pushes, pulls, slow rises from near the ground. When someone speaks to it, it reframes a few degrees toward them and settles. Inserts are locked.

FORMAT MODE — timed multishot, cuts only at the stated seconds, the camera does not cut on its own. Language: [language, delivery].
0.0s to N.0s — [FOV]° [shot] [move]: [action]. @tag (intention → emotion → delivery): {line}
N.0s HARD CUT
… one insert per action block: 12° insert, locked: [object + named texture].
… last segment ends on a visible end state.

PERFORMANCE
[Register for this piece: restraint / animation "one notch past real"; 2–4 observable cues for the main emotional turn; faces dry.]

STYLE
[Identical across the series — look, texture language, optical character, grain.]

AUDIO
On-set sound only: [list]. No music, no score. No subtitles, no on-screen text or graphics.

POSITIVE LOCKS
[Continuity fixers: who looks at the lens and when, who holds what, what stays still, what stays dry, one speaker at a time, daylight/night as set.]
```

---

## 2. Series kit — paragraphs kept identical across parts

Paste these into every part of the same video and change only what the scene changes.

**CAMERA (house default)**
```
CAMERA
A held camera, not a mounted one: it breathes. It moves only in depth — pushes, pulls, slow rises from near the ground — never sideways. When someone speaks to it, it reframes a few degrees toward them and settles, like a guest turning to listen. Inserts are locked.
```

**STYLE (live-action photoreal)**
```
STYLE
Photoreal cinema with an organic anamorphic character: oval bokeh, gentle horizontal flare, manual focus pulls that breathe and land a hair late, shallow depth of field, slight chromatic aberration at the edges, fine grain, natural motion blur; pore-level skin, fabric weave, wood grain, dust in the light.
```

**STYLE (3D animated feature with photoreal texture)**
```
STYLE
Ultra-detailed 3D animated feature, photoreal texture on cartoon performance: pore-level skin, fabric weave, wood grain, dust in the light, shallow depth of field, slight chromatic aberration at the edges, fine grain, natural motion blur, warm [K] light, shadow-side camera.
```

**AUDIO (house default)**
```
AUDIO
On-set sound only: [room tone / footsteps / the specific contacts of this scene]. No music, no score. No subtitles, no on-screen text or graphics.
```

**PERFORMANCE (animation register)**
```
PERFORMANCE
Animated-feature acting, lived-in and slightly caricatured: big readable faces, anticipation before each move, overshoot and settle after it, clear mouth shapes. Eyes meet the lens only on lines addressed to it. Faces dry. Every line is acted, not read: tempo, volume and pitch change inside the sentence.
```

**Insert discipline (how to choose the one insert)**
The insert goes where the attention already is: the object everyone is looking at, the hand doing the action, the surface just touched, the thing that just changed state. Name the material and what light does to it. One per action block, 12°, locked.

---

## 3. Tag Indicator — onboarding the set, the cast and the props

When a project starts, or when a scene has recurring elements with no tag, hand the user this list (adapted to the story) — short, in their language, no lecture:

```
Para essa história eu precisaria dos seguintes elementos cadastrados no Higgsfield:

Personagens (character sheet: frente do corpo SEM cabeça, costas, rosto grande)
- [name] — [one line: what makes them recognizable]
- …

Cenários (um quadro do lugar, sem gente, no ângulo que a cena pede)
- [place] — [which scenes use it]
- …

Objetos / veículos / criaturas que repetem
- [item]
- …

Figuração recorrente (quem volta em mais de um episódio)
- [figure]

Quando subir, me manda só os nomes das tags e eu linko tudo nos prompts.
```

When the names come back:
- Use the exact strings. Don't normalize beyond what the user wrote.
- Answer with a usage map: tag → scenes where it appears; flag what is still missing.
- From then on, every prompt carries the tags with a role line ("provides X / do not copy Y"), and the same tag is used every time the thing repeats.

Character sheet note (house format the user already works with, validated): three panels on a plain neutral gray background, no text, no labels, the reference's exact rendering style preserved.
- Panel 1 (left, small): full-body FRONT view from the neck down, HEADLESS — the body ends at the collar, no head, no face, no hat, empty space above the collar, arms relaxed, signature prop held at the side.
- Panel 2 (center, small): full-body BACK view — only the back of the head, hair and hat visible, no face.
- Panel 3 (right, large, filling the right half): big head-and-shoulders FACE close-up, front view, neutral expression, every facial detail sharp. This is the only face on the sheet.
Why: small faces on the full-body panels get mixed up by the video model (wrong face, duplicated heads); one large face gives a single unambiguous identity anchor. Same clothing and colors in all panels. When regenerating an existing character in this format, pass the previous sheet as a second reference to keep the design. Add "do not take the gray backdrop or the panel layout" to the role line whenever a sheet is the reference.

---

## 4. Previous take as reference

The user generated Part A and wants Part B to inherit its look and the voices. One line in ACTIVE REFERENCES:

```
@video1 defines only the visual style (grade, texture, light character, grain) and the voice timbre of @nina, @tito and @zinho. Do not use its action, blocking, camera path, timing or scene content. The video follows only the script below.
```

Rules:
- Nothing else in the prompt changes; the new video is built only from the new script.
- Video references: 1.8–30s each, ≤30s combined per generation; 5–10s is the stable range — if the previous take is 30s, a trimmed 8–10s excerpt with clear faces and at least one line works better than the whole clip.
- If the previous clip is meant to be continued frame-to-frame, use its last frame as an image reference instead: `@image1 is the exact first frame; continue forward from that moment; do not replay what happened before it.`

---

## 5. Editing an uploaded video — templates

Facts (Higgsfield surface, 2026): video edit ignores duration and aspect ratio (both inherit the source) and bills by the source's length; stable with sources ≤20s and 1–5 supporting reference images; the model preserves the master's timeline and changes one scoped thing inside it. A full rebuild of a shot (swap a character, keep the plate) is the omni-reference v2v lane in § INPUT VIDEO (source ≥4s, duration = source; if the same defect appears across all four batches, the source lacks the anchor — switch to image-to-video from a frame).

Write edits short and direct. One edit per prompt.

**Add an element**
```
@video1 is the sole editing master for camera, framing, focus, motion, timing, background, lighting, grain and duration.
EDIT: add [element] — [what it looks like, referenced by @image1 if supplied].
SCOPE: [where it appears, from Ns to Ns], [how it enters and how it leaves].
PRESERVE: every pixel outside the added element remains exactly as in @video1 — faces, wardrobe, props, background, camera, and the original audio.
The element casts shadows and catches light consistent with @video1.
```

**Replace a subject**
```
@video1 is the sole editing master for camera, framing, focus, motion, timing, background, lighting, grain and duration.
EDIT: replace [old subject] with [new subject, @image1 defines its appearance only].
INHERIT: the new subject follows the exact timing, path, occlusion, expression timing and exit of [old subject] in @video1.
PRESERVE: every pixel outside the replaced subject remains exactly as in @video1; original audio kept.
```

**Replace the background**
```
@video1 is the sole editing master for camera, framing, focus, motion, timing and duration.
EDIT: replace the background with [new environment, @image1 defines its layout and light].
SCOPE: outside the subject's silhouette only; the subject, wardrobe, hair edges and contact shadows stay exactly as in @video1.
PRESERVE: camera movement, parallax and the original audio.
```

**Restyle / relight**
```
@video1 is the sole editing master for composition, characters, performance, camera movement and duration.
EDIT: relight the whole clip to [new light: source, direction, Kelvin, quality].
PRESERVE: identity, wardrobe, blocking, camera path, timing and the original audio.
```

**Audio-only edit**
```
@video1 is the sole editing master for every visual element.
EDIT: replace only the dialogue of [character] with: Language: [language]. @character (direction): {new line}. Lip-sync to the new line.
PRESERVE: all other audio (room tone, effects) and every visual element exactly as in @video1.
```

---

## 6. Music when asked

Default is no music. When the user asks for a score inside the generation:

1. Read the script and the established style: what the piece is (tender, tense, comic, epic), where the emotional turn is, whether the world is animated or live.
2. Design one cue, not a playlist: instrument family, tempo or feel, dynamics, the exact seconds it enters and leaves, and what it underlines. Decide whether it sits under dialogue (low, sparse) or owns a wordless stretch.
3. Write it with the music syntax and keep diegetic sound alive:
```
AUDIO
(Soft orchestral cue: sustained strings and a single piano line, slow, entering at 6.0s under the silence, swelling gently through 14.0s to 18.0s and thinning to a held note by 22.0s; it underlines her realization, never the cuts.) On-set sound continues underneath: [list]. No subtitles, no on-screen text.
```
4. Never "epic music", "cinematic music", "emotional soundtrack" alone — those words sample nothing.
5. If the user will add music in post instead, keep "No music, no score" and leave room: a wordless stretch where the cue will live.

---

## 7. Compact worked example (animated dialogue scene, 12s)

```
SCENE CONTEXT
12-second 3D animated film moment, daytime interior. In the control room @nina calmly explains to her two frightened friends that the frozen figures were already created and will be given motion tomorrow; the two exhale with relief. She speaks to them, not to the camera.

ACTIVE REFERENCES
@sala-de-comando provides the wooden control room. @nina — tall, oversized jacket; low warm voice, patient. @tito — round, large front teeth, tablet in hand. @zinho — lanky, crooked glasses, clipboard. All 100% match their references.

FIRST FRAME / LOCATION
@sala-de-comando, the three around the tablet, late sun through the side window, dust in the beam, the camera on the shadow side.

CAMERA
A held camera, not a mounted one: it breathes. It moves only in depth — pushes, pulls, slow rises from near the ground. Inserts are locked.

FORMAT MODE — timed multishot, cuts only at the stated seconds, the camera does not cut on its own. Language: Brazilian Portuguese, natural Brazilian delivery.
0.0s to 3.0s — 47°, starting low at console height and rising slowly to eye level as @nina straightens up: she lets her shoulders drop and looks from @tito to @zinho with the patience of someone who has seen this before. @nina (calming them down — warm, unhurried; low, slowing on "criados", a small nod): {Relaxa. Eles já foram criados.}
3.0s HARD CUT
3.0s to 5.0s — 12° insert, locked: @nina's hand settling on @tito's shoulder, the weave of his jacket and her fingers pressing gently into it, a few hairs lit by the window.
5.0s HARD CUT
5.0s to 8.0s — 29° close on @nina, a slow push of a few centimeters: a beat, then a small confident smile. @nina (the good news, simple and certain; lighter, "amanhã" lifted, a half smile on "Rick"): {Amanhã o Rick dá movimento pra eles.}
8.0s HARD CUT
8.0s to 10.0s — 29° close two-shot, a slow pull-back as the tension leaves them: @tito exhales first with a long {Aaaah…}, shoulders collapsing, and @zinho follows half a beat later with his own {Aaaah…}, glasses sliding down his nose.
10.0s HARD CUT
10.0s to 12.0s — 63° wide rising slowly from floor height, dust drifting through the beam in the foreground: the two slump against the console, @tito hugging the tablet, @zinho fanning himself with the clipboard, @nina already turning toward the door.

PERFORMANCE
Animated-feature acting, lived-in and slightly caricatured: big readable faces, anticipation, overshoot and settle, clear mouth shapes; relief is a full-body collapse. Faces dry. Every line is acted, not read: tempo, volume and pitch change inside the sentence.

STYLE
Ultra-detailed 3D animated feature, photoreal texture on cartoon performance: pore-level skin, fabric weave, wood grain, dust in the beam, shallow depth of field, slight chromatic aberration at the edges, fine grain, natural motion blur, warm 5000K window light, shadow-side camera.

AUDIO
On-set sound only: room tone, two long exhales, the clipboard fanning, a creak of the console. No music, no score. No subtitles, no on-screen text or graphics.

POSITIVE LOCKS
@nina speaks to her friends, never to the lens. The two exhales happen one after the other, not together. @zinho keeps the clipboard, @tito keeps the tablet. The camera holder stays unseen. Daylight throughout.
```

What makes it house-standard: one insert and it is motivated (the hand that calms); the camera only pushes, pulls and rises; the two exhales are staggered (no chorus); every line has intention → emotion → delivery; no music; faces dry; the word count sits inside the 30s-multishot budget even though the piece is 12s, because dialogue direction costs words and earns them.