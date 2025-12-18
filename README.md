# Xcraft Audify.js (FORK of Audify.js)

Xcraft Audify.js - Play/Stream/Record PCM audio data &amp; Encode/Decode Opus to PCM audio data

This project is a **fork** of https://github.com/almoghamdani/audify where the usual node-gyp is used instead of CMake, libopus has been dropped and some backends are not compiled.

## Features

- Complete API for realtime audio input/output across Linux (native ALSA and PulseAudio), Macintosh OS X (CoreAudio), and Windows (DirectSound and WASAPI) operating systems using C++ RtAudio library.

## Installation

```
npm install xcraft-audify
```

#### Requirements for source build

- Node or Electron versions that support N-API 5 and up ([N-API Node Version Matrix](https://nodejs.org/docs/latest/api/
- A proper C/C++ compiler toolchain of the given platform
  - **Windows**:
    - [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) or a recent version of Visual C++ will do ([the free Community](https://www.visualstudio.com/products/visual-studio-community-vs) version works well)
    - MingW64
  - **Unix/Posix**:
    - Clang or GCC

## Example

#### Record audio and play it back realtime

```javascript
const { RtAudio, RtAudioFormat } = require("xcraft-audify");

// Init RtAudio instance using default sound API
const rtAudio = new RtAudio(/* Insert here specific API if needed */);

// Open the input/output stream
rtAudio.openStream(
  {
    deviceId: rtAudio.getDefaultOutputDevice(), // Output device id (Get all devices using `getDevices`)
    nChannels: 1, // Number of channels
    firstChannel: 0, // First channel index on device (default = 0).
  },
  {
    deviceId: rtAudio.getDefaultInputDevice(), // Input device id (Get all devices using `getDevices`)
    nChannels: 1, // Number of channels
    firstChannel: 0, // First channel index on device (default = 0).
  },
  RtAudioFormat.RTAUDIO_SINT16, // PCM Format - Signed 16-bit integer
  48000, // Sampling rate is 48kHz
  1920, // Frame size is 1920 (40ms)
  "MyStream", // The name of the stream (used for JACK Api)
  (pcm) => rtAudio.write(pcm) // Input callback function, write every input pcm data to the output buffer
);

// Start the stream
rtAudio.start();
```

## Legal

This project is licensed under the MIT license.
