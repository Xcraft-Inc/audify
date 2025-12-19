{
  "targets": [
    {
      "target_name": "audify",
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "vendor/rtaudio"
      ],
      "dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"],
      "sources": [
        "src/audify.cpp",
        "src/rt_audio_converter.cpp",
        "src/rt_audio.cpp",
        "vendor/rtaudio/RtAudio.cpp"
      ],
      "defines": ["NAPI_ENABLE_CPP_EXCEPTIONS", "NODE_ADDON_API_CPP_EXCEPTIONS"],
      "conditions": [
        ["OS=='win'", {
          "msvs_settings": {
            "VCCLCompilerTool": {
              "ExceptionHandling": 1,
              "AdditionalOptions": ["/EHsc"]
            }
          },
          "defines": [
            "__WINDOWS_WASAPI__",
            "__WINDOWS_DS__",
            "<!@(echo ✓ Windows WASAPI and DirectSound enabled (MSVC) >&2 && echo)"
          ],
          "libraries": [
            "winmm.lib",
            "ole32.lib",
            "ksuser.lib",
            "mfplat.lib",
            "mfuuid.lib",
            "wmcodecdspuuid.lib",
            "dsound.lib"
          ]
        }],
        ["OS=='linux'", {
          "cflags_cc": [
            "-fpermissive",
            "-fexceptions",
            "-pthread"
          ],
          "ldflags": ["-pthread"],
          "libraries": ["-pthread"],
          "conditions": [
            ["<!(pkg-config --exists alsa 2>/dev/null && echo 1 || echo 0)==1", {
              "defines": [
                "__LINUX_ALSA__",
                "<!@(echo ✓ ALSA support enabled >&2 && echo)"
              ],
              "cflags": ["<!@(pkg-config --cflags alsa 2>/dev/null || echo)"],
              "libraries": ["<!@(pkg-config --libs alsa 2>/dev/null || echo)"]
            }],
            ["<!(pkg-config --exists libpulse-simple 2>/dev/null && echo 1 || echo 0)==1", {
              "defines": [
                "__LINUX_PULSE__",
                "<!@(echo ✓ PulseAudio support enabled >&2 && echo)"
              ],
              "cflags+": ["<!@(pkg-config --cflags libpulse-simple 2>/dev/null || echo)"],
              "libraries+": ["<!@(pkg-config --libs libpulse-simple 2>/dev/null || echo)"]
            }]
          ]
        }],
        ["OS=='mac'", {
          "defines": [
            "__MACOSX_CORE__",
            "<!@(echo ✓ macOS CoreAudio enabled >&2 && echo)"
          ],
          "cflags_cc": [
            "-fpermissive",
            "-fexceptions",
            "-pthread"
          ],
          "xcode_settings": {
            "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
            "OTHER_CPLUSPLUSFLAGS": ["-pthread"]
          },
          "link_settings": {
            "libraries": [
              "-framework CoreAudio",
              "-framework CoreFoundation",
              "-lpthread"
            ]
          }
        }]
      ]
    }
  ]
}